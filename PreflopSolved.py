#!/usr/bin/env python
# coding: utf-8

# ## Preflop solutions
# 
# ### Goal
# * Want to have all preflop combinations/decision points hard-coded for 6 handed poker
# * Preflop has been solved through the usage of charts
# * Anything not listed on the preflop charts is a scenario, in which we automatically fold
# * We can potentially use abstraction here if needed, but with fully hard coded decision points it SHOULDNT BE
# 

# In[2]:


import random
import Deck 
import pandas as pd
import sqlalchemy as sqa


# ## Storing this in the database
# 1. We have a relation with primary key being the hand, eg: AA, AKs, AKo, etc
# 2. Within these tuples there are five attributes: UTG, HJ, CO, BTN, SB
# 3. Within these attributes there is a simple string value that is either:
#     * F: if the hand should not be opened
#     * L: if the hand should be opened with a limp
#     * R: if the hand should be opened with a raise

# In[19]:


## Creating RFI Table to read for actions
def createRFI():
    deck = Deck.Deck(shuffle=False)
    deck.value_list.reverse()
    df_range = pd.DataFrame(data=0, index=deck.value_list, columns=deck.value_list)
    val_dict = {}
    for val in deck.value_list:
        match val:
            case 'A':
                val_dict[val] = 14
            case 'K':
                val_dict[val] = 13
            case 'Q':
                val_dict[val] = 12
            case 'J':
                val_dict[val] = 11
            case 'T':
                val_dict[val] = 10
            case _:
                val_dict[val] = int(val)
    df_explain = df_range.copy(deep=True)
    for val1, row in df_explain.iterrows():
        for val2 in row.index:
            prio1 = val_dict[val1]
            prio2 = val_dict[val2]
            if prio1 == prio2:
                df_explain.loc[val1, val2] = val1+val2 
            if prio1 > prio2:
                 df_explain.loc[val1, val2] = val1+val2+'s'
            if prio2 > prio1:
                 df_explain.loc[val1,val2] = val2+val1+'o'            
    #display(df_explain)


    pos_opt = ['UTG', 'HJ', 'CO', 'BTN', 'SB']
    hand_list = []
    for idx, row in df_explain.iterrows():
        for col in row.index:       
            name = f'{df_explain.loc[col,idx]}'
            hand_list.append(name)
    RFI_df = pd.DataFrame(data='F', index=hand_list, columns=pos_opt, dtype='object')        
    RFI_df.to_sql(name='RFI_Action', con=engine, schema='public', if_exists='fail', index=True)


# ## Raise First Open
# 1. Ensure no one has opened previously
# 2. Take position and hand as inputs
# 3. Search RFI table for primary key=hand, and attribute=position
# 4. Return action listed

# In[18]:


## Returning right action in real time
def getRFIAction(position, hand, engine):
    qry = f"""SELECT "{position}" 
              FROM "RFI_Action" ra 
              WHERE "index" = '{hand}'; 
            """
    act = pd.read_sql(qry, engine).squeeze()
    return act


# In[ ]:





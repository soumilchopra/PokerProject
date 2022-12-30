#!/usr/bin/env python
# coding: utf-8

# ## Deck and cards
# 
# ### List of functions
# 
# 
# #### Card class
# * getValue: get the value of the card
# * getSuit: get the suit of the card
# * getName: get the name of the card (composite attribute/unique identifier)
# 
# #### Deck class
# * drawCard: return a card, and add it to the dead list

# In[1]:


import random


# In[2]:


class Card: 
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.name = str(self.value) + self.suit


# In[3]:


class Deck:
    # TODO:
    # self.dealt = [] 
    # getDealt
    # updateDealt
    # burntCards
    def __init__(self, shuffle=True):
        self.value_list = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
        self.suit_list = ['s', 'h', 'd', 'c']        
        self.live = self.makeDeck(self.value_list, self.suit_list, shuffle)
        self.dead = []
        
    def makeDeck(self, value, suit, shuffle):
        deck = []
        if shuffle:         
            random.shuffle(value)
            random.shuffle(suit)
        for v in value:
            for s in suit:
                if shuffle: random.shuffle(deck)
                deck.append(Card(v, s))
        return deck
    
    
    def drawCard(self, number=1):
        drawn = []
        for i in range(number):
            active_card = self.live.pop()
            drawn.append(active_card)
            self.dead.append(active_card)
        return drawn    


# In[ ]:





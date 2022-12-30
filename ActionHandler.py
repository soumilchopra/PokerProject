#!/usr/bin/env python
# coding: utf-8

# ## Action handler and rules configuration
# 
# ### List of functions
# * getActions
# * getMinRaise
# * getValidActions
# * startAction
# * makeFlag
# * checkFlag
# * getRaiseAmount
# 
# 
# 
# 
# 
# 
# 
# 
# 

# In[1]:


class ActionHandler:
    def __init__(self, start_action='no action'):
        self.last_action = start_action
        self.current_call = 1
        self.flag = {}

        
    def getValidActions(self, player):
        match self.last_action:
            case 'raise':
                return ['raise', 'call', 'fold']
            case 'call':
                if player.active!=self.current_call:
                    return ['raise', 'call', 'fold'] 
                else:
                    return ['raise', 'check']
            case 'check':
                return ['raise', 'check']
            case 'no action':
                return ['raise', 'check']

            
    def makeFlag(self, player_list):
        flag = {}
        for player in player_list:
            if player.status == 'active':
                flag[player] = False
        self.flag = flag
    
    
    def checkFlag(self):
        return all(self.flag.values())

    
    def startAction(self, player_list):
        self.makeFlag(player_list)
        street_pot = 0
        while not self.checkFlag():
            player_iter = player_list.copy()
            active_players = list(self.flag.keys())
            for player in active_players:
                print("_________________________________")
                valid = self.getValidActions(player)
                print(valid)
                action = input(player.name + " action?")
                action = action.strip()
                match action:
                    case 'raise':
                        sizing = self.raiseAmount(player)
                        player.bet(sizing)
                        street_pot += sizing
                        self.current_call = sizing
                        self.last_action = 'raise'
                        self.makeFlag(player_list)
                        self.flag[player] = True
                    case 'call':
                        diff = self.current_call - player.active
                        player.call(diff)
                        street_pot += diff
                        self.last_action = 'call'
                        self.flag[player] = True
                        if self.checkFlag(): break
                    case 'check':
                        player.check()
                        self.last_action = 'check'
                        self.flag[player] = True
                        if self.checkFlag(): break
                    case 'fold':
                        player.fold()
                        del self.flag[player]
                        if self.checkFlag(): break
        return street_pot
        

    def raiseAmount(self, player):
        minRaise = 1
        maxRaise = player.stack
        if self.current_call*2 >= maxRaise:
            return maxRaise
        if self.current_call != 0:
            minRaise = self.current_call*2
        print([minRaise, maxRaise])        
        sizing = int(input(player.name + " raise sizing?"))
        while not (minRaise <= sizing <= maxRaise):
            sizing = int(input("Invalid sizing, try again"))
        return sizing

        
# TODO: Swap to inquirer for user input


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def choice(player):
    while 1==1:
        ch=input(f"please enter your choice player{player}:")
        ch.lower()
        if(ch=="rock")or(ch=="paper")or(ch=="scissors"):
            
            return ch
        
        else:
            print(f" Sorry!invalid choice")
            
            
            
def winner(p1,p2):
    if p1==p2:
        print(f"it is a tie")
        
    elif(p1=='rock')and (p2=='scissors') or \
        (p1=='rock')and (p2=='paper') or \
        (p1=='scissors')and (p2=='paper'):
        return  "player 1 wins!"
    
    else:
        return "player 2 wins!"
        
    
    
    
    
    
    
    
def start_game():
    print(f"hello! welcome to the game =>")
    
    p1=choice(1)
    p2=choice(2)
    
    
    print(f"player 1 chose :{p1}")
    print(f"player 2 chose :{p2}")
    
    
    res=winner(p1,p2)
    print(res)
    
    
if __name__=="__main__":
    start_game()
    

    


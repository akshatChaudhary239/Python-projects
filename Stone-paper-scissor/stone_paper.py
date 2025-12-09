# Stone Paper Scissor
import random
Keys = ["stone","paper","scissor"]
SPS = random.choice(Keys)

comp_points=0
my_points = 0
while True:
    User_input=input("enter your call ")
    if SPS==User_input:
        print(SPS,"Damn same thinking")
    elif SPS== "stone" and User_input=="paper":
        print(SPS,"good one point for you")  
        my_points+=1
    elif SPS == "paper" and User_input=="scissor":
        print(SPS,"Hey, you are on fire") 
        my_points+=1   
    elif SPS == "scissor" and User_input=="stone":
        print(SPS,"Damn you are good")      
        my_points+=1
    elif SPS== "paper" and User_input=="stone":
        print(SPS,"Hehe got you this time")  
        comp_points+=1
    elif SPS == "scissor" and User_input=="paper":
        print(SPS,"Try harder mate") 
        comp_points+=1   
    elif SPS == "stone" and User_input=="scissor":
        print(SPS,"That's an another point for me")      
        comp_points+=1
    if comp_points ==5 or my_points==5:
        print("we have a winner")  
        break  


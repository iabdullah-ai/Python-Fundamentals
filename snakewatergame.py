import random
print("1-snake\n2-water\n3-gun")
print("enter quit to exit game")
computer=['snake', 'water' , 'gun']
computerpoint=0
humanpoint=0
while True:
    try:
     a=input("enter the action you want to choose: ")
     b=random.choice(computer)
     print(b)
     if(b==a):
        print("drawww")
     elif(b=="snake" and a=="water"):
         print("computer winns!")
         computerpoint=computerpoint+10
         print(f'computer point: {computerpoint}')
     elif(b=="snake" and a=="gun"):
         print("you winn")
         humanpoint=humanpoint+10
         print(f" your point: {humanpoint}")
     elif(b=="water" and a=="snake"):
         print("you winn!")
         humanpoint=humanpoint+10
         print(f" your point: {humanpoint}")
     elif(b=="water" and a=="gun"):
         print("computer winns!")
         computerpoint=computerpoint+10
         print(f'computer point: {computerpoint}')
     elif(b=="gun" and a=="water"):
         print("you winn!")
         humanpoint=humanpoint+10
         print(f"your point: {humanpoint}")
     elif(b=="gun" and a=="snake" ):
         print("computer winn!")
         omputerpoint=computerpoint+10
         print(f'computer point: {computerpoint}')
     elif(a=="quit"):
         break
     else:
         print("enter valid action")
    except Exception as e:
       print("error",e)
print(f"computer points = {computerpoint}\nyour points {humanpoint}")
if(computerpoint>humanpoint):
    print("computer wins")
else:
    print("you winn!")
input('click anywhere to exit')





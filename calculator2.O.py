while True:
    try:
      a=int(input(" enter first number "))
      b=int(input("enter second number "))
      c= int(input("\n1-ADDITION\n2-MULTIPLICATION\n3-DIVISION\n4-SUBSTRACTION\n5-'EXIT'\n"))
      if(c==5):
          break
      elif(c==1):
          print(a+b)
      elif(c==2):
          print(a*b)
      elif(c==3):
          print(a/b)
      elif(c==4):
          print(a-b)
      else:
          print("operation doesnt exist")   
    except:
          print("'\npls enter number!!!'")
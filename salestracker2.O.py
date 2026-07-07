
import csv
import os
medicine=[]
qunant=[]
mrp=[]
print("-"*50)
print("RAHMABAD MEDICAL STORE SALES AND INCOME TRACKER ")
print("-"*50)
while True:
    m=input("Enter Name Of Medicine (Or Write 'quit' To Exit) :  ")
    if m=="quit":
       break
    else:
     n=int(input(f"enter quantity of {m} sold :"))
     o=float(input(f"Enter MRP Of {m} :"))
     print("\n")
     medicine.append(m)
     qunant.append(n)
     mrp.append(o)
print("\n-"*2)
totalmoney=0
for i in range(len(medicine)):
    money=qunant[i]*mrp[i]
    totalmoney=totalmoney+money
    print(f"medicine name:{medicine[i]}---quantity:{qunant[i]}---{medicine[i]} x {qunant[i]} = {money}")
print("your file is saved")
input("click anywhere to exit ")
print("="*50)
print(f"todays total sale --RS{totalmoney}")
print("="*50)
with open("rahimabadsales.txt","a") as f: #ye meri file hardisk me create ho gyi dot ke baad txt isliye lagaya taki windows ko pta chal jaye ki yeh text hai agar mp3 likhte toh windows ise music samjhta aur music wala icon dikhata lekin wo file chalti nhi 
   f.write("\n" )  #ye humne file us file me likhna shuru kar diya 
   f.write("NEW ENTRY")
   f.write('\n')
   for i in range(len(medicine)): #range batata hai ki for loop kitni baar chalega humne range ke andar len(medicine) likh diya matlab jitni mere list me element hoge utni baar mera loop chalega 
      money=qunant[i]*mrp[i]
      f.write(f'Medicine: {medicine[i]}  Quantity: {qunant[i]}  Total Price: {medicine[i]}x{qunant[i]}={money}\n')
   f.write(f"Todays Total Sale :{totalmoney}\n ")
   f.write("_"*50)#f.write KHALI EK ARGUMENT ACCEPT KARTA HAI IS KO SOLVE KARNE KE LIYE MUJHE 2 HOUR LAGE 
   f.flush()
print("file is saved to notepad ")
csvwalifile='rahimabadsales.csv'
with open("rahimabadsales.csv","a", newline='') as s:
   pen = csv.writer(s)
   for i in range(len(medicine)):
      money=qunant[i]*mrp[i]
   pen.writerow([medicine[i],qunant[i],money])
   s.flush() #paranthesis lagana na bhoolo
print("your fie is also saved as csv")
input(" click any where to exit ")

   
   

      
      



                                                                                        

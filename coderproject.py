need=input("DO YOU WANT TO CODE OR DECODE\n")
if(need=="code"):
    lan=input("enter you message: ")
    m=lan.split()
    print(m)
    for k in m:
     if(len(k)>3):
        b=k[2]+k[1:len(k)]+k[0]+k[2]
        print(b)
     else:
        print(k[::-1])
elif(need=="decode"):
    dec=input("enter you code your code: ")
    s=dec.split()
    print(s)
    for l in s:
        if(len(l)>3):
            t=l[-2]+l[1:-2]
            print(t)
        else:
            w=l[::-1]
            print(w)
else:
    print("enter your requirement")
input("press anywhere to exit")
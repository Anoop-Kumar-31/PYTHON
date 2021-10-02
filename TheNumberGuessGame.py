def guess(d,l):
      gue=int(input("Player two: Enter Your 4 digit guess: "))
      dic=dict()
      ll=[]
      while(gue>0):
            a=gue%10
            gue//=10
            ll.append(a)
      ll.reverse()
      for i in range(len(ll)):
            dic[i]=ll[i]
      y=0
      z=0
      for i in range(len(ll)):
            if ll[i] in l:
                  y+=1
                  if(ll[i]==l[i]):
                        z+=1
      if(y==len(ll) and z==len(ll)):
            print("Congrats right guess")
      else:
            print("Right number:",y)
            print("Right location:",z)
            if(input("Want to try again[y/s]:")=='y'):
                  guess(d,l)
            else:
                  print("Better Luck next time")
print("ENTER THE NUMBER WHICH HAS NO DUPLICATE DIGITS")
origin=int(input('Player one: Enter your 4 digit number: '))
copy=origin
d=dict()
l=[]
while(copy>0):
      a=copy%10
      copy//=10
      l.append(a)
l.reverse()
for i in range(len(l)):
      d[i]=l[i]
guess(d,l)


def stackpop(stack):
    top=len(stack)-1
    if(stack==[]):
        print("Stack is empty")
    elif(len(stack)==1):
        stack.pop()
        top=None
    else:
        stack.pop()
        top=len(stack)-1
def stackpush(stack,item):
      stack.append(item)
      top=len(stack)-1
def stackdisplay(stack):
      if(stack==[]):
            print('stack is empty')
      else:
            top=len(stack)-1
            print("------------------")
            print(stack[top],'<---Top')
            for i in range(top-1,-1,-1):
                  print(stack[i])
            print("------------------")
stack=[]
top=None
def choi():
      choice=input('Enter "I" for INPUT,"P" for POPING ELEMENT,"D" to DISPLAY STACK,or nothing to EXIT\nEnter Your Choice: ').strip()
      if(choice=='I' or choice=='i'):
            noe=int(input('enter no. of element to insert: '))
            while(noe>0):
                  no=int(input('enter no. to insert :'))
                  stackpush(stack,no)
                  noe-=1
            choi()
      elif(choice=='P' or choice=='p'):
            stackpop(stack)
            choi()
      elif(choice=='D' or choice=='d'):
            stackdisplay(stack)
            choi()
      else:
            print("Bye")
choi()

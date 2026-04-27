x=input()

stack=[]
for i in range(len(x)):
  a=0
  b=0
  if(x[i]=='+'):
    a = stack.pop()
    b = stack.pop()
    stack.append(b+a)
  elif(x[i]=='-'):
    a = stack.pop()
    b = stack.pop()
    stack.append(b-a)
  elif(x[i]=='*'):
    a = stack.pop()
    b = stack.pop()
    stack.append(b*a)
  elif(x[i]=='/'):
    a = stack.pop()
    b = stack.pop()
    stack.append(b//a)
  else:
    stack.append(int(x[i]))
print(stack[0])
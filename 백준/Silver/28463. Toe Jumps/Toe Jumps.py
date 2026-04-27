i,r,l,t=input,reversed,list,tuple
o,f,s=i(),i(),i()
a={'S':[t(f),t(s)],'E':l(zip(s,f)),'W':l(zip(r(f),r(s))),'N':[t(r(s)),t(r(f))]}
x={"[('.', 'O'), ('P', '.')]":'T',"[('I', '.'), ('.', 'P')]":'F',"[('O', '.'), ('.', 'P')]":'Lz'}
b=a[o]
if str(b) in x:print(x[str(b)])
else:print('?')
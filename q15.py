x=str(input('enter the first string'))
y=str(input('enter the second string'))
z=(x.replace(x[0],y[0])+" "+y.replace(y[0],x[0]))
print(z)
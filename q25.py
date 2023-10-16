list="web programming using php"
newlist=[i for i in list]
dict={}.fromkeys(newlist,0)
for i in list:
  if i in dict:
   dict[i]=dict[i]+1
print(list)
print(dict)
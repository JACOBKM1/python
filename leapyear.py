findyear= int(input ("enter the initial year"))
lastyear= int(input("enter the last year"))
for i in range(findyear,lastyear):
    if((i%4 == 0) and (i%100 != 0)or(i%400 == 0)):
        print(i)
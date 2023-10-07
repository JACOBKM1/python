fruits = {'Apple': 14, 'Orange': 5, 'Pinapple': 31, 'Watermelon': 61, 'Grapes': 10}
l=list(fruits.items())
l.sort()
print("the ascending order is " , l)
l.sort(reverse=True)
print('the descending order is ',l)
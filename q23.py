#Generate a list of four digit numbers in a given range with all their digits even and the
#number is a perfect square.
lower = int(input("Enter lower limit:"))
upper = int(input("Enter upper limit:"))
for i in range (lower,upper):
    if i%2==0:
        print(i)




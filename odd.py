#Python program to calculate the sum of all the odd numbers within the given range.
n=10
sum=0
for i in range(n):
    if i%2!=0:
        sum+=i
        print(sum)
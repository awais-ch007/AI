#   Activity 1
for i in range(20):
    if i % 3 == 0:
        print(i)
    elif i % 5 == 0:
        print("Bingo !!")
        print("-----")
    else:
        pass

#   Activity 2
inp = input("Enter a Number to check if it is Even or Odd       :")
if int(inp) % 2 == 0:
    print("The Number  "+inp+"  is Even Number")
else:
    print("The Number  "+inp+"  is Odd Number")

#   Activity 3
sum= 0
n = int(input("Enter Any Integer    :"))

while n !=0:
    n = int(input("Enter Any Integer    :"))
    sum=sum+n

print("Sum of the Integers Is    :", sum)

#   Activity 4

isPrime = True
i = 2
n = int(input("Enter a Number   :"))
while i<n:
    rem = n%i
    if rem == 0:
        isPrime = False
        break
    else:
        i = i+1
if isPrime:
    print(n, " is a prime Number   ")
else:
    print(n, " is not a prime Number   ")




sum = 0
i = 1
while i<=5:
    s= int(input("Enter a  Number       :"))
    sum=sum+s
    i=i+1

print("Sum Of the Integers is  :", sum)


sum = 0
i =1
while i<=10:
    print(i)
    sum=sum+i
    i=i+1

print("--------")
print("Sum is ", sum)
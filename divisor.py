x=int(input('Enter the first number : '))
y=int(input('Enter the first number : '))
l=[]
for i in range(1,x or y):
    if (x%i==0 and y%i==0):
        l.append(i)
print(max(l))
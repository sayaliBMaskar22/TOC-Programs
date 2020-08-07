q0=0
q1=1
q2=2
num=int(input("Enter the no"))
n=bin(num)
print("Binary of ",num,"is:",n)
if num%3==0:
    print(n,"is divisible by 3","\n Reminder is:",q0)
elif num%3==1:
    print(n,"is notdivisible by 3","\n Reminder is:",q1)
elif num%3==2:
    print(n,"is not divisible by 3","\n Reminder is:",q2)
print("Done!")
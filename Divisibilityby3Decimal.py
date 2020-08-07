q0=0
q1=1
q2=2
n = int(input("Enter the no"))
while n>=0:

    num=int(input("Enter the number"))
    if num%3==0:
        print(num,"is divisible by 3","\n Reminder is:",q0)
        print("It will remain in the same state [q0]")

    if num%3==1:
            print(" [q0->q1] state \n reminder is:",q1)
            break



#else:
 #       print("q1->q0 reminder is:",q1)
#if num%3==1:
 #   print(num,"is divible by 3","\n Reminder is:",q1)
    if num%3==2:
        print(num,"is not divisible by 3","\n Reminder is:",q2)
        print(" [q1->q2] state")

    elif num%3==1:
        print(" [q2->q1] state")
        break
print("Program Executed!!")
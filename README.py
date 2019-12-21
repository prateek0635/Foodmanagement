# Foodmanagement
#A food management system which will store what did you had at any time and any time you can check read that data.
import datetime
def gettime():
    return datetime.datetime.now()
def meal():
    a=gettime()
    n=int(input("Enter 1 for prateek , 2 for akash and 3 for Vivek ,4 for dheeraj"))
    k=int(input("Enter 1 for write and 2 for retrive"))

    if n==1:
        if k==1:
            with open("Prateek.txt", 'a') as op:
                print("Welcome Prateek.. ")
                j=input("\nWhat did you had?\n")
                op.write(str([str(gettime())]) + ":" + j +"\n")
                print("Successfull Written")
        else:
            print("Welcome Prateek.. ")
            with open("Prateek.txt", ) as op:
                for i in op:
                    print(i,end="")
    elif n == 2:
        if k == 1:
            with open("Akash.txt", 'a') as op:
                print("Welcome Akash.. ")
                j = input("\nWhat did you had?\n")
                op.write(str([str(gettime())]) + ":" + j + "\n")
                print("Successfull Written")
        else:
            print("Welcome Akash.. ")
            with open("Akash.txt", ) as op:
                for i in op:
                    print(i, end="")
    elif n == 3:
        if k == 1:
            with open("vivek.txt", 'a') as op:
                print("Welcome Vivek.. ")
                j = input("\nWhat did you had?\n")
                op.write(str([str(gettime())]) + ":" + j + "\n")
                print("Successfull Written")
        else:
            print("Welcome Vivek.. ")
            with open("vivek.txt", ) as op:
                for i in op:
                    print(i, end="")
    elif n == 4:
        if k == 1:
            with open("dheeraj.txt", 'a') as op:
                print("Welcome Dheeraj.. ")
                j = input("\nWhat did you had?\n")
                op.write(str([str(gettime())]) + ":" + j + "\n")
                print("Successfull Written")
        else:
            print("Welcome Dheeraj.. ")
            with open("dheeraj.txt", ) as op:
                for i in op:
                    print(i, end="")
            #
b=0
while(b==0):
    print("Welcome the the meal management system\n")
    meal()
    b=int(input("Press 1 to EXIT!!, Press 0 to continue"))

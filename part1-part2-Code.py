
def Outcome(Pass, Defer, Fail):

    if (Pass == 120):
        print("Progress")
    elif (Pass == 100):
       print("Progress - module trailer")
    elif Fail <= 60:
       print("Do not Progress - module retriever")
    
    else:
        print("Exclude")
      




try:
    Pass = int(input("pass: "))
    Defer = int(input("defer: "))
    Fail = int(input(("fail: ")))
except ValueError:
        print("Integers required")

Sum = Pass + Defer + Fail
if (Pass % 20 != 0):
    print("Range error")
elif (Defer % 20 != 0):
    print("Range error")
elif (Fail % 20 != 0):
    print("Range error") 
elif (Sum != 120):
    print("Total Incorrect")
else:
    Outcome(Pass, Defer, Fail)
        

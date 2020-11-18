def PrintHistogram(P, T, R, E):
    print("Progress: ",P,"\n")
    print("Trailing: ",T,"\n")
    print("Retriever: ",R,"\n")
    print("Excluded: ",E,"\n")

ProgressString = ""
TrailingString = ""
RetrieverString = ""
ExcludedString = ""

Quit = ""   
outcome = 0

while Quit != "q":

  
  

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
    
      if (Pass == 120):
          ProgressString = ProgressString + "*"
      elif (Pass == 100):
          TrailingString = TrailingString + "*"
      elif Fail <= 60:
          RetrieverString = RetrieverString + "*"
    
      else:
          ExcludedString = ExcludedString + "*"
      outcome = outcome + 1
      Quit = input("Enter to prompt credits of a new student, q to quit\n")    # \n creates a new line
PrintHistogram(ProgressString, TrailingString, RetrieverString, ExcludedString) 
print(outcome, " outcomes in total")
      


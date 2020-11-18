def printHistogram(P, T, R, E):
    print("Progress:",P)
    print("Trailing:",T)
    print("Retriever:",R)
    print("Excluded:",E)

dataArray = [
    [120, 0, 0],
    [100, 20, 0],
    [100, 0, 20],
    [80, 20, 20],
    [60, 40, 20],
    [40, 40, 40],
    [20, 40, 60],
    [20, 20, 80],
    [20, 0, 100],
    [0, 0, 120],
]

#method computes student is Progressed, Trailered, Retrievered, Excluded.
def printProgress(data):
    for i in data:
        if i[0] == 120:
            print("Progress")
        elif i[0] == 100:
            print("Progress (module trailer)")
        elif i[2] <= 60:
            print("Do not progress = module retriever")
        else:
            print("Excluded")
      
#method adds star for each case: Progress, Trailer, Retriever, Exclude
#from dataArray variable. And shows the outcome.
def computeHistogram(data):
  print()
    
  ProgressString = ""
  TrailingString = ""
  RetrieverString = ""
  ExcludedString = ""

  Outcome = 0
  
  for i in data:
    if i[0] == 120:
      ProgressString += "*"
    elif i[0] == 100:
      TrailingString += "*"
    elif i[2] <= 60:
      RetrieverString += "*"
    else:
      ExcludedString += "*"

    Outcome += 1
      
  printHistogram(ProgressString, TrailingString, TrailingString, ExcludedString)
  #/n moves to the new line
  print("\n", Outcome, " outcomes in total")

printProgress(dataArray)
computeHistogram(dataArray)



      


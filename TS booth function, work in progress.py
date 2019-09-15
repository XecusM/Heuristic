def xValues(maximumum, minimum):
  xVals = list(range(maximumum,minimum))
  return xVals

def yValues(maximumum, minimum):
  yVals = list(range(maximumum, minimum))
  return yVals

def getuserfunc():
  userFunc = input('Enter function: ')
  return userFunc

userinput = getuserfunc()

def combineVals(x, y):
  
  minValue = 10000
  xCoord = xValues(x, y)
  yCoord = yValues(x, y)
  for x in xCoord:
    for y in yCoord:
      fxy = eval(userinput)
      print(fxy)
      if fxy < minValue:
        minValue = fxy
        bestX = x
        bestY = y
  print('Minimum value obtained was ' + str(minValue) + ' with x-value: ' + str(bestX) + ' and y-value: ' + str(bestY))

combineVals(-10, 10)
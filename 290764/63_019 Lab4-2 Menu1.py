#63011212019
def mainMenu():
  result1 = 0.0
  result2 = 0.0
  while True:
    print("Main Menu")
    print("1. Calculate triangle area")
    print("2. Calculate rectagle area")
    print("3. Display")
    print("4. Quit")
    choice=""
    try:
      choice=int(input("Enter Choice:"))
    except ValueError:
      prin("invalid choice. Enter 1-4\n")
      continue
    if choice == 1:
      result1 = triagleArea()
      continue
    elif choice == 2:
      result2 = rectangleArea()
      continue
    elif choice == 3:
      printArea(result1, result2)
      continue
    elif choice == 4:
      print("Quit")
      break
    else:
      print("Invalid choice.Enter 1-4\n")
      continue
def triagleArea():
  base = float(input("Input base : "))
  height = float(input("Input height : "))
  area = 0.5 * base * height
  if base >= 0 or height >= 0 :
    return area
  else:
    print("Base or height less than 0")

def rectangleArea():
  width = float(input("Input width : "))
  height = float(input("Input height : "))
  area = width * height
  if width >= 0 or height >= 0:
    return area
  else:
    print("width or height less than 0")

def printArea(result1,result2):
  print("tangle = %5.2f"%(result1))
  print("rectangle = %5.2f"%(result2))


mainMenu()

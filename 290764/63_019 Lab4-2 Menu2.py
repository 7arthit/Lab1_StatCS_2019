def mainMenu():
  ans1 = 0.0
  ans2 = 0.0
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
      prin("invalid choice. Enter 1-3\n")
      continue
    if choice == 1:
      ans1 = triagleArea()
      continue
    elif choice == 2:
      ans2 = rectangleArea()
      continue
    elif choice == 3:
      printArea(ans1, ans2)
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
    #print("Triagle area of base = %5.2f and height = %5.2f is %6.2f"%(base, height, area))
  else:
    print("Base or height less than 0")

def rectangleArea():
  width = float(input("Input width : "))
  height = float(input("Input height : "))
  area = width * height
  if width >= 0 or height >= 0:
    return area
   # print("Rectangle area of base = %5.2f and height = %5.2f is %6.2f"%(width, height, area))
  else:
    print("width or height less than 0")

def printArea(ans1,ans2):
  print("tangle = %5.2f"%(ans1))
  print("rectangle = %5.2f"%(ans2))


mainMenu()

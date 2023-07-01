#63011212019
def mainMenu():
    area = 0
    while True:
      print('Main Menu')
      print('1.Calculate triangle area')
      print('2.Calculate rectangle area')
      print('3.Quit')
      choice = ''
      try:
        choice = int(input('Enter choice : '))
      except ValueError:
        print('invalid choice.Enter1-3\n')
        continue
      if choice == 1:
         triangleArea()
         continue
      elif choice == 2:
          rectangleArea()
          continue
      elif choice == 3:
         print('Quit')
         break
      else:
           print('Invild choice.Enter1-3\n')
           
def triangleArea():
  base = float(input('input base = '))
  height = float(input('input height = '))
  area = 0.5*base*height
  if base >= 0 or height >=0:
      print('Triangle area of base = %5.2f and height = %5.2f is %6.2f'%(base,height,area))
  else:
      print('base or height less than 0')

def rectangleArea():
    width = float(input('Input width = '))
    height = float(input('Input height = '))
    area = width*height
    if width >=0 or height >=0:
        print('Recatangle area of base = %5.2f and height = %5.2f is %6.2f'%(width,height,area))
    else:
        print('width or height less than 0')

######main
mainMenu()

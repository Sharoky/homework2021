while True:
   num1=input("Введите первое число")

   try:
      a=int(num1)
      break

   except:
      if num1.isalpha():
         print("Вы ввели букву вместо 1го числа")
      else:
         print("Вы ввели символ вместо 1 числа")

while True:
   num2= input("Введите второе число")
   try:
      b=int(num2)
      break

   except:
      if num2.isalpha():
         print("Вы ввели букву вместо 2го числа")
      else:
         print("Вы ввели символ вместо 2го числа")

while a!=0 and b!=0:
   if a>b:
      a=a%b
   else:
      b=b%a

print("НОД данных числел =",a+b)

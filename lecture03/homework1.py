while True:
   num=input("Введите число")
   
   try:
      n=int(num)
      break
      
   except:
      if num.isalpha():
         print("Вы ввели букву")
      else:
         print("Вы ввели символ")
           
print("N =",n)

s=[x for x in range(2,n+1)\
if x not in [i for a in [list(range(2*b,n+1,b))\
for b in range(2, n//2)] for i in a]]

print("Числа в промежутке от 2 до N")
print(s)

#Генератор случайных чисел
import random

while True:
   print("Введите число, до которого будет сгенерирован список")
   b = input()
   print("Введите количество чисел в списке")
   N = input()

   try:
      numlast=int(b)
      num=int(N)
      break

   except:
      print("Некорректный ввод данных")

      
#Сортировка Bogosort
a=[]
for i in range(num):
   a.append(random.randint(0,numlast-1))



r=sorted(a)

while a!=r:
   random.shuffle(a)
   continue
   
print(a)

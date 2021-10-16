#Генератор случайных чисел
import random
from typing import List

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

a=[]
for i in range(num):
   a.append(random.randint(0,numlast-1))


#Сортировка Bogosort
r=sorted(a)

while a!=r:
   random.shuffle(a)
   continue
   
print(a)

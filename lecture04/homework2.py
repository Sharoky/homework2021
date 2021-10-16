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

a=[]
for i in range(num):
   a.append(random.randint(0,numlast))


#Сортировка пузырьком
i=0
while i<num:

   j=0
   while j<num-i-1:

       if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
       j+=1

   i+=1
print(a)

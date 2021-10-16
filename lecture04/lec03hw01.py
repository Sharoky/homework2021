#Исправление дз за 3 лекцию

while True:
    num = input("Введите число")

    try:
        n = int(num)
        break

    except:
        print("Некорректный ввод")

print("N =", n)

a=[]

for i in range(2,n):
    a.append(i)

i=2
while i<=len(a):

    if i in a:
        for j in range(2*i,n,i):

            if j in a:
                a.remove(j)
    i+=1
print(a)

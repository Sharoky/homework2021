print("Введите два слова через пробел")
n = input()

s=n.split()
a=[x.lower() for x in s[0]]

b=[y.lower() for y in s[1]]

print(s)
z=[]

for i in a:

    if i in z:
        continue
    for k in b:

        if i==k:
            z.append(i)
            break

print("Одинаковые буквы:",z)

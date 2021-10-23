with open ('task1.txt') as f, open('output1.txt','w') as o:

    z=[int(n) for n in f]
    print("Имеем список:",z)

    for a in range(len(z)):
        for b in range(len(z)):
            for c in range(len(z)):

                if z[a]+z[b]+z[c]==2020:
                    i=z[a]*z[b]*z[c]
                    
    print(o.writelines(["The result is ",str(i)]))

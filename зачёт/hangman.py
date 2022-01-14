from tkinter import  *
import random

#Окно игры
window=Tk()
window.title("Виселица")
canvas=Canvas(window, width=600, height=600)
canvas.pack()

#Создаём фон в клеточку
def but():
    y=0
    while y<600:
        x=0
        while x<600:
            canvas.create_rectangle(x, y, x+33, y+27, fill="white", outline="blue")
            x=x+33
        y=y+27

#Начальный экран
info='''Приветствую в игре Виселица!
Попробуй отгадать загаданное слово
за ограниченное количество попыток
Удачи и хорошей игры!
'''
canvas.create_text(310, 240, text=info, fill="purple",  font=("Helvetion", "14"))


#Открываем список слов
with open('words.txt', encoding='utf-8') as f:
    words=f.readlines()
words=[x.rstrip() for x in words]



#В каждом слове выводим на экран только первую и последнюю букву. Остальое заменяем на _
def arr():
    but()
    word=random.choice(words)

    #Возвращаем все элементы кроме первого и последнего и заносим в отдельный список
    wo=word[1:-1]
    wor=[]
    for i in wo:
        wor.append(i)
    a0=canvas.create_text(282, 40, text=word[0], fill="purple", font=("Helvetice","18"))
    a1= canvas.create_text(315, 40, text="_", fill="purple", font=("Helvetice", "18"))
    a2= canvas.create_text(347, 40, text="_", fill="purple", font=("Helvetice", "18"))
    a3= canvas.create_text(380, 40, text="_", fill="purple", font=("Helvetice", "18"))
    a4= canvas.create_text(412, 40, text="_", fill="purple", font=("Helvetice", "18"))
    a5= canvas.create_text(444, 40, text="_", fill="purple", font=("Helvetice", "18"))
    a6= canvas.create_text(477, 40, text="_", fill="purple", font=("Helvetice", "18"))
    a6= canvas.create_text(510, 40, text=word[-1], fill="purple", font=("Helvetice", "18"))

#Для неизвестных букв создаем список
    list1=[1,2,3,4,5,6]
    alfabet="абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    #Победа и порожение
    win=[]
    lose=[]


    #Добавление букв в слова
    def a(v):
        ind_alf = alfabet.index(v)
        key = alfabet[ind_alf]
        if v in wor:
            ind=wor.index(v)
            b2=list1[ind]
            wor[ind]='1'

            #Координаты
            def coord():
                if b2==1:
                    x1,y1=315,40
                if b2==2:
                    x1,y1=347,40
                if b2==3:
                    x1,y1=380,40
                if b2==4:
                    x1,y1=412,40
                if b2==5:
                    x1,y1=444,40
                if b2==6:
                    x1,y1=477,40
                return x1, y1
            x1,y1 = coord()
            win.append(v)
            a2=canvas.create_text(x1, y1, text=wo[ind], fill="purple", font=("Helvetica", "18"))
            btn[key]["bg"]="green"#В случае верной буквы кнопка загарается зелёным

            #Выключенное состояние кнопок
            if not v in wor:
                btn[key]["state"]="disabled"
            if v in wor:
                win.append(v)
                ind2=wor.index(v)
                b2=list1[ind2]
                x1,y1=coord()
                canvas.create_text(x1, y1, text=wo[ind2], fill="purple", font=("Helvetica", "18"))
            if len(win)==6:
                canvas.create_text(148, 313, text="Ты победил!", fill="purple", font=("Helvetica", "25"))

                #Проверяем правильность ответов
                for i in alfabet:
                    btn[i]["state"]="disabled"
        else:
            lose.append(v)
            btn[key]["bg"]="red"#Красный-неверная буква
            btn[key]["state"]="disabled"#Кнопка становится неактивной
            if len(lose)==1:
                golova()
            elif len(lose)==2:
                telo()
            elif len(lose)==3:
                rukaP()
            elif len(lose)==4:
                rukaL()
            elif len(lose)==5:
                nogaL()
            elif len(lose)==6:
                nogaP()
                end()
            window.update()
            
    #Создаем кнопки с буквами
    btn={}
    def gen(u, x, y):
        btn[u] = Button(window, text=u, width=3, height=1, command=lambda: a(u))
        btn[u].place(x=str(x), y=str(y))

        #Подставляем буквы
    x=265
    y=110
    for i in alfabet[0:8]:
        gen(i, x, y)
        x=x+33
    x=265
    y=137
    for i in alfabet[8:16]:
        gen(i, x, y)
        x=x+33
    x=265
    y=164
    for i in alfabet[16:24]:
        gen(i, x, y)
        x=x+33
    x=265
    y=191
    for i in alfabet[24:33]:
        gen(i, x, y)
        x=x+33

    #Рисуем части туловища
    def golova():
        canvas.create_line(45, 40, 45, 305, width=4)
        canvas.create_line(45, 40, 150, 40, width=4)
        canvas.create_oval(79, 39, 120, 80, width=4, fill='black')
        window.update()
    def telo():
        canvas.create_line(100, 80, 100, 200, width=4)
        window.update()
    def rukaP():
        canvas.create_line(100, 80, 145, 100, width=4)
        window.update()
    def rukaL():
        canvas.create_line(100, 80, 45, 100, width=4)
        window.update()
    def nogaL():
        canvas.create_line(100, 200, 45, 250, width=4)
        window.update()
    def nogaP():
        canvas.create_line(100, 200, 145, 250, width=4)
        window.update()
    def end():
        canvas.create_text(148, 313, text="Ты проиграл :(",  fill="purple", font=("Helvetica", "25"))#78
        for i in alfabet:
            btn[i]["state"]="disabled"

#Кнопка начала игры
btn01 = Button(window, text="Начать", width=10, height=1, command=lambda: arr())
btn01.place(x=250, y=542)
btn01["bg"]="red"
window.mainloop()

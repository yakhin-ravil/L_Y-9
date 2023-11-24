#Создать окно регистрации/авторизации пользователя. Данные пользователя записывать в локальный файл.

from tkinter import *
from tkinter import font
import os as os

def AutorizeUser():
    def Window(): # Создаём окно и открываем его
        root.destroy() # Закрываем лишние окна
        start.destroy()
    font1 = font.Font(family= "Helvetica", size=9, weight="normal", slant="roman")
    if os.path.exists("users.txt"):
        file = open("users.txt", "r+") # Открываем файл с данными логина и пароля пользователей
        if not (login.get() or password.get()):
            message = Label(anchor=W, bg="#68b095", text="Заполните все поля!", font=font1)
        else:
            if (login.get() and password.get()) in file.read().split(): # Если введённые данные уже есть
                start = Tk()
                start.geometry("300x100")
                start.configure(background="#68b095")
                message = Label(master=start, anchor=W, bg="#68b095", text="Вы успешно авторизовались!", font=font1)  # Авторизуем пользователя
                message.pack(padx=6, pady=6)
                btn = Button(master=start, text="Закрыть", anchor=W, bg="#ff6817", fg="#FFFFFF", font=font1, command=Window)
                btn.pack(padx=6, pady=6) 
                start.mainloop()
            else:
                message = Label(anchor=W, bg="#68b095", text="Неверный логин или пароль!", font=font1) # Сообщение об ошибке входа
                message.pack(padx=6, pady=6)
    else:  # Если данные введены впервые
        message = Label(anchor=W, bg="#68b095", text="Вы не зарегистрированы!", font=font1)
        message.pack(padx=6, pady=6)

def RegisterUser():
    if not (login.get() or password.get()):
        message = Label(anchor=W, bg="#68b095", text="Заполните все поля!", font=font1)
    elif os.path.exists("users.txt"):
        file = open("users.txt", "r+") # Открываем файл с данными пользователей
    else:
        file = open("users.txt", "w") # Создаём файл с данными пользователей
        file.write(login.get() + " " + password.get() + "\n") # Регистрируем пользователя
        file.close()
        root.destroy()
        message = Label(anchor=W, bg="#68b095", text="Вы успешно зарегистрировались!", font=font1) 
        message.pack(padx=6, pady=6)
    if login.get() in file.read().split(): # Если введённые данные уже есть
        message = Label(anchor=W, bg="#68b095", text="Такой пользователь уже зарегистрирован!", font=font1)
        message.pack(padx=6, pady=6)
    else:
        file.write(login.get() + " " + password.get() + "\n") # Регистрируем пользователя
        file.close()
        root.destroy()
        message = Label(anchor=W, bg="#68b095", text="Вы успешно зарегистрировались!", font=font1) 
        message.pack(padx=6, pady=6)

root = Tk()     # Создаем окно
root.title("Окно регистрации/авторизации пользователя") 
root.geometry("400x300") 
root.configure(background="#68b095")
font1 = font.Font(family= "Helvetica", size=9, weight="normal", slant="roman")
llogin = Label(font=font1, anchor=W, background="#68b095", text="Введите Ваш логин")
llogin.pack(padx=6, pady=6)
login=Entry(bd=2)
login.pack(padx=6, pady=6)
lpassword = Label(font=font1, anchor=W, background="#68b095", text="Введите Ваш пароль") 
lpassword.pack(padx=6, pady=6)
password=Entry(bd=2)
password.pack(padx=6, pady=6)
btn1 = Button(text="Войти", bg="#ff6817", fg="#FFFFFF", font=font1, command=AutorizeUser) # Создаём кнопки и устанавливаем внутри окна
btn1.pack(padx=6, pady=6) 
btn2 = Button(text="Зарегистрироваться", bg="#ff6817", fg="#FFFFFF", font=font1, command=RegisterUser)
btn2.pack(padx=6, pady=6)
root.mainloop()
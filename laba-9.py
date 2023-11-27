#Создать окно регистрации/авторизации пользователя. Данные пользователя записывать в локальный файл.

import os
from tkinter import *
from tkinter import font
from tkinter.messagebox import showinfo, showerror

def check_login(): # Проверяем наличие логина в файле
    if os.path.exists("users.txt"):
        file = open("users.txt", "r+")
        with open("users.txt", "r") as file:
            lines = file.readlines()
            login_input = login.get()
            for line in lines:
                if login_input in line:
                    return True
        return False

def check_users(): # Проверяем наличие данных в файле о пользователе
    if os.path.exists("users.txt"):
        file = open("users.txt", "r+")
        lines = file.readlines()
        login_input = login.get()
        password_input = password.get()
        for line in lines:
            parts = line.strip().split(':')
            if len(parts) == 2:
                stored_login, stored_password = parts
                if login_input == stored_login and password_input == stored_password:
                    return True
        return False
    
def registration_user(): # Регистрируем пользователя
    if not login.get() or not password.get():
        showerror("Ошибка", "Поля 'Логин' и 'Пароль' должны быть заполнены.")
    elif check_login():
        showerror("Ошибка", "Учетная запись с таким логином уже существует.")
    else:
        with open("users.txt", "a") as file:
            file.write(f"{login.get()}:{password.get()}\n")
        root.destroy()
        showinfo("Успех", "Регистрация успешно завершена.\nПри следующем входе введите свои данные, чтобы войти в игру!")

def enter_users(): # Атвторизуем пользователя
    def start_game(): # Запускаем игоровое окно, если пользователь выполнил вход в свой аккаунт
        root.destroy()
        game = Tk()
        game.title("Игра")
        game.geometry("800x800")
        game.configure(background="#6b0568")
        game.mainloop()
    
    if check_users():
        showinfo("Успех!", "Вы вошли в свой аккаунт")
        start_game()
    else:
        showerror("Ошибка", "Неверный логин или пароль.")

root = Tk() # Создаем окно
root.title("Лабораторная работа №9") # Устанавливаем заголовок окна
root.geometry("400x300") # Устанавливаем размеры окна
root.configure(background="#F8F8FF")
font1 = font.Font(family="Verdana", size=11, weight="normal", slant="roman")
llogin = Label(font=font1, anchor=W, background="#F8F8FF", text="Введите Ваш логин")
llogin.pack(padx=6, pady=6)
login = Entry(bd=2)
login.pack(padx=6, pady=6)
lpassword = Label(font=font1, anchor=W, background="#F8F8FF", text="Введите Ваш пароль") 
lpassword.pack(padx=6, pady=6)
password = Entry(bd=2, show="*")
password.pack(padx=6, pady=6)
btn1 = Button(text="Войти", bg="#6b0568", fg="#FFFFFF", font=font1, command=enter_users)
btn1.pack(padx=6, pady=6) 
btn2 = Button(text="Зарегистрироваться", bg="#6b0568", fg="#FFFFFF", font=font1, command=registration_user)
btn2.pack(padx=6, pady=6) 

root.mainloop()
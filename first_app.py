import tkinter
from tkinter import messagebox


def button_click():
    messagebox.showinfo(title='Информация', message='Ты жмакнул на кнопку')


# --- Создание основного окна ---
root = tkinter.Tk()
root.geometry('400x250')

# --- Создание заголовка ---
root.title('Мое приложение')

# --- Создание надписи ---
label = tkinter.Label(root, text='Меня зовут Артём', font=('Arial', 16))
label.pack()

# --- Создание кнопки ---
button = tkinter.Button(root, text='Жмакать здесь', command=button_click)
button.pack()

# --- Запуск основного цикла (отрисовка) ---
root.mainloop()



# Задача №49. Решение в группах
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной
# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.

from tkinter import *
from tkinter.ttk import Combobox 
from tkinter import filedialog
from tkinter import ttk
import tkinter.messagebox

phone__book_main = []

#  Открыть файл
def open_file():
    filepath = filedialog.askopenfilename(title = "Открыть файл", initialfile = "Выберите файл")
    if filepath != "":
        global phone__book_main
        phone__book_main = []
        with open(filepath, "r", encoding = 'utf-8') as data:
            for line in data:
                if line != '\n':
                    record = line.split('::')
                    if record[3][-1] == '\n':
                        record[3] = record[3][0:-1]
                    phone__book_main.append(record)
            sort_phone_book(phone__book_main)
            # phone__book_main = phone_book
            show_phone_book(phone__book_main)

# Сохранить файл 
def save_file():
    global phone__book_main
    filepath = filedialog.asksaveasfilename(initialfile = "phone_book", title = "Сохранить файл", defaultextension='.txt', filetypes = [("txt files","*.txt"),("all files","*.*")])
    if filepath != "":
        with open(filepath, "w", encoding = 'utf-8') as file:
            for i in range(len(phone__book_main)):
                s=''
                for v in phone__book_main[i]:
                    s = s + v + '::'
                file.write(f'{s[:-2]}\n')

def sort_phone_book(phone_book):
    phone_book.sort(key=lambda e: e[0])

#  Вывод справочника в формате таблицы    
def show_phone_book(phone_book):
    phone_book_table.delete(*phone_book_table.get_children())
    for i, (l_n, f_n, p, num) in enumerate(phone_book, start=1):
        phone_book_table.insert("", "end", values=(i, l_n, f_n, p, num))

# Для кнопки показать весь справочник
def show_phone_book_btn():
    global phone__book_main
    phone_book_table.delete(*phone_book_table.get_children())
    for i, (l_n, f_n, p, num) in enumerate(phone__book_main, start=1):
        phone_book_table.insert("", "end", values=(i, l_n, f_n, p, num))

#  Выбор действия
def choice_action():
    global phone__book_main
    if combo_do.get() == 'Добавить':
        phone__book_main = add_abonent(phone__book_main)
        sort_phone_book(phone__book_main)
        show_phone_book(phone__book_main)
    if combo_do.get() == 'Найти':
        finder = find_abonent(phone__book_main)
        show_phone_book(finder)
    if combo_do.get() == 'Удалить':
        phone__book_main = delete_abonent(phone__book_main)
        sort_phone_book(phone__book_main)
        show_phone_book(phone__book_main)
    return

# Добавить запись в телефонную книгу
def add_abonent(phone_book):
    add_arr = []
    add_arr.append(txt_last_name.get())
    add_arr.append(txt_first_name.get())
    add_arr.append(txt_patronymic.get())
    add_arr.append(txt_phone_number.get())
    phone_book.append(add_arr)
    return phone_book

# Найти абонента в телефонной книге
def find_abonent(phone_book):
    res = []
    for i in phone_book:
        if txt_last_name.get().lower() in i[0].lower() and txt_first_name.get().lower() in i[1].lower() and txt_patronymic.get().lower() in i[2].lower() and txt_phone_number.get() in i[3]:
            res.append(i)
    if res == []:
        res = phone_book
        show_info() 
    return res     

# Удалить абонента из телефонной книги
def delete_abonent(phone_book):
    res = []
    for i in phone_book:
        if txt_last_name.get().lower() != i[0].lower() and txt_first_name.get().lower() != i[1].lower() and txt_patronymic.get().lower() != i[2].lower() and txt_phone_number.get() != i[3]:
            res.append(i)    
    return res

# Уведомление "абонент не найден" 
def show_info():
        msg = "абонент не найден"
        tkinter.messagebox.showinfo("Информация", msg)
        return

# Уведомление "Данные абонента успешно изменены" 
def show_info_accept():
        msg = "Данные абонента успешно изменены"
        tkinter.messagebox.showinfo("Информация", msg)
        return
    

# Функция заменяет пользователя
def change_abonent_accept():
    global phone__book_main
    count = 0
    for i in phone__book_main:
        if txt_last_name_before.get().lower() == i[0].lower() and txt_first_name_before.get().lower() == i[1].lower() and txt_patronymic_before.get().lower() == i[2].lower() and txt_phone_number_before.get() == i[3]:
           i[0] = txt_last_name_after.get()   
           i[1] = txt_first_name_after.get()
           i[2] = txt_patronymic_after.get()
           i[3] = txt_phone_number_after.get()
           count += 1
    show_info() if count == 0 else show_info_accept()    
    show_phone_book(phone__book_main)
    return phone__book_main
    
# Изменить данные пользователя Создание окна
def change_abonent():
    global phone__book_main, txt_last_name_before, txt_last_name_after, txt_first_name_before, txt_first_name_after
    global txt_patronymic_before, txt_patronymic_after, txt_phone_number_before, txt_phone_number_after
    change_win = Tk()
    w = window.winfo_screenwidth()
    h = window.winfo_screenheight()
    w = w // 2  # середина экрана
    h = h // 2
    w = w - 300  # смещение от середины
    h = h - 150
    change_win.geometry(f'600x300+{w}+{h}')
    
    user_data_before = Label(change_win, text="Данные Пользователя", font=("Isocpeur", 10))
    user_data_before.grid(column=0, row=1)
    user_data_after = Label(change_win, text="Заменить на:", font=("Isocpeur", 10))
    user_data_after.grid(column=0, row=2)
    
    # Кнопка изменить данные пользователя
    btn_change_accept = Button(change_win, text="Изменить данные", height=1, width=18, command=change_abonent_accept)
    btn_change_accept.grid(column=0, row=3)
    
    # Ячейка Фамилия
    lbl_last_name = Label(change_win, text="Фамилия", font=("Isocpeur", 10))
    lbl_last_name.grid(column=1, row=0)
    txt_last_name_before = Entry(change_win,width=15)  
    txt_last_name_before.grid(column=1, row=1, padx=5)
    txt_last_name_after = Entry(change_win,width=15)  
    txt_last_name_after.grid(column=1, row=2, padx=5)

    # Ячейка Имя
    lbl_first_name = Label(change_win, text="Имя", font=("Isocpeur", 10))
    lbl_first_name.grid(column=2, row=0)
    txt_first_name_before = Entry(change_win,width=15)  
    txt_first_name_before.grid(column=2, row=1, padx=5)
    txt_first_name_after = Entry(change_win,width=15)  
    txt_first_name_after.grid(column=2, row=2, padx=5)

    # Ячейка Отчество
    lbl_patronymic = Label(change_win, text="Отчество", font=("Isocpeur", 10))
    lbl_patronymic.grid(column=3, row=0)
    txt_patronymic_before = Entry(change_win,width=15)  
    txt_patronymic_before.grid(column=3, row=1, padx=5)
    txt_patronymic_after = Entry(change_win,width=15)  
    txt_patronymic_after.grid(column=3, row=2, padx=5)

    # Ячейка Номер телефона
    lbl_phone_number = Label(change_win, text="Номер телефона", font=("Isocpeur", 10))
    lbl_phone_number.grid(column=4, row=0, padx=5)
    txt_phone_number_before = Entry(change_win,width=15)  
    txt_phone_number_before.grid(column=4, row=1)
    txt_phone_number_after = Entry(change_win,width=15)  
    txt_phone_number_after.grid(column=4, row=2)
    
    
    return

window =Tk()
window.title("Телефонный справочник")

# text_editor = Text()

w = window.winfo_screenwidth()
h = window.winfo_screenheight()

w = w // 2  # середина экрана
h = h // 2
w = w - 400  # смещение от середины
h = h - 300
window.geometry(f'800x600+{w}+{h}')


# Кнопка открыть файл
btn_open = Button(text="Открыть файл", height=1, width=15, command=open_file)
btn_open.grid(column=0, row=0)


# Кнопка сохранить файл
btn_save = Button(text="Сохранить файл", height=1, width=15, command=save_file)
btn_save.grid(column=0, row=1)

# Кнопка показать весь справочник
btn_show = Button(text="Показать весь\n справочник", height=2, width=15, command=show_phone_book_btn)
btn_show.grid(column=0, row=2)

# Кнопка изменить данные пользователя
btn_change = Button(text="Изменить данные\n абонента", height=2, width=15, command=change_abonent)
btn_change.grid(column=0, row=3)

# Ячейка Фамилия
lbl_last_name = Label(window, text="Фамилия", font=("Isocpeur", 10))
lbl_last_name.grid(column=1, row=0)
txt_last_name = Entry(window,width=15)  
txt_last_name.grid(column=1, row=1, padx=5)

# Ячейка Имя
lbl_first_name = Label(window, text="Имя", font=("Isocpeur", 10))
lbl_first_name.grid(column=2, row=0)
txt_first_name = Entry(window,width=15)  
txt_first_name.grid(column=2, row=1, padx=5)

# Ячейка Отчество
lbl_patronymic = Label(window, text="Отчество", font=("Isocpeur", 10))
lbl_patronymic.grid(column=3, row=0)
txt_patronymic = Entry(window,width=15)  
txt_patronymic.grid(column=3, row=1, padx=5)

# Ячейка Номер телефона
lbl_phone_number = Label(window, text="Номер телефона", font=("Isocpeur", 10))
lbl_phone_number.grid(column=4, row=0, padx=5)
txt_phone_number = Entry(window,width=15)  
txt_phone_number.grid(column=4, row=1)


# Список выбора действия
combo_do = Combobox(window)
combo_do['values'] = ('Найти', 'Добавить', 'Удалить')
combo_do.current(0)
combo_do.grid(column=5, row=0)

# Кнопка выполнить действие
btn_save = Button(text="Выполнить", height=1, width=10, command=choice_action)
btn_save.grid(column=5, row=1)

# Вывод телефонной книги
cols = ('п/п','Фамилия', 'Имя', 'Отчество', 'Номер телефона')
phone_book_table = ttk.Treeview(window, columns = cols, show = 'headings')
for col in cols:
    phone_book_table.heading(col, text=col)    
    
phone_book_table.column("п/п", minwidth=0, width=40, stretch=NO)
phone_book_table.column("Фамилия", minwidth=0, width=120, stretch=YES)
phone_book_table.column("Имя", minwidth=0, width=120, stretch=YES)
phone_book_table.column("Отчество", minwidth=0, width=120, stretch=YES)
phone_book_table.column("Номер телефона", minwidth=0, width=120, stretch=YES)
phone_book_table.grid(column=1, row=3, rowspan=50, columnspan=8, pady=10)

# set column headings

window.mainloop()

from tkinter import *
from tkinter.ttk import Combobox 
from tkinter import scrolledtext  
from tkinter import filedialog
from tkinter import ttk


def clicked():
    return
    # res = "Привет {}".format(txt.get())
    # lbl.configure(text = res)

# открываем файл в текстовое поле

phone__book_main = []

#  Открыть файл
def open_file():
    filepath = filedialog.askopenfilename(title = "Открыть файл", initialfile = "Выберите файл")
    if filepath != "":
        global phone__book_main
        phone__book_main = []
        phone_book = []
        fields = ['Фамилия', 'Имя', 'Отчество', 'Телефон']
        with open(filepath, "r", encoding = 'utf-8') as data:
            for line in data:
                if line != '\n':
                    record = dict(zip(fields, line.split('::')))
                    if record['Телефон'][-1] == '\n':
                        record['Телефон'] = record['Телефон'][0:-1]
                    phone_book.append(record)
            phone__book_main = phone_book
            show_phone_book(phone_book)

# Сохранить файл 
def save_file():
    global phone__book_main
    filepath = filedialog.asksaveasfilename(initialfile = "Выберите место сохранения",title = "Сохранить файл",filetypes = (("txt file","*.txt"),("all files","*.*")))
    if filepath != "":
        with open(filepath, "w", encoding = 'utf-8') as file:
            for i in range(len(phone__book_main)):
                s=''
                for v in phone__book_main[i].values():
                    s = s + v + '::'
                file.write(f'{s[:-2]}\n')

#  Вывод справочника в формате таблицы    
def show_phone_book(phone_book):
    phone_book_table.delete(*phone_book_table.get_children())
    dicti = []
    for i in phone_book:
        dicti1 = []
        for value in i.values():
            dicti1.append(value)
        dicti.append(dicti1)
    dicti.sort(key=lambda e: e[0])
    for i, (l_n, f_n, p, num) in enumerate(dicti, start=1):
        phone_book_table.insert("", "end", values=(i, l_n, f_n, p, num))
 
 
#  Выбор действия
def choice_action():
    global phone__book_main
    if combo_do.get() == 'Добавить':
        phone__book_main = add_abonent(phone__book_main)
    
    return

def add_abonent(phone_book):
    add_arr = []
    add_arr.append(txt_last_name.get())
    
    return
 
 
 
            
             
window =Tk()
window.title("Телефонный справочник")

text_editor = Text()

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
combo_do = Combobox(window, state="readonly")
combo_do['values'] = ('Найти', 'Добавить', 'Удалить')
combo_do.current(0)
combo_do.grid(column=5, row=0)

# Кнопка выполнить действие
btn_save = Button(text="Выполнить", height=1, width=10, command=choice_action)
btn_save.grid(column=5, row=1)

# # # Вывод телефонной книги
# txt_phone_book = scrolledtext.ScrolledText(window, width=40, height=20)  
# txt_phone_book.grid(column=1, columnspan=10, rowspan=10, row=2)


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
phone_book_table.grid(column=0, row=3, columnspan=8, pady=10)

# set column headings



window.mainloop()

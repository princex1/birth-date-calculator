from tkinter import Label, Entry, Tk, messagebox, StringVar, Button
import time


def calculator():
    # global final_birth_date, final_birth_mouth, final_birth_year
    year = int(time.strftime('%Y'))
    mouth = int(time.strftime('%m'))
    date = int(time.strftime('%d'))

    birth_date = birth_date_var.get()
    birth_month = birth_month_var.get()
    birth_year = birth_year_var.get()

    try:
        final_birth_date = int(birth_date)
        final_birth_mouth = int(birth_month)
        final_birth_year = int(birth_year)

        birth_date_main = date - final_birth_date
        birth_mouth_main = mouth - final_birth_mouth
        birth_year_main = year - final_birth_year

        mouth = birth_year_main * 12
        day = birth_date_main + birth_mouth_main * 30 + birth_year_main * 356
        print(day)
        hour = day * 24
        print(hour)
        sec = day * 24 * 60 * 60
        print(sec)
        milli_sec = sec * 1000
        print(milli_sec)
        year_lab.config(text=birth_year_main)
        month_lab.config(text=mouth)
        day_lab.config(text=day)
        hour_lab.config(text=hour)
        sec_lab.config(text=sec)
        milli_sec_lab.config(text=milli_sec)

    except:
        if birth_date == '' or birth_month == '' or birth_year == '':
            messagebox.showinfo(message='please enter all info')
        else:
            messagebox.showinfo(message='please enter number')


def reset():
    birth_date_var.set('')
    birth_month_var.set('')
    birth_year_var.set('')

    year_lab.config(text='')
    month_lab.config(text='')
    day_lab.config(text='')
    hour_lab.config(text='')
    sec_lab.config(text='')
    milli_sec_lab.config(text='')


root = Tk()
root.title('birth date calculator')
root.geometry('500x400')
root.resizable(width=False, height=False)
root.config(bg='white')

birth_date_var = StringVar()
birth_month_var = StringVar()
birth_year_var = StringVar()

Label(text='birth date calculator',
      font=('Shruti', '15', 'bold'),
      bg='white',
      padx=150).grid(row=0, column=0, columnspan=8)

Label(text='', bg='white').grid(row=1, column=1)

Label(text='birth date: ', bg='white', font=('Shruti', '10', 'bold')).grid(row=2, column=1)
Entry(textvariable=birth_date_var, bg='#BEBDBD').grid(row=2, column=2)

Label(text='birth month: ', bg='white', font=('Shruti', '10', 'bold')).grid(row=3, column=1)
Entry(textvariable=birth_month_var, bg='#BEBDBD').grid(row=3, column=2)

Label(text='birth year: ', bg='white', font=('Shruti', '10', 'bold')).grid(row=4, column=1)
Entry(textvariable=birth_year_var, bg='#BEBDBD').grid(row=4, column=2)

Label(text='', bg='white').grid(row=5, column=1)

Button(text='  Go!  ', command=calculator).grid(row=6, column=2)

Button(text='reset', command=reset).grid(row=6, column=3)

Label(text='', bg='white').grid(row=5, column=1)

Label(text='year you lived: ', font=('Shruti', '10', 'bold'), bg='white').grid(row=7, column=1)

year_lab = Label(text='', font=('Shruti', '10', 'bold'), bg='white')
year_lab.grid(row=7, column=2)

Label(text='month you lived: ', font=('Shruti', '10', 'bold'), bg='white').grid(row=8, column=1)

month_lab = Label(text='', font=('Shruti', '10', 'bold'), bg='white')
month_lab.grid(row=8, column=2)

Label(text='day you lived: ', font=('Shruti', '10', 'bold'), bg='white').grid(row=9, column=1)

day_lab = Label(text='', font=('Shruti', '10', 'bold'), bg='white')
day_lab.grid(row=9, column=2)

Label(text='hour you lived: ', font=('Shruti', '10', 'bold'), bg='white').grid(row=10, column=1)

hour_lab = Label(text='', font=('Shruti', '10', 'bold'), bg='white')
hour_lab.grid(row=10, column=2)

Label(text='second you lived: ', font=('Shruti', '10', 'bold'), bg='white').grid(row=11, column=1)

sec_lab = Label(text='', font=('Shruti', '10', 'bold'), bg='white')
sec_lab.grid(row=11, column=2)

Label(text='milli second you lived: ', font=('Shruti', '10', 'bold'), bg='white').grid(row=12, column=1)

milli_sec_lab = Label(text='', font=('Shruti', '10', 'bold'), bg='white')
milli_sec_lab.grid(row=12, column=2)

root.mainloop()

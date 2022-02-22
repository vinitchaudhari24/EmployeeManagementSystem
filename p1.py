from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *
import matplotlib.pyplot as plt
import pandas as pd
import requests
import bs4
import os


def f1():
    global add_window, ent_id, ent_name, ent_salary
    add_window = Toplevel(main_window)
    add_window.title("add")
    add_window.geometry("500x600+500+125")
    add_window.config(bg="cyan")
    lbl_id = Label(add_window, text="Enter Id", font=f)
    lbl_id.pack(pady=10)

    ent_id = Entry(add_window, font=f, width=20)
    ent_id.pack(pady=10)

    lbl_name = Label(add_window, text="Enter name", font=f)
    lbl_name.pack(pady=10)

    ent_name = Entry(add_window, font=f, width=20)
    ent_name.pack(pady=10)

    lbl_salary = Label(add_window, text="Enter salary", font=f)
    lbl_salary.pack(pady=10)

    ent_salary = Entry(add_window, font=f, width=20)
    ent_salary.pack(pady=10)

    btn_submit = Button(add_window, text="submit", font=f, command=save)
    btn_submit.pack(pady=10)

    btn_back = Button(add_window, text="back", font=f, command=f11)
    btn_back.pack(pady=10)

    p1 = PhotoImage(file='C:/Users/Vinit/Desktop/python/Internship project/image.png')
    add_window.iconphoto(False, p1)

def f11():
    main_window.deiconify()
    add_window.withdraw()


def f2():
    global view_window
    view_window = Toplevel(main_window)
    view_window.title("view records")
    view_window.geometry("900x600+300+125")
    view_window.config(bg="cyan")
    view_data = ScrolledText(view_window, width=800, height=10, font=f)
    view_data.pack(pady=10)

    btn_vw_back = Button(view_window, text="Back", bd=1, font=f, command=f22)
    btn_vw_back.pack(pady=10)

    p1 = PhotoImage(file='C:/Users/Vinit/Desktop/python/Internship project/image.png')
    view_window.iconphoto(False, p1)
    view_data.delete(1.0, END)
    info = ""
    con = None
    try:
        con = connect("C:/Users/Vinit/Desktop/python/Internship project/ems.db")
        cursor = con.cursor()
        sql = "select * from  employee"
        cursor.execute(sql)
        data = cursor.fetchall()
        for d in data:
            info = info + "id: " + str(d[0]) + "         name : " + str(d[1]) + "                 salary: " + str(
                d[2]) + "\n"
        view_data.insert(INSERT, info)

    except Exception as e:
        showerror("Issue", e)
    finally:
        if con is not None:
            con.close()


def f22():
    main_window.deiconify()
    view_window.withdraw()


def f3():
    global update_window, ent_up_id, ent_up_name, ent_up_salary
    update_window = Toplevel(main_window)
    update_window.title("update records")
    update_window.geometry("500x600+500+125")
    update_window.config(bg="cyan")
    lbl_up_id = Label(update_window, text="Enter id", font=f)
    lbl_up_id.pack(pady=10)

    ent_up_id = Entry(update_window, font=f, width=20)
    ent_up_id.pack(pady=10)

    lbl_up_name = Label(update_window, text="Enter new name", font=f)
    lbl_up_name.pack(pady=10)

    ent_up_name = Entry(update_window, font=f, width=20)
    ent_up_name.pack(pady=10)

    lbl_up_salary = Label(update_window, text="Enter new salary", font=f)
    lbl_up_salary.pack(pady=10)

    ent_up_salary = Entry(update_window, font=f, width=20)
    ent_up_salary.pack(pady=10)

    btn_up_sub = Button(update_window, text="update", font=f, command=update)
    btn_up_sub.pack(pady=10)

    btn_up_back = Button(update_window, text="back", font=f, command=f33)
    btn_up_back.pack(pady=10)

    p1 = PhotoImage(file='C:/Users/Vinit/Desktop/python/Internship project/image.png')
    update_window.iconphoto(False, p1)

def f33():
    main_window.deiconify()
    update_window.withdraw()


def f4():
    global del_window, ent_id_del
    del_window = Toplevel(main_window)
    del_window.title("delete records")
    del_window.geometry("500x500+500+125")
    del_window.config(bg="cyan")
    lbl_id_del = Label(del_window, text="enter id", font=f)
    lbl_id_del.pack(pady=20)

    ent_id_del = Entry(del_window, font=f, width=20)
    ent_id_del.pack(pady=10)

    btn_sub_del = Button(del_window, text="delete record", font=f, command=delete)
    btn_sub_del.pack(pady=10)

    btn_back_del = Button(del_window, text="back", font=f, command=f44)
    btn_back_del.pack(pady=10)

    p1 = PhotoImage(file='C:/Users/Vinit/Desktop/python/Internship project/image.png')
    del_window.iconphoto(False, p1)

def f44():
    main_window.deiconify()
    del_window.withdraw()


def update():
    con = None
    try:

        id = int(ent_up_id.get())
        name = ent_up_name.get()
        salary = int(ent_up_salary.get())
        con = connect("C:/Users/Vinit/Desktop/python/Internship project/ems.db")
        cursor = con.cursor()
        sql = "update employee set name='%s', salary='%s' where id='%s' "
        cursor.execute(sql % (id, name, salary))
        if cursor.rowcount == 1:
            con.commit()
            showinfo("success", "record updated")
        else:
            showerror("issue", "not updated")

    except Exception as e:
        showerror("issue", e)
        con.rollback()
    finally:
        if con is not None:
            con.close()


def save():
    con = None
    try:
        id = int(ent_id.get())
        name = ent_name.get()
        salary = int(ent_salary.get())
        if (id == ""):
            showerror("issue", "Fields cannot be empty")
        elif (name == ""):
            showerror("issue", "Fields cannot be empty")
        elif (salary == ""):
            showerror("issue", "Fields cannot be empty")
        elif (len(name) <= 2):
            showerror("issue", "enter valid name")
        elif (salary <= 8000):
            showerror("issue", "enter valid salary")


        else:

            con = connect("C:/Users/Vinit/Desktop/python/Internship project/ems.db")
            cursor = con.cursor()
            sql = "insert into employee values('%d', '%s', '%d')"
            cursor.execute(sql % (id, name, salary))
            con.commit()
            showinfo("Success", "record added")

    except Exception as e:
        showerror("Issue", e)


    finally:
        ent_id.delete(0, END)
        ent_name.delete(0, END)
        ent_salary.delete(0, END)
        if con is not None:
            con.close()


def delete():
    con = None
    try:
        con = connect("C:/Users/Vinit/Desktop/python/Internship project/ems.db")
        cursor = con.cursor()
        sql = "delete from employee where id = '%d' "
        id = int(ent_id_del.get())
        cursor.execute(sql % (id))
        if cursor.rowcount == 1:
            con.commit()
            showinfo("success", "record deleted")

    except Exception as e:
        showerror("issue", e)
        con.rollback()
    finally:
        ent_id_del.delete(0, END)
        if con is not None:
            con.close()


def chart_ems():
    con = None
    try:

        con = connect("C:/Users/Vinit/Desktop/python/Internship project/ems.db")
        cursor = con.cursor()
        sql = "select name, salary from employee order by salary desc limit(5)"
        cursor.execute(sql)
        data = cursor.fetchall()
        print(data)
        ddata = dict(data)
        NAME = list(ddata.keys())
        SALARY = list(ddata.values())

        # Name = []
        # Salary = []
        # info1 = ""
        # info2 = ""
        # data0 = data[0]
        # data1 = data[1]
        # data2 = data[2]
        # data3 = data[3]
        # data4 = data[4]
        # print(data0)
        # print(data1)
        # print(data2)
        # print(data3)
        # print(data4)

        # for d in data:
        #	info1 = info1 + str(d)
        #	info2 = info2 + str(d)
        # print(info1)
        # print(info2)

        plt.bar(NAME, SALARY, color='powderblue', width=0.4)
        plt.xlabel("Employee")
        plt.ylabel("Salary")
        plt.title("TOP 5 HIGHEST PAID EMPLOYEE")
        plt.show()


    except Exception as e:
        showerror("issue", e)

    finally:
        if con is not None:
            con.close()


try:
    wa = "https://www.brainyquote.com/quote_of_the_day"
    res = requests.get(wa)
    print(res)
    data = bs4.BeautifulSoup(res.text, "html.parser")
    info = data.find("img", {"class": "p-qotd"})
    quote = info["alt"]


except Exception as e:
    print("issue ", e)

main_window = Tk()
main_window.title("E.M.S")
main_window.geometry("500x600+500+125")
main_window.config(bg="cyan")
f = ("Ariel", 20, "bold")

btn_add = Button(main_window, text="Add", font=f, width=20, command=f1)
btn_add.pack(pady=20)

btn_view = Button(main_window, text="View", font=f, width=20, command=f2)
btn_view.pack(pady=10)

btn_update = Button(main_window, text="Update", font=f, width=20, command=f3)
btn_update.pack(pady=10)

btn_delete = Button(main_window, text="Delete", font=f, width=20, command=f4)
btn_delete.pack(pady=10)

btn_charts = Button(main_window, text="Charts", font=f, width=20, command=chart_ems)
btn_charts.pack(pady=10)

lbl_quote = Label(main_window, text="QTOD: " + quote)
lbl_quote.pack(pady=10)

p1 = PhotoImage(file='C:/Users/Vinit/Desktop/python/Internship project/image.png')
main_window.iconphoto(False, p1)

# add window



# view window


# update window



# delete window



main_window.mainloop()






















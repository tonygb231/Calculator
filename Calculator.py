from tkinter import *


def expression(value: int) -> int:
    current = label.cget("text")
    new = str(current) + value
    label.config(text=new)


def delete_all():
    label.config(text=" ")


def delete():
    current = label.cget("text")
    new = str(current)[:-1]
    label.config(text=new)


def result():
    try:
        label.config(text=(eval(label.cget("text"))))
    except ZeroDivisionError:
        label.config(text='Can not divided by zero')
    except SyntaxError:
        label.config(text='Type error')
    except TypeError:
        pass


window = Tk()

window.title("Calculator")
window.geometry("360x580")
window.config(bg="black")

cal_name = Label(window, text="Math destroyer 3000", font=("Arial", 15), fg="red", bg="black", bd=10)
cal_name.pack()

label = Label(window, text=" ", bd=12, bg="white", padx=336, fg="black", font=("Arial", 17), justify="right")
label.pack()

AC = Button(window, text="AC", font=("Ariel", 15),
            padx=20, pady=20, bd=5, command=delete_all)
AC.place(x=0, y=165)

delete = Button(window, text="D", font=("Arial", 15),
                padx=27, pady=20, bd=5, command=delete)
delete.place(x=90, y=165)

result = Button(window, text="=", font=("Arial", 15),
                padx=27, pady=20, bd=5, command=result)
result.place(x=180, y=165)

divide = Button(window, text="/", font=("Ariel", 15),
                padx=30, pady=20, bd=5, command=lambda: expression("/"))
divide.place(x=270, y=165)

seven = Button(window, text="7", font=("Ariel", 15),
               padx=28, pady=20, bd=5, command=lambda: expression("7"))
seven.place(x=0, y=248)

eight = Button(window, text="8", font=("Ariel", 15),
               padx=28, pady=20, bd=5, command=lambda: expression("8"))
eight.place(x=90, y=248)

nine = Button(window, text="9", font=("Ariel", 15),
              padx=28, pady=20, bd=5, command=lambda: expression("9"))
nine.place(x=180, y=248)

multiply = Button(window, text="*", font=("Ariel", 15),
                  padx=28, pady=20, bd=5, command=lambda: expression("*"))
multiply.place(x=270, y=248)

four = Button(window, text="4", font=("Ariel", 15),
              padx=28, pady=20, bd=5, command=lambda: expression("4"))
four.place(x=0, y=330)

five = Button(window, text="5", font=("Ariel", 15),
              padx=28, pady=20, bd=5, command=lambda: expression("5"))
five.place(x=90, y=330)

six = Button(window, text="6", font=("Ariel", 15),
             padx=28, pady=20, bd=5, command=lambda: expression("6"))
six.place(x=180, y=330)

minus = Button(window, text="-", font=("Ariel", 15),
               padx=29, pady=20, bd=5, command=lambda: expression("-"))
minus.place(x=270, y=330)

one = Button(window, text="1", font=("Ariel", 15),
             padx=28, pady=20, bd=5, command=lambda: expression("1"))
one.place(x=0, y=413)

two = Button(window, text="2", font=("Ariel", 15),
             padx=28, pady=20, bd=5, command=lambda: expression("2"))
two.place(x=90, y=413)

three = Button(window, text="3", font=("Ariel", 15),
               padx=28, pady=20, bd=5, command=lambda: expression("3"))
three.place(x=180, y=413)

add = Button(window, text="+", font=("Ariel", 15),
             padx=27, pady=20, bd=5, command=lambda: expression("+"))
add.place(x=270, y=413)

left_parentheses = Button(window, text="(", font=("Ariel", 15),
                          padx=30, pady=20, bd=5, command=lambda: expression("("))
left_parentheses.place(x=0, y=495)

zero = Button(window, text="0", font=("Ariel", 15),
              padx=28, pady=20, bd=5, command=lambda: expression("0"))
zero.place(x=90, y=495)

decimal = Button(window, text=".", font=("Ariel", 15),
                 padx=31, pady=20, bd=5, command=lambda: expression("."))
decimal.place(x=180, y=495)

right_parentheses = Button(window, text=")", font=("Ariel", 15),
                           padx=29, pady=20, bd=5, command=lambda: expression(")"))
right_parentheses.place(x=270, y=495)

window.mainloop()

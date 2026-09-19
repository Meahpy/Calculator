from tkinter import Tk, Entry, Button, StringVar

class Calculator:
    def __init__(self, master):
        master.title("Kalkulator Elfan")
        master.geometry("357x427+0+0")
        master.config(bg="gray")
        master.resizable(False,False)

        self.equation=StringVar()
        self.entry_value=""
        Entry(width=17, bg="#ccddff", font=("Tahoma",28),textvariable=self.equation).grid(row=0, column=0, columnspan=4)

        buttons = [
            ("(", 1, 0 ), (")", 1, 1), ("%", 1, 2), ("/", 1, 3),
            ("7", 2, 0 ), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3),
            ("4", 3, 0 ), ("5", 3, 1), ("6", 3, 2), ("+", 3, 3),
            ("1", 4, 0 ), ("2", 4, 1), ("3", 4, 2), ("-", 4, 3),
            ("c", 5, 0 ), ("0", 5, 1), (".", 5, 2), ("=", 5, 3)

        ]
        for (text, row, col)in buttons:
            if text == "=":
                Button(master, width=11, height=4, text=text, bg="lightblue", command=self.solve).grid(row=row, column=col)
            elif text == "c":
                Button(master, width=11, height=4, text=text, bg="white", command=self.clear).grid(row=row, column=col)
            else:
                Button(master, width=11, height=4, text=text, bg="white", command=lambda t=text:self.show(t)).grid(row=row, column=col)

        master.bind("<Key>", self.key_press)

    def key_press(self, event):
        valid_keys= "0123456789+-*/.()"
        if event.char in valid_keys:
            self.show(event.char)
        elif event.keysym == "Return":
            self.solve()
        elif event.keysym == "BackSpace":
            self.entry_value = self.entry_value[:-1]
            self.equation.set(self.entry_value)


    def show(self, value):
        if self.entry_value == "Error":
            self.entry_value = ""

        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value=""
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            result=str(eval(self.entry_value))
            self.equation.set(result)
            self.entry_value = result
        except (ZeroDivisionError, SyntaxError):
            self.equation.set("Error")
            self.entry_value= "Error"


root=Tk()
calculator=Calculator(root)
root.mainloop()

        
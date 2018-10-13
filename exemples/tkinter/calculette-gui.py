from tkinter import *

class App:

    def operation(self, sign):
        self.label_sign_op.config(text=sign)
        try:
            result = eval('a' + sign + 'b', {'a':self.var_a.get(), 'b':self.var_b.get()})
            self.label_result.config(text=str(result))
        except Exception as e:
            error = Toplevel()
            label_error = Label(error, text='Error : {}'.format(e))
            label_error.pack(fill=X)
            btn_quitter = Button(error, text='Ok', command=error.destroy)
            btn_quitter.pack(fill=X)

    def __init__(self, master_ui):
        master_ui.title('Calculatrice')

        label_a = Label(master_ui, text='A')
        label_a.grid(sticky=W, column=0, row=0, columnspan=3)

        label_b = Label(master_ui, text='B')
        label_b.grid(sticky=W, column=0, row=1, columnspan=3)

        label_a_op = Label(master_ui, text='A')
        label_a_op.grid(sticky=W, column=0, row=2)

        self.label_sign_op = Label(master_ui, text=' ')
        self.label_sign_op.grid(sticky=W, column=1, row=2)

        label_b_op = Label(master_ui, text='B')
        label_b_op.grid(sticky=W, column=2, row=2)

        self.var_a = DoubleVar()
        self.entry_a = Entry(master_ui, textvariable=self.var_a)
        self.entry_a.grid(sticky=W+E, column=3, row=0)

        self.var_b = DoubleVar()
        self.entry_b = Entry(master_ui, textvariable=self.var_b)
        self.entry_b.grid(sticky=W+E, column=3, row=1)

        label_action = Label(master_ui, text='Action')
        label_action.grid(sticky=N+S+W+E, column=4, row=0, columnspan=2)

        self.label_result = Label(master_ui, text='')
        self.label_result.grid(sticky=E, column=3, row=2)

        btn_plus = Button(master_ui, text='+', command=lambda sign='+': self.operation(sign))
        btn_plus.grid(sticky=N+S+W+E, column=4, row=1)

        btn_moins = Button(master_ui, text='-', command=lambda sign='-': self.operation(sign))
        btn_moins.grid(sticky=N+S+W+E, column=5, row=1)

        btn_multi = Button(master_ui, text='*', command=lambda sign='*': self.operation(sign))
        btn_multi.grid(sticky=N+S+W+E, column=4, row=2)

        btn_div = Button(master_ui, text='/', command=lambda sign='/': self.operation(sign))
        btn_div.grid(sticky=N+S+W+E, column=5, row=2)


if __name__ == '__main__':
    root = Tk()
    app = App(root)
    root.mainloop()

import tkinter as tk
from src.client.resolvers import check_login
import tkinter.messagebox


class LoginForm(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.username = tk.StringVar()
        self.userpassword = tk.StringVar()
        self.font = ('Arial Bold', 16)

        lbl_main = tk.Label(self, text="Вход в систему", font=self.font)
        lbl_login = tk.Label(self, text="Логин", font=self.font)
        lbl_pass = tk.Label(self, text='Пароль', font=self.font)
        entry_login = tk.Entry(self, font=self.font,
                               textvariable=self.username)
        entry_pass = tk.Entry(self, font=self.font,
                              textvariable=self.userpassword)
        btn_enter = tk.Button(self, text='Вход', font=self.font,
                              command=self.login)
        btn_close = tk.Button(self, text='Отмена', font=self.font)

        lbl_main.grid(row=0, columnspan=2, column=1)
        lbl_login.grid(row=1, column=0, pady=10, ipadx=10)
        entry_login.grid(row=1, column=1, columnspan=3, padx=30, pady=10)
        lbl_pass.grid(row=2, column=0, pady=10, ipadx=10)
        entry_pass.grid(row=2, column=1, columnspan=3, padx=30, pady=10)
        btn_enter.grid(row=3, column=1, pady=10)
        btn_close.grid(row=3, column=2, pady=10)

    def login(self):
        l = check_login(login=self.username.get(),
                        password=self.userpassword.get())

        if not l:
            tk.messagebox.showerror(title="Wrong login",
                                    message="Логин или пароль неверны")
        else:
            tk.messagebox.showinfo(title='Успешно', message='Успешный вход')



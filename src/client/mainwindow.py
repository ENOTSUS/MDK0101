import tkinter as tk
from src.client.login_form import LoginForm

font = ('Arial Bold', 14)


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.btn = tk.Button(text="Login", font=font,
                             command=self.open_login)
        self.btn.pack(pady=20, padx=50)

    def open_login(self):
        login_form = LoginForm(self)
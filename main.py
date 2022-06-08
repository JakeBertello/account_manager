from sqlite3 import Row
from tkinter.tix import COLUMN, ROW
import constants
import tkinter as tk
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class AccountManager(ctk.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title("Account Manager")
        self.geometry(f"{constants.MAIN_WINDOW_WIDTH}x{constants.MAIN_WINDOW_HEIGHT}")
        self.resizable(False, False)
        
        add_account_button = ctk.CTkButton(master=self,
                                 width=100,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Add Account",
                                 hover=True,
                                 command=self.add_account_button_event)
        add_account_button.place(relx=0.995, rely=0.011, anchor=tk.NE)
        
        account_frame = ctk.CTkFrame(master=self,
                                     width=790,
                                     height=357)
        account_frame.grid_propagate(False)
        account_frame.place(relx=0.5, rely=0.545, anchor=tk.CENTER)
        
        for i in range(6):
            account_frame.columnconfigure(i, weight=1, uniform=True)
        
        for j in range(10):
            account_frame.rowconfigure(j, weight=1, uniform=True)
        
    def add_account_button_event(self):
        add_account_window = ctk.CTkToplevel(self)
        add_account_window.title("Add Account")
        add_account_window.geometry(f"{constants.ADD_ACCOUNT_WINDOW_WIDTH}x{constants.ADD_ACCOUNT_WINDOW_HEIGHT}")

app = AccountManager()
app.mainloop()
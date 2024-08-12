from tkinter import *
from tkinter import ttk
import datetime
import re
import sqlite3
from contextlib import closing
import customtkinter as ctk
from tkcalendar import DateEntry
import os
import csv
from functools import partial

connection = sqlite3.connect("Task_6_Database.db")

path= os.getcwd()

# Defining variables to make it easier to change the size of everything
standard_height = 30
standard_width = 250
standard_font = "", 18
standard_y_padding = 5
standard_x_padding = 5

# Defining colour mode for the program (light or dark)
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.title("Task_6")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"500x275")
root.resizable(False, False)

def log_in_window():

    for widget in root.winfo_children():
        widget.destroy()
    
    password_label = ctk.CTkLabel(
        root,
        text="Please Enter Your \n Username And Password",
        font=standard_font)
    password_label.pack(pady=standard_y_padding)

    username_entry = ctk.CTkEntry(
        root,
        placeholder_text="Enter Username",
        font=standard_font,
        width=standard_width,
        height=standard_height)
    username_entry.pack(pady=standard_y_padding)

    password_entry = ctk.CTkEntry(
        root,
        placeholder_text="Enter Password",
        font=standard_font,
        width=standard_width,
        height=standard_height,
        show='*')
    password_entry.pack(pady=standard_y_padding)

    login_button = ctk.CTkButton(
        root,
        text="Log In",
        font=standard_font,
        width=standard_width,
        height=standard_height,
        command=lambda: main(button_type = ["login",username_entry.get(),password_entry.get(),"N/A","N/A"]))
    login_button.pack(pady=standard_y_padding)

    close_button = ctk.CTkButton(
        root,
        text="Close Window",
        font=standard_font,
        width=standard_width,
        height=standard_height,
        command=root.destroy)
    close_button.pack(pady=standard_y_padding)

def display_user_password_window():
    for widget in root.winfo_children():
        widget.destroy()

    display_password_label = ctk.CTkLabel(
        root,
        text="secret_question",
        font=standard_font)
    display_password_label.pack(pady=standard_y_padding)

    close_button = ctk.CTkButton(
        root,
        text="Go Back to Login",
        font=standard_font,
        width=standard_width,
        height=standard_height,
        command=lambda:main(button_type=None))
    close_button.pack(pady=standard_y_padding)

class ErrorWindow:
    def __init__(self,parent,message,on_close):
        self.parent = parent
        self.message = message
        self.on_close = on_close

    def create(self):
        error_window = ctk.CTkToplevel(self.parent)
        error_window.title("Error")
        error_window.resizable(False, False)

        error_label = ctk.CTkLabel(
            error_window,
            text=self.message,
            font=standard_font)
        error_label.pack(pady=standard_y_padding)

        close_button = ctk.CTkButton(
            error_window,
            text="Close",
            font=standard_font,
            width=standard_width,
            height=standard_height,
            command=lambda: [error_window.destroy(),self.on_close()])
        close_button.pack(pady=standard_y_padding)

class CredentialsChecker:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def username_checker(self):
        usernames = str(connection.cursor().execute("SELECT Username FROM Accounts").fetchall()).replace("(","").replace(")","").replace("'","").replace(",","").replace(" ",",")
        if self.username not in usernames:
            username_in_usernames = False
            return username_in_usernames
        else:
            username_in_usernames = True
            return username_in_usernames
        
    def password_checker(self):
        database_password = connection.cursor().execute(f"SELECT Password FROM Accounts WHERE Username= '{self.username}'").fetchone()[0]
        if self.password != database_password:
            correct_password = False
            return correct_password
        else:
            correct_password = True
            return correct_password
    


def main(button_type): 
    for widget in root.winfo_children():
        widget.destroy()

    if button_type == None:
        log_in_window()
    else:    
        button_value = button_type[0]
        username = button_type[1]
        password = button_type[2]
        other_value_1 = button_type[3]
        secret_question_entry = button_type[4]

        print(button_type)
        print(button_value)
        print(username)
        print(password)
        print(other_value_1)
        print(secret_question_entry)

        credentials_checker_1 = CredentialsChecker(username, password)
        credentials_checker_2 = CredentialsChecker(username, password)
        error_window_1 = ErrorWindow(root, "Your password or username was incorect.\nPlease go back and try again.", lambda: log_in_window())
        error_window_2 = ErrorWindow(root, "We encountered a problem, please try again.", lambda: log_in_window())
        error_window_3 = ErrorWindow(root, "Your secret question answer was incorect.\nPlease go back and try again.", lambda: log_in_window())

        if button_value == "login":
            if credentials_checker_1.username_checker() == True:
                if credentials_checker_2.password_checker() == True:
                    print("yay1")
                else:
                    error_window_1.create()
            else:
                error_window_1.create()
        else:
            error_window_2.create()







if __name__ == "__main__":
    main(button_type = None)

root.mainloop()
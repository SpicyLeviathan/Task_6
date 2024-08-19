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
        command=lambda: main(button_type = ["login",username_entry.get(),password_entry.get(),"N/A"]))
    login_button.pack(pady=standard_y_padding)

    close_button = ctk.CTkButton(
        root,
        text="Close Window",
        font=standard_font,
        width=standard_width,
        height=standard_height,
        command=root.destroy)
    close_button.pack(pady=standard_y_padding)

def account_type_ID_retreval(username):
    account_type_ID = str(connection.cursor().execute(f"SELECT AccountTypeID FROM User WHERE Username= '{username}'").fetchall()).replace("(","").replace(")","").replace("'","").replace(",","").replace("[","").replace("]","").replace(" ","")
    return(account_type_ID)

def events(left_frame,right_frame):
    for widgets in left_frame.winfo_children():
        widgets.destroy()
    for widgets in right_frame.winfo_children():
        widgets.destroy()

    data=[]
    cursor = connection.cursor()
    data = cursor.execute("""
        SELECT
            Catering.CateringID AS Catering_ID,
            Event.EventName AS Event_Name,
            User.FirstName ||' '|| User.LastName AS Requester,
            Meals.MealName AS Meal,
            Catering.CardID AS Card_ID,
            TypesOfCatering.TypesOfCateringName AS Type_Of_Catering,
            Catering.SpecificCateringRequests AS Specific_Catering_Requests
        FROM Catering
        JOIN "User"
        ON User.UserID = Catering.UserID 
        JOIN Meals
        ON Meals.MealID = Catering.MealID
        JOIN Event
        ON Event.EventID = Catering.EventID
        JOIN TypesOfCatering
        ON TypesOfCatering.TypesOfCateringID = Catering.TypesOfCateringID;""").fetchall()

    treeview_frame= ctk.CTkFrame(right_frame, fg_color= "#292929")
    treeview_frame.pack()

    ttk.Style().theme_use("clam")
    ttk.Style().configure("Treeview", background="#292929",foreground="White", fieldbackground="#292929")
    ttk.Style().configure('Treeview.Heading', background='#292929', foreground='White')

    columns = ("CateringID", "Event_Name", "Requester_Name", "Meal", "CardID", "Specific_Requests", "Specific_Requests")
    events_treeview = ttk.Treeview(treeview_frame, columns=columns, show="headings", height= 40)

    events_treeview.column("# 1",anchor=W, stretch=True, width = 100)
    events_treeview.heading("# 1", text="CateringID")
    events_treeview.column("# 2", anchor=W, stretch=True,width = 200)
    events_treeview.heading("# 2", text="Event_Name")
    events_treeview.column("# 3", anchor=W, stretch=True,width = 200)
    events_treeview.heading("# 3", text="Requester_Name")
    events_treeview.column("# 4", anchor=W, stretch=True,width = 200)
    events_treeview.heading("# 4", text="Meal")
    events_treeview.column("# 5", anchor=W, stretch=True,width = 100)
    events_treeview.heading("# 5", text="CardID")
    events_treeview.column("# 6", anchor=W, stretch=True,width = 150)
    events_treeview.heading("# 6", text="Type_Of_Catering")
    events_treeview.column("# 7", anchor=W, stretch=True,width = 400)
    events_treeview.heading("# 7", text="Specific_Requests")

    for row in data:
        events_treeview.insert("", "end", values=row)

    treeviewScrollbarY= ttk.Scrollbar(treeview_frame, command=events_treeview.yview)
    treeviewScrollbarY.pack(side=LEFT, fill=Y)
    events_treeview.config(yscrollcommand=treeviewScrollbarY.set)
    events_treeview.pack(side=RIGHT)

def select_event_menu(left_frame,right_frame):
    for widgets in left_frame.winfo_children():
        widgets.destroy()
    for widgets in right_frame.winfo_children():
        widgets.destroy()
    #Creating a label
    label = ctk.CTkLabel(left_frame, text="Select The Event You Wish To View", fg_color="transparent", font= standard_font)
    label.pack(pady = standard_y_padding)

    #Creating list box frame
    listbox_frame= ctk.CTkFrame(left_frame, fg_color= "#292929")
    listbox_frame.pack(pady = standard_y_padding)

    events_listbox = Listbox(listbox_frame, bg= "#292929", fg= "Silver", width= 30, height= 25, font= standard_font)
    cursor = connection.cursor()
    data = cursor.execute("SELECT EventID,EventName FROM Event").fetchall()
    for row in data:
        events_listbox.insert(END, row)
    events_listbox.pack(side=LEFT)

    listboxScrollbar= ctk.CTkScrollbar(listbox_frame, command=events_listbox.yview)
    listboxScrollbar.pack(side="right", fill=Y)
    events_listbox.config(yscrollcommand=listboxScrollbar.set) 

    #Creating a button
    changeRankButton = ctk.CTkButton(
        left_frame,
        text= "View Event Menu",
        font= standard_font,
        width= standard_width,
        height= standard_height,
        command= lambda: event_menu(right_frame,events_listbox),
        )
    changeRankButton.pack(pady = standard_y_padding)

def event_menu(right_frame,events_listbox):
    for widgets in right_frame.winfo_children():
        widgets.destroy()
    selection = events_listbox.curselection()
    eventID = selection[0]
    eventID = eventID + 1
    cursor = connection.cursor()
    data = cursor.execute(f"""SELECT Menu.ItemName AS Item
        FROM Event
        INNER JOIN Catering
        ON Event.EventID = Catering.EventID  
        INNER JOIN EventMenu
        ON Catering.CateringID = EventMenu.CateringID 
        INNER JOIN Menu
        ON EventMenu.MenuID = Menu.MenuID
        WHERE Event.EventID = {eventID}
        ORDER BY Event.EventName, Menu.ItemName;""").fetchall()
    
    #Creating list box frame
    listbox_frame= ctk.CTkFrame(right_frame, fg_color= "#292929")
    listbox_frame.pack(pady = standard_y_padding)

    events_menu_listbox = Listbox(listbox_frame, bg= "#292929", fg= "Silver", width= 50, height= 35, font= standard_font)
    for row in data:
        events_menu_listbox.insert(END, row)
    events_menu_listbox.pack(side=LEFT)

    listboxScrollbar= ctk.CTkScrollbar(listbox_frame, command=events_listbox.yview)
    listboxScrollbar.pack(side="right", fill=Y)
    events_menu_listbox.config(yscrollcommand=listboxScrollbar.set) 

def select_event_dietary_requirements(left_frame,right_frame):
    for widgets in left_frame.winfo_children():
        widgets.destroy()
    for widgets in right_frame.winfo_children():
        widgets.destroy()
    #Creating a label
    label = ctk.CTkLabel(left_frame, text="Select The Event You Wish To View", fg_color="transparent", font= standard_font)
    label.pack(pady = standard_y_padding)

    #Creating list box frame
    listbox_frame= ctk.CTkFrame(left_frame, fg_color= "#292929")
    listbox_frame.pack(pady = standard_y_padding)

    events_listbox = Listbox(listbox_frame, bg= "#292929", fg= "Silver", width= 30, height= 25, font= standard_font)
    cursor = connection.cursor()
    data = cursor.execute("SELECT EventID,EventName FROM Event").fetchall()
    for row in data:
        events_listbox.insert(END, row)
    events_listbox.pack(side=LEFT)

    listboxScrollbar= ctk.CTkScrollbar(listbox_frame, command=events_listbox.yview)
    listboxScrollbar.pack(side="right", fill=Y)
    events_listbox.config(yscrollcommand=listboxScrollbar.set) 

    #Creating a button
    changeRankButton = ctk.CTkButton(
        left_frame,
        text= "View Event Menu",
        font= standard_font,
        width= standard_width,
        height= standard_height,
        command= lambda: event_dietary_requirements(right_frame,events_listbox),
        )
    changeRankButton.pack(pady = standard_y_padding)

def event_dietary_requirements(right_frame,events_listbox):
    for widgets in right_frame.winfo_children():
        widgets.destroy()
    selection = events_listbox.curselection()
    eventID = selection[0]
    eventID = eventID + 1
    cursor = connection.cursor()
    data = cursor.execute(f"""SELECT DietaryTypes.DietaryTypesName AS Dietary_Types, EventDietaryRequirements.Qty AS Qty
        FROM Event
        JOIN Catering
        ON Event.EventID = Catering.EventID  
        JOIN EventDietaryRequirements
        ON Catering.CateringID = EventDietaryRequirements.CateringID 
        JOIN DietaryTypes
        ON EventDietaryRequirements.DietaryTypesID = DietaryTypes.DietaryTypesID
        WHERE Event.EventID = {eventID};""").fetchall()
    
    #Creating list box frame
    listbox_frame= ctk.CTkFrame(right_frame, fg_color= "#292929")
    listbox_frame.pack(pady = standard_y_padding)

    events_dietary_requirements_listbox = Listbox(listbox_frame, bg= "#292929", fg= "Silver", width= 50, height= 35, font= standard_font)
    for row in data:
        events_dietary_requirements_listbox.insert(END, row)
    events_dietary_requirements_listbox.pack(side=LEFT)

    listboxScrollbar= ctk.CTkScrollbar(listbox_frame, command=events_listbox.yview)
    listboxScrollbar.pack(side="right", fill=Y)
    events_dietary_requirements_listbox.config(yscrollcommand=listboxScrollbar.set) 

def select_event(left_frame,right_frame):
    for widgets in left_frame.winfo_children():
        widgets.destroy()
    for widgets in right_frame.winfo_children():
        widgets.destroy()
    #Creating a label
    label = ctk.CTkLabel(left_frame, text="Select The Event You Wish To View", fg_color="transparent", font= standard_font)
    label.pack(pady = standard_y_padding)

    #Creating list box frame
    listbox_frame= ctk.CTkFrame(left_frame, fg_color= "#292929")
    listbox_frame.pack(pady = standard_y_padding)

    events_listbox = Listbox(listbox_frame, bg= "#292929", fg= "Silver", width= 30, height= 25, font= standard_font)
    cursor = connection.cursor()
    data = cursor.execute("SELECT EventID,EventName FROM Event").fetchall()
    for row in data:
        events_listbox.insert(END, row)
    events_listbox.pack(side=LEFT)

    listboxScrollbar= ctk.CTkScrollbar(listbox_frame, command=events_listbox.yview)
    listboxScrollbar.pack(side="right", fill=Y)
    events_listbox.config(yscrollcommand=listboxScrollbar.set) 

    #Creating a button
    changeRankButton = ctk.CTkButton(
        left_frame,
        text= "View Event Menu",
        font= standard_font,
        width= standard_width,
        height= standard_height,
        command= lambda: show_event(right_frame,events_listbox),
        )
    changeRankButton.pack(pady = standard_y_padding)

def show_event(right_frame,events_listbox):
    for widgets in right_frame.winfo_children():
        widgets.destroy()
    selection = events_listbox.curselection()
    eventID = selection[0]
    eventID = eventID + 1
    cursor = connection.cursor()
    data = cursor.execute(f"""SELECT
            User.FirstName ||' '|| User.LastName AS User,
            Event.EventName AS Event,
            User.PhoneNumber AS Phone,
            User.Email AS Email,
            Event.NumberOfPeople AS Number_of_People,
            Event.Date AS Date,
            Event.Time AS Time
        FROM Catering
        INNER JOIN User
        ON User.UserID = Catering.UserID 
        INNER JOIN Event
        ON Event.EventID = Catering.EventID;""").fetchall()
    
    treeview_frame= ctk.CTkFrame(right_frame, fg_color= "#292929")
    treeview_frame.pack()

    ttk.Style().theme_use("clam")
    ttk.Style().configure("Treeview", background="#292929",foreground="White", fieldbackground="#292929")
    ttk.Style().configure('Treeview.Heading', background='#292929', foreground='White')

    columns = ("Requester_Name", "Event_Name", "Phone_Number", "Email", "Number_Of_People", "Date", "Time")
    events_treeview = ttk.Treeview(treeview_frame, columns=columns, show="headings", height= 40)

    events_treeview.column("# 1",anchor=W, stretch=True, width = 200)
    events_treeview.heading("# 1", text="Requester_Name")
    events_treeview.column("# 2", anchor=W, stretch=True,width = 200)
    events_treeview.heading("# 2", text="Event_Name")
    events_treeview.column("# 3", anchor=W, stretch=True,width = 200)
    events_treeview.heading("# 3", text="Phone_Number")
    events_treeview.column("# 4", anchor=W, stretch=True,width = 200)
    events_treeview.heading("# 4", text="Email")
    events_treeview.column("# 5", anchor=W, stretch=True,width = 150)
    events_treeview.heading("# 5", text="Number_Of_People")
    events_treeview.column("# 6", anchor=W, stretch=True,width = 100)
    events_treeview.heading("# 6", text="Date")
    events_treeview.column("# 7", anchor=W, stretch=True,width = 100)
    events_treeview.heading("# 7", text="Time")

    for row in data:
        events_treeview.insert("", "end", values=row)

    treeviewScrollbarY= ttk.Scrollbar(treeview_frame, command=events_treeview.yview)
    treeviewScrollbarY.pack(side=LEFT, fill=Y)
    events_treeview.config(yscrollcommand=treeviewScrollbarY.set)
    events_treeview.pack(side=RIGHT)

def catterer_gui(left_frame,right_frame):
    menu_bar = Menu(root)
    root.config(menu=menu_bar)

    exit_menu = Menu(menu_bar)
    exit_menu.add_command(label='Exit', command=root.destroy)
    events_menu = Menu(menu_bar)
    events_menu.add_command(label='View All', command= lambda: events(left_frame,right_frame))
    events_menu.add_command(label='Select Event', command= lambda: select_event(left_frame,right_frame))
    events_menu.add_command(label='Event Menu', command= lambda: select_event_menu(left_frame,right_frame))
    events_menu.add_command(label='Event Dietary Requirements', command= lambda: select_event_dietary_requirements(left_frame,right_frame))

    menu_bar.add_cascade(label="Exit", menu=exit_menu)
    menu_bar.add_cascade(label="Event", menu=events_menu)

def requester_gui(left_frame,right_frame):
    menu_bar = Menu(root)
    root.config(menu=menu_bar)

    exit_menu = Menu(menu_bar)
    exit_menu.add_command(label='Exit', command=root.destroy)
    events_menu = Menu(menu_bar)
    events_menu.add_command(label='View All', command= lambda: events(left_frame,right_frame))
    events_menu.add_command(label='Select Event', command= lambda: select_event(left_frame,right_frame))
    events_menu.add_command(label='Event Menu', command= lambda: select_event_menu(left_frame,right_frame))
    events_menu.add_command(label='Event Dietary Requirements', command= lambda: select_event_dietary_requirements(left_frame,right_frame))

    menu_bar.add_cascade(label="Exit", menu=exit_menu)
    menu_bar.add_cascade(label="Event", menu=events_menu)
























def deactivated_account(right_frame):
    #Creating a label
    label = ctk.CTkLabel(right_frame, text="Your account has been deactivated. \nPlease go talk to a catering staff member about the issue.", fg_color="transparent", font= standard_font)
    label.pack(pady = standard_y_padding)

    close_button = ctk.CTkButton(
        right_frame,
        text="Close Window",
        font=standard_font,
        width=standard_width,
        height=standard_height,
        command=root.destroy)
    close_button.pack(pady=standard_y_padding)

class ErrorWindow:
    def __init__(self,parent,message,on_close):
        self.parent = parent
        self.message = message
        self.on_close = on_close

    def create(self):
        for widget in root.winfo_children():
            widget.destroy()
        
        error_label = ctk.CTkLabel(
            self.parent,
            text=self.message,
            font=standard_font)
        error_label.pack(pady=standard_y_padding)

        close_button = ctk.CTkButton(
            self.parent,
            text="Close",
            font=standard_font,
            width=standard_width,
            height=standard_height,
            command=lambda: main(button_type = None))
        close_button.pack(pady=standard_y_padding)

class CredentialsChecker:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def username_checker(self):
        usernames = str(connection.cursor().execute("SELECT Username FROM User").fetchall()).replace("(","").replace(")","").replace("'","").replace(",","").replace("[","").replace("]","").replace(" ",",")
        usernames = usernames.split(",")
        username_in_usernames = False
        for item in usernames:
            if self.username == item:
                username_in_usernames = True
                break
        return username_in_usernames           
   
    def password_checker(self):
        database_password = connection.cursor().execute(f"SELECT Password FROM User WHERE Username= '{self.username}'").fetchone()[0]
        if self.password != database_password:
            correct_password = False
            return correct_password
        else:
            correct_password = True
            return correct_password

def main(button_type): 
    for widget in root.winfo_children():
        widget.destroy()

    valid_login = False

    if button_type == None:
        log_in_window()
    else:    
        button_value = button_type[0]
        username = button_type[1]
        password = button_type[2]

        credentials_checker_1 = CredentialsChecker(username, password)
        credentials_checker_2 = CredentialsChecker(username, password)
        error_window_1 = ErrorWindow(root, "Your password or username was incorect.\nPlease go back and try again.", lambda: log_in_window())
        error_window_2 = ErrorWindow(root, "We encountered a problem, please try again.", lambda: log_in_window())

        if button_value == "login":
            if credentials_checker_1.username_checker() == True:
                if credentials_checker_2.password_checker() == True:
                    valid_login = True
                else:
                    error_window_1.create()
            else:
                error_window_1.create()
        else:
            error_window_2.create()

    if valid_login == True:
        account_type_ID = int(account_type_ID_retreval(username))
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        root.geometry(f"{screen_width}x{screen_height}")
        root.resizable(True, True)
        main_frame = ctk.CTkFrame(root)
        main_frame.pack(fill="both", expand=True)
        main_frame.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=5)
        left_frame = ctk.CTkFrame(main_frame, fg_color="#292929")
        left_frame.grid(row=0, column=0, sticky="nsew", padx=standard_x_padding)
        left_frame.grid_propagate(False)
        left_frame.pack_propagate(False)
        right_frame = ctk.CTkFrame(main_frame, fg_color="#292929")
        right_frame.grid(row=0, column=1, sticky="nsew", pady=standard_y_padding, padx=standard_x_padding)
        right_frame.grid_propagate(False)
        right_frame.pack_propagate(False)

        if account_type_ID == 1:
            catterer_gui(left_frame,right_frame)
        elif account_type_ID == 2:
            requester_gui(left_frame,right_frame)
        else:
            deactivated_account(right_frame)
    
if __name__ == "__main__":
    main(button_type = None)

root.mainloop()
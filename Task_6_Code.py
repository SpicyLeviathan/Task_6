#Imports all python libraties required for the code
from tkinter import *
from tkinter import ttk
import sqlite3
import customtkinter as ctk
import os

#Connects the database to the python program
connection = sqlite3.connect("Task_6_Database.db")

# Defining variables to make it easier to change the size of everything
standard_height = 30
standard_width = 200
standard_font = "", 15
standard_y_padding = 5
standard_x_padding = 5

# Defining colour mode for the program (light or dark)
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

#Creting the window
root = ctk.CTk()
root.title("Task_6")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"500x275")
root.resizable(False, False)

#Creating all the login widgits
def log_in_window():

    #Clears all widgits on the window
    for widget in root.winfo_children():
        widget.destroy()
    
    #Creates a label
    password_label = ctk.CTkLabel(
        root,
        text="Please Enter Your \n Username And Password",
        font=standard_font)
    password_label.pack(pady=standard_y_padding)

    #Creates a user entry
    username_entry = ctk.CTkEntry(
        root,
        placeholder_text="Enter Username",
        font=standard_font,
        width=standard_width,
        height=standard_height)
    username_entry.pack(pady=standard_y_padding)

    #Creates a user entry
    password_entry = ctk.CTkEntry(
        root,
        placeholder_text="Enter Password",
        font=standard_font,
        width=standard_width,
        height=standard_height,
        show='*')
    password_entry.pack(pady=standard_y_padding)

    #Creates a button
    login_button = ctk.CTkButton(
        root,
        text="Log In",
        font=standard_font,
        width=standard_width,
        height=standard_height,
        command=lambda: main(button_type = ["login",username_entry.get(),password_entry.get(),"N/A"]))
    login_button.pack(pady=standard_y_padding)

    #Creates a button
    close_button = ctk.CTkButton(
        root,
        text="Close Window",
        font=standard_font,
        width=standard_width,
        height=standard_height,
        command=root.destroy)
    close_button.pack(pady=standard_y_padding)

#Retrieving the account type id and returning it to the program
def account_type_ID_retreval(username):
    account_type_ID = str(connection.cursor().execute(f"SELECT AccountTypeID FROM User WHERE Username= '{username}'").fetchall()).replace("(","").replace(")","").replace("'","").replace(",","").replace("[","").replace("]","").replace(" ","")
    return(account_type_ID)

#Creates the catering staff gui
def catterer_gui():
    #Creates the frames everything sits in
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

    #Creates a menu bar up the top of the window
    menu_bar = Menu(root)
    root.config(menu=menu_bar)

    #Adds dropdown menu to menu bar
    exit_menu = Menu(menu_bar)
    exit_menu.add_command(label='Exit', command=root.destroy)
    events_menu = Menu(menu_bar)
    events_menu.add_command(label='View All', command= lambda: events(left_frame,right_frame))
    events_menu.add_command(label='Select Event', command= lambda: select_event(left_frame,right_frame))
    events_menu.add_command(label='Event Menu', command= lambda: select_event_menu(left_frame,right_frame))
    events_menu.add_command(label='Event Dietary Requirements', command= lambda: select_event_dietary_requirements(left_frame,right_frame))
    menu_bar.add_cascade(label="Exit", menu=exit_menu)
    menu_bar.add_cascade(label="Event", menu=events_menu)

#Defines a function that is used to display all events
def events(left_frame,right_frame):
    #Clears all widgits
    for widgets in left_frame.winfo_children():
        widgets.destroy()
    for widgets in right_frame.winfo_children():
        widgets.destroy()

    #Extracting data from the data base
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

    #Creating a table to display the data
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

    #Entering the data into the table
    for row in data:
        events_treeview.insert("", "end", values=row)

    #Adding a scroll bar
    treeviewScrollbarY= ttk.Scrollbar(treeview_frame, command=events_treeview.yview)
    treeviewScrollbarY.pack(side=LEFT, fill=Y)
    events_treeview.config(yscrollcommand=treeviewScrollbarY.set)
    events_treeview.pack(side=RIGHT)

#Defines a function that lets you select events to view
def select_event_menu(left_frame,right_frame):
    #Clears all widgits
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

    #Creating a list box and inserting data from the database into it
    events_listbox = Listbox(listbox_frame, bg= "#292929", fg= "Silver", width= 30, height= 25, font= standard_font)
    cursor = connection.cursor()
    data = cursor.execute("SELECT EventID,EventName FROM Event").fetchall()
    for row in data:
        events_listbox.insert(END, row)
    events_listbox.pack(side=LEFT)

    #Creating a scroll bar
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

#Defines a function that shows all the menu items for the selected event
def event_menu(right_frame,events_listbox):
    #Clears all widgits
    for widgets in right_frame.winfo_children():
        widgets.destroy()
    #Gets the user selection from the listbox and extracts the eventID from the selection
    selection = events_listbox.curselection()
    eventID = selection[0]
    eventID = eventID + 1

    #Extracting data from the database
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

    #Creating a list box and inserting data from the databse into it
    events_menu_listbox = Listbox(listbox_frame, bg= "#292929", fg= "Silver", width= 50, height= 35, font= standard_font)
    for row in data:
        events_menu_listbox.insert(END, row)
    events_menu_listbox.pack(side=LEFT)

    #Creates a scroll bar
    listboxScrollbar= ctk.CTkScrollbar(listbox_frame, command=events_listbox.yview)
    listboxScrollbar.pack(side="right", fill=Y)
    events_menu_listbox.config(yscrollcommand=listboxScrollbar.set) 

#Defines a function that lets you select events to view
def select_event_dietary_requirements(left_frame,right_frame):
    #Clears all widgits
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

    #Creates a list box that pulls data from the database to display
    events_listbox = Listbox(listbox_frame, bg= "#292929", fg= "Silver", width= 30, height= 25, font= standard_font)
    cursor = connection.cursor()
    data = cursor.execute("SELECT EventID,EventName FROM Event").fetchall()
    for row in data:
        events_listbox.insert(END, row)
    events_listbox.pack(side=LEFT)

    #Creates a scroll bar
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

#Defines a function that shows all the dietary requirements for the selected event
def event_dietary_requirements(right_frame,events_listbox):
    #Clears all the widgits
    for widgets in right_frame.winfo_children():
        widgets.destroy()
    
    #Gets the user selection from the listbox and extracts the eventID from the selection
    selection = events_listbox.curselection()
    eventID = selection[0]
    eventID = eventID + 1

    #Extracting data from the database
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

    #Creates a list box and inserts data from the listbox into it
    events_dietary_requirements_listbox = Listbox(listbox_frame, bg= "#292929", fg= "Silver", width= 50, height= 35, font= standard_font)
    for row in data:
        events_dietary_requirements_listbox.insert(END, row)
    events_dietary_requirements_listbox.pack(side=LEFT)

    #Creates a scroll bar
    listboxScrollbar= ctk.CTkScrollbar(listbox_frame, command=events_listbox.yview)
    listboxScrollbar.pack(side="right", fill=Y)
    events_dietary_requirements_listbox.config(yscrollcommand=listboxScrollbar.set) 

#Defines a function that lets you select events to view
def select_event(left_frame,right_frame):
    #Clears all the widgits
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

    #Creates a list box that extracts data frmo the database to display
    events_listbox = Listbox(listbox_frame, bg= "#292929", fg= "Silver", width= 30, height= 25, font= standard_font)
    cursor = connection.cursor()
    data = cursor.execute("SELECT EventID,EventName FROM Event").fetchall()
    for row in data:
        events_listbox.insert(END, row)
    events_listbox.pack(side=LEFT)

    #Creates a scroll bar
    listboxScrollbar= ctk.CTkScrollbar(listbox_frame, command=events_listbox.yview)
    listboxScrollbar.pack(side="right", fill=Y)
    events_listbox.config(yscrollcommand=listboxScrollbar.set) 

    #Creating a button
    view_event_button = ctk.CTkButton(
        left_frame,
        text= "View Event Menu",
        font= standard_font,
        width= standard_width,
        height= standard_height,
        command= lambda: show_event(right_frame,events_listbox),
        )
    view_event_button.pack(pady = standard_y_padding)

#Defines a function that shows the selected event
def show_event(right_frame,events_listbox):
    #Clears all widgits
    for widgets in right_frame.winfo_children():
        widgets.destroy()
    
    #Gets the user selection from the listbox and extracts the eventID from the selection
    selection = events_listbox.curselection()
    eventID = selection[0]
    eventID = eventID + 1

    #Extracting data from the database
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
    
    #Creates a table to display the data
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

    #Inserts data into the table
    for row in data:
        events_treeview.insert("", "end", values=row)

    #Creates a scroll bar
    treeviewScrollbarY= ttk.Scrollbar(treeview_frame, command=events_treeview.yview)
    treeviewScrollbarY.pack(side=LEFT, fill=Y)
    events_treeview.config(yscrollcommand=treeviewScrollbarY.set)
    events_treeview.pack(side=RIGHT)

#Creates the requester gui
def requester_gui():
    #Clears all widgits
    for widget in root.winfo_children():
        widget.destroy()

    #Creates a menu bar
    menu_bar = Menu(root)
    root.config(menu=menu_bar)

    #Creates the main frame the widgits will sit in
    main_frame = ctk.CTkFrame(root)
    main_frame.pack(fill="both", expand=True)
    main_frame.rowconfigure(0, weight=1)
    main_frame.columnconfigure(0, weight=1)
    main_frame.columnconfigure(1, weight=1)
    main_frame.columnconfigure(2, weight=1)

    #Clears all widgits
    for widget in main_frame.winfo_children():
        widget.destroy()
    
    #Creates the widgits
    left_frame = ctk.CTkFrame(main_frame, fg_color="#1f1f1f")
    left_frame.grid(row=0, column=0, sticky="nsew", padx=standard_x_padding)
    left_frame.grid_propagate(False)
    left_frame.pack_propagate(False)
    middle_frame = ctk.CTkFrame(main_frame, fg_color="#1f1f1f")
    middle_frame.grid(row=0, column=1, sticky="nsew", pady=standard_y_padding, padx=standard_x_padding)
    middle_frame.grid_propagate(False)
    middle_frame.pack_propagate(False)
    right_frame = ctk.CTkFrame(main_frame, fg_color="#1f1f1f")
    right_frame.grid(row=0, column=2, sticky="nsew", pady=standard_y_padding, padx=standard_x_padding)
    right_frame.grid_propagate(False)
    right_frame.pack_propagate(False)

    #Clears all widgits
    for widget in left_frame.winfo_children():
        widget.destroy()
    for widget in middle_frame.winfo_children():
        widget.destroy()
    for widget in right_frame.winfo_children():
        widget.destroy()

    #Creates the menu bar
    exit_menu = Menu(menu_bar)
    exit_menu.add_command(label='Exit', command=root.destroy)

    #Adds dropdown menu to the menubar
    catering_menu = Menu(menu_bar)
    catering_menu.add_command(label='Catering Requests', command= lambda: cattering_request(left_frame,middle_frame,right_frame))
    menu_bar.add_cascade(label="Exit", menu=exit_menu)
    menu_bar.add_cascade(label="Catering", menu=catering_menu)

#Creates the catering request form
def cattering_request(left_frame,middle_frame,right_frame):
    #Clears all widgits
    for widget in left_frame.winfo_children():
        widget.destroy()
    for widget in middle_frame.winfo_children():
        widget.destroy()
    for widget in right_frame.winfo_children():
        widget.destroy()

    #Creates a label
    event_name_label = ctk.CTkLabel(left_frame, text="Please enter event name:", fg_color="transparent", font= standard_font)
    event_name_label.grid(row = 0, column = 0, pady = 10)

    #Creates a user entry
    event_name_entry = ctk.CTkEntry(
        left_frame, 
        font= standard_font,
        width= standard_width,
        height= standard_height,
        )
    event_name_entry.grid(row = 0, column = 1, pady = 10)

    #Creates a label
    number_of_people_label = ctk.CTkLabel(left_frame, text="Please enter number of people:", fg_color="transparent", font= standard_font)
    number_of_people_label.grid(row = 1, column = 0, pady = 10)

    #Creates a user entry
    number_of_people_entry = ctk.CTkEntry(
        left_frame, 
        font= standard_font,
        width= standard_width,
        height= standard_height,
        )
    number_of_people_entry.grid(row = 1, column = 1, pady = 10)

    #Creating a label
    date_label = ctk.CTkLabel(left_frame, text="Select The Date Of The Event", fg_color="transparent", font= standard_font)
    date_label.grid(row = 2, column = 0)

    #Creates a frame
    date_dropdown_frame= ctk.CTkFrame(left_frame, fg_color= "#292929")
    date_dropdown_frame.grid(row = 3, column = 0, pady = 10)  

    #Creates a dropdown menu
    day_dropdown = ctk.CTkOptionMenu(master=date_dropdown_frame, values=["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"])
    day_dropdown.grid(row = 0, column = 0)
    day_dropdown.set("Day")

    #Creates a dropdown menu
    month_dropdown = ctk.CTkOptionMenu(master=date_dropdown_frame, values=["01","02","03","04","05","06","07","08","09","10","11","12"])
    month_dropdown.grid(row = 1, column = 0)
    month_dropdown.set("Month")

    #Creates a dropdown menu
    year_dropdown = ctk.CTkOptionMenu(master=date_dropdown_frame, values=["2024","2025","2026","2027","2028","2029","2030","2031","2032","2033","2034"])
    year_dropdown.grid(row = 2, column = 0)
    year_dropdown.set("Year")

    #Creating a label
    time_label = ctk.CTkLabel(left_frame, text="Enter The Time Of The Event", fg_color="transparent", font= standard_font)
    time_label.grid(row = 4, column = 0, pady = 10)

    #Creates a dropdown menu
    hour_dropdown = ctk.CTkOptionMenu(master=left_frame, values=["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24"])
    hour_dropdown.grid(row = 5, column = 0)
    hour_dropdown.set("Hour")

    #Creates a dropdown menu
    minute_dropdown = ctk.CTkOptionMenu(master=left_frame, values=["00","15","30","45"])
    minute_dropdown.grid(row = 5, column = 1)
    minute_dropdown.set("Minute")

    #Creates a label
    type_of_catering_label = ctk.CTkLabel(left_frame, text="Select The Type Of Catering", fg_color="transparent", font= standard_font)
    type_of_catering_label.grid(row = 6, column = 0, pady = 10)

    #Creates a dropdown menu
    type_of_catering_dropdown = ctk.CTkOptionMenu(master=left_frame, values=["On Sight-Catering","Off Sight-Catering"])
    type_of_catering_dropdown.grid(row = 6, column = 1, pady = 10)
    type_of_catering_dropdown.set("On Sight-Catering")

    #Creates a label
    cattering_for_label = ctk.CTkLabel(left_frame, text="Catering For:", fg_color="transparent", font= standard_font)
    cattering_for_label.grid(row = 7, column = 0, pady = 10)

    #Creates a dropdown menu
    cattering_for_dropdown = ctk.CTkOptionMenu(master=left_frame, values=["Breakfast","Morning Tea","Lunch","Afternoon Tea","Dinner"])
    cattering_for_dropdown.grid(row = 7, column = 1, pady = 10)
    cattering_for_dropdown.set("Breakfast")

    #Creates a label
    cattering_requirements_label = ctk.CTkLabel(left_frame, text="Special Catering Requirements:", fg_color="transparent", font= standard_font)
    cattering_requirements_label.grid(row = 8, column = 0, pady = 10)

    #Creates a user entry
    cattering_requirements_entry = ctk.CTkEntry(
        left_frame, 
        font= standard_font,
        width= standard_width,
        height= standard_height,
        )
    cattering_requirements_entry.grid(row = 8, column = 1, sticky = W, pady = 10)

    #Creating a button
    confirm_button = ctk.CTkButton(
        left_frame,
        text= "Enter Request",
        font= standard_font,
        width= standard_width,
        height= standard_height,
        command= lambda: confirm_request(event_name_entry,number_of_people_entry,day_dropdown,month_dropdown,year_dropdown,minute_dropdown,hour_dropdown,type_of_catering_dropdown,cattering_for_dropdown,cattering_requirements_entry,event_menu_listbox,event_dietary_types_listbox),
        )
    confirm_button.grid(row = 9, column = 0, pady = 150)

    #Creates a ctk label
    label = ctk.CTkLabel(middle_frame, text="Select An Item Then Click The Button Bellow \nThe Box To Add/Remove It From The Order \n\nFORMAT = MenuID, ItemName", fg_color="transparent", font= standard_font)
    label.grid(row = 0, column = 3)

    #Creating list box frame
    listbox_frame= ctk.CTkFrame(middle_frame, fg_color= "#292929")
    listbox_frame.grid(row = 1, column = 3)

    #Creates a listbox and inserts data from the database into it
    menu_listbox = Listbox(listbox_frame, bg= "#292929", fg= "Silver", width= 30, height= 12, font= standard_font)
    cursor = connection.cursor()
    data = cursor.execute("SELECT MenuID,ItemName FROM Menu").fetchall()
    for row in data:
        menu_listbox.insert(END, row)
    menu_listbox.pack(side=LEFT)

    #Creates a scroll bar
    listboxScrollbar= ctk.CTkScrollbar(listbox_frame, command=menu_listbox.yview)
    listboxScrollbar.pack(side="right", fill=Y)
    menu_listbox.config(yscrollcommand=listboxScrollbar.set)

    #Creating a button
    add_button = ctk.CTkButton(
        middle_frame,
        text= "Add Item",
        font= standard_font,
        width= standard_width,
        height= standard_height,
        command= lambda: add_item_menu(menu_listbox,event_menu_listbox),
        )
    add_button.grid(row = 2, column = 3, pady = 10)

    #Creates a ctk frame
    listboxFrameTwo= ctk.CTkFrame(middle_frame, fg_color= "#292929")
    listboxFrameTwo.grid(row = 4, column = 3, pady = 10)

    #Creates a list box
    event_menu_listbox = Listbox(listboxFrameTwo, bg= "#292929", fg= "Silver", width= 30, height= 12, font= standard_font)
    event_menu_listbox.pack(side=LEFT)

    #Creates a scroll bar
    listboxScrollbar= ctk.CTkScrollbar(listboxFrameTwo, command=event_menu_listbox.yview)
    listboxScrollbar.pack(side="right", fill=Y)
    event_menu_listbox.config(yscrollcommand=listboxScrollbar.set)

    #Creating a button
    remove_button = ctk.CTkButton(
        middle_frame,
        text= "Remove Item",
        font= standard_font,
        width= standard_width,
        height= standard_height,
        command= lambda: remove_item_menu(menu_listbox,event_menu_listbox),
        )
    remove_button.grid(row = 5, column = 3, pady = 10)

    #Creates a ctk label
    label = ctk.CTkLabel(right_frame, text="Select An Item Then Click The Button Bellow \nThe Box To Add/Remove It From The Order \nIf Dietary Type Isn't In List Contact Catering Staff  \n\nFORMAT = DietaryTypesID, Name", fg_color="transparent", font= standard_font)
    label.grid(row = 0, column = 4)

    #Creating list box frame
    listbox_frame= ctk.CTkFrame(right_frame, fg_color= "#292929")
    listbox_frame.grid(row = 1, column = 4)

    #Creates a listbox and inserts data from the database into it
    dietary_types_listbox = Listbox(listbox_frame, bg= "#292929", fg= "Silver", width= 30, height= 12, font= standard_font)
    cursor = connection.cursor()
    data = cursor.execute("SELECT DietaryTypesID,DietaryTypesName FROM DietaryTypes").fetchall()
    for row in data:
        dietary_types_listbox.insert(END, row)
    dietary_types_listbox.pack(side=LEFT)

    #Creates a scroll bar
    listboxScrollbar= ctk.CTkScrollbar(listbox_frame, command=dietary_types_listbox.yview)
    listboxScrollbar.pack(side="right", fill=Y)
    dietary_types_listbox.config(yscrollcommand=listboxScrollbar.set)

    #Creates a user entry
    qty_entry = ctk.CTkEntry(
        right_frame, 
        placeholder_text="Please enter Qty",
        font= standard_font,
        width= standard_width,
        height= standard_height,
        )
    qty_entry.grid(row = 2, column = 4, pady = 10)

    #Creating a button
    add_button = ctk.CTkButton(
        right_frame,
        text= "Add Item",
        font= standard_font,
        width= standard_width,
        height= standard_height,
        command= lambda: add_item_dietary(dietary_types_listbox,event_dietary_types_listbox,qty_entry),
        )
    add_button.grid(row = 3, column = 4, pady = 10)

    label = ctk.CTkLabel(right_frame, text="FORMAT = DietaryTypesID, Name, Qty", fg_color="transparent", font= standard_font)
    label.grid(row = 4, column = 4)

    #Creates a ctk frame
    listboxFrameTwo= ctk.CTkFrame(right_frame, fg_color= "#292929")
    listboxFrameTwo.grid(row = 5, column = 4, pady = 10)

    event_dietary_types_listbox = Listbox(listboxFrameTwo, bg= "#292929", fg= "Silver", width= 30, height= 12, font= standard_font)
    event_dietary_types_listbox.pack(side=LEFT)

    listboxScrollbar= ctk.CTkScrollbar(listboxFrameTwo, command=event_dietary_types_listbox.yview)
    listboxScrollbar.pack(side="right", fill=Y)
    event_dietary_types_listbox.config(yscrollcommand=listboxScrollbar.set)

    #Creating a button
    remove_button = ctk.CTkButton(
        right_frame,
        text= "Remove Item",
        font= standard_font,
        width= standard_width,
        height= standard_height,
        command= lambda: remove_item_dietary(dietary_types_listbox,event_dietary_types_listbox,qty_entry),
        )
    remove_button.grid(row = 6, column = 4, pady = 10)
 
#Defines function that adds an item to a list box
def add_item_menu(menu_listbox,event_menu_listbox):
    #Gets the user selection
    selection = menu_listbox.curselection()

    #Checks if their is a selection
    if selection:
        #Insert item into the empty listbox and delete it from the original
        item = str(menu_listbox.get(selection[0])).replace("(","").replace(",","").replace("'","").replace(")","")
        event_menu_listbox.insert(END, f"{item}")
        menu_listbox.delete(selection[0])

#Defines function that removes an item from a list box
def remove_item_menu(menu_listbox,event_menu_listbox):
    #Gets the user selection
    selection = event_menu_listbox.curselection()

    #Checks if their is a selection
    if selection:
        #Insert item into the original listbox and delete it from the empty one
        item = str(event_menu_listbox.get(selection[0])).replace("(","").replace(",","").replace("'","").replace(")","")
        menu_listbox.insert(END, f"{item}")
        event_menu_listbox.delete(selection[0])

#Defines function that adds an item to a list box
def add_item_dietary(dietary_types_listbox,event_dietary_types_listbox,qty_entry):
    #Gets the user selection
    selection = dietary_types_listbox.curselection()

    #Checks if their is a selection
    if selection:
        #Gets required information
        qty = str(qty_entry.get())
        item = str(dietary_types_listbox.get(selection[0])).replace("(","").replace(",","").replace("'","").replace(")","")
        item = item + " " + qty

        #Inserts it into one list box and deletes it from the other
        event_dietary_types_listbox.insert(END, f"{item}")
        dietary_types_listbox.delete(selection[0])

#Defines function that removes an item from a list box
def remove_item_dietary(dietary_types_listbox,event_dietary_types_listbox,qty_entry):
    #Gets the user selection
    selection = event_dietary_types_listbox.curselection()

    #Checks if their is a selection
    if selection:
        #Gets required information
        item = str(event_dietary_types_listbox.get(selection[0])).replace("(","").replace(",","").replace("'","").replace(")","")
        item = item.split(" ")
        id = item[0]
        item_name = item[1]
        item = id + " " + item_name

        #Inserts it into one list box and deletes it from the other
        dietary_types_listbox.insert(END, f"{item}")
        event_dietary_types_listbox.delete(selection[0])

#Defines function that adds the new information to the database
def confirm_request(event_name_entry,number_of_people_entry,day_dropdown,month_dropdown,year_dropdown,minute_dropdown,hour_dropdown,type_of_catering_dropdown,cattering_for_dropdown,cattering_requirements_entry,event_menu_listbox,event_dietary_types_listbox):
    #Gathers all the required information and formats it.
    event_name = str(event_name_entry.get())
    number_of_people = str(number_of_people_entry.get())
    day = str(day_dropdown.get())
    month = str(month_dropdown.get())
    year = str(year_dropdown.get())
    date = year + "-" + month + "-" + day
    minute = str(minute_dropdown.get())
    hour = str(hour_dropdown.get())
    time = hour + ":" + minute
    type_of_catering = str(type_of_catering_dropdown.get())
    if type_of_catering == "On Sight-Catering":
        type_of_catering = 1
    elif type_of_catering == "Off Sight-Catering":
        type_of_catering = 2
    catering_for = str(cattering_for_dropdown.get())
    if catering_for == "Breakfast":
        catering_for = 1
    elif catering_for == "Morning Tea":
        catering_for = 2
    elif catering_for == "Lunch":
        catering_for = 3
    elif catering_for == "Afternoon Tea":
        catering_for = 4
    elif catering_for == "Dinner":
        catering_for = 5
    cattering_requirements = str(cattering_requirements_entry.get())
    event_menu = event_menu_listbox.get(0, END)
    event_dietary_types = event_dietary_types_listbox.get(0, END)

    #Inserts information into the database
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO Event (EventName,NumberOfPeople,Date,Time) VALUES ('{event_name}','{number_of_people}','{date}','{time}')").fetchall()
    connection.commit()
    
    #Extracts required information from the database
    cursor = connection.cursor()
    eventID = str(cursor.execute(f"SELECT EventID FROM Event ORDER BY EventID DESC LIMIT 1").fetchone()).replace("(","").replace(",","").replace(")","")
    cursor = connection.cursor()
    userID = str(cursor.execute(f"SELECT UserID FROM User WHERE Username = '{username}'").fetchone()).replace("(","").replace(",","").replace(")","")
    cursor = connection.cursor()
    cardID = str(cursor.execute(f"SELECT CardID FROM CardDetails WHERE UserID = '{userID}'").fetchone()).replace("(","").replace(",","").replace(")","")
    
    #Inserts information into the database
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO Catering (UserID,MealID,EventID,CardID,TypesOfCateringID,SpecificCateringRequests) VALUES ('{userID}','{catering_for}','{eventID}','{cardID}','{type_of_catering}','{cattering_requirements}')").fetchall()
    connection.commit()
    
    #Extracts information from the database
    cursor = connection.cursor()
    cateringID = str(cursor.execute(f"SELECT CateringID FROM Catering WHERE EventID = '{eventID}'").fetchone()).replace("(","").replace(",","").replace(")","")

    #Adds the menu items requested for the event into the database
    for item in event_menu:
        item = str(item).split(" ")
        menuID = item[0]
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO EventMenu (CateringID,MenuID) VALUES ('{cateringID}','{menuID}')").fetchall()
        connection.commit()
        
    #Adds the dietary requirements for the event into the database
    for item in event_dietary_types:
        item = str(item).split(" ")
        dietary_typeID = item[0]
        dietary_type_qty = item[2]
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO EventDietaryRequirements (DietaryTypesID,CateringID,Qty) VALUES ('{dietary_typeID}','{cateringID}','{dietary_type_qty}')").fetchall()
        connection.commit()

    #Calls the function requester_gui
    requester_gui()

#Defines function that creates the deativated account gui
def deactivated_account():

    #Creates the main frame for the widgits
    main_frame = ctk.CTkFrame(root)
    main_frame.pack(fill="both", expand=True)
    
    #Clears all the widgits
    for widget in main_frame.winfo_children():
        widget.destroy()

    #Creating a label
    label = ctk.CTkLabel(main_frame, text="Your account has been deactivated. \nPlease go talk to a catering staff member about the issue.", fg_color="transparent", font= standard_font)
    label.pack(pady = standard_y_padding)

    #Creates a button
    close_button = ctk.CTkButton(
        main_frame,
        text="Close Window",
        font=standard_font,
        width=standard_width,
        height=standard_height,
        command=root.destroy)
    close_button.pack(pady=standard_y_padding)

#Creates a class that manages error windows
class ErrorWindow:
    #Defines all variables in the class
    def __init__(self,parent,message,on_close):
        self.parent = parent
        self.message = message
        self.on_close = on_close

    #Defines the method that creates the error window
    def create(self):
        #Clears all widgits
        for widget in root.winfo_children():
            widget.destroy()
        
        #Creates a label
        error_label = ctk.CTkLabel(
            self.parent,
            text=self.message,
            font=standard_font)
        error_label.pack(pady=standard_y_padding)

        #Creates a button
        close_button = ctk.CTkButton(
            self.parent,
            text="Close",
            font=standard_font,
            width=standard_width,
            height=standard_height,
            command=lambda: main(button_type = None))
        close_button.pack(pady=standard_y_padding)

#Creates a class that handles credentials
class CredentialsChecker:
    #Defines all the variables in the class
    def __init__(self, username, password):
        self.username = username
        self.password = password

    #Defines the method that checks if the username is valid
    def username_checker(self):
        usernames = str(connection.cursor().execute("SELECT Username FROM User").fetchall()).replace("(","").replace(")","").replace("'","").replace(",","").replace("[","").replace("]","").replace(" ",",")
        usernames = usernames.split(",")
        username_in_usernames = False
        for item in usernames:
            if self.username == item:
                username_in_usernames = True
                break
        return username_in_usernames           
    #Defines the method that checks if the password is valid
    def password_checker(self):
        database_password = connection.cursor().execute(f"SELECT Password FROM User WHERE Username= '{self.username}'").fetchone()[0]
        if self.password != database_password:
            correct_password = False
            return correct_password
        else:
            correct_password = True
            return correct_password

#Defines the function that contains the code to start the program.
def main(button_type): 
    #Clears all widgits
    for widget in root.winfo_children():
        widget.destroy()

    #Sets the variable to False
    valid_login = False

    #Checks if the log in button has been pressed yet
    if button_type == None:
        #Calls the function to create the log in gui
        log_in_window()
    else:
        #Makes the username a global variable
        global username

        #Gets all the information attached to the button
        button_value = button_type[0]
        username = button_type[1]
        password = button_type[2]

        #Creates items for the classes
        credentials_checker_1 = CredentialsChecker(username, password)
        credentials_checker_2 = CredentialsChecker(username, password)
        error_window_1 = ErrorWindow(root, "Your password or username was incorect.\nPlease go back and try again.", lambda: log_in_window())
        error_window_2 = ErrorWindow(root, "We encountered a problem, please try again.", lambda: log_in_window())

        #Checks if was a valid login. If it was it will set the value to True
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

    #Checks if was a valid login 
    if valid_login == True:
        #Gathers required information
        account_type_ID = int(account_type_ID_retreval(username))

        #Modifies the window to be full screen
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        root.geometry(f"{screen_width}x{screen_height}")
        root.resizable(True, True)

        #Launches the correct gui bassed off of the account type
        if account_type_ID == 1:
            catterer_gui()
        elif account_type_ID == 2:
            requester_gui()
        else:
            deactivated_account()
    
#Launches the programs code
if __name__ == "__main__":
    main(button_type = None)

#Makes the tkinter code work
root.mainloop()
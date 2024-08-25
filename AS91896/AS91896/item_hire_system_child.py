import os.path
import tkinter
from item_hire_system_parent import *
import random


# This is the son of WindowsParent
class WindowsSon(WindowsParent):
    # Expand the function for front page
    def front_page(self):
        self.Root.title("Item Hire System")  # Create a title for main window(Root)
        self.Root.geometry("400x500")  # Define the size of the main window(Root)
        self.Root.config(bg="peach puff")  # Define the color of background in the main window(Root)
        self.Root.resizable(False, False)

        # Create a button for appending details
        append_but = Button(self.Root, text="Append Details", width=16, command=self.win_for_append)
        append_but.place(x=140, y=300)  # Define the coordinate of button in the main window(Root)

        # Create a button for searching details
        show_history_but = Button(self.Root, text="Show History", width=16, command=self.win_for_search)
        show_history_but.place(x=140, y=350)  # define the coordinate of button in the main window(Root)

        # Create a button for deleting details
        delete_but = Button(self.Root, text="Delete Details", width=16, command=self.win_for_delete)
        delete_but.place(x=140, y=400)  # Define the coordinate of button in the main window(Root)

        # Create a button for quitting
        exit_but = Button(self.Root, text="Quit", width=16, command=self.my_quit,
                          bg="light blue")
        exit_but.place(x=140, y=450)  # Define the coordinate of button in the main window(Root)

        # Create a canvas with definite size
        canvas = Canvas(self.Root, height=200, width=800)
        self.global_image_file = PhotoImage(
            file=r"tropical-10201.gif")  # Create an image variable
        image = canvas.create_image(0, 0, anchor="center",
                                    image=self.global_image_file)  # Put the image variable into canvas
        canvas.pack(side="top")  # Pack the canvas and put into the top

        # Create a label for title of main window(Root)
        label_title = Label(self.Root, text="Party Hire Management System", font=("Arial", 14, "italic"))
        label_title.place(x=60, y=205)  # Define the coordinate fo the label in the main window(Root)

        # Create a button for viewing details
        view_but = Button(self.Root, text="View", width=10, command=self.view_detail)
        view_but.pack(side=tkinter.BOTTOM, anchor="e", padx=10, pady=10)

        # Try to find the file
        try:
            os.path.getsize("item_name_list.json")
        except:
            f = open("item_name_list.json", 'a+', encoding="UTF-8")
            item_list = ["table", "chair", "audio", "fireworks", "banner"]
            for str in item_list:
                json.dump(str, f)
                f.write("\r")
            f.close()

        if (os.path.getsize("item_name_list.json") == 0):
            f = open("item_name_list.json", 'a+', encoding="UTF-8")
            item_list = ["table", "chair", "audio", "fireworks", "banner"]
            for str in item_list:
                json.dump(str, f)
                f.write("\r")
            f.close()

    # Expand the function of appending
    def win_for_append(self):
        # This function is for receive details for entry and save the detail
        def receive_save_file():
            # Open or create the file with appending
            f = open("item_hire_list.json", 'a', encoding="UTF-8")

            dhi = DetailHireItem()  # Create an object of DetailHireItem
            condition1 = True  # This condition is for sent a message of warning
            custom_name = custom_name_entry.get()  # Get customer name from entry

            times = 0
            # This is for making sure that customer name doesn't have digit, symbol and blank.
            for char in custom_name:  # Traverse the string to judge
                times += 1
                if (custom_name.isalpha() or (char == " " and times != 1)):  # Judgment condition
                    dhi.customer_Name = custom_name
                    name_label.config(bg=new_window.cget("bg"))  # Initialize the background of the label
                    condition1 = False  # To make sure that doesn't send the warning message if fit the condition

            # Sent message of warning if condition doesn't fit
            if (condition1):
                name_label.config(bg="red")  # Turn the color of background into red

                # Sent message
                custom_name_message = messagebox.showwarning(title="Warning",
                                                             message="name can not be digit, symbol or blank")
                return 0  # End the function

            #  This is for making sure that receipt number doesn't have symbol, char and blank
            if (receipt_num_entry.get().isdigit() and int(receipt_num_entry.get()) > 0):  # Judgment condition
                f1 = open("item_hire_list.json", 'r', encoding="UTF-8")  # Open file with reading
                try:
                    for line in f1:  # line(str)
                        for key in json.loads(line)[0].keys():
                            if (
                                    receipt_num_entry.get() == key):  # If the receipt is the same with the receipt in the file
                                message = messagebox.showwarning(title="Warning",
                                                                 message="same receipt number found")  # Show warning
                                receipt_number_label.config(bg="red")
                                f1.close()
                                return 0  # End the function
                except:
                    f1.close()
                    pass

                dhi.receipt_Number = receipt_num_entry.get()  # Get receipt number from entry
                receipt_number_label.config(bg=new_window.cget("bg"))  # Initialize the background of the label

            #  Sent a message of warning if condition doesn't fit
            else:
                receipt_number_label.config(bg="red")  # Turn the color of background into red

                # Sent message
                receipt_number_message = messagebox.showwarning(title="Warning",
                                                                message="positive number can't be symbol, char or blank")
                return 0  # End the function

            item_name = item_hired_label_combo.get()  # Get item name from combobox
            condition2 = True  # This condition is for sent a message of warning
            times = 0
            if(item_name == "Choose one item"):
                item_hired_label.config(bg="red")  # Turn the color of background into red
                message = messagebox.showwarning(title="Warning",
                                                 message="Wrong hired name")
                return 0  # End the function
            else:
                for char in item_name:  # Traverse the string to judge
                    times += 1
                    if (item_name.isalpha() or (char == " " and times != 1)):  # Judgment condition
                        dhi.item_Hired = item_name  # Create an object of DetailHireItem
                        name_label.config(bg=new_window.cget("bg"))  # Initialize the background of the label
                        condition2 = False  # To make sure that doesn't send the warning message if fit the condition

            # Sent message of warning if condition doesn't fit
            if (condition2):
                item_hired_label.config(bg="red")  # Turn the color of background into red
                # Sent message
                custom_name_message = messagebox.showwarning(title="Warning",
                                                             message="Hired name can not be digit, symbol or blank")
                return 0  # End the function

            #  This is for making sure that hired number doesn't have symbol, char and blank
            if (number_hired_entry.get().isdigit() and 0 < int(number_hired_entry.get()) <= 500):
                dhi.number_Item_Hired = number_hired_entry.get()
                number_hired_label.config(bg=new_window.cget("bg"))  # Initialize the background of the label
            else:
                number_hired_label.config(bg="red")  # Turn the color of background into red
                # Sent message
                number_hired_message1 = messagebox.showwarning(title="Warning",
                                                               message="number are between 1~500 and number can't be symbol, char or blank")
                return 0  # End the function

            # Create a dictionary variable
            data = [{dhi.receipt_Number: [dhi.customer_Name, dhi.item_Hired, dhi.number_Item_Hired]}]
            # Save the dictionary variable in the file with json
            json.dump(data, f)  # Only save data in buffer
            f.write("\n")  # Make a new line
            f.flush()  # Save the data in file from buffer
            f.close()  # Close the file
            # Tell customer that save successfully
            bg_color = new_window.cget("bg")
            name_label.config(bg=bg_color)
            receipt_number_label.config(bg=bg_color)
            item_hired_label.config(bg=bg_color)
            number_hired_label.config(bg=bg_color)
            massage = messagebox.showinfo(title="Hi", message="Save Successfully!")

        def add_item():
            window = Toplevel()  # Create a new window
            window.title("Add hired item")  # Define the title for the new window
            window.geometry("230x150")  # Define the size for the new window
            window.config(bg="peach puff")
            window.resizable(False, False)  # No resizeable

            add_label = Label(window, text="Add Item", font=("Arial", 10))  # create a new label
            add_label.place(x=10, y=50)  # Place the label
            add_entry = Entry(window)  # Create a new entry
            add_entry.place(x=70, y=50)  # Place the new entry

            # Append the item name into file
            def save_file():
                item_name = add_entry.get()
                flag = True
                times = 0
                for char in item_name:
                    times += 1
                    if (item_name.isalpha() or (char == " " and times != 1)):
                        flag = False

                if (flag):
                    add_label.config(bg="red")
                    message = messagebox.showwarning(title="Warning",
                                                     message="name can not be digit, symbol or blank")
                    return 0  # End the function

                f1 = open("item_name_list.json", 'r', encoding="UTF-8")
                for line in f1:
                    if (item_name == json.loads(line)):
                        f1.close()
                        message = messagebox.showwarning(title="Warning", message="Same item name found")
                        add_label.config(bg="red")
                        return 0  # End this function

                f = open("item_name_list.json", 'a', encoding="UTF-8")
                json.dump(item_name, f)
                f.write("\n")
                f.flush()
                f.close()
                message = messagebox.showinfo(title="Hi",
                                              message="Save Successfully!\r\nPlease flush the appending page")

            add_but = Button(window, text="Submit", width=12, command=save_file)
            add_but.pack(side=tkinter.BOTTOM, anchor="e", padx=10, pady=10)

        def delete_item():
            window = Toplevel()  # Create a new window
            window.title("Delete hired item")  # Define the title for the new window
            window.geometry("230x150")  # Define the size for the new window
            window.config(bg="peach puff")
            window.resizable(False, False)  # No resizeable

            delete_label = Label(window, text="Delete Item", font=("Arial", 10))  # Create a new label
            delete_label.place(x=10, y=50)  # Place the label
            delete_entry = Entry(window)  # Create a new entry
            delete_entry.place(x=80, y=50)  # Place the new entry

            # Delete item name from the file
            def del_item():
                item_name = delete_entry.get()
                flag = True
                items = []
                times = 0

                for char in item_name:
                    times += 1
                    if (item_name.isalpha() or (char == " " and times != 1)):
                        flag = False

                if (flag):
                    delete_label.config(bg="red")
                    message = messagebox.showwarning(title="Warning",
                                                     message="name can not be digit, symbol or blank")
                    return 0  # End the function

                flag = True
                f1 = open("item_name_list.json", 'a+', encoding="UTF-8")
                f1.seek(0)  # Offset the pointer to beginning
                # Loop the file to append items into list and check found or not
                for line in f1:
                    str = json.loads(line)
                    if (item_name == str):
                        flag = False
                    else:
                        items.append(str)
                f1.close()

                # Couldn't find the delete name
                if (flag):
                    message = messagebox.showwarning(title="Warning", message="Couldn't Find!")
                    return 0

                f = open("item_name_list.json", 'w', encoding="UTF-8")
                for item in items:
                    json.dump(item, f)
                    f.write("\n")
                f.close()
                message = messagebox.showinfo(title="Hi",
                                              message="Delete Successfully\r\nPlease refresh the appending page")

            delete_but = Button(window, text="Submit", width=12, command=del_item)
            delete_but.pack(side=tkinter.BOTTOM, anchor="e", padx=10, pady=10)

        def get_item_list():  # OverRide function
            f = open("item_name_list.json", 'r', encoding="UTF-8")
            new_list = []
            for line in f:
                str = json.loads(line)
                new_list.append(str)
            new_list.sort()
            f.close()
            return new_list

        def get_rand_num():  # Generate an unique receipt number
            receipt_num_entry.delete(0, END)  # Clear the entry first
            while(True):
                receipt_num = random.randint(0, 1000000000)
                f1 = open("item_hire_list.json", 'r', encoding="UTF-8")  # Open file with reading
                isLoop = True
                try:
                    for line in f1:  # line(str)
                        if(not isLoop): break
                        for key in json.loads(line)[0].keys():
                            if (
                                    receipt_num == key):  # If the receipt is the same with the receipt in the file
                                isLoop = False
                                f1.close()
                                break
                except:
                    f1.close()
                    pass
                if(isLoop):
                    receipt_num_entry.insert(0, str(receipt_num))
                    return 0  # End this function if not the same number

        new_window = Toplevel()  # Create a new window
        new_window.title("Append")  # Define the title for the new window
        new_window.geometry("400x300")  # Define the size for the new window
        new_window.config(bg="peach puff")
        new_window.resizable(False, False)  # No resizeable

        # Define the title for the new window
        title_label = Label(new_window, text="Fill out all the information", font=("Arial", 14))
        title_label.place(x=90, y=10)  # define the coordinate for the title

        # Define a label for name in the new window
        name_label = Label(new_window, text="Customer Name", font=("Arial", 10))
        name_label.place(x=70, y=45)  # define the coordinate for the label of name
        # Create an entry for customer name
        custom_name_entry = Entry(new_window, relief="ridge")
        custom_name_entry.place(x=180, y=45)  # define the coordinate for the Entry of name

        # Create a label for receipt number
        receipt_number_label = Label(new_window, text="Receipt Number", font=("Arial", 10))
        receipt_number_label.place(x=70, y=90)  # Define the coordinate for the label of receipt number
        receipt_num_entry = Entry(new_window, relief="ridge")  # Create an entry for receipt number
        receipt_num_entry.place(x=180, y=90)  # Define the coordinate for the Entry of receipt number

        # Create a label for item hired
        item_hired_label = Label(new_window, text="Item Hired", font=("Arial", 10))
        item_hired_label.place(x=70, y=135)  # Define the coordinate for the label of hired item
        item_list = get_item_list()
        item_hired_label_combo = tkinter.ttk.Combobox(new_window, values=item_list)  # Create a combobox for hired item
        item_hired_label_combo.set("Choose one item")
        item_hired_label_combo.place(x=180, y=135)  # Define the coordinate for the Entry of hired number

        # Create a label for number hired
        number_hired_label = Label(new_window, text="Number Hired", font=("Arial", 10))
        number_hired_label.place(x=70, y=180)  # Define the coordinate for the label of number hired
        number_hired_entry = Entry(new_window, relief="ridge")  # Create an entry for number hired
        number_hired_entry.place(x=180, y=180)  # Define the coordinate for the Entry of number hired

        # Create a button for submitting
        submit_but = Button(new_window, text="Submit", width=12, command=receive_save_file)
        submit_but.place(x=140, y=220)  # define the coordinate for the button of submitting

        # Create a button for deleting hired items
        item_delete_but = Button(new_window, text="Delete Item", width=10, command=delete_item)
        item_delete_but.pack(side=tkinter.BOTTOM, anchor="e", padx=5, pady=5)

        # Create a button for adding hired items
        item_add_but = Button(new_window, text="Add Item", width=10, command=add_item)
        item_add_but.pack(side=tkinter.BOTTOM, anchor="e", padx=5, pady=5)

        # Create a button for generating receipt num
        receipt_num_but = Button(new_window, text="Generate", width=8, command=get_rand_num)
        receipt_num_but.place(x=330, y=90)

    # Expand the function of searching
    def win_for_search(self):
        # Define a function for showing history
        def show_history():
            data = []  # Create a container(list) for data
            condition1 = True  # Create a bool variable for send the warning message
            condition2 = False  # Create a bool variable for only showing the details once
            my_list = []  # Create a container(list) for data
            receipt_number = receipt_entry.get()  # Get the customer inputting
            if (receipt_number.isdigit() and int(receipt_number) > 0):
                # Try to find the receipt number that same with file's
                try:
                    try:
                        f = open("item_hire_list.json", 'r', encoding="UTF-8")  # Try to open file with reading
                    except:
                        message = messagebox.showwarning(title="Warning",
                                                         message="Can not find history")  # Send a message for warning
                        return 0  # End the function
                    for line in f:
                        data.append(json.loads(line))
                    f.close()
                    for new_line in data:  # New_line is each[{2:["w", "chair", "1"]}]
                        keys = new_line[0].keys()
                        for key in keys:  # Key is the receipt number in the file
                            if (receipt_number == key):
                                my_list = new_line[0][key]  # [name, item name, item number]
                                condition1 = False
                                condition2 = True
                except:
                    pass
            else:
                message = messagebox.showwarning(title="Warning",
                                                 message="positive number can't be symbol, char or blank")
                return 0
            # Show the details in a new window if it finds.
            if (condition2):
                new_win_for_search(receipt_number, my_list)

            # Sent a warning message if it can't find
            if (condition1):
                messagebox.showwarning(title="Warning", message="Couldn't Find!")

        # Define a function for searching
        def new_win_for_search(receipt_number, my_list):
            second_window = Toplevel()  # Create a new window
            second_window.title("Search Result")  # Define the title of the new window
            second_window.geometry("350x300")  # Define the size of the new window
            second_window.config(bg="peach puff")
            second_window.resizable(False, False)  # No resizable

            # Create a label for showing customer name
            name_label = Label(second_window, text=f"name:\t {my_list[0]}", font=("Arial", 18), bg="burlywood1")
            name_label.place(x=30, y=100)  # Define the coordinate of the label

            # Create a label for showing receipt number
            receipt_number_label = Label(second_window, text=f"receipt num: {receipt_number}", font=("Arial", 18),
                                         bg="burlywood2")
            receipt_number_label.place(x=30, y=130)  # Define the coordinate of the label

            # Create a label for item hired
            item_hired_label = Label(second_window, text=f"item name: {my_list[1]}", font=("Arial", 18),
                                     bg="burlywood3")
            item_hired_label.place(x=30, y=160)  # Define the coordinate of the label

            # Create a label for hired number
            number_hired_label = Label(second_window, text=f"num hired: {my_list[2]}", font=("Arial", 18),
                                       bg="burlywood4")
            number_hired_label.place(x=30, y=190)  # define the coordinate of the hired number

            # Create a label for new title
            new_title_label = Label(second_window, text="Find it", bg="red", font=("Arial", 18))
            new_title_label.place(x=130, y=10)  # Define the coordinate of the new title

        new_window = Toplevel()  # Create a new window
        new_window.title("Search")  # Define a title for the new window
        new_window.geometry("300x200")  # Define a size of the new window
        new_window.config(bg="peach puff")
        new_window.resizable(False, False)  # No resizable

        # Create a label for title
        title_label = Label(new_window, text="Put receipt number into the entry", font=("Arial", 12))
        title_label.place(x=40, y=10)  # define the coordinate of the new title

        # Create a label for receipt number
        receipt_label = Label(new_window, text="Receipt Number", font=("Arial", 10))
        receipt_label.place(x=30, y=80)  # define the coordinate of the receipt number

        # Create an entry for receipt number
        receipt_entry = Entry(new_window)
        receipt_entry.place(x=130, y=80)  # define the coordinate of the receipt number

        # Create a button for searching
        search_button = Button(new_window, text="Search", width=12, command=show_history)
        search_button.place(x=110, y=120)  # define the coordinate of the search button

    #  Expand the function of deleting
    def win_for_delete(self):
        # Create a function for deleting
        def delete_row():
            condition = True  # Create a bool variable to send a warning message
            data = []  # Create a list variable
            count = -1  # To get a specific row that same with receipt number
            receipt_number = receipt_entry.get()
            if (receipt_number.isdigit() and int(receipt_number) > 0):
                try:
                    # Open the json file with reading
                    f1 = open("item_hire_list.json", 'r', encoding="UTF-8")
                except:
                    message = messagebox.showwarning(title="Warning",
                                                     message="Can not find history")  # Sent a warning message
                    return 0  # End the function

                # An algorithm for searching the specific receipt number and deleting it
                try:
                    for line in f1:  # line(str)
                        data.append(json.loads(line))  # data(list)
                    f1.close()  # Close file
                    for new_line in data:  # new_line(list)
                        keys = new_line[0].keys()
                        count += 1  # To make sure that delete the right row
                        for key in keys:
                            if (receipt_number == key):
                                del data[count]
                                f2 = open("item_hire_list.json", 'w', encoding="UTF-8")  # Open file with writing
                                for new_line1 in data:
                                    json.dump(new_line1, f2)  # Write in file
                                    f2.write("\n")  # Make a new line
                                    f2.flush()
                                f2.close()  # Close file
                                message = messagebox.showinfo(title="Hi", message="Delete Successfully")  # Sent message
                                condition = False
                            else:
                                continue  # If it doesn't find, then jump into next one
                except:
                    pass
            else:
                message = messagebox.showwarning(title="Warning",
                                                 message="positive number can't be symbol, char or blank")
                return 0

            if (condition):  # Send warning message if condition doesn't fit
                messagebox.showwarning(title="Warning", message="Couldn't Find!")

        # Clear all the details
        def delete_all():
            try:
                f = open("item_hire_list.json", 'r', encoding="UTF-8")
                f.close()
            except:
                message = messagebox.showwarning(title="Warning", message="Can not find history")
                return 0

            ret = messagebox.askyesno(title="Ask", message="Are you sure you want to clear all the history?")
            if (ret):
                f = open("item_hire_list.json", 'w', encoding="UTF-8")
                f.close()
                message = messagebox.showinfo(title="Hi", message="Clear Successfully")
            else:
                return 0

        # Create a new window
        new_window = Toplevel()
        new_window.title("Delete")  # Create a title for new window
        new_window.geometry("300x200")  # Define the size of the new window
        new_window.config(bg="peach puff")
        new_window.resizable(False, False)  # No resizable

        # Create a label for title
        title_label = Label(new_window, text="Put receipt number into the entry", font=("Arial", 12))
        title_label.place(x=40, y=10)  # Define the coordinate of title

        # Create a label for receipt number
        receipt_label = Label(new_window, text="Receipt Number", font=("Arial", 10))
        receipt_label.place(x=30, y=80)  # Define the coordinate of receipt number

        # Create an entry for receipt number
        receipt_entry = Entry(new_window)
        receipt_entry.place(x=130, y=80)  # Define the coordinate of receipt number

        # Create a button for deleting row
        delete_row_button = Button(new_window, text="delete", width=12, command=delete_row)
        delete_row_button.place(x=110, y=120)  # Define the coordinate of deleting

        # Create a button for deleting all
        delete_all_button = Button(new_window, text="clear", width=12, command=delete_all)
        delete_all_button.place(x=110, y=160)  # Define the coordinate of deleting

    def view_detail(self):
        new_window = Toplevel()  # Create new window
        new_window.geometry("500x340+400+300")  # Set size
        new_window.config(bg="peach puff")
        new_window.resizable(False, False)  # Set can not resize

        frame = Frame(new_window)  # Create new frame on the new window
        frame.place(x=0, y=10, width=480, height=280)

        new_window.title("View Detail")  # Add a title
        tree = ttk.Treeview(frame, columns=("c1", "c2", "c3", "c4"), show="headings")
        tree.column("c1", width=100, anchor="center")
        tree.column("c2", width=150, anchor="center")
        tree.column("c3", width=80, anchor="center")
        tree.column("c4", width=100, anchor="center")
        scroll_bar = Scrollbar(frame)
        scroll_bar.pack(side=RIGHT, fill=Y)

        # Put names into each subtitle
        tree.heading("c1", text="Name")
        tree.heading("c2", text="Receipt Number")
        tree.heading("c3", text="Item Hired")
        tree.heading("c4", text="Number Hired")
        tree.pack(side=LEFT, fill=Y)
        scroll_bar.config(command=tree.yview)
        tree.config(yscrollcommand=scroll_bar.set)

        try:
            f = open("item_hire_list.json", 'r', encoding="UTF-8")  # Try to open file with reading
        except:
            message = messagebox.showwarning(title="Warning",
                                             message="Can not find history")  # Send a message for warning
            return 0  # End the function

        arr = self.my_sort(f)  # Call sort function to sort data
        row = 0  # Control row
        for dict in arr:  # Get each dict from
            for receipt_num in dict:  # 1 time loop
                arr1 = dict[receipt_num]  # Arr1 = ["name", "Item hired", "num hired"]
                name = arr1[0]
                item_hired = arr1[1]
                num_hired = arr1[2]
                list = [name, receipt_num, item_hired, num_hired]  # Make a list
                tree.insert("", row, values=list)  # Put object into treeView
                row += 1  # One object, one row
        f.close()

    def my_sort(self, file):
        old_arr = []  # Arr = [{}, {}...]
        new_arr = []  # New_arr = [{},{}...]
        keys = []
        for line in file:
            dict = json.loads(line)[0]  # Get each dict from file
            old_arr.append(dict)  # Add unsorted data into list
            for key in dict:  # 1 time loop
                keys.append(int(key))  # Key's type is string so need to transfer to int

        keys.sort()  # Sort keys
        for key in keys:  # For each keys
            for dict in old_arr:  # Find same key
                for sub_key in dict:  # 1 time loop
                    if (key == int(sub_key)):  # sub_key's type is string so need to transfer to int
                        new_arr.append(dict)  # Add correct dict into list
        return new_arr

    def my_quit(self):
        self.Root.destroy()  # Close all the windows

    def run(self):  # Run this program
        try:
            self.Root.mainloop()
        except KeyboardInterrupt:
            print("Program interrupted")
            self.Root.destroy()

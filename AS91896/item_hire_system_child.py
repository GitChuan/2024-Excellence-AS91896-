import tkinter.ttk

from item_hire_system_parent import *


# this is the son of WindowsParent
class WindowsSon(WindowsParent):

    # expand the function for front page
    def front_page(self):
        self.Root.title("Item Hire System")  # create a title for main window(Root)
        self.Root.geometry("400x500")  # define the size of the main window(Root)
        self.Root.config(bg="peach puff")  # define the color of background in the main window(Root)
        self.Root.minsize(width=400, height=500)  # define the minimum size of the main window(Root)
        self.Root.maxsize(width=400, height=500)  # define the maximum size of the main window(Root)

        # create a button for appending details
        append_but = Button(self.Root, text="Append Details", width=16, command=self.win_for_append)
        append_but.place(x=140, y=300)  # define the coordinate of button in the main window(Root)

        # create a button for searching details
        show_history_but = Button(self.Root, text="Show History", width=16, command=self.win_for_search)
        show_history_but.place(x=140, y=350)  # define the coordinate of button in the main window(Root)

        # create a button for deleting details
        delete_but = Button(self.Root, text="Delete Details", width=16, command=self.win_for_delete)
        delete_but.place(x=140, y=400)  # define the coordinate of button in the main window(Root)

        # create a button for quitting
        exit_but = Button(self.Root, text="Quit", width=16, command=self.my_quit, relief="groove",
                          bg="light blue")
        exit_but.place(x=140, y=450)  # define the coordinate of button in the main window(Root)

        # create a canvas with definite size
        canvas = Canvas(self.Root, height=200, width=800)
        self.global_image_file = PhotoImage(
            file=r"tropical-10201.gif")  # create an image variable
        image = canvas.create_image(0, 0, anchor="center",
                                    image=self.global_image_file)  # put the image variable into canvas
        canvas.pack(side="top")  # pack the canvas and put into the top

        # create a label for title of main window(Root)
        label_title = Label(self.Root, text="Party Hire Management System", font=("Arial", 14, "italic"))
        label_title.place(x=60, y=205)  # define the coordinate fo the label in the main window(Root)

    # expand the function of appending
    def win_for_append(self):

        # this function is for receive details for entry and save the detail
        def receive_save_file():
            # open or create the file with appending
            f = open("D:/item_hire_list.json", 'a', encoding="UTF-8")

            dhi = DetailHireItem()  # create an object of DetailHireItem
            condition1 = True  # this condition is for sent a message of warning
            custom_name = custom_name_entry.get()  # get customer name from entry

            # this is for making sure that customer name doesn't have digit, symbol and blank.
            for char in custom_name:  # traverse the string to judge
                if (custom_name.isalpha() or char == " "):  # judgment condition
                    dhi.customer_Name = custom_name
                    name_label.config(bg=new_window.cget("bg"))  # initialize the background of the label
                    condition1 = False  # to make sure that doesn't send the warning message if fit the condition

            # sent message of warning if condition doesn't fit
            if (condition1):
                name_label.config(bg="red")  # turn the color of background into red

                # sent message
                custom_name_message = messagebox.showwarning(title="Warning",
                                                             message="name can not be digit, symbol or blank")
                return 0  # end the function

            #  this is for making sure that receipt number doesn't have symbol, char and blank
            if (receipt_num_entry.get().isdigit() and int(receipt_num_entry.get()) > 0):  # judgment condition
                f1 = open("D:/item_hire_list.json", 'r', encoding="UTF-8")  # open file with reading
                try:
                    for line in f1:  # line(str)
                        for key in json.loads(line)[0].keys():
                            if (
                                    receipt_num_entry.get() == key):  # if the receipt is the same with the receipt in the file
                                message = messagebox.showwarning(title="Warning",
                                                                 message="same receipt number found")  # show warning
                                f1.close()
                                return 0  # end the function
                except:
                    f1.close()
                    pass

                dhi.receipt_Number = receipt_num_entry.get()  # get receipt number from entry
                receipt_number_label.config(bg=new_window.cget("bg"))  # initialize the background of the label

            #  sent a message of warning if condition doesn't fit
            else:
                receipt_number_label.config(bg="red")  # turn the color of background into red

                # sent message
                receipt_number_message = messagebox.showwarning(title="Warning",
                                                                message="positive number can't be symbol, char or blank")
                return 0  # end the function

            item_name = item_hired_label_combo.get()  # get item name from combobox
            condition2 = True  # this condition is for sent a message of warning
            for char in item_name:  # traverse the string to judge
                if (item_name.isalpha() or char == " "):  # judgment condition
                    dhi.item_Hired = item_name  # create an object of DetailHireItem
                    name_label.config(bg=new_window.cget("bg"))  # initialize the background of the label
                    condition2 = False  # to make sure that doesn't send the warning message if fit the condition

            # sent message of warning if condition doesn't fit
            if (condition2):
                name_label.config(bg="red")  # turn the color of background into red
                # sent message
                custom_name_message = messagebox.showwarning(title="Warning",
                                                             message="name can not be digit, symbol or blank")
                return 0  # end the function

            #  this is for making sure that hired number doesn't have symbol, char and blank
            if (number_hired_entry.get().isdigit() and 0 < int(number_hired_entry.get()) <= 500):
                dhi.number_Item_Hired = number_hired_entry.get()
                number_hired_label.config(bg=new_window.cget("bg"))  # initialize the background of the label
            else:
                number_hired_label.config(bg="red")  # turn the color of background into red
                # sent message
                number_hired_message1 = messagebox.showwarning(title="Warning",
                                                               message="number are between 1~500 and number can't be symbol, char or blank")
                return 0  # end the function

            # create a dictionary variable
            data = [{dhi.receipt_Number: [dhi.customer_Name, dhi.item_Hired, dhi.number_Item_Hired]}]
            # save the dictionary variable in the file with json
            json.dump(data, f)  # only save data in buffer
            f.write("\n")  # make a new line
            f.flush()  # save the data in file from buffer
            f.close()  # close the file
            # tell customer that save successfully
            massage = messagebox.showinfo(title="Hi", message="Save Successfully!")

        new_window = Toplevel()  # create a new window
        new_window.title("Append")  # define the title for the new window
        new_window.geometry("400x300")  # define the size fir the new window
        new_window.minsize(width=400, height=300)  # define the minimum size for the new window
        new_window.maxsize(width=400, height=300)  # define the maximum size for the new window

        # define the title for the new window
        title_label = Label(new_window, text="Fill out all the information", font=("Arial", 14))
        title_label.place(x=90, y=10)  # define the coordinate for the title

        # define a label for name in the new window
        name_label = Label(new_window, text="Customer Name", font=("Arial", 10))
        name_label.place(x=70, y=45)  # define the coordinate for the label of name
        # create an entry for customer name
        custom_name_entry = Entry(new_window)
        custom_name_entry.place(x=180, y=45)  # define the coordinate for the Entry of name

        # create a label for receipt number
        receipt_number_label = Label(new_window, text="Receipt Number", font=("Arial", 10))
        receipt_number_label.place(x=70, y=90)  # define the coordinate for the label of receipt number
        receipt_num_entry = Entry(new_window)  # create an entry for receipt number
        receipt_num_entry.place(x=180, y=90)  # define the coordinate for the Entry of receipt number

        # create a label for item hired
        item_hired_label = Label(new_window, text="Item Hired", font=("Arial", 10))
        item_hired_label.place(x=70, y=135)  # define the coordinate for the label of hired item
        item_list = ["table", "chair", "audio", "fireworks", "banner"]
        item_hired_label_combo = tkinter.ttk.Combobox(new_window, values=item_list)  # create a combobox for hired item
        item_hired_label_combo.set("choose one item")
        item_hired_label_combo.place(x=180, y=135)  # define the coordinate for the Entry of hired number

        # create a label for number hired
        number_hired_label = Label(new_window, text="Number Hired", font=("Arial", 10))
        number_hired_label.place(x=70, y=180)  # define the coordinate for the label of number hired
        number_hired_entry = Entry(new_window)  # create an entry for number hired
        number_hired_entry.place(x=180, y=180)  # define the coordinate for the Entry of number hired

        # create a button for submitting
        submit_but = Button(new_window, text="Submit", width=12, command=receive_save_file)
        submit_but.place(x=140, y=220)  # define the coordinate for the button of submitting

    # expand the function of searching
    def win_for_search(self):
        # define a function for showing history
        def show_history():
            data = []  # create a container(list) for data
            condition1 = True  # create a bool variable for send the warning message
            condition2 = False  # create a bool variable for only showing the details once
            my_list = []  # create a container(list) for data
            receipt_number = receipt_entry.get()  # get the customer inputting
            if (receipt_number.isdigit() and int(receipt_number) > 0):
                # try to find the receipt number that same with file's
                try:
                    try:
                        f = open("D:/item_hire_list.json", 'r', encoding="UTF-8")  # try to open file with reading
                    except:
                        message = messagebox.showwarning(title="Warning",
                                                         message="Can not find history")  # send a message for warning
                        return 0  # end the function
                    for line in f:
                        data.append(json.loads(line))
                    f.close()
                    for new_line in data:  # new_line is 每个[{2:["w", "chair", "1"]}]
                        keys = new_line[0].keys()
                        for key in keys:  # key is the receipt number in the file
                            if (receipt_number == key):
                                my_list = new_line[0][key]  # [name, item name, item number]
                                condition1 = False
                                condition2 = True
                except:
                    pass
            else:
                message = messagebox.showwarning(title="Warning",
                                                 message="postive number can't be symbol, char or blank")
                return 0
            # show the details in a new window if it finds.
            if (condition2):
                new_win_for_search(receipt_number, my_list)

            # sent a warning message if it can't find
            if (condition1):
                messagebox.showwarning(title="Warning", message="Couldn't Find!")

        # define a function for searching
        def new_win_for_search(receipt_number, my_list):
            second_window = Toplevel()  # create a new window
            second_window.title("Search Result")  # define the title of the new window
            second_window.geometry("350x300")  # define the size of the new window
            second_window.minsize(width=350, height=300)  # define the minimum size of the new window
            second_window.maxsize(width=350, height=300)  # define the maximum size of the new window

            # create a label for showing customer name
            name_label = Label(second_window, text=f"name:\t {my_list[0]}", font=("Arial", 18), bg="burlywood1")
            name_label.place(x=30, y=100)  # define the coordinate of the label

            # create a label for showing receipt number
            receipt_number_label = Label(second_window, text=f"receipt num: {receipt_number}", font=("Arial", 18),
                                         bg="burlywood2")
            receipt_number_label.place(x=30, y=130)  # define the coordinate of the label

            # create a label for item hired
            item_hired_label = Label(second_window, text=f"item name: {my_list[1]}", font=("Arial", 18),
                                     bg="burlywood3")
            item_hired_label.place(x=30, y=160)  # define the coordinate of the label

            # create a label for hired number
            number_hired_label = Label(second_window, text=f"num hired: {my_list[2]}", font=("Arial", 18),
                                       bg="burlywood4")
            number_hired_label.place(x=30, y=190)  # define the coordinate of the hired number

            # create a label for new title
            new_title_label = Label(second_window, text="Find it", bg="red", font=("Arial", 18))
            new_title_label.place(x=130, y=10)  # define the coordinate of the new title

        new_window = Toplevel()  # create a new window
        new_window.title("Search")  # define a title for the new window
        new_window.geometry("300x200")  # define a size of the new window
        new_window.minsize(width=300, height=200)  # define a minimum size of the new window
        new_window.maxsize(width=300, height=200)  # define a maximum size of the new window

        # create a label for title
        title_label = Label(new_window, text="Put receipt number into the entry", font=("Arial", 12))
        title_label.place(x=40, y=10)  # define the coordinate of the new title

        # create a label for receipt number
        receipt_label = Label(new_window, text="Receipt Number", font=("Arial", 10))
        receipt_label.place(x=30, y=80)  # define the coordinate of the receipt number

        # create an entry for receipt number
        receipt_entry = Entry(new_window)
        receipt_entry.place(x=130, y=80)  # define the coordinate of the receipt number

        # create a button for searching
        search_button = Button(new_window, text="Search", width=12, command=show_history)
        search_button.place(x=110, y=120)  # define the coordinate of the search button

    #  expand the function of deleting
    def win_for_delete(self):
        # create a function for deleting
        def delete_row():
            condition = True  # create a bool variable to send a warning message
            data = []  # create a list variable
            count = -1  # to get a specific row that same with receipt number
            receipt_number = receipt_entry.get()
            if (receipt_number.isdigit() and int(receipt_number) > 0):
                try:
                    # open the json file with reading
                    f1 = open("D:/item_hire_list.json", 'r', encoding="UTF-8")
                except:
                    message = messagebox.showwarning(title="Warning",
                                                     message="Can not find history")  # sent a warning message
                    return 0  # end the function

                # an algorithm for searching the specific receipt number and deleting it
                try:
                    for line in f1:  # line(str)
                        data.append(json.loads(line))  # data(list)
                    f1.close()  # close file
                    for new_line in data:  # new_line(list)
                        keys = new_line[0].keys()
                        count += 1  # to make sure that delete the right row
                        for key in keys:
                            if (receipt_number == key):
                                del data[count]
                                f2 = open("D:/item_hire_list.json", 'w', encoding="UTF-8")  # open file with writing
                                for new_line1 in data:
                                    json.dump(new_line1, f2)  # write in file
                                    f2.write("\n")  # make a new line
                                    f2.flush()
                                    f2.close()  # close file
                                message = messagebox.showinfo(title="Hi", message="Delete Successfully")  # sent message
                                condition = False
                            else:
                                continue  # if it doesn't find, then jump into next one
                except:
                    pass
            else:
                message = messagebox.showwarning(title="Warning",
                                                 message="postive number can't be symbol, char or blank")
                return 0

            if (condition):  # send warning message if condition doesn't fit
                messagebox.showwarning(title="Warning", message="Couldn't Find!")

        def delete_all():
            try:
                f = open("D:/item_hire_list.json", 'r', encoding="UTF-8")
                f.close()
            except:
                message = messagebox.showwarning(title="Warning", message="Can not find history")
                return 0

            ret = messagebox.askyesno(title="Ask", message="Are you sure you want to clear all the history?")
            if (ret):
                f = open("D:/item_hire_list.json", 'w', encoding="UTF-8")
                f.close()
                message = messagebox.showinfo(title="Hi", message="Clear Successfully")
            else:
                return 0

        # create a new window
        new_window = Toplevel()
        new_window.title("Delete")  # create a title for new window
        new_window.geometry("300x200")  # define the size of the new window
        new_window.minsize(width=300, height=200)  # define the minimum size of the new window
        new_window.maxsize(width=300, height=200)  # define the maximum size of the new window

        # create a label for title
        title_label = Label(new_window, text="Put receipt number into the entry", font=("Arial", 12))
        title_label.place(x=40, y=10)  # define the coordinate of title

        # create a label for receipt number
        receipt_label = Label(new_window, text="Receipt Number", font=("Arial", 10))
        receipt_label.place(x=30, y=80)  # define the coordinate of receipt number

        # create an entry for receipt number
        receipt_entry = Entry(new_window)
        receipt_entry.place(x=130, y=80)  # define the coordinate of receipt number

        # create a button for deleting row
        delete_row_button = Button(new_window, text="delete", width=12, command=delete_row)
        delete_row_button.place(x=110, y=120)  # define the coordinate of deleting

        # create a button for deleting all
        delete_all_button = Button(new_window, text="clear", width=12, command=delete_all)
        delete_all_button.place(x=110, y=160)  # define the coordinate of deleting

    def my_quit(self):
        self.Root.destroy()  # close all the windows


def do_work():
    m_w = WindowsSon()

    m_w.front_page()

    m_w.Root.mainloop()







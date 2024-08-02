from tkinter import *
import json
from tkinter import messagebox
from tkinter import ttk
from tkinter import Scrollbar


# this class is created for the following details
class DetailHireItem:

    # for initialization of DetailHireItem (might don't need to)
    def __init__(self):
        pass

    # this variable is created for customer's name
    customer_Name = None

    # this variable is created for the receipt number
    receipt_Number = None

    # this variable is created for the item's names that are hired
    item_Hired = None

    # this variable is created for the number of item that the customer has hired
    number_Item_Hired = None


# define WindowsParent class and inherit DetailHireItem
class WindowsParent(DetailHireItem):

    # create a global variable main window Root
    Root = Tk()

    # create an image for front page
    global_image_file = 0

    # this function is for the widget in the front page
    def front_page(self):
        pass

    # this function is for appending in the new window
    def win_for_append(self):
        pass

    # this function is for searching in the new window
    def win_for_search(self):
        pass

    # this function is for deleting in the new window
    def win_for_delete(self):
        pass

    # this function is for quitting
    def my_quit(self):
        pass

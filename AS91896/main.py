from item_hire_system_child import *


# create do work function
def do_work():
    m_w = WindowsSon()  # initialize class object

    m_w.front_page()  # quote front page function

    m_w.Root.mainloop()


# create main function
def main():
    do_work()


# test main function
if __name__ == '__main__':
    main()

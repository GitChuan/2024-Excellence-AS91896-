from item_hire_system_child import *


# Create do work function
def do_work():
    m_w = WindowsSon()  # Initialize class object

    m_w.front_page()  # Quote front page function

    m_w.run()  # Run this function


# Create main function
def main():
    do_work()


# Test main function
if __name__ == '__main__':
    main()

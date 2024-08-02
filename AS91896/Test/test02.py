# import json
# from tkinter import messagebox
#
# try:
#     f = open("D:/item_hire_list.json", 'r', encoding="UTF-8")  # try to open file with reading
# except:
#     message = messagebox.showwarning(title="Warning",
#                                      message="Can not find history")  # send a message for warning
# for line in f:
#     sub_arr = json.loads(line)
#     print(type(sub_arr))
# f.close()
keys = [12,1,2,1,3,1,31]
keys.sort()
print(keys)

import json

f1 = open("D:/item_name_list.json", 'r', encoding="UTF-8")
for line in f1:
    str = json.loads(line)
    print(str)
    print(type(str))
f1.close()
import os

path = "C://Users//works//dev//basic-web-master//images//passport"
# path="."
dir_list = os.listdir(path)

for i in dir_list:
    # print(i)
    if "1800" in i:
        index = i.index("1800")
        new_name = i[index:index+7]+".jpg"
        print(new_name)
        os.rename(path+"//"+i, path+"//"+new_name)

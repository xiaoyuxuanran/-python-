import os

def file_name(file_dir):   
    for root, dirs, files in os.walk(file_dir):  
        # print(root) #当前目录路径
        # print(dirs) #当前路径下所有子目录
        # print(files) #当前路径下所有非目录子文件
        for i in range(len(files)):
            music_root=str(root)
            music_name=str(files[i])
            music_os=music_root+'/'+music_name
            print(music_os)
def file_name2(file_dir):
    music_list=[]
    for root, dirs, files in os.walk(file_dir):
    # print(root) #当前目录路径
    #         # print(dirs) #当前路径下所有子目录
    #         # print(files) #当前路径下所有非目录子文件
        for i in range(len(files)):
            music_root=str(root)
            music_name=str(files[i])
            music_os=music_root+'/'+music_name
            music_list[i]=music_os
    for i2 in range(len(music_list)):
        print(music_list[i2])
# x=os.path.dirname(__file__)  # 当前文件所在的目录
# print(x)
file_name('./voice')
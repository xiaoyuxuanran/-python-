name=[]
age=[]
high=[]

def sys_init():
    i=0
    while(i<3):
        print("*****************学生管理系统******************")
        a=input("username:")
        b=input("password:")
        if(a=="pi"):
            if(b=="respberry"):
                print("登录成功")
                break
            else:
                i=i+1
                print("登录失败",i)
        else:
            i=i+1
            print("登录失败",i)
    if(i>=3):
        print("错误超过3次，登录超次")
    meau()
def meau():
    while(True):
        print("**************欢迎进入学生管理系统************")
        print("1.查询")
        print("2.增加")
        print("3.删除")
        print("4.退出")
        c=input("请选择:")
        if(c=="1"):
            print("进入查询...")
            seach_data()
        elif(c=="2"):
            print("进入增加函数")
            add_data()
        elif(c=="3"):
            print("进入删除函数")
            delete_data()
        elif(c=="4"):
            print("退出系统")
            break
        else:
            print("输入错误")
        print("******************************")
def seach_data():
    for i in range(len(name)):
        n=name[i]
        a=age[i]
        h=high[i]
        print("%s->姓名:%s | 年龄:%s | 身高:%s\n"%(i,n,a,h))
    print("空")

def delete_data():
    p=input("请输入要删除的序号:")
    p=int(p)
    del name[p]
    del age[p]
    del high[p]
def add_data():
    o1=input("name:")
    o2=input("age:")
    o3=input("high:")
    name.append(o1)
    age.append(o2)
    high.append(o3)
    print("增加成功")
if __name__ == '__main__':
    sys_init()

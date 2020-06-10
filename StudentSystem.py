import re
def menu():
    print("""
     ———————————学生信息管理系统————————————
    |                                      |
    |       =======功能菜单=======         |                       
    |                                      | 
    |       1.录入学生信息                  |
    |       2.查询学生信息                  |
    |       3.删除学生信息                  |
    |       4.修改学生信息                  |
    |       5.排序                         | 
    |       6.统计学生人数                  |
    |       7.显示所有学生信息              |
    |       0.退出系统                      |
    |                                       |
    |       ========================        |
    |       说明：通过数字或者上下选择菜单    | 
    |                                       | 
    ———————————————————————————————————————
    """)



def main():
    ctrl = True
    while():
        menu()
        option = input("请选择：")
        option_str =re.sub(r"\D","",option)
        if option_str in ['0','1','2','3','4','5','6','7']:
            if option_str == 0:
                print("您已经退出学生信息管理系统！")
                ctrl = False
            elif option_str == 1:
                insert()
            elif option_str == 2:
                search()
            elif option_str == 3:
                delete()
            elif option_str == 4:
                modify()
            elif option_str == 5:
                sort()
            elif option_str ==6:
                total()
            elif option_str ==7:
                show()



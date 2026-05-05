from toools import *
success = True
while success:
    print("=====个人命令行工具======\n"
          "---1.字符串操作工具---\n"
          "---2.文件操作工具-----\n"
          "---3.待办清单工具-----\n"
          "---0.退 出 程 序-----")
    user_input = int(input("请输入你的选择（0-3）："))
    print("\n")
    while success:
        if -1 < user_input<4:
            if user_input == 1:
                print("=====字符串操作工具======\n"
                      "---1.字符串反转工具---\n"
                      "---2.自定义切片工具---\n"
                      "---3.字符统计工具----\n"
                      "---0.返回上一级------")
                user_one_input = int(input("请输入你的选择0-3）："))
                if user_one_input == 1:
                    str_reverse()
                elif user_one_input == 2:
                    str_slice()
                elif user_one_input == 3:
                    str_count_char()
                elif user_one_input == 0:
                    print("\n\n------------------------------------------------")
                    break
                else:
                    print('请重新输入有效数字')
                    print("\n\n------------------------------------------------")
            elif user_input == 2:
                print("=====文件操作工具======\n"
                      "---1.读取文件内容------\n"
                      "---2.写入文件内容------\n"
                      "---3.检查文件是否存在---\n"
                      "---0.返回上一级--------")
                user_two_input = int(input("请输入你的选择0-3）："))
                if user_two_input == 1:
                    file_path =input("请输入你要查看的文件路径：")
                    encoding = input("请输入文件编码格式（可留空）默认为utf-8:")
                    print(safe_read_file(file_path,encoding))
                    print("\n\n------------------------------------------------")
                elif user_two_input == 2:
                    file_path = input("请输入你要写入的文件路径：")
                    content = input('请输入你要写入的内容：')
                    append = input('请分类覆盖还是追加（a,w）：')
                    res = safe_write_file(file_path, content, append=(append == 'a'))
                    print(res)
                    print("\n\n------------------------------------------------")
                elif user_two_input == 3:
                    file_path = input('请输入你要查看的文件路径：')
                    check_file_exist(file_path=file_path)
                    print(check_file_exist(file_path=file_path))
                elif user_two_input == 0:
                    print("\n\n------------------------------------------------")
                    break
            elif user_input == 3:
                print("=====代办清单工具======\n"
                      "---1.查看所有待办---\n"
                      "---2.添加新待办-----\n"
                      "---3.删除待办------\n"
                      "---4.修改待办------\n"
                      "---5.搜索待办------\n"
                      "---0.返回上一级---")
                user_three_input = int(input("请输入你的选择0-5）："))
                if user_three_input == 1:
                    print(get_all_tasks())
                elif user_three_input == 2:
                    content = input('请输输入要添加的任务名称：')
                    add_task(content)
                elif user_three_input == 3:
                    task_id = int(input('请输出要删除的任务ID:'))
                    delete_task(task_id)
                elif user_three_input == 4:
                    task_id = int(input('请输入要修改的任务ID：'))
                    new_content = input('请输入要修改的任务内容：')
                    new_status = input('请输入要修改的任务完成情况：')
                    update_task(task_id=task_id, new_content=new_content, new_status=new_status)
                elif user_three_input == 5:
                    keyword = input('请输入你要查询的任务名称：')
                    print(query_task(keyword=keyword))
                elif user_three_input == 0:
                    break
                else:
                    print('请重新输入有效数字')
                    print("\n------------------------------------------------")
            elif user_input == 0:
                print("程序已退出，欢迎您再次使用")
                success = False
                break
        else:
            print("无效数字，请重新输入\n---------------------------------")
            break
    else:
        print("无效数字，请重新输入\n---------------------------------")

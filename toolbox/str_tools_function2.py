
# -------------------------------------------------------------
"""功能二：接收字符串参数，自定义切片函数
(待改进缺少 下表为负的情况和跳过默认步长和结束下表的功能)"""
def str_slice ():
    success = False
    str_old = input("请输入想要切片的字符串:\t\t\t\t")
    start,end,step = 0,len(str_old),1
    while not success:

        while not success:
            s_start = input("请输入想要切片的 起始 下表:\t\t\t")
            start = 0 if s_start == '' else int(s_start)               #若内容为空则使用默认参数
            temp_start = start+len(str_old) if start < 0 else start    #负索引修正
            if temp_start > len(str_old) or temp_start < 0 :
                print("注意，起始值越界了，请重新输入")
                continue
            else:break
        
        while not success:
            e_end = input("请输入想要切片的 结束 下表:\t\t\t")
            end=len(str_old) if e_end == '' else int(e_end)             #若内容为空则使用默认参数
            temp_end = end + len(str_old) if end < 0 else end           #负索引修正
            if temp_end > len(str_old) or temp_end < 0 :
                print("注意，终止值越界了，请重新输入")
                continue
            else:success = True
            
            step = int(input("请输入想要切片的步长（默认为1）：\t ") or 1)
            if start > end and step> 0:
                print("若正向切片，起始下表不能超过结束下表，请重新输入")
                continue
            if step == 0:
                print("步长不能为零，请重新输入")
                continue
            else:success = True
        while (step > 0 and start < end) or (step < 0 and start > end):

                print(str_old[start],end='')
                start += step


str_slice()
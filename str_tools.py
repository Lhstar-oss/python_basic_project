"""--------------字符处理模块--------------"""
# -------------------------------------------------------------
"""功能一：接收字符串参数，返回反转后的新字符串"""
def str_reverse():
    str_old = input("请输入想要反转的字符串:")
    c = len(str_old)-1
    print('反转后的字符为串: ',end='')
    while c >=0 :
        print(str_old[c],end="")
        c = c - 1
    print('\n---------------------------')
    return 0

# -------------------------------------------------------------
"""功能二：接收字符串参数，自定义切片函数
(待改进)"""

def str_slice():
    success = False
    str_old = input("请输入想要切片的字符串:\t\t\t\t")
    start, end, step = 0, len(str_old), 1
    while not success:

        while not success:
            s_start = input("请输入想要切片的 起始 下表:\t\t\t")
            start = 0 if s_start == '' else int(s_start)  # 若内容为空则使用默认参数
            temp_start = start + len(str_old) if start < 0 else start  # 负索引修正
            if temp_start > len(str_old) or temp_start < 0:
                print("注意，起始值越界了，请重新输入")
                continue
            else:
                break

        while not success:
            e_end = input("请输入想要切片的 结束 下表:\t\t\t")
            end = len(str_old) if e_end == '' else int(e_end)  # 若内容为空则使用默认参数
            temp_end = end + len(str_old) if end < 0 else end  # 负索引修正
            if temp_end > len(str_old) or temp_end < 0:
                print("注意，终止值越界了，请重新输入")
                continue
            else:
                success = True

            step = int(input("请输入想要切片的步长（默认为1）：\t ") or 1)
            if start > end and step > 0:
                print("若正向切片，起始下表不能超过结束下表，请重新输入")
                continue
            if step == 0:
                print("步长不能为零，请重新输入")
                continue
            else:
                success = True
        while (step > 0 and start < end) or (step < 0 and start > end):
            print(str_old[start], end='')
            start += step
    print("\n----------------------------")


# -------------------------------------------------------------
"""功能三：接收字符串参数，统计指定字符串中的英文字符、数字、空额、其他字符出现次数，
要求：返回字典类型例如：{'alpha':5,"digit":4,""spice":2,other":4}"""
def str_count_char ():
    str_old = input("请输入字符串:")
    count_dict = {'alpha':0,"digit":0,"spice":0,"other":0}
    for char in str_old:
        if char.isdigit():
            count_dict['digit'] += 1
        elif char.isalpha():
            count_dict['alpha'] += 1
        elif char == " ":
            count_dict['spice'] += 1
        else:
            count_dict['other'] += 1
    for k,v in count_dict.items():
        print(f"{k}：{v}",end="\t")
    print()

__all__ = ['str_slice','str_reverse','str_count_char']
# -------------------------------------------------------------测试
if __name__ == '__main__':
     # str_reverse()              #功能一：反转字符
    str_slice()               #功能二：切片函数
    # str_count_char()          #功能三：统计字符
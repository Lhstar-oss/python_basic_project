"""--------------文件处理模块--------------"""
# -------------------------------------------------------------
"""功能一：读取文件"""
def safe_read_file(file_path='',encoding="utf-8"):
    if not encoding:
        encoding = 'utf-8'
    if not file_path:
        return "请输入有效文件地址"
    print("\n-------------------")

    try:
        with open(file_path,'r',encoding=encoding) as f:
            return f.read()
    except FileNotFoundError:
        return "文件不存在，请检查路径"
    except PermissionError:
        return "没有权限读取该文件"
    except UnicodeDecodeError:
        return f"文件编码错误，无法读取为文本，请确认编码格式是否为{encoding}"
    except IsADirectoryError :
        return f"无法读取,这是一个文本夹，请确认txt文件"


# -------------------------------------------------------------
"""功能二：写文件"""
def safe_write_file(file_path='',content='',append=False):
    if not file_path:
        return "请输入要写入文件的地址"
    mode = 'a' if append else 'w'
    try:
        with open(file_path, mode=mode, encoding="UTF-8") as f:
            f.write(content)
            return "写入成功"
    except Exception as e:
        return f"文件写入失败{e}"
    except PermissionError:
        return "没有权限写入该文件，请检查路径或权限"
    except IsADirectoryError:
        return "指定路径为文件夹，并非文件"

# -------------------------------------------------------------
"""功能三：文件检查"""
import os
def check_file_exist(file_path=''):
    if not file_path:
        return False,'❕文件路径不能为空'
    try:
        if os.path.exists(file_path) and os.path.isfile(file_path):
            return True,'文件检查通过'
        else:
            return False,'文件不存在或不是合法文件'
    except PermissionError:
        return False,'没有访问权限'
    except Exception as e:
        return False,f"未知错误{str(e)}"

__all__ = ['check_file_exist','safe_read_file','safe_write_file']

# -------------------------------------------------------------测试
if __name__ == '__main__':
    # print(safe_read_file())                          #功能一：读区文件
    # print(safe_write_file(content='测试写入'))        #功能二：写入文件
    s,res =check_file_exist('你的测试文件路径')             #功能三：文件检查
    print(f"检查结果为 {s} ,提示{res}")
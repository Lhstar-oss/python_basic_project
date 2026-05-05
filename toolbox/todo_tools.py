"""--------------待办清单处理模块--------------"""

#持久化函数
# -------------------------------------------------------------
from .file_tools import * #------------------------导入文件处理模块
tasks = [{'task_id':1,
          'content':'学python',
          'is_finished':True
          }
        ]
#加载任务
def load_tasks():
    global tasks
    file_content = safe_read_file("todo.txt")       #默认保存到此文件内
    try:
        if file_content.strip():
            tasks = eval(file_content)
        else:
            tasks =[]
    except Exception as e:
        print("发现文件损坏，自动重制列表")
        tasks = []
        save_tasks()
#保存任务
def save_tasks():
    global tasks
    safe_write_file("todo.txt",str(tasks))

# -------------------------------------------------------------
# 增删改查函数
#----------------------------------------增
def add_task(content):
    global tasks
    new_id = tasks[-1]['task_id'] + 1 if tasks else 1
    tasks.append({'task_id':new_id,"content":content,"is_finished":False})
    save_tasks()
    print(f"已添加任务 {content}")
    print("--------------------")
    return True
#----------------------------------------删
def delete_task(task_id):
    global tasks
    for index,task in enumerate(tasks):
        if tasks[index]['task_id'] == task_id:
            del tasks[index]
            save_tasks()
            print(f"已经删除ID为{task_id}的任务")
            print("--------------------------")
        else:
            print(f"未找到ID为{task_id}的任务")
    return False
#----------------------------------------改
def update_task(task_id,new_content=None,new_status=None):
    global tasks
    found = False
    for task in tasks:
        if task['task_id'] == task_id:
            found = True
            if new_content :
                task['content'] = new_content
            if new_status is not None :
                task['is_finished'] = new_status
            save_tasks()
            print(f"已更新ID为{task_id}的任务")
            print("--------------------------")
            break
    if not found :
        print(f"未找到ID为{task_id}的任务")
        return False
    return True
#----------------------------------------查
def query_task(keyword=None):
    keyword=str(keyword)
    if keyword:
        return [t for t in tasks if keyword in t['content']]
    print("--------------------------")
    return tasks.copy()
#--------------------------------返回所有任务
def get_all_tasks():
    print("--------------------------")
    return tasks.copy()



__all__ = ['load_tasks','save_tasks','add_task','delete_task','update_task','query_task','get_all_tasks']





















def add_task(task_list: list, task_name: str):
    task_list.append(task_name)
    return task_list

def remove_task(task_list, task_index):
    pass

def print_task(task_list, hide_done=False):
    pass

def mark_done(task_list, task_index):
    pass

def main(task_list):
    while True:
        print(">>>> TASKS <<<<")
        print("9: exit")

        choice = input("Choices: ")
        if choice.startswitch("0"):
            break
main([])
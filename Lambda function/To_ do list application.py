todo_list=[]
while True:
    print("1.Add Task:")
    print("2.View Task:")
    print("3.Exit:")
    choice=input("Enter your choice:")
    if choice=='1':
        task=input("Enter task:")
        todo_list.append(task)
    elif choice=='2':
        print("Task:")
        for i,taskl in enumerate(todo_list,1):
            print(f"{i}.{task}")
    elif choice=='3':
        break
    else:
         print("invalid choice")
    
        
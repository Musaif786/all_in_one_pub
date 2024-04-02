
a =True
data =[]
while a:
    text = "Enter anything here ==>"
    user = input(text).strip()

    match user:
        case 'a':
            add = input("Add values: ").upper()
            data.append(add)
        case 'show':
            if data:
                for ind, value in enumerate(data):
                    print(ind," : ",value)
                print("Count: ",len(data))
            else:
                print("Nothing to print")
        case 'p':
            data.pop()
        case 'r':
            for ind, value in enumerate(data):
                print(ind," : ",value)
            remove = input("What do you want to remove from above list:? ").upper()
            data.remove(remove)
        case 'exit':
            break
        case "":
            break

    
    
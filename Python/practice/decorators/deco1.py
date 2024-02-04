def Project(func):
    def wrapper():
        print("This is wrapper function...")
        func()
        print("function called")
    return wrapper


@Project
def main():
    print("Main function")

main()
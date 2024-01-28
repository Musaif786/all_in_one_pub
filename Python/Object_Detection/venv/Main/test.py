# print("hello world")
import time
def checkvalue():
    while True:
        line = input("Please enter any value: ")
        try:
            return int(line)
        except ValueError:
            print("This is not a valid value, try again...")

def main():
    value = checkvalue()
    print(30*"#")
    print(f"\nUser value is: {value}\n")
    print(30*"#")


if __name__=="__main__":
    main()
    time.sleep(5)
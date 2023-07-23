import package

# Starting
def start():
    instructions = package.help
    action = input(f'{package.path} ')

    # Actions
    def sum(a, b):
        return a + b

    def sub(a, b):
        return a - b

    def div(a, b):
        return a / b

    def mul(a, b):
        return a * b
        
    # Checking the action
    if (action == "+"):
        a = float(input("1st number: "))
        b = float(input("2nd number: "))
        ans = "Answer: " + str(sum(a, b))
        print(ans)
        print("====")
        start()

    elif (action == "-"):
        a = float(input("1st number: "))
        b = float(input("2nd number: "))
        ans = "Answer: " + str(sub(a, b))
        print(ans)
        print("====")
        start()

    elif (action == "/"):
        a = float(input("1st number: "))
        b = float(input("2nd number: "))
        ans = "Answer: " + str(div(a, b))
        print(ans)
        print("====")
        start()

    elif (action == "*"):
        a = float(input("1st number: "))
        b = float(input("2nd number: "))
        ans = "Answer: " + str(mul(a, b))
        print(ans)
        print("====")
        start()

    elif action == "help":
        print(instructions)
        print("")
        start()
    
    elif action == "":
        start()

    elif (action == "~" or action == "exit"):
        print("Closed.") # Closing the program
        
    else:
        print("Invalid action.\n")
        start()

if __name__ == "__main__":
    start()
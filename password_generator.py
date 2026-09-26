import random
def generate_strong_password():
    add_elements=[]
    for i in range(1,31):
        element=random.choice("!@#$%^&*()_+-=[]{}|;:',.<>/?`~§±€£¥¢©®ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890")
        add_elements+=element
        return_password = "".join(add_elements)
        if i==30:
            return return_password
    return ""
def generate_medium_password():
    add_elements=[]
    for i in range(1, 13):
        element=random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890")
        add_elements+=element
        return_password = "".join(add_elements)
        if i==12:
            return return_password
    return ""
def generate_easy_password():
    add_elements=[]
    for i in range(1, 9):
        element=random.choice("abcdefghijklmnopqrstuvwxyz1234567890")
        add_elements+=element
        return_password = "".join(add_elements)
        if i==8:
            return return_password
    return ""
def save_passwords():
    return_passwords = {"Strong": generate_strong_password(),
                        "Medium": generate_medium_password(),
                        "Easy": generate_easy_password()}
    return return_passwords
passwords=save_passwords()
def save_password_to_file():
    global passwords
    while True:
        choice = input("Choose one version from the latest generation: ")
        if choice.capitalize()=="Strong":
            with open("password_from_generator.txt", "w",encoding="utf-8") as save_password:
                save_password.write(passwords["Strong"])
                print("Saved!")
            break
        elif choice.capitalize()=="Medium":
            with open("password_from_generator.txt", "w") as save_password:
                save_password.write(passwords["Medium"])
                print("Saved!")
            break
        elif choice.capitalize()=="Easy":
            with open("password_from_generator.txt", "w") as save_password:
                save_password.write(passwords["Easy"])
                print("Saved!")
            break
        else:
            print("Invalid input!\nOptions: Strong, Medium, Easy")
def print_passwords():
    global passwords
    print("Password versions:")
    print("Strong: " + passwords["Strong"])
    print("Medium: " + passwords["Medium"])
    print("Easy: " + passwords["Easy"])
    while True:
        press = input("\nPress enter to generate again or space+enter to save: ")
        if press==(" "
                     ""):
            save_password_to_file()
            break
        elif press==(""
                   ""):
            passwords=save_passwords()
            print("\nPassword versions:")
            print("Strong: "+passwords["Strong"])
            print("Medium: "+passwords["Medium"])
            print("Easy: "+passwords["Easy"])
        else:
            print("Error!")

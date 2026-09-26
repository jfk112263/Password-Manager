print("Password manager - save your passwords here.")
from password_generator import (generate_strong_password,
                                generate_medium_password,
                                generate_easy_password,
                                save_passwords,
                                print_passwords,
                                )
def for_pin():
    lista=[]
    for x in range(1,10000):
        lista.append(str(x))
    return lista
pin_list=for_pin()
length_pin=open("data/pin.txt","r")
def if_pin_doesnt_exist():
    if len(length_pin.read())<=0:
        print("Create PIN for password manager")
        for x in range(1, 4):
            pinc = input("PIN:")
            if len(pinc) != 4 or pinc not in pin_list:
                print("Please enter a 4 digit PIN number.")
            else:
                return pinc
            if x == 3:
                print("Error!")
                break
        return "Error!"
    else:
        return ""
user_pin=if_pin_doesnt_exist()
def if_pin_exist():
    verify=open("data/pin.txt","r")
    read=verify.read()
    if user_pin == "":
        for z in range(1,4):
            pinc=input("PIN:")
            if len(pinc) != 4 or pinc not in pin_list or pinc != read:
                print("Wrong PIN entered!")
            else:
                print("Success!")
                return pinc
            if z == 3:
                print("Error!")
                break
    return "Error!"
pin=if_pin_exist()
def return_true_false(verify):
    if verify!="Error!" and user_pin != "Error!" or len(user_pin) == 4 and user_pin in pin_list:
        return True
    else:
        return False
true_false=return_true_false(pin)
def create_pin(pincode):
    if len(user_pin) == 4 and user_pin in pin_list:
        pin_open=open("data/pin.txt","w")
        pin_open.write(pincode)
        pin_open.close()
        print("Saved!")
    else:
        print("",end="")
create_pin(user_pin)
i=1
def save_name_and_password(name,password):
    text=open("data/passwords.txt","a")
    text.write(name+" - "+password+"\n")
    text.close()
while true_false:
    print("Item",i)
    Name=input("Name: ")
    generate_strong_password()
    generate_medium_password()
    generate_easy_password()
    save_passwords()
    print_passwords()
    with open("data/password_from_generator.txt","r") as file:
        password_from_generator=file.read()
    Password = password_from_generator
    save_name_and_password(Name,Password)
    Enter=input("Press enter to continue or space + enter to exit and save.")
    if Enter!=(""
               ""):
        print('Your passwords are stored here: "data/password_manager.txt"')
        break
    else:
        print("")
        i+=1

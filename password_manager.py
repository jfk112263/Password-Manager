print("Password manager - save your passwords here.")
from password_generator import (generate_strong_password,
                                generate_medium_password,
                                generate_easy_password,
                                save_passwords,
                                print_passwords,
                                )
# def for_pin():
#     lista=[]
#     for x in range(1,10000):
#         lista.append(str(x))
#     return lista
# pin_list=for_pin()
with open("pin.txt","r") as pin_file:
    pin_length=pin_file.read()
def create_pin():
    if len(pin_length)<=0:
        print("Create PIN for password manager")
        for x in range(0, 3):
            if x == 3:
                print("Error!")
                break
            try:
                pinc = int(input("PIN:"))
                if len(str(pinc))!=4:
                    print("The PIN most consists of 4 digits.")
            except ValueError:
                print("A PIN cannnot contain letters.")
            else:
                 if len(str(pinc))==4:
                     with open("pin.txt", "w") as pin_write:
                         pin_write.write(str(pinc))
                     print("Saved!")
                     return pinc
        return "Error!"
    else:
        return ""
user_pin=create_pin()
with open("pin.txt", "r") as pin_file2:
    pin_verify = pin_file2.read()
def if_pin_exist():
        for z in range(0, 3):
            try:
                if user_pin == "":
                        pinc = int(input("PIN:"))
                        if str(pinc)!=pin_verify:
                            print("Wrong PIN!")
                            if len(str(pinc)) != 4:
                                print("The PIN most consists of 4 digits.")
                        else:
                            print("Success!")
                            return pinc
            except ValueError:
                print("A PIN cannnot contain letters.")

        return "Error!"
pin=if_pin_exist()
print(pin,user_pin)
def true_false(check_error):
    if check_error!="Error!" and user_pin != "Error!":
        return True
    else:
        return False
boolean=true_false(pin)
i=1
def save_name_and_password(name,password):
    text=open("passwords.txt","a")
    text.write(name+" - "+password+"\n")
    text.close()
while boolean:
    print("Item",i)
    Name=input("Name: ")
    generate_strong_password()
    generate_medium_password()
    generate_easy_password()
    save_passwords()
    print_passwords()
    with open("password_from_generator.txt","r") as file:
        password_from_generator=file.read()
    Password = password_from_generator
    save_name_and_password(Name,Password)
    Enter=input("Press enter to continue or space + enter to exit and save.")
    if Enter!=(""
               ""):
        print('Your passwords are stored here: "passwords.txt"')
        break
    else:
        print("")
        i+=1

# import module
import sue
from colorama import init, Fore
init()

print(Fore.YELLOW + "starting Sue...")
sue = sue.Sue()  # create object
print("Sue started successful\n")

with open("lps.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        sue.upload_new_language_package(line.strip())

print(Fore.CYAN + "\nПривет! Меня зовут Сью. Можете мне что-нибудь написать, поболтаем."
                  "\nПросто скажите \"привет\", чтобы начать")

run = True  # program operation flag
while run:  # main program loop
    user_message = input(Fore.WHITE + ":::")  # get user message from terminal
    if not user_message:  # checking for an empty message
        run = False
    elif user_message == "nlp":  # nlp - New Language Package
        sue.upload_new_language_package(input(Fore.YELLOW + "enter language package path: "))
    else:
        print(Fore.CYAN + sue.process_user_action(user_message))  # print sue's response

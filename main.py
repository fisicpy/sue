import sue  # import module

print("starting Sue...")
sue = sue.Sue()  # create object
print("Sue started successful")

sue.upload_new_language_package("suelp1.2a.json")  # upload standard language pack

run = True  # program operation flag
while run:  # main program loop
    user_message = input(":::")  # get user message from terminal
    if not user_message:  # checking for an empty message
        run = False
    elif user_message == "nlp":  # nlp - New Language Package
        sue.upload_new_language_package(input("enter language package path: "))
    else:
        print(sue.process_user_action(user_message))  # print sue's response

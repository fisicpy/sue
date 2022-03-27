import sue  # import module

sue = sue.Sue()  # create object

sue.upload_new_language_package("suelp1.2a.json")  # upload standard language pack

run = True  # program operation flag
while run:  # main program loop
    user_message = input(":::")  # get user message from terminal
    if not user_message:  # checking for an empty message
        run = False
    print(sue.process_user_action(user_message))  # print sue's responce

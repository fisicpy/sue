import sue

sue = sue.Sue()

sue.upload_new_language_package("suelp1.0a.json")

run = True
while run:
    user_message = input(":::")
    if not user_message:
        run = False
    print(sue.process_user_action(user_message))

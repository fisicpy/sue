# import modules
import json
import random
import functions.main as functions


punctuation_marks = [
    ",", ".", "?", ":", ";", ")", "(", "-", "&", "$", "#", "№", "!", "`", "~",
    "%", "*", "@"
]


class Sue:
    def __init__(self):
        self.language_package = []  # init language package list

    def upload_new_language_package(self, language_package_name):
        """
        This function upload new language package. You can upload several
        language packages so that Sue understands more phrases.
        """
        try:
            with open(language_package_name, "r", encoding="utf-8") as file:
                print("Open file")
                data = json.load(file)
                print("Load data from file")
                try:
                    self.language_package.extend(data["root"])
                    print("Upload language package was successful")
                except KeyError:
                    print("Error: Incorrect spelling of the language package")
        except FileNotFoundError:
            print(f"Error: language package \"{language_package_name}\" not found")

    def process_user_action(self, user_action):
        """
        This function returns Sue's response to the user's message.
        """
        for punctuation_mark in punctuation_marks:
            user_action = user_action.replace(punctuation_mark, "")  # delete all punctuation marks from user message
        for block in self.language_package:
            if block["action_type"] == "w":  # check type of an action
                if user_action.lower() in block["action"]:
                    return random.choice(block["answer"])
            elif block["action_type"] == "f":
                message = f"starting function \"{block['answer']}\"...\n"
                try:
                    result = functions.functions[block["answer"]](block["action"])
                    return message + result + "\nfunction \"{block['answer']}\" finished successful"
                except Exception as exc:
                    message += f"function \"{block['answer']}\" failed with error:\n{exc}"
                    return message


if __name__ == "__main__":
    sue = Sue()
    sue.upload_new_language_package("suelp1.0a.json")

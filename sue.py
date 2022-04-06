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
                    print(f"Uploading language package \"{language_package_name}\" was successful")
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
            if block["action_type"] == "w":  # check type of an action, w - words
                if user_action.lower() in block["action"]:
                    return random.choice(block["answer"])
            elif block["action_type"] == "f":  # f - function
                if user_action.lower() in block["action"]:
                    print(f"starting function \"{block['answer']}\"...")
                    try:
                        result = functions.functions[block["answer"]](user_action.lower())
                        print(f"function \"{block['answer']}\" finished successful")
                        return result
                    except Exception as exc:
                        print(f"function \"{block['answer']}\" failed with error:\n{exc}")
                        return f"function \"{block['answer']}\" failed with error:\n{exc}"
        return "извините, не поняла вас"


if __name__ == "__main__":
    sue = Sue()
    print(sue.is_string_in_list("что такое процедурная генерация?", ["что такое", "кто такая", "кто такой"]))

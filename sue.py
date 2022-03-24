import json
import random


class Sue:
    def __init__(self):
        self.language_package = []

    def upload_new_language_package(self, language_package_name):
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
        for block in self.language_package:
            if block["action_type"] == "w":
                if user_action.lower() in block["action"]:
                    return random.choice(block["answer"])


if __name__ == "__main__":
    sue = Sue()
    sue.upload_new_language_package("suelp1.0a.json")
    print(sue.process_user_action("я проснулся"))

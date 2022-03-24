# Sue

## Why is it needed?
Sue - imitation of human communication using the simplest algorithm.
In the plan of using neural networks. Sue is can talk with you,
control your computer, wish you sweet dreams.
The alpha version supports only Russian, but this can be fixed
by writing your own language package, more on that later.

## How to install it
You need download file from this GitHub repository and install python 3x.
Then start `main.py`. Alpha version work in terminal. Release version
will use headset to communicate with user.

## Methods of the class

### sue.upload_new_language_package(language_package_name)
This function upload new language package. You can upload several
language packages so that Sue understands more phrases:
```
sue.upload_new_language_package("suelp1.0a.json")
sue.upload_new_language_package("another_language_package.json")
```
### sue.process_user_action(user_message)
This function returns Sue's response to the user's message.
```
print(sue.process_user_action("привет"))
>>>здравствуй
```

## How to write language package
Language package is a JSON file with a list "root"
with objects with user actions and responses to them:
```
{
    "root": [
        {
            "action_type": "w",
            "action": ["привет", "здравствуй", "здравствуйте", "приветствую"],
            "answer": ["приветствую", "привет", "здравствуй"]
        },
        {
            "action_type": "w",
            "action": ["пока", "прощай", "до свидания", "прощайте", "скоро увидимся", "до завтра"],
            "answer": ["пока", "прощайте", "до свидания", "прощайте, мой госпадин", "скоро увидимся", "до завтра"]
        }
    ]
}
```
Action is a list with possible user messages. Answers is a list
with possible Sue answers.


# Sue

## Why is it needed?
Sue is a imitation of human communication using the simplest algorithm.
In the plan of using neural networks. Sue can talk with you,
control your computer, wish you sweet dreams.
The alpha version supports only Russian, but this can be fixed
by writing your own language package, more on that later.

## How to install it
Download the latest version installer from
[this page](https://github.com/fisicpy/sue/releases).
Then run the exe file.
The installer will start and that's all you have to do.

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
            "action_type": "w
            "action_type": "f",
            "action": ["сколько времени", "время", "сколько время"],
            "answer": "time_function_name"
        },
    ]
}
```",
            "action": ["пока", "прощай", "до свидания", "прощайте", "скоро увидимся", "до завтра"],
            "answer": ["пока", "прощайте", "до свидания", "прощайте, мой госпадин", "скоро увидимся", "до завтра"]
        },
        {
You can name your own language pack whatever you want,
but the file extension must be `.json`, for example `my_sue_lp.json`. 
To add your own language package you need to use command `npl`.

Action is a list with possible user messages.
Answers is a list with possible Sue answers.
Action type is type of actions, which Sue will understand. Type `w` is for
list of words. Type `f` is for functions.

## Functions
If you want Sue to perform some action after your words,
and not just respond to you with text, then use custom functions.

First you need to add words, which you want talk to Sue so that
she performs the action. Block in language package looks like that:

```
{
    "action_type": "f",
    "action": ["сколько времени", "время", "сколько время"],
    "answer": "time_function_name"
}
```

In this variant answer is name of function in tuple of functions. A file
with functions is `/functions/main.py`. In this file you need to init
standard python function and add in tuple:
```
# import modules
import datetime

# init function
def time(action):
    print("time function work")
    return datetime.datetime.now().strftime("%H:%M")

# add it in tuple
functions = {
    "time_function_name": time,
    "say_hello": say_hello
}
```
Name in tuple and in language package must be the same.

## Special commands
### npl
This command allows you to add your own language package:
```
:::nlp
enter language package path: my_sue_lp.json
Open file
Load data from file
Uploading language package "my_sue_lp.json" was successful
```

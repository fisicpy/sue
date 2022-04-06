# file with user functions

# import modules
import datetime


def time(action):
    print("time function work")
    return datetime.datetime.now().strftime("%H:%M")


def say_hello(action):
    return "привет"


functions = {
    "time_function_name": time,
    "say_hello": say_hello
}

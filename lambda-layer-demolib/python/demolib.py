import json

def my_function(message_in):
    print("Inside my_function")

    my_dict = dict(message_from_lambda=message_in,message_from_library="Hello from My Library Function!")

    return my_dict

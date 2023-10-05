import json

def my_lib_function(message_in):
    print("Inside my_lib_function")

    my_dict = dict(message_from_lambda=message_in,message_from_library="Hi from Test Library Function!")

    return my_dict

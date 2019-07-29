

# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(friend_name):
    if type(friend_name) is not str:
        raise TypeError("Input parameter is not of string type")
    message = 2
    if type(message) is not str:
        raise TypeError("Output message is not of string type")
    return message





# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(friend_name):
    #raise NotImplementedError()
    if type(friend_name) is not str:
        raise TypeError("Input parameter is not of string type")
    message = str("Hello World!")
    return message

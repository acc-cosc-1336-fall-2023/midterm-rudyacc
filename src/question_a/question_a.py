#write functions here, don't add input('') statements here!
def test_config():
    return True

def reverse_string(string1):
    reversed_string = ""
    index = len(string1) - 1
    while index >= 0:
        reversed_string += string1[index]
        index -= 1
    return reversed_string
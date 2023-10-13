#write functions here, don't add input('') statements here!

global_var = 1

def use_global():

    global global_var

    global_var += 5

use_global()

print("Global variable after modification:", global_var)
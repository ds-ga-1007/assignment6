'''
Created on Nov 3, 2016

@author: Yang



'''
#
# Python hello world
#
def hello_world():
    return "Hello World: ", time.strftime("%c")
if __name__ == "__main__":
    import sys, time
    print(hello_world())
'''
Created on Nov 4, 2016

@author: da1933
'''

def hello_world():
    return "Hello World: ", time.strftime("%c")


#
# Python hello world
#
if __name__ == "__main__":
    import sys, time
    print(hello_world())


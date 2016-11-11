'''
Created on Nov 1, 2016

@author: Caroline
'''

def hello_world():
    return print("Hello World: ", time.strftime("%c"))

#
# Python hello world
#
if __name__ == "__main__":
    import sys, time
    hello_world()
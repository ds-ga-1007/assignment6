'''
Created on Nov 3, 2016

@author: sunevan
'''

def hello_word():
    return(print("Hello World: ", time.strftime("%c")))
#
# Python hello world
#
if __name__ == "__main__":
    import sys, time
    hello_word()
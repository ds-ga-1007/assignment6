'''
Created on Nov 4, 2016

@author: sj238


'''
#
# Python hello world
#
def hello_world():
    return print("Hello World: ", time.strftime("%c"))


if __name__ == "__main__":
    import sys, time
    hello_world()
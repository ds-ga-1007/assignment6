'''
Created on Nov 4, 2016

@author: wxy

'''

def hello_world():
    print "Hello World: ", time.strftime("%c")

if __name__ == "__main__":
    import sys, time
    hello_world()
'''
import time
#from decorator import Checker

def check(a):
    print("Function finished. Calculating the time...")
    if a < 0:
        raise ValueError
    else:
        get_time(a)

def get_time(a):
    print("Time:", time.ctime(a))

def function():
    try:
        #checker = Checker()
        b = time.time()
        print(b)
        check(b)
        #checker.Check()
    except:
        raise ValueError

function()
'''
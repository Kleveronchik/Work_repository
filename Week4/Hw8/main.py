import time
def check(a):
    print("Function finished. Calculating the time...")
    if type(a) != float:
        raise TypeError("TypeError: невірний тип даних.")
    elif a < 0:
        raise ValueError("ValueError: число менше за нуль.")
    else:
        get_time(a)
def get_time(a):
    print("Time:", time.ctime(a))
def function():
    try:
        b = time.time()
        #b = -3.3
        #b = "hhh"
        #підставляючи у b тип даних відмінний від float або від'ємне десяткове число видаватиме помилку
        check(b)
    except (ValueError, TypeError) as error:
        print("Error", error)
function()
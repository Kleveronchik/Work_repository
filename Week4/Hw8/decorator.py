'''
import time
class Checker:
    def Check(self, *exc_type):
        def Check(function):
            def Check(*args, **kwargs):
                try:
                    print(function(*args, **kwargs))
                except (exc_type) as ex:
                    print(ex)
                else:
                    print("No exception")
            return Check
        return Check

    def get_time(a):
        print("Time:", time.ctime(a))
    def Check(a):
        if a < 0:
            raise ValueError
        else:
            get_time(a)

    @Check(NameError, TypeError, SyntaxError, ZeroDivisionError, Exception)
    def Calculate(self, expresion):
        return eval(expresion)
'''
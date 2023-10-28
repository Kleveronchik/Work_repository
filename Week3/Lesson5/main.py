import requests
#help(requests)
'''
r = requests.get('https://www.python.org')
print(r.status_code)
print(r.content)
'''
'''
payload = dict(key1="group", key2="S2813")
r = requests.post("https://httpbin.org/post", data=payload)
print(r.text)
'''
#print(requests.__name__)
#print(type(requests.Response))
#print(dir(requests.Response))
#help(str)
'''
name = 'Andrii'
print(hasattr(name, 'reverse'))
print(hasattr(name, 'index'))
print(getattr(name, 'startswith1', "object has no attribute 'startswith1'"))

def get_full_name():
    pass
print(callable(name))
print(callable(get_full_name))
'''
class Parent:
    pass
class Child(Parent):
    pass
class Auto:
    pass
bmw = Auto()
son = Child()
print(issubclass(Child, Parent))
print(issubclass(Auto, Parent))
print(isinstance(bmw, Auto))
print(isinstance(son, Child))
print(isinstance(son, Parent))

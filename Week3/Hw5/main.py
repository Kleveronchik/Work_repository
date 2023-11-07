import inspect
import colorama
print("Це бібліотека? -", inspect.ismodule(colorama))
print("\nЧи її можна викликати? - ", callable(colorama))
print("\nШлях розташування бібліотеки\n", inspect.getmodule(colorama))
print("\nКоментарі\n", inspect.getcomments(colorama))
print("Коментарі + вихідний код\n", inspect.getsource(colorama))
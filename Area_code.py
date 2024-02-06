import time
from time import sleep
a = float(input("Enter Bigger Dia: "))
b = float(input("Enter smaller Dia: "))
c = 3.14*a*a/4-3.14*b*b/4
area = round(c,2)
print("area of curves : " , area)
sleep(10)
#for code running in command prompt
#you have to run some library
#python -m pip install auto-py-to-exe
#then after
#python -m auto_py_to_exe
#then it will ask for the directory path
#choose your directory or direct file path.

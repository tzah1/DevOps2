import datetime
import mydep as m
import my_other_dep
from mydep import test
from my_other_dep import test
from requests import Request

test()
print(datetime.datetime.now())
m.test()

def wait_for_print():
    from time import sleep
    sleep(3)
    print("waited for 3 seconds")


def wait_for_print2():
    from time import sleep
    sleep(3)
    print("waited for 3 seconds")

wait_for_print2()
"""
age = int(input("Enter your age: "))
if 31 < age < 41:
    print("your are ok")


years_of_experience = int(input("Enter your years of experience: "))
if 2 < years_of_experience < 10:
    print("your are eligible for the job")

def check_interval(question, min_v, max_v, answer):
    current_value = int(input(question))
    if min_v < current_value < max_v:
        print(answer)



q = "what is your age? "
b = 30
c = 50
d = "ok"
check_interval(q, b, c, d)
check_interval("was up? ", 2, 3, "cool")
def sqr(n=1):
    print (n*n)

sqr(5)

def addition(n=1, c=1):
    return n + c

result = addition(5, 7500)
print (result)
"""

def check_interval(question: str, min_v: int, max_v: int):
    current_value = int(input(question))
    if min_v < current_value < max_v:
        return True
    return False

check = check_interval("Enter your age: ", 30, 50)
if check:
    print("Your age is ok")



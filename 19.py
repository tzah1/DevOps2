a = "tzah"
b = "marciano"
names = ["ben", "hod", "liron" ]
[print(a) for i in range(0,5,1)]
print (b*5)

[print(f"hello {name}!") for name in names]

for name in names:
    if name == "hod":
        name = "moshe"
    print(f"hello {name}!")
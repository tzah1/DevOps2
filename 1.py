from Tools.scripts.md5sum import printsumfp

a = 4
b = "tzzah"
c = False
d = ["tzzah", "marciano", 34, True]
e = {"fname": "avial",
     "lname": "marciano",
     "age": 34}

f = dict(fname="tzah", lname="marciano", age=34)

list_of_people = [e, f]

print(e["lname"])
print(d[2])
print(a)
print("name is: " + b)
print(c)
print(list_of_people)
r = 4 + 4
s = "tzah" + "marciano"
t = "tzah" * 4
u = "tzah" + str(4)
print(t)
v = int(5.4)
fname = "tzah"
lname = "marciano"
first =  fname + lname
second = "{} {}".format(lname, fname)
third = f"{fname} {lname}"
forth = "%s %s" % (lname, fname)



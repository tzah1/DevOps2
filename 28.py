a = range(1,101)
for i in a:
    if i % 7 == 0 or str(i) in "7":
        continue
    else:
        print(i)


result = [i for i in a if i % 7 == 0 or str(i) in "7"]
print (result)


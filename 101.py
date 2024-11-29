current_name = input('Enter name:')

my_file = open('name.txt', 'a')
my_file.write(current_name + '\n')
my_file.close()

my_file = open('name.txt', 'r')
for name in my_file.readlines():
    if "t" in name:
        print(f'Hello, {name.strip()}!')
my_file.close()

'''opendefinitions:
r- reading
w - writing and truncatenating
a - appending
w+ -'''
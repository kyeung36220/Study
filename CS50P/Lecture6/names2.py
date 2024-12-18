names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse = True):
    print(f"hello, {name}")



#can also do this:
#with open("names.txt") as file:
    #for line in sorted(file):
        #print("hello,", line.rstrip())

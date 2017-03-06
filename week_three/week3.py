file1 = open("w3.txt", 'w')
file1.write("Hello world\n")
file1.write("Anotha one")
file1.close()

file1 = open('w3.txt', 'r')
#list1 = file1.readlines()
for line in file1:
    print(line)

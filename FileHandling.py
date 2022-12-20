print("__________ Khaerunnisa Isnaeni Lestari ___________")
print("________________ Kelas TI 22 C1 __________________")
print("__________________ 312210008 _____________________")

print(" File Handling ")

f = open("demofile.txt", "r")
print(f.read())	
print(f.readline())

f = open("demofile.txt", "a")
f.write("Hello this is first line message")
f.write("Hello this is 2nd line message")

f = open("demofile.txt", "w")
f.write("Woops! I have deleted the content!")
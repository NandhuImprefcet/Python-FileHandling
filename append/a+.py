f=open('test.txt','a+')
print(f.read())
f.write("\nthis is a added line")
f.seek(0)
print()
print(f.read())
f.seek(0)
f.write('im trying to add this line as the first line\n')
print(f.read())
print()
f.seek(0)
print(f.read())

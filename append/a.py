f=open('test.txt','a')

f.write("\nthis is a added line")
f.seek(0)
print('\n\n')
print(f.read())
f.seek(0)
f.write('editing the statement')
print('\n\n')
f.seek(0)
print(f.read())

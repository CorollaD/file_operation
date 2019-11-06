filename = 'G:\\1.txt'
with open(filename) as f_obj:
    a = f_obj.read()
    b = a.split()
    i = 0
    while i < len(b):
        i += 1
        print(b[i-1])

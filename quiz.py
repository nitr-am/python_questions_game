f = open('/home/ubuntu/environment/files/relative_data.txt', 'r') # Here the 'r' is to read.
lines = f.read()
f.close()
print(lines)
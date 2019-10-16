f = open('newfile.txt', 'a') # 'w' is to write 'a' Is to append. The difference is that write rewrite and replace new word each time and the 'a' appends every new word. 
# The thing is that with every new word it will be appended in the same single line. If I want every new word to be appenden in a new line I must use \n right next to the line. 
# f.write('World\n')
# f.close()
lines = ['Hello','World','Welcome','To','File IO\n']
text = ' '.join(lines)
f.writelines(text)
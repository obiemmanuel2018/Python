# with open('file_binary.txt', 'w') as f:
#
#     f.write('To be or not to be\n')
#     f.write('That is the question.\n')
#     f.write('Whether tis nobler in the mind\n')
#     f.write('To suffer the slings and arrows\n')
#
# with open('file.txt', 'r') as f:
#     print(f.seekable())
#     print(f.tell())
#     s = ' '  # Set to a blank space initially
#     print('first time')
#     while s:
#         s = f.readline()
#         print(s,end='')
#     print(f.tell())
#     print('second time')
#
#     s = ''
#     while 1:
#         s = f.readline()
#         print(s,end='')
#
#
#
# with open('my.dat', 'wb') as f:
#     f.write(bytes([1,2,3,4,5,0x10]))
#
# with open('my.dat', 'rb') as f:
#         bss = f.read()
#         for i in bss:
#             print(i, end=' ')

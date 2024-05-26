import os
import shutil

directory = 'empty-directory-created-from-python'
parent_directory = 'D:\Python Code Practices'
newDir_path = os.path.join(parent_directory, directory)

os.mkdir(newDir_path)
file_name = open('sample.txt', 'w')
file_name.write('Hey, I created this file with the help of python scripting.')
file_name.close()

shutil.move('sample.txt', 'D:\empty-directory-created-from-python\sample.txt')
print("Directory '%s' created" %directory)

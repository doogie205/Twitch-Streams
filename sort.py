import os
import time

#Reference:
#list1 = ["juice", "jam", "quac"]
#list2 = ["juice", "jam", "java"]
#
#for _ in range(len(list1)):
#  if(list1[_] not in list2):
#    print(list1[_])
#Output: quac



initial_dir = os.listdir()
dir_path = os.path.dirname(os.path.realpath(__file__))
#print(dir_path)

while True:
  new_dir = os.listdir()
  if(initial_dir != new_dir):
    for _ in range(len(new_dir)):
      if(new_dir[_] not in initial_dir):
        print(new_dir[_])
        if(new_dir[_][len(new_dir[_])-4:] == ".txt"):
          #os.rename("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
          #FileExistsError: [WinError 183] Cannot create a file when that file already exists: 'E:\\Programming\\Python/Test.txt' -> 'E:\\Programming\\Python/Text Files/Test.txt'
          #IF the file already exists, we will have to create a case for it where we use a counter and just go up on the naming convention: (#)
          #Test.txt -> Test(1).txt -> Test(2).txt ...
          os.rename("{}/{}".format(dir_path,new_dir[_]),"{}/{}".format(dir_path,"Text Files/{}".format(new_dir[_])))
          print("{}/{}".format(dir_path,new_dir[_]))
          print("{}/{}".format(dir_path,"Text Files/{}".format(new_dir[_])))

  time.sleep(1)

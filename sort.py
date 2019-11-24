import os
import time

#Set the dir here:
initial_dir = os.listdir(r"E:/Temp")#Inside here.
dir_path = r"E:/Temp"
new_dir_path = r"E:"

while True:
  new_dir = os.listdir(r"E:/Temp")#Set it again here.
  if(initial_dir != new_dir):
    for _ in range(len(new_dir)):
      if(new_dir[_] not in initial_dir):
        print(new_dir[_])
        if(new_dir[_][len(new_dir[_])-4:] == ".txt"):
            #FileExistsError: [WinError 183] Cannot create a file when that file already exists: 'E:\\Programming\\Python/Test.txt' -> 'E:\\Programming\\Python/Text Files/Test.txt'
            #IF the file already exists, we will have to create a case for it where we use a counter and just go up on the naming convention: (#)
            #Test.txt -> Test(1).txt -> Test(2).txt ...
            try:
                os.rename("{}/{}".format(dir_path,new_dir[_]),"{}/{}".format(new_dir_path,"Text Files/{}".format(new_dir[_])))
            except FileExistsError:
                file_exists = False
                count = 0
                while(file_exists == False):
                    try:
                        os.rename("{}/{}".format(dir_path,new_dir[_]),"{}/{}".format(new_dir_path,"Text Files/({}){}".format(count, new_dir[_])))
                        file_exists = True
                    except:
                        count += 1
                        pass
           

  time.sleep(1)

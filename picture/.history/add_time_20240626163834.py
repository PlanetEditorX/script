import hashlib
import os
import time
import re

def add_time(folder_path):
    #读取文件的日期，将其添加到文件名前缀
    modifytime = 0
    hashes = {}
    for dirname, subdirs, filelist in os.walk(folder_path):
        print(f"Scanning {dirname}...")
        for filename in filelist:
            file_path = os.path.join(dirname, filename)
            file_time = os.stat(file_path)
            pattern = re.compile(r'\d{4}(\-|\/|.)\d{1,2}\1\d{1,2}')
            if (re.match()) {
                
            }
            #st_ctime:创建日期
            #st_mtime: 最后一次修改的时间
            st_ctime = file_time.st_ctime
            st_mtime = file_time.st_mtime
            #找到最早的日期
            if st_ctime >= st_mtime:
                f_time = st_mtime
            else:
                f_time = st_ctime

            timeArray = time.localtime(f_time)
            preTime = time.strftime("%Y_%m_%d_%H_%M_%S_", timeArray)
            print(preTime)

            #设置新文件名
            newname = dirname + '\\' + preTime + filename

            os.rename(file_path, newname)
            print(file_path, '======>', newname)
            modifytime += 1

    return modifytime

# 选择你照片视频文件夹的路径
folder_path = 'C:\\Users\\DearX\\Downloads\\picture'

start_time = time.time()
modifytime = add_time(folder_path)
end_time = time.time()

print(f"Found and modify {modifytime} duplicate files.")
print(f"Time taken: {end_time - start_time} seconds.")
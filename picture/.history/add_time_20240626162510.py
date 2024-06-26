import hashlib
import os
import time

def add_time(folder_path):
    #读取文件的日期，将其添加到文件名前缀
    duplicates = []
    hashes = {}
    for dirname, subdirs, filelist in os.walk(folder_path):
        print(f"Scanning {dirname}...")
        for filename in filelist:
            file_path = os.path.join(dirname, filename)
            file_time = os.stat(file_path)
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

            #设置旧文件名（就是路径+文件名）
            oldname=dirname + filename

            #设置新文件名
            newname=path + os.sep +'a'+str(n+1)+'.JPG'

            os.rename(oldname,newname)   #用os模块中的rename方法对文件改名
            print(oldname,'======>',newname)

        #   if filehash in hashes:
        #      duplicates.append(file_path)
        #   else:
        #        hashes[filehash] = file_path

    # 删除重复文件
    # for duplicate in duplicates:
    #   os.remove(duplicate)

    return duplicates

# 选择你照片视频文件夹的路径
folder_path = 'C:\\Users\\DearX\\Downloads\\picture'

start_time = time.time()
duplicates = add_time(folder_path)
end_time = time.time()

print(f"Found and removed {len(duplicates)} duplicate files.")
print(f"Time taken: {end_time - start_time} seconds.")
#此脚本实现所需import的都是Python自带的标准库，所以不需要安装任何第三方库
import hashlib
import os
import time


def file_hash(filepath):
    """计算文件的哈希值"""
    with open(filepath, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

def file_time(file_path):
    """读取文件的创建日期"""
    with open(filepath, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

def remove_duplicates(folder_path):
    """删除文件夹中的重复文件"""
    duplicates = []
    hashes = {}
    for dirname, subdirs, filelist in os.walk(folder_path):
        print(f"Scanning {dirname}...")
        for filename in filelist:
            file_path = os.path.join(dirname, filename)
            file_time = os.stat(file_path)
            #st_ctime:创建日期
            #st_mtime: 最后一次修改的时间
            if file_time.st_ctime >file_time.st_mtime
            st_ctime = file_time.st_ctime
            st_mtime = file_time.st_mtime

            timeArray = time.localtime(st_ctime < st_mtime ? st_ctime : st_mtime)
            otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)


            print(otherStyleTime)
        #   if filehash in hashes:
        #      duplicates.append(file_path)
        #   else:
        #        hashes[filehash] = file_path

    # 删除重复文件
    # for duplicate in duplicates:
    #   os.remove(duplicate)

    return duplicates

# 选择你照片视频文件夹的路径，Mac OS下可以按住Option后右键选择拷贝文件路径
folder_path = 'C:\\Users\\DearX\\Downloads\\picture'

start_time = time.time()
duplicates = remove_duplicates(folder_path)
end_time = time.time()

print(f"Found and removed {len(duplicates)} duplicate files.")
print(f"Time taken: {end_time - start_time} seconds.")
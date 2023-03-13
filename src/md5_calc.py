import hashlib

def md5_calc(path,file_list):
    mymd5=hashlib.md5()
    for file in file_list:
        with open(path+file,'rb') as f:
            mymd5.update(f.read())
    return mymd5.hexdigest()
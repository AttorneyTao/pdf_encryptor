#encoding:utf-8
from src import encryptor,md5_calc
import os
if __name__=='__main__':
    path='.\\files\\'
    file_list=os.listdir(path)
    for file_name in file_list:
        encryptor.pdf_encrypt(path+file_name,'199262')
    md5=md5_calc.md5_calc('.\\encrypted\\',file_list)
    md5_test=md5_calc.md5_calc('.\\encrypted\\',file_list)
    with open('md5.txt','w') as f:
        f.write('md5: '+md5_calc.md5_calc('.\\encrypted\\',file_list))
    if md5==md5_test:
        print('md5 verify passed')
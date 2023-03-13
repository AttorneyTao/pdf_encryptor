from PyPDF2 import PdfReader, PdfWriter
import os
from enum import IntFlag
def pdf_encrypt(file:str,  pwd:str = '123456' , target:str ='.\\encrypted\\' ,permission=-3900):
    """
     Encrypt a PDF file with a password This is useful for encrypting documents that are stored in a PDF file and can be used to verify the integrity of the document.
     
     @param file - The path to the PDF file to encrypt.
     @param target - The text to write the encrypted file to.
     @param pwd - The password to encrypt the file with. Default is 123456
     
     @return True if the operation was successful False otherwise. Note that a return value of False does not indicate success
    """
    writer=PdfWriter()
    reader=PdfReader(file)
    i=0
    # Add all pages to writer.
    for page in reader.pages:
        writer.add_page(page)
        i+=1
    print(f'encrypting {i} pages in {file}')
    # Add a password to the new PDF
    writer.encrypt(user_password="",owner_password=pwd,permissions_flag=permission)

    # Save the new PDF to a file
    with open(target+os.path.basename(file), "wb") as f:
        writer.write(f)
    return
    

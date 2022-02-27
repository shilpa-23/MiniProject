import hashlib
import os
def file_hash(filename):
   #function gives SHA-1 hash when pass a file

   # make a hash object
   h = hashlib.sha1()

   # open file for reading in binary mode

   with open(filename,'rb') as file:

       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           # read only 1024 bytes at a time
           chunk = file.read(1024)
           h.update(chunk)

   # return the hex representation of digest
   return h.hexdigest()
n1=input("first uploaded file:")
n2=input("second uploaded file:")
hash = file_hash(n1)
hash1 = file_hash(n2)
#print(message)
#print(message1)
if hash == hash1:
    print("Both files are same")
    os.remove(n2)
    print("File",n2,"Removed from the folder")
    print("Hash:" ,hash)


else:
    print("Files are different!")
    print("Hash of File 1:", hash)
    print("Hash of File 2:", hash1)



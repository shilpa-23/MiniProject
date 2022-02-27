import hashlib

def hash_file(filename):
   """"This function returns the SHA-1 hash
   of the file passed into it"""

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
message = hash_file(n1)
message1 = hash_file(n2)
#print(message)
#print(message1)
if message == message1:
    print("Both files are same")
    print(f"Hash: {message}")


else:
    print("Files are different!")
    print(f"Hash of File 1: {message}")
    print(f"Hash of File 2: {message1}")



import hashlib, os

dict = {}

lis = os.listdir("python")


for i in lis:
    with open("python/" + i, "rb") as f:
        content = f.read()
        hash_value = hashlib.md5(content).hexdigest()
    if hash_value in dict:    
        print("중복", i)
        
    else:
        dict[hash_value] = i
        print(dict)
        
    
    

# with open("test.txt", "rb") as f:
#     content = f.read()
#     hash_value = hashlib.md5(content).hexdigest()
#     print(hash_value)
    
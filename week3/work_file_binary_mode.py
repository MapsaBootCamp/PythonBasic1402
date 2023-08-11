from lib.utils import is_falsy




# f = open("note.txt", "rb")

# f.seek(3) #  cursor 3 ta az aval bere jelo
# f.seek(3, 1) # cursor 3 ta boro jelo az injai ke alan hastam!
# f.seek(-3, 2) # cursor boro akhar va 3 ta bargard!
# print(f.read())

# f.close()


import hashlib

# hashlib.sha256(b"SALAM")

# print(bytearray("SALAM", encoding='utf-8'))

print(hashlib.sha256(bytearray("SALAM", encoding='utf-8')).hexdigest())

with open("test_for_hash.txt", "rb") as f:
    print(hashlib.sha256(f.read()).hexdigest())




# condition = {}     # "", [], 0, None, {}, 
# if is_falsy(condition):
#     print("Falsy")
# else:
#     print("Trusy")


# ### read chunk_by_chunk
buffer_size = 1
hashed_data = hashlib.sha256()
with open("test_for_hash.txt", "rb") as f:
    while chunked_data := f.read(buffer_size):
        hashed_data.update(chunked_data)
print(hashed_data.hexdigest())

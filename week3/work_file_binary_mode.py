import hashlib

print(hashlib.sha256(bytearray("SALAM", encoding='utf-8')).hexdigest())

with open("test_for_hash.txt", "rb") as f:
    print(hashlib.sha256(f.read()).hexdigest())

### read chunk_by_chunk
buffer_size = 10
hashed_data = hashlib.sha256()
with open("test_for_hash.txt", "rb") as f:
    while chunked_data := f.read(buffer_size):
        hashed_data.update(chunked_data)
print(hashed_data.hexdigest())

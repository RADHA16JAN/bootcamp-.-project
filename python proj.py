import hashlib

text = "think and wonder,wonder and think"
hash_obj = hashlib.md5(text.encode())
md5_hash = hash_obj.hexdigest()
print(md5_hash)

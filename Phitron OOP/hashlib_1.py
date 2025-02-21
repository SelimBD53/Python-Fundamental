import hashlib

email = "selim@gmail.com"
pwd = "SelimReza"
pwd_encode = pwd.encode()
pwd_hash = hashlib.md5(pwd_encode).hexdigest()
print(pwd_hash)


your_email = "selim@gmail.com"
your_pwd = "SelimReza"
hased_your_password = hashlib.md5(your_pwd.encode()).hexdigest()
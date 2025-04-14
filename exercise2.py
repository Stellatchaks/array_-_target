plainText = "python"
distance = 3
code = ""
for char in plainText:
    ordvalue = ord(char)
    cipherValue = ordvalue + distance
    if cipherValue > ord('z'):
         cipherValue = ord('a') + distance - \
         (ord('z') - ordvalue + 1)
    code += chr(cipherValue)
print(code)


plainText = "hacker"
distance = 3
code = ""
for char in plainText:
    ordvalue = ord(char)
    cipherValue = ordvalue + distance
    if cipherValue > ord('z'):
         cipherValue = ord('a') + distance - \
         (ord('z') - ordvalue + 1)
    code += chr(cipherValue)
print(code)


plainText = "wow"
distance = 3
code = ""
for char in plainText:
    ordvalue = ord(char)
    cipherValue = ordvalue + distance
    if cipherValue > ord('z'):
         cipherValue = ord('a') + distance - \
         (ord('z') - ordvalue + 1)
    code += chr(cipherValue)
print(code)
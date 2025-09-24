a = ["Artem Pronin", "Novikov Ivan", "Dmytrii Korolev", "Anastasia Palchick"]

for name in a:
    for char in name:
        code = ord(char)
        print(f"{char}\n10: {code}\n2: {bin(code)[2:]}\n16: {hex(code)[2:]}\n")

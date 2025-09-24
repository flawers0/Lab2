# Бригада №8 Пронін Артем, Новіков Іван, Дмитрій Корольов, Анастасія Пальчик
a = ["Artem Pronin", "Novikov Ivan", "Dmytrii Korolev", "Anastasia Palchick"]

for name in a:
    for char in name:
        code = ord(char)
        print(f"{char} - {code} - {bin(code)[2:]} - {hex(code)[2:]}")

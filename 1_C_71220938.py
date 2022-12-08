kata = input("masukan kata atau angka:")
def reversed(kata):
    str=""
    for i in kata:
        str = i + str
    return str
print(reversed(kata))
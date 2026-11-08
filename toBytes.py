from numpy import byte


raw =  open("./fra.txt", "r")

asciiArr = raw.readlines()
# 0xF0 = EMPTY (!)
# 0xF1 = FULL (*)
# 0xF2 = EQUAL (=)
# 0xF3 = TOEOL (])
# 0xF4 = NEXTLINE
# 0xFE = NEXTFRAME
conv = {"!" : b'\xF0',
        "*" : b'\xF1',
        "=" : b'\xF2',
        "]" : b'\xF3',
        "%" : b'\xF4'}


with open("./bitten_F.bin", "wb") as butter:
    for k in asciiArr:
        fks = k.strip().split(',')
        for llm in fks:
            if llm in conv:
                butter.write(conv[llm])
            else:
                butter.write(bytes([int(llm)]))
        butter.write(b'\xFE')


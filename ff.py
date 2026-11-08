dest = open(r"./fra.txt", "w")
frame = []
rows = []
nFrame = []
lFrame = []
with open(r"./frames.txt", "r") as origin:
    k = 0
    rows = origin.readlines()
    
    # while line is not None and line.strip() != "%":
    #     rows.append(line)
    #     line = origin.readline()
    # break
ker = 1

def frameequals(f1, f2):
    if len(f1) != len(f2):
        return False

    for i in range(len(f1)):
        if str(f1[i]).strip() != str(f2[i]).strip():
            return False

    return True

for line in rows:
    started = False
    off = True
    ft = []
    total = 0
    
    if len(nFrame) == 65:
        if frameequals(nFrame, lFrame):
            frame.append(["=", "%"])
            lFrame = nFrame.copy()
            nFrame = []
        else:
            for i in range(64):
                if nFrame[i].strip() == lFrame[i].strip() && len(nFrame[i].strip()) != 1:
                    nFrame[i] = "="



    if line.strip() == "%":
        print(f"frame: {ker}")
        ker += 1
        ft.append('%')
        nFrame.append(ft)
        continue

    if line is None:
        continue
    
    for i, c in enumerate(line.strip()):
        if c == "▓":
            total += 1
            if not started:
                ft.append(i+1)
                started = True
                off = False
                
        elif c == "·" and not off:
            ft.append(i)
            started = False
            off = True

    if total == 128:
        nFrame.append(["*"])
        continue
        
    if total == 0:
        nFrame.append(["!"])
        continue

    if len(ft) % 2 == 1:
        ft.append(']')
        

    if total == 128:
        frame.append(["*"])
        continue

    if len(ft) < 1:
        frame.append(["!"])
        continue

    elif len(ft) % 2 == 1:
        ft.append(']')
    
    if frameequals(ft, lFrame):
        frame.append("=")   
    else:
        frame.append(ft)

dest.writelines(''.join('\n'.join(','.join(str(k) for k in f) for f in l) for l in frame))

# print('\n'.join(','.join(str(k) for k in f) for f in frame))

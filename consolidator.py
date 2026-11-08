c = open("./consolidated.txt", "w", encoding="utf-8")
with open ("./frames.txt", "r", encoding="utf-8") as f:
    frame = []
    for line in f:
        if line == "%":
            c.writelines(frame+'%\n')
        off =0
        on = 0
        for j, k in enumerate(line): 
            if k == "▓":
            

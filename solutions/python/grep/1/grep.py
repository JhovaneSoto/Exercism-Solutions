def grep(pattern, flags, files):
    coincidencias = []

    ban_i=False
    if "-i" in flags:
        pattern=pattern.upper()
        ban_i=True
        
    for file in files:
        with open(file,"r") as f:
            data = f.read()
        lines = data.split("\n")
        lines = [item for item in lines if item!=""]
        for idx,line in enumerate(lines):
            line_temp=line
            if ban_i:
                line_temp=line.upper()
                
            if "-x" in flags:
                if "-v" in flags:
                    if not(pattern==line_temp):
                        coincidencias.append([line,idx+1,file])
                else:
                    if pattern==line_temp:
                        coincidencias.append([line,idx+1,file])
            else:
                if "-v" in flags:
                    if not pattern in line_temp:
                        coincidencias.append([line,idx+1,file])
                else:
                    if pattern in line_temp:
                        coincidencias.append([line,idx+1,file])
    out=""
    l_idx=-1
    n_idx=-1
    if "-l" in flags:
        l_idx=list(flags).index("l")

    if "-n" in flags:
        n_idx=list(flags).index("n")

    ban_files=False
    if len(files)>1:
        ban_files=True
    for con in coincidencias:
        temp_out=""
        file_ubicacion=""
        if ban_files:
            file_ubicacion=con[2]+":"
        if "-l" in flags:
            if con[2]+"\n" not in out:
                temp_out+=con[2]+"\n"
            
    
        if "-n" in flags and n_idx>l_idx:
            temp_out+=f"{file_ubicacion}{con[1]}:{con[0]}\n"

        if not("-l" in flags or "-n" in flags):
            temp_out+=file_ubicacion+con[0]+"\n"
        
        
        
        out+=temp_out
    
    return out
    

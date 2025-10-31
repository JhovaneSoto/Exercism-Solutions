seven_segment_digits = {
    '1111110': "0",
    '0110000': "1",
    '1101101': "2",
    '1111001': "3",
    '0110011': "4",
    '1011011': "5",
    '1011111': "6",
    '1110000': "7",
    '1111111': "8",
    '1111011': "9"
}

def convert(input_grid):
    if len(input_grid)%4!=0:
        raise ValueError("Number of input lines is not a multiple of four")

    if any([True if len(item)%3!=0 else False for item in input_grid]):
        raise ValueError("Number of input columns is not a multiple of three")

    #dividir segmentos
    cifras_verticales=[input_grid[pos:pos+4] for pos in range(0,len(input_grid),4)]
    out=[]
    for cifras in cifras_verticales:
        cifras_horizontales=[cifra[pos:pos+3] for pos in range(0,len(cifras[0]),3) for cifra in cifras]
        
        items=[cifras_horizontales[pos:pos+4] for pos in range(0,len(cifras_horizontales),4)]
        
        out.append("".join([convert_digit(item) for item in items]))
        
    
    return ",".join(out)

def convert_digit(grid):
    [_,a,_],[f,g,b],[e,d,c],[_,_,_]=grid

    if (any([True if segmento!="_" and segmento!=" " else False for segmento in [a,g,d]])) or (any([True if segmento!="|" and segmento!=" " else False for segmento in [f,b,e,c]])):
        return "?"
    
    binario="".join(["1" if car!=" " else "0" for car in [a,b,c,d,e,f,g]])
    #print(binario)
    if binario in seven_segment_digits.keys():
        return seven_segment_digits[binario]
    
    return "?"

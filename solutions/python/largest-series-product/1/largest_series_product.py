def largest_product(series, size):
    if len(series)<size:
        raise ValueError("span must not exceed string length")
    if size<=0:
        raise ValueError("span must not be negative")
    if any([not letter.isdigit() for letter in series]):
        raise ValueError("digits input must only contain digits")
    digits=[]
    for pos in range(0,len(series)-size+1):
        item=series[pos:pos+size]
        prod=1
        nums=[int(letter) for letter in item]
        for num in nums:
            prod*=num
        digits.append([item,prod])

    digits=sorted(digits,key=lambda x:x[1],reverse=True)
    return digits[0][1]

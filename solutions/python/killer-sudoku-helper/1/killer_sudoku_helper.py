def combinations(target, size, exclude):
    data=all_sums(size,[1,2,3,4,5,6,7,8,9])
    return [item for item in data if sum(item)==target and not any([excluido in item for excluido in exclude])]

def all_sums(tam,digits):
    if tam == 0:
        return [[]]
    if len(digits) < tam:
        return []

    out = []
    for i in range(len(digits)):
        num = digits[i]
        for rest in all_sums(tam - 1, digits[i+1:]):
            out.append([num] + rest)
    return out

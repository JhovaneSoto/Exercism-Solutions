def transform(legacy_data):
    salida = {}
    for points in legacy_data.keys():
        values = legacy_data[points]
        for value in values:
            value=value.lower()
            salida[value]=points

    return salida

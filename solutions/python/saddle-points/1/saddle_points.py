def saddle_points(matrix):
    if matrix==[]:
        return []
    if len(set([len(item) for item in matrix]))!=1:
        raise ValueError("irregular matrix")
    out=[]
    for idx_row in range(len(matrix)):
        for idx_column in range(len(matrix[idx_row])):
            if smallest(matrix,idx_column)==largest(matrix,idx_row)==matrix[idx_row][idx_column]:
                out.append({'row': idx_row+1, 'column': idx_column+1})
    return out


def largest(matrix,idx):
    return max(matrix[idx])

def smallest(matrix,idx):
    return min([item[idx] for item in matrix])
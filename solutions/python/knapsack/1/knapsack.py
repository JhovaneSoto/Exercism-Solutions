def maximum_value(maximum_weight, items):
    items=sorted(items,key=lambda x:(x['value'],-x['weight']),reverse=True)

    all_combinations=make_combo(maximum_weight,items)
    combinations=sorted(all_combinations,key=lambda x:sum([item["value"] for item in x]),reverse=True)
    if len(combinations)==0:
        return 0

    return sum([item["value"] for item in combinations[0]])

def make_combo(maximum_weight,items):
    if maximum_weight<=0 or len(items)==0:
        return []
    out=[]
    for idx,item in enumerate(items):
        candidate=[]
        if item["weight"]<=maximum_weight:
            other_items=make_combo(maximum_weight-item["weight"],items[idx+1:])
            if len(other_items)==0:
                out.append([item])
            else:
                for o_i in other_items:
                    out.append([item]+o_i)
    return out
    
forbidden = []
def measure(bucket_one, bucket_two, goal, start_bucket):

    if start_bucket=="one":
        a=bucket_one
        b=0
    else:
        a=0
        b=bucket_two

    item, cont = movements([[a, b]], [bucket_one, bucket_two], goal, start_bucket)
    
    if not item:
        raise ValueError("d")
        
    out=[cont]
    idx = item.index(goal)
    if idx == 0:
        out.append("one")
    else:
        out.append("two")
    out.append(item[(idx+1)%2])
    print("-",item,"-")
    return tuple(out)

def movements(buckets_list, limits, goal, start_bucket):
    history=buckets_list
    cont = 1
    while buckets_list!=[]:
        
        tempo_buckets = []
        
        print("---",buckets_list)
        for buckets in buckets_list:
            
            for action in range(3):
                for idx, bucket in enumerate(buckets):
                    item=buckets.copy()
                    if goal in item:
                        return item,cont
                    idx_a = idx
                    idx_b = (idx+1)%2
    
                    if action == 0:
                        item[idx_a] = limits[idx_a]
    
                    if action == 1:
                        item[idx_a] = 0

                    if action == 2:
                        delta_a = item[idx_a]
                        delta_b = limits[idx_b] - item[idx_b]

                        delta = min([delta_a,delta_b])
                        
                        item[idx_a] -= delta
                        item[idx_b] += delta
                        
                    if goal in item:
                        return item,cont+1
                        
                    if is_valid(item,start_bucket,limits):
                        if item not in history:
                            tempo_buckets.append(item)
        cont += 1
        history+=tempo_buckets
        buckets_list=tempo_buckets
        
    return None, None

def is_valid(buckets,start_bucket,limits):
    if sum(buckets) == 0:
        return False
    if start_bucket=="one":
        if buckets[0]==0 and buckets[1]==limits[1]:
            return False
    else:
        if buckets[1]==0 and buckets[0]==limits[0]:
            return False
    return True

                                        
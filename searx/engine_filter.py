def filter_engines(results, filters): 
    temp =  results
    for i in filters:
        if i != None:
           remove_engine(i, temp)

    return results


def remove_engine(domain, arr):
    nums = []

    for idx, val in enumerate(arr):
        if(val["parsed_url"].netloc == domain):
            nums.append(idx)

    for i in range(len(arr) - 1, -1, -1):
        if  i in nums:
            arr.pop(i)

    return arr

def is_valid(s):
    valid_start=['[','{','(']
    valid_stop=[']',')','}']
    valid_pairs=['()','{ }','[]']
    temp=[]
    for i in s:
        if i in valid_start:
            temp.append(i)
        elif i in valid_stop:
            if temp:
                p=temp.pop()+i
                if p not in valid_pairs:
                    return False
            else:
                return False
    if temp:
        return False
    return True

print(is_valid('ff(kk}j['))

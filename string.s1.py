# Length of the String
def str_length(k):
    count = 0
    for i in k:
        count += 1
    return count
print(str_length(input()))


# return first two last two letters of string
def str_lengt(k):
    if len(k) <= 2:
        return ''
    else:
        return k[0:2] + k[-2:]
print(str_lengt(input()))  

# first, middle, last chars
def fml(fml):
    fml_op = fml[0]+fml[int(len(fml)/2)]+fml[-1]
    return fml_op
print(fml(input()))

# middle three characters
def mid_3(fml):
    m = int(len(fml)/2)
    if len(fml) % 2 != 0: 
        mid_3 = fml[m-1:m+2]
        return mid_3
    else:
        return 'even'
print(mid_3(input()))

# Homework - Day 4 - Sivakumar
#
def divisible(n):
    ans = False
    for i in range(2,n):
        if n%i == 0:
            ans = True
            break

    return ans

def prim_nmbrs(st, en):
    prm_lst = []
    for i in range(st, en+1):
        if divisible(i):
            continue
        else:
            prm_lst.append(i)
    
    return prm_lst
    

start = 0
end = 100
print("Prime numbers between ", start, " and ", end, " are: ")
print(prim_nmbrs(start,end))


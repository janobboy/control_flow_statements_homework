def main(a,b,c):
    k=0
    if a<0:
        k+=1
    if b<0:
        k+=1
    if c<0:
        k+=1
    return k
print(main(-2,4,1))
print(main(3,-3,-6))
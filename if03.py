def main(a):
    """
    If the number is positive, increase it to 1,if the number is negative decrease it to 2.
    If it is 0, assign 10.
    Args:
        a: integer
    Returns:
        a: integer
    """
    if a<0:
        a+=-2
    if a>0:
        a+=1
    return a
print(main(-9))
print(main(3))
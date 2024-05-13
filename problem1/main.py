def compare(a, b):
    pattern = ""
    for x,y in zip (a,b):
        if x != y :
            pattern += str(x)
        else :
            pattern += str(y)
    return pattern

if __name__ == '__main__':
    print(compare("AKA", "AKASHI")) # AKA
    print(compare("KANGOORO", "KANG")) # KANG
    print(compare("KI", "KIJANG")) # KI
    print(compare("KUPU-KUPU", "KUPU")) # KUPU
    print(compare("ILALANG", "ILA")) # ILA
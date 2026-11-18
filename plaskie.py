def pp_kwadratu(a:float)->float:
    return a**2

def pp_porstokata(a:float, b:float)->float:
    return a*b

def legenda_pp()->None:
    print("a -- pp_kwadratu")
    print("b -- pp_porstokata")
    print("e -- Exsit")


def jakie_pp()->None:
    while True:
        legenda_pp()
        inp = input().lower().strip()
        if inp == "e":
            print("Exsit")
            break
        elif inp == "a":
            a = float(input("a = "))
            print(f"dla {a} pp_kwadratu = {pp_kwadratu(a)}")
        elif inp == "b": 
            a = float(input("a = "))
            b = float(input("b = "))
            print(f"dla {a} {b} pp_porstokata = {pp_porstokata(a,b)}")

            

# ------------------------------------------------------------------------------
def obw_kwadaru(a:float)->float:
    return 4*a

def obw_prostokata(a:float, b:float)->float:
    return 2*a+2*b

def obw_trapezu(a:float, b:float, c:float, d:float)->float:
    return a + b + c + d

def legenda_obw()->None:
    print("a -- obw_kwadaru")
    print("b -- obw_prostokata")
    print("c -- obw_trapezu")
    print("e -- zkoncz program")

# ------------------------------------------------------------------------------

def jaki_obw()->None:
    while True:
        legenda_obw()
        inp = input().lower().strip()
        if inp == "e":
            print("Exsit")
            break
        elif inp == "a":
            a = float(input("a = "))
            print(f"dla {a} obw_kwadratu = {obw_kwadaru(a)}")
        elif inp == "b": 
            a = float(input("a = "))
            b = float(input("b = "))
            print(f"dla {a} {b} obw_prostokata = {obw_prostokata(a,b)}")
        elif inp == "c":
            a = float(input("a = "))
            b = float(input("b = "))
            c = float(input("c = "))
            d = float(input("d = "))
            print(f"dla {a} {b} {c} {d} obw trapezu = {obw_trapezu(a,b,c,d)}")


# ------------------------------------------------------------------------------

def plaskie()->None:
    while True:
        print("a -- pp fig plaskich")
        print("b -- obw fig plaskich")
        print("e -- Exsit ")
        inp = input().lower().strip()
        if inp == "a":
            jakie_pp()
        elif inp == "b":
            jaki_obw()
        elif inp == "e":
            print("Exsit")
            break



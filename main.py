import funkcje.plaskie as pl


def main():
    print("e - zakoncz program")
    print("a - plaskie")
    print("b - bryly")
    print("c - warunki")
    while True:
        inp = input().lower().strip()
        if inp == "e":
            print("Program zkonczyl dzialanie")
            break
        elif inp == "a":
            pl.plaskie()
        elif inp == "b":
            pass
        elif inp == "c":
            pass

# --------------------------------------------------

main()














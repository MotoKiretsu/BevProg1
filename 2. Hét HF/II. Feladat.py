import math


def main():
    print("Pitagorasz-tétel")
    a = int(input("Adja meg a derékszögű háromszög 'a' oldalát: "))
    b = int(input("Adja meg a derékszögű háromszög 'b' oldalát: "))
    c = math.sqrt(a**2+b**2)
    
    print("A derékszögű háromszög 3. oldala, azaz a 'c' oldala: {0}.\n".format(c))

    #Ez nem igazán jött össze a képlet használatával
    #print("Másodfukú egyenlet megoldóképlet")
    #a2 = int(input("Adja meg a másodfukú egyenlet a elemét [(a)x²+(b)x+(c)]: "))
    #b2 = int(input("Adja meg a másodfukú egyenlet b elemét [(a)x²+(b)x+(c)]: "))
    #c2 = int(input("Adja meg a másodfukú egyenlet c elemét [(a)x²+(b)x+(c)]: "))

    #x1 = (-b2+math.sqrt(b2**2-4*a2*c2))/2*a2
    #x2 = (-b2-math.sqrt(b2**2-4*a2*c2))/2*a2
    #print("A megadot másodifokú egyenletnek az x₁={0} és az x₂={1} az eredménye.".format(x1,x2))

    print("Sinus háromszögben")
    szog = int(input("Adja meg a szöget: "))
    atfogo =int(input("Adja meg az atfogot: "))
    SzoggelSzemkoztiBefogo=math.sin(szog)*atfogo
    print("A háromszög szöggel szemközti befogója {0}".format(SzoggelSzemkoztiBefogo))

if __name__ == "__main__":
    main()
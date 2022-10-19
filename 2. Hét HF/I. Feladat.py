def main():
    EletKor = int(input('Adja meg az életkorát: '))

    
    if EletKor >= 21:
        print("Fogyaszthat legálisan alkoholt Amerikában.");
    else:
        print("Ahhoz hogy fogyaszton legálisan alkoholt Amerikában még várnod a kell {0} évet.".format(21-EletKor));
    
    if EletKor >= 18:
        print("Vásárolhat dohányterméket Magyarországon.");
    else:
        print("Ahhoz hogy vásárolj dohányterméket Magyarországon még várnod a kell {0} évet.".format(18-EletKor));

    if EletKor >= 16:
        print("Szerezhet jogosítványt.");
    else:
        print("Ahhoz hogy szerezhetsz jogosítványt még várnod a kell {0} évet.".format(16-EletKor));
    
    if EletKor >= 12:
         print("Megnézheti egyedül a Shrek 2-t.")
    else:
        print("Ahhoz hogy megnézhese a Shrek 2-t egyedül még várnod a kell {0} évet.".format(12-EletKor))


if __name__ == "__main__":
    main()
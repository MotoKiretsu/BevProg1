class Verem:
    def __init__(self) -> None:
        
        

def main():
    v = Verem()     
    print(v)         
    print(v.ures())  
    v.betesz(1)
    v.betesz(4)
    v.betesz(5)
    print(v)         
    print(v.meret()) 
    print(v.ures())  
    x = v.kivesz()
    print(x)         
    print(v)         
    v.kivesz()
    v.kivesz()       
    x = v.kivesz()
    print(x) 
    
if __name__ == "__main__":
    main()
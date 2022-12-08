def main():
    f = open("9. Hét HF\string1.py",'r')
    f2 = open("9. Hét HF\string1_clean.py",'w')
    li = f.readlines()
    for x in li:
        if x[0] != "#" and x != "\n" and x[4] != "#" :
                print(x,file=f2)
    f.close()
    f2.close()

if __name__ == "__main__":
    main()
def main():
    FkM=[2, 4, 8, 3, 9, 7, 1]
    i=0
    H=0

    while len(FkM)-2 <= i:
        if FkM[i] < FkM[i+1]:
            H+=FkM[i+1]-FkM[i]
        else:
            H+=FkM[i]-FkM[i+1]
    i+=1

    print(H)

if __name__ == "__main__":
    main()
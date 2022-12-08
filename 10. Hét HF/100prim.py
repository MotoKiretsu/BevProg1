import PrimModul as m

def main():
    for x in range(100):
        if m.is_prime(x)==True:
            print(x)

if __name__ == '__main__':
    main()
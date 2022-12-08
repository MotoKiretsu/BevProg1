import random

def main():
    RandomSzam=random.randint(0,100)
    tipp= int(input("Milyen számra gondoltam: "))
    while RandomSzam != tipp:
        if tipp> RandomSzam:
            tipp= int(input("Kisebb számra gondoltam\n"))
        elif tipp< RandomSzam:
            tipp= int(input("Nagyobb számra gondoltam\n"))

    print(f"Kitaláltad a számot {RandomSzam}")

if __name__ == "__main__":
    main()
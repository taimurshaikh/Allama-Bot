''' Main Program '''

def main():
    options = ["english", "1", "urdu", "2"]
    languageChoice = input("1. English or 2. Urdu? ").lower()
    while languageChoice not in options:
        languageChoice = input("Invalid.\n 1. English or 2. Urdu? ").lower()


if __name__ == "__main__":
    main()

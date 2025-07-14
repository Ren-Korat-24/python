name=input("Enter the name:")

match name:
        case 'a'|'i'|'o'|'e'|'u'|'A'|'E'|'I'|'O'|'U':
            print("Vowels")
        case _:
            print("Constants")
        
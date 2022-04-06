def is_int():
    try: 
        x = int(input("Enter something: "))
    except ValueError:
        return False
    return True
print(is_int())

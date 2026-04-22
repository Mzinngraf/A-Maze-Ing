from parser import parser
if __name__ == "__main__":
    try:
        a = parser()
        print(a)
    except (TypeError, ValueError) as error:
        print(error)

from parser import parser
if __name__ == "__main__":
    try:
        parser()
    except (TypeError, ValueError) as error:
        print(error)

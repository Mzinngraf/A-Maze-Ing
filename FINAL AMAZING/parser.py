import sys
from typing import Dict, Any, List


def parser() -> Dict[str, Any]:
    """
    Docstring for parser

    Parses and validates  the config file.

    :return: Dict with keys: width, height, entry, exit,
            perfect, output, seed (optional).
    :rtype: Dict[str, Any]
    """
    if len(sys.argv) != 2:
        print("usage: python3 a_maze_ing.py config.txt")
        sys.exit(1)
    filename: str = sys.argv[1]
    data: Dict[str, Any] = {}
    mandatory_keys: List[str] = ["WIDTH", "ENTRY", "HEIGHT",
                                 "OUTPUT_FILE", "PERFECT", "EXIT"]
    found_keys: List[str] = []
    try:
        with open(filename, "r") as config:
            for x in config:
                x = x.split('#')[0].strip()
                if not x:
                    continue
                if "=" not in x:
                    print(f"Error: invalid line format {x}")
                    sys.exit(1)
                y: List[str] = x.split("=")
                key: str = y[0].strip().upper()
                value: str = y[1].strip()
                found_keys.append(key)
                if key == "SEED":
                    val: int = int(value)
                    data["seed"] = val
                elif key == "WIDTH":
                    val = int(value)
                    if val < 3 or val > 50:
                        print("Width error")
                        sys.exit(1)
                    data["width"] = val
                elif key == "HEIGHT":
                    val = int(value)
                    if val < 3 or val > 50:
                        print("Height error")
                        sys.exit(1)
                    data["height"] = val
                elif key == "ENTRY":
                    cordinate: List[str] = value.split(",")
                    if len(cordinate) != 2:
                        print("Error : Entry must be a tuple (x,y)")
                        sys.exit(1)
                    cordx = int(cordinate[0])
                    cordy = int(cordinate[1])
                    data["entry"] = (cordy, cordx)
                elif key == "EXIT":
                    cordinate = value.split(",")
                    if len(cordinate) != 2:
                        print("Error : Exit must be a tuple (x,y)")
                        sys.exit(1)
                    cordx = int(cordinate[0])
                    cordy = int(cordinate[1])
                    data["exit"] = (cordy, cordx)
                elif key == "OUTPUT_FILE":
                    if not value.lower().endswith(".txt"):
                        print("Error OUTPUT_FILE must be a .txt file")
                        sys.exit(1)
                    data["output"] = value
                elif key == "PERFECT":
                    if y[1] != "False" and y[1] != "True":
                        print(y[1])
                        print("Format error")
                        sys.exit(1)
                    data["perfect"] = (value == "True")
        missing_errors: List[str] = []
        for k in mandatory_keys:
            if k not in found_keys:
                missing_errors.append(k)
        if missing_errors:
            print(f"ERROR: missing keys {', '.join(missing_errors)}")
            sys.exit(1)
        w: int = data["width"]
        h: int = data["height"]
        entry_y: int
        entry_x: int
        entry_y, entry_x = data["entry"]
        exit_y: int
        exit_x: int
        exit_y, exit_x = data["exit"]

        if not (0 <= entry_x < w and 0 <= entry_y < h):
            print("Entry point is out of bounds")
            sys.exit(1)
        if not (0 <= exit_x < w and 0 <= exit_y < h):
            print("Exit point is out of bounds")
            sys.exit(1)
        if data["entry"] == data["exit"]:
            print("Error : ENTRY and EXIT cannot be the same")
            sys.exit()
        return data
    except FileNotFoundError:
        print("File not found")
        sys.exit(1)
    except Exception as e:
        print(f"error : {e}")
        sys.exit(1)

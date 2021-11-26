#!/usr/bin/python3
if __name__ == "__main__":
    """print all the names defined in modeule hidden_4"""
    import hidden_4
    for name in dir(hidden_4):
        if "__" not in name:
            print(name)

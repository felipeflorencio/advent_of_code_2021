
def loadInput(name: str):
    
    with open(f"{name}.txt", "r") as input:
        return list(map(str, input.readlines()))
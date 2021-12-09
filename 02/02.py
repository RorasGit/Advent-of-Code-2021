with open("input.txt" , 'r') as input :
    values = input.read().splitlines()
    pos = 0
    depth = 0
    for value in values:
        op, size = value.split(" ")
        size = int(size)
        if op == "forward":
            pos+=size
        elif op == "down":
            depth+=size
        else:
            if size > depth:
                depth = 0
            else:
                depth -= size
    
    print(f"pos: {pos}, depth: {depth}, total: {pos*depth}")

    aim = 0
    pos = 0
    depth = 0
    for value in values:
        op, size = value.split(" ")
        size = int(size)
        if op == "up":
            aim-=size
        elif op == "down":
            aim+=size
        else:
            pos+=size
            depth+=aim*size
            if(depth < 0):
                depth = 0
            
    
    print(f"pos: {pos}, depth: {depth}, aim: {aim} total: {pos*depth}")

import argparse
import pathlib

parser = argparse.ArgumentParser(description="AoC 2021\nDay 2, Problem 1")
parser.add_argument('path', metavar='path', type=pathlib.Path, nargs=1, help='Input file')
args = parser.parse_args()

pos = 0
depth = 0
print(args.path)
with open(args.path[0], mode='r') as file:
    for line in file:
        keys = line.split(" ")
        cmd = keys[0]
        value = int(keys[1])

        if cmd == "forward":
            pos = pos + value
        elif cmd == "down":
            depth = depth + value
        elif cmd == "up":
            depth = depth - value
        else:
            print("Unknown command {cmd}\n".format(cmd=cmd))

    #print(f"pos = {pos}, depth = {depth}")
print("Horizontal position is {pos}\nDepth is {depth}\nProduct is {prod}".format(pos=pos,depth=depth,prod=pos*depth))

            
    
    
    

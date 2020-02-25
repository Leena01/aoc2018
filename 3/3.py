import numpy as np

f  = open("input.txt", "r")
B = np.zeros((1000, 1000), dtype = int)
for line in f:
    line = line.split(' @ ')
    idrow = int(line[0][1:])
    parts = line[1].split(': ')
    pos = parts[0].split(',')
    size = parts[1].split('x')
    for i in range(int(pos[1]), int(pos[1]) + int(size[1])):
        for j in range(int(pos[0]), int(pos[0]) + int(size[0])):
            if B[i][j] == 0:
                B[i][j] = idrow
            else:
                B[i][j] = -1
  
print(len(B[B == -1]))

f  = open("input.txt", "r")
for line in f:
    line = line.split(' @ ')
    idrow = int(line[0][1:])
    parts = line[1].split(': ')
    pos = parts[0].split(',')
    size = parts[1].split('x')
    overlap = False
    for i in range(int(pos[1]), int(pos[1]) + int(size[1])):
        for j in range(int(pos[0]), int(pos[0]) + int(size[0])):
            if not overlap:
                overlap = (B[i][j] == -1)
    if not overlap:
        print(idrow)
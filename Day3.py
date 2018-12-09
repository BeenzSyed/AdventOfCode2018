import numpy as np

def overlap():
    matrix = np.zeros((1100,1100))
    count = 0
    
    with open('InputData/Day3Input.txt', 'r') as f:
        for line in f:
            edges = line.split(' ')
            left_edge = int(edges[2].split(',')[0])
            top_edge = int(edges[2].split(',')[1][:-1])
            width = int(edges[3].split('x')[0])
            height = int(edges[3].split('x')[1])
        
            for i in range(top_edge+1, top_edge+1+height):
                for j in range(left_edge+1, left_edge+1+width):
                    num = matrix[i, j]
                    matrix[i, j] = num+1

        for m in range(0, 1100):
            for n in range(0, 1100):
                num = matrix[m, n]
                if num >= 2:
                    count = count + 1
        print "Overlap is:", count
    
    with open('InputData/Day3Input.txt', 'r') as f:
        for line in f:
            intact_claim = 0
            edges = line.split(' ')
            left_edge = int(edges[2].split(',')[0])
            top_edge = int(edges[2].split(',')[1][:-1])
            width = int(edges[3].split('x')[0])
            height = int(edges[3].split('x')[1])
        
            for i in range(top_edge+1, top_edge+1+height):
                for j in range(left_edge+1, left_edge+1+width):
                    num = matrix[i, j]
                    if (num != 1):
                        intact_claim = 1
                        break
        
            if intact_claim == 0:
                print line

if __name__ == '__main__':
    import sys
    overlap()
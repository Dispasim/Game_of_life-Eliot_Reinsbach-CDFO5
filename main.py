import numpy as np
import time



grille = np.zeros((20,20))
grille[5][5] = 1
grille[4][5] = 1
grille[6][5] = 1




def sum_neighbour(ligne,col,grille):
    sum = 0
    for i in range(-1,2):
        if ligne + i > 0 and ligne + i < len(grille[0]):
            for j in range(-1,2):
                if col + j > 0 and col + j < len(grille[:,0]):
                    sum += grille[ligne + i][col + j]
    sum -= grille[ligne][col]
    return(sum)                
            
def afficher_grille(grille):
    aff = [["." for _ in range(len(grille[0]))] for _ in range(len(grille[:,0]))]
    #aff = [["." for _ in range(cols)] for _ in range(grille[:,0]))]
    
    for i in range(len(grille[0])):
        for j in range(len(grille[:,0])):
            if grille[i][j] == 0:
                aff[i][j] = "."
                
                
        else:
            aff[i][j] = "0"
        print(aff)    
            
                
print(grille)            
time.sleep(5)
def start(grille):
    while(True):
        transform_to_one  = []
        transform_to_zero = []
        
        for ligne in range(len(grille[0])):   
            for col in range(len(grille[:,0])):
                neighbours = sum_neighbour(ligne,col,grille)
                if neighbours != 0:
                    print(ligne,col,neighbours)
                if grille[ligne][col] == 0 and neighbours == 3:
                    transform_to_one.append([ligne,col])
                    #grille[ligne][col] = 1
                elif grille[ligne][col] == 1 and (neighbours <2 or neighbours >3):
                    transform_to_zero.append([ligne,col])
                    #grille[ligne][col] = 0
        for i in transform_to_one:
            grille[i[0]][i[1]] = 1
        for i in transform_to_zero:
            grille[i[0]][i[1]] = 0
            
                    
        print(grille)
        time.sleep(1)
            
        
        
start(grille)        
                    
                    
                    
                    
            
            
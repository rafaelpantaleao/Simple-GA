# -*- coding: utf-8 -*-
"""
A simple GA, for beginners
"""

##ideia do programa é criar um target aleatorio e usar o GA para encontrar individuos próximos dele

import random

pop = 50
gen = 1000
target = [random.uniform(-100,100),random.uniform(-100,100)]

##inviduos tem coordenadas iniciais pseudoaleatorias entre -15 e 15 vezes a posição do target
class individual(object):
    
    def __init__ (self):
        
        self.x = random.uniform(-target[0]*15,target[0]*15)
        self.y = random.uniform(-target[0]*15,target[0]*15)
        self.score = -1
    
    def __str__(self):
        
        return 'x = ' + str(self.x) + ' y = ' + str(self.y) + ' score = ' + str(self.score)
     

def firstpopulation(pop):
    
    return [individual() for _ in range(pop)]


##avalição é a distancia da coordenada ao target
def score(generation,target):
    
  for individual in generation:
      
      individual.score = ((individual.x - target[0])**2 + (individual.y - target[1])**2)**(1/2)
      
  return generation
##vetor da população é organizado em ordem decrescente de distancias (menores distancias em cima)
def sort(generation):
    
    generation = sorted(generation , key=lambda individual:individual.score)
    
    return generation

#normalização linear, taxa 10
def normal(generation):
    
    i = 0;
    for i in range(len(generation)):
        generation[len(generation)-i-1].score = 10*(i+1) 
    
    return generation
##Crossover e mutação, facilitou ser implementado em só uma função.

def crossovermutation(generation):
    
    next_gen = []
    
    ## Steady State (gap = 20%) primeiros 20% de next_gen são iguais do de generation
    gap = 0.2
    next_gen= generation[:int(gap*len(generation))] 
    
    ##crossover & mutation
    
    for _ in range(int((1-gap)*len(generation)/2)):
        
        #torneio
       
        parent1 = random.choice(generation)
        j = random.choice(generation)
        if parent1.score < j.score:
            parent1 = j
        generation.remove(parent1)
        
        parent2 = random.choice(generation)
        k = random.choice(generation)
        if parent2.score < k.score:
            parent2 = k
        generation.remove(parent2)
        
        
        #crossover aritmético
        n1 = random.random()
        n2 = 1- n1
        n3 = random.random()
        n4 = 1- n3
        child1 = individual()
        child2 = individual()
        
        child1.x = n1 * parent1.x + n2 * parent2.x
        child1.y = n1 * parent1.y + n2 * parent2.y
        
        child2.x = n3 * parent1.x + n4 * parent2.x
        child2.y = n3 * parent1.y + n4 * parent2.y  
        
        ##mutation
        m1=random.random()
        m2=random.random()
        
        ##taxa de mutação de 8% -> m1 e m2 são numeros aleatórios entre 0 e 1, só ocorre mutação se o m1 ou m2 forem maiores que 0.92
        ##a mutação em si é bem localizada, variando um numero aleatório até 20% (+ ou -) do inicial
        if m1 >=0.92:
            child1.x = child1.x*random.uniform(0.8,1.2)
            child2.x = child2.x*random.uniform(0.8,1.2)
        if m2 >=0.92:
            child1.y = child1.y*random.uniform(0.8,1.2)
            child2.y = child2.y*random.uniform(0.8,1.2)
            
        next_gen.append(child1)
        next_gen.append(child2)
        del child1
        del child2
    
    return next_gen
 
    ##  GA função final, imprime as distâncias do mais apto a kd geração (objetivo é que sempre diminua) 
    ## também imprime o resultado optimo encontrado no final do GA
def GA():
    
    generation = firstpopulation(pop)
    generation = score(generation,target)
    generation = sort(generation)
    generation = normal(generation)
    
    for _ in range(0,gen):
        
       print('Dist = ' + str(((generation[0].x - target[0])**2 + (generation[0].y - target[1])**2)**(1/2)))
       
       generation = crossovermutation(generation)
       generation = score(generation,target)
       generation = sort(generation)
       generation = normal(generation)
    
    print(' target = ' + str(target[0]) + ',' + str(target[1]) )
    print(' x,y =' + str(generation[0].x) + ' , ' + str(generation[0].y))              
          
 
if __name__ =='__main__':
    GA()       
    
    




    


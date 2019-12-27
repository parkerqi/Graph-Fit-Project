import GeneticAlgorithm as GA
import matplotlib.pyplot as plt
import numpy as np
import random

class Environment:

    #points to be fitted 
    def __init__(self, x, y, totalPopulation, mutationRate): 
        self.x = x
        self.y = y
        self.totalPopulation = totalPopulation
        self.mutationRate = mutationRate
        #list of DNA
        self.population = []
        self.matingPool = []
        self.totalFitness = 0
        for i in range(0, self.totalPopulation):
            newDNA = GA.DNA(self.x, self.y)
            self.population.append(newDNA)

    def selection(self):
        self.matingPool[:] = []
        #calculate fitness for all DNA
        for i in range(0, self.totalPopulation):
            self.population[i].findFitness()
        #calculate total fitness
        self.totalFitness = 0
        for i in range(0, self.totalPopulation):
            self.totalFitness += self.population[i].fitness
        #build mating pool according to its fitness
        rank = sorted(self.population, key=lambda x: x.fitness)
        num = []
        has = 0
        for i in range(0, self.totalPopulation):
            a = int(self.population[i].fitness/self.totalFitness*self.totalPopulation)
            num.append(a)
            has += a
            print(self.population[i].genes)
        num.sort(reverse=True)
        num[0] += self.totalPopulation - has
        print(num)
        for i in range(0, self.totalPopulation):
            for k in range(0, num[i]):
                self.matingPool.append(rank[i])
        print('mating pool')
        for i in range(0, self.totalPopulation):
            print(self.matingPool[i].genes)
        print('______________')

    def reproduction(self):
        self.population[:] = []
        for i in range(0, len(self.matingPool)):
            parentA = random.choice(self.matingPool)
            parentB = random.choice(self.matingPool)
            child = parentA.crossover(parentB)
            self.population.append(child.mutation(self.mutationRate))

    def drawPopulation(self):
        #get linespace
        x1 = np.linspace(0, np.amax(self.x)*1.2, 1000)
        for i in range(0, self.totalPopulation):
            self.population[i].drawLine(x1)
        plt.show()

    def graphDots(self):
        #setting plot style 
        plt.style.use('fivethirtyeight') 
        #plotting points 
        plt.scatter(self.x, self.y) 
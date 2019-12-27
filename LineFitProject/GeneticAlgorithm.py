import random
import math
import matplotlib.pyplot as plt

class DNA:

    #create DNA randomlly 
    def __init__(self, x, y): 
        self.x = x
        self.y = y
        #[y intersect from -10^4 to 10^4, angle of line respect to x from -90 to 90]
        self.genes = [random.randrange(-10**3, 10**3), random.randrange(-90, 90)] 
        #from 0 to 1
        self.fitness = 0

    def findFitness(self):
        #convert from degress to slope
        gene1 = [self.genes[0], math.atan(self.genes[1]*math.pi/180)]
        for i in range(0, len(self.x)):
            dy = abs(gene1[1]*self.x[i]+gene1[0]-self.y[i])
            self.fitness += dy
        # the lower the fitness the better
        return self.fitness

    def crossover(self, partner):
        child = DNA(self.x, self.y)
        if random.random() > 0.5:
            child.genes[1]=self.genes[1]
        else: 
            child.genes[0]=self.genes[0]
        return child

    def mutation(self, mutRate):
        if random.random() < mutRate:
            self.genes[0] = random.randrange(-10**4, 10**4)
            print('mutation')
        if random.random() < mutRate:
            self.genes[1] = random.randrange(-90, 90)
            print('mutation')
        return self

    # x1 is linespace
    def drawLine(self, x1):
        line = [self.genes[0], math.atan(self.genes[1]*math.pi/180)]
        plt.plot(x1, line[0] + line[1]*x1)
        #plt.title('y = ' + np.format_float_positional(a[1], precision=3) + 'x + ' + np.format_float_positional(a[0], precision=3))
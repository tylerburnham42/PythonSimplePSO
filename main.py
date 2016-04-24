from Particle import Particle
import matplotlib.pyplot as plt


class ParticleSwarm(object):
   
    def __init__(self, swarmSize, dimensions, minVal, maxVal):
        self.maxVal = maxVal
        self.minVal = minVal
        self.dimensions = dimensions
        self.swarmSize = swarmSize
        self.swarm = []
        self.solution = []
        for i in range(swarmSize):
            particle = Particle(dimensions, minVal, maxVal)
            self.swarm.append(particle)
            
        return


    def run(self, steps):
        
        self.swarm = sorted(self.swarm)
        
        for step in range(steps):
            print("---Itteration " + str(step) + "---")
            
              
            globalBest = self.swarm[0]
            self.solution = globalBest
            
            
            for particle in self.swarm:
                particle.updateParticle(globalBest.getPositionList())
                
            self.swarm = sorted(self.swarm)
            
            #Print swarm
            for particle in self.swarm:     
                print(particle)
                
            self.plotParticles(step)
                
         
    def plotParticles(self, step):     
        xlist = []
        ylist = []
        for particle in self.swarm:
            posList = particle.getPositionList()
            xlist.append(posList[0])
            ylist.append(posList[1])
            
        plt.scatter(x=xlist, y=ylist, label='Particles', color = 'blue', )
                
        plt.title("Swarm at Iteration " + str(step))
        plt.xlabel('X Val')
        plt.ylabel('Y Val')
        plt.axis((0,20,0,20))
        plt.legend(loc='upper right')
        plt.savefig('image/'+str(step)+'.png') 
        plt.close()  
            
            
            
            #for particle in self.swarm:
            #    if(particle)
                


def main():
    swarmSize = 50
    dimensions = 2
    minVal = 0
    maxVal = 20
    swarm = ParticleSwarm(swarmSize, dimensions, minVal, maxVal)
    print(swarm.run(50))








if __name__ == '__main__':
    main() 
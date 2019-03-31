import random

class Neuron:
    def __init__(self, potential,neuron_id, synaptic_strength):
        self.potential = potential
        self.neuron_id = neuron_id
        self.synaptic_strength = synaptic_strength
    
    def __str__(self):
        str_to_print = f"""
            Neuron id: {self.neuron_id}
            Potential: {self.potential}
            Synaptic_strength: {self.synaptic_strength}
            """
        return str_to_print

    def fire (self):
        shooting_strength = random.randint(1,100)
        print(shooting_strength)
        if shooting_strength > self.synaptic_strength:
            self.potential = self.potential + shooting_strength
            return True

class PyramidalNeuron(Neuron):
    def __init__(self,potential,neuron_id,synaptic_strength):
        super().__init__(potential,neuron_id,synaptic_strength)

class NeuralNetwork(Neuron):
    def __init__(self, neurons):
        self.neurons = []

    def show_neural_network(self):
        print('The neural network described is a column:')
        for i in range(0,len(neurons)):
            print(neurons[i])
            if(i!=len(neurons)-1):
                print('             |')             
                print('             V')

    def start_firing(self):
        shoot=random.randint(1,100)
        neurons[0].potential = neurons[0].potential + shoot
        
        for i in range(1,len(neurons)):
            if neurons[i].fire() == True:
                i+=1
                print("shooting successfull")
            
class InhibitoryNeuron(Neuron):
    def __init__(self,potential,neuron_id,synaptic_strength):
        super().__init__(potential,neuron_id,synaptic_strength)

    def fire(self):
        #when it does fire, it has an increased chance to fire a second spike
        shooting_strength = random.randint(1,100)
        print(shooting_strength)
        if shooting_strength > self.synaptic_strength:
            self.potential = self.potential + shooting_strength
            self.synaptic_strength= self.synaptic_strength/2
            return True

if __name__ == '__main__':
    p1 = Neuron(60,60,40)
    p2 = Neuron(6,10,32)
    p3 = Neuron(42,45,100)
    p4 = Neuron(73,21,100)
    neurons=[p1,p2,p3,p4]
    nn=NeuralNetwork(neurons)
    nn.start_firing()




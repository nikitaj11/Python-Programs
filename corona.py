import random

class Corona:
    def _init_(self):
        self.population = 1000000
        self.killed = 0
        self.infected = 0

    def infected(self, species, age):
        if species == 'human':
            self.infected = self.infected + 1
            self.population = self.population - 1
            if age < 55:
                self.infected = self.infected - 1
                self.population = self.population + 1

    def stats(self):
        print(self.population)
        print(self.killed)
        print(self.infected)
    

def main():
    virus = Corona()
    for i in range(1000):
        age = random.randint(1,80)
        virus.infect('human',age)
        virus.stats()

main()

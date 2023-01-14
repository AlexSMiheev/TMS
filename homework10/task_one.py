class Country:
    pass


class Russia(Country):
    def __init__(self, population):
        self.population = population

    @property
    def population(self):
        return self.population

    @population.setter
    def population(self, value):
        self.population = value

    @population.deleter
    def population(self):
        self.population = None


class Canada(Country):
    def __init__(self, population):
        self.population = population

    @property
    def population(self):
        return self.population

    @population.setter
    def population(self, value):
        self.population = value

    @population.deleter
    def population(self):
        self.population = None


class Germany(Country):
    def __init__(self, population):
        self.population = population

    @property
    def population(self):
        return self.population

    @population.setter
    def population(self, value):
        self.population = value

    @population.deleter
    def population(self):
        self.population = None

#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Author: Douglas Sales A. Amante
#University of Beira Interior - Portugal
#Date: 05/01/21

from random import randint
from string import maketrans

class GeneticAlgorithm():
    """
       Usinng Genetic Algorithm to find the x value in which the function x² +7x -3 assume the maximum value
    """
    def __init__(self, x_min, x_max, population_size, mutation_rate, crossover_rate, generation_numb):

        """
            Initialize all the instances' atributes
        """

        self.x_min = x_min
        self.x_max = x_max
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.generation_numb = generation_numb

        # Calculate the number of bits of the "x_min" and "x_max" for binary format with signal(positive or negative)
        qtd_bits_x_min = len(bin(x_min).replace('0b', '' if x_min < 0 else '+'))
        qtd_bits_x_max = len(bin(x_max).replace('0b', '' if x_max < 0 else '+'))

        # The number of bits represents the number of bits to be used to create the individual
        self.num_bits = qtd_bits_x_max if qtd_bits_x_max >= qtd_bits_x_min else qtd_bits_x_min

        # Create the population's individual
        self.create_population()

    def create_population(self):

        """
            Create a population of a determine size with individual that have a specific number of bits
        """

        # Initialize a population about "population_size" variable with non values individues, that is, void values.
        self.population = [[] for i in range(self.population_size)]

        # Fill the population
        for individual in self.population:

            # To each population individual choose random number between "x_min" and "x_max"
            num = randint(self.x_min, self.x_max)

            # Convert the chose number to binary format with signal
            num_bin = bin(num).replace('0b', '' if num < 0 else '+').zfill(self.num_bits)

            # Transform the binary number resultant in an array
            for bit in num_bin:
                individual.append(bit)

    def goal_function(self, num_bin):

        """
            Calculate a goal function used to evaluate the produced soluctions
        """

        # Convert the from binary format to integer format
        num = int(''.join(num_bin), 2)

        # Calculate and return the goal function result
        return num**2 +7*num - 3

    def evaluate(self):

        """
            Evaluate the produced soluction associating an evaluation to every population element
        """

        self.evaluation = []

        for individual in self.population:
            self.evaluation.append(self.goal_function(individual))

    def select(self):

        """
            Do a individual's selection more fit to tornament, consider N =2
        """

        # Cluster the individuaos with him avalations and create the tornament participants
        participantes_torneio = zip(self.population, self.evaluation)

        # Choose two random individuals
        individual_1 = participantes_torneio[randint(0, self.population_size - 1)]
        individual_2 = participantes_torneio[randint(0, self.population_size - 1)]

        # Return the individual with biggest avalation, that is, the tornament's winner
        return individual_1[0] if individual_1[1] >= individual_2[1] else individual_2[0]

    def fit(self, individual):

        """
            Case the individual have been out of the x limits, it is adjusted accordingly with the limit nearest
        """

        if int(''.join(individual), 2) < self.x_min:

            # If the individual is smallest that the minimium limit, it is changed to itself minimium limit
            fit = bin(self.x_min).replace('0b', '' if self.x_min < 0 else '+').zfill(self.num_bits)

            for indice, bit in enumerate(fit):
                individual[indice] = bit

        elif int(''.join(individual), 2) > self.x_max:

            #  If the individual is big than maximium limit, it is changed itself maximium limit
            fit = bin(self.x_max).replace('0b', '' if self.x_max < 0 else '+').zfill(self.num_bits)

            for indice, bit in enumerate(fit):
                individual[indice] = bit

    def crossover(self, dad, mom):

        """
            Apply the crossover accordingly with a probability provided(crossover rate)
        """

        if randint(1,100) <= self.crossover_rate:

            # Case the crossover to be applied, the parents changed their cut and with this create two children
            cut_point = randint(1, self.num_bits - 1)
            chill_1 = dad[:cut_point] + mom[cut_point:]
            chill_2 = mom[:cut_point] + dad[cut_point:]

            # If anyone of the children had been x out of limits, it is fit accordingly with limit nearest
            self.fit(chill_1)
            self.fit(chill_2)    
        else:
            # Otherwise, the children are exactly copies identics about the parents
            chill_1 = dad[:]
            chill_2 = mom[:]

        # return the children obtained by crossover
        return (chill_1, chill_2)

    def mutation(self, individual):

        """
            Do a bits' mutation of each individual about a probability provided, that is, mutation_rate
        """

        # Create a table with mutation rules, with maketrans library
        mutation_table = maketrans('+-01', '-+10')

        # Case the mutation rate would be achived, it is realized in a random bit
        if randint(1,100) <= self.mutation_rate:
            bit = randint(0, self.num_bits - 1)
            individual[bit] = individual[bit].translate(mutation_table)

        # If the individual had been x out of limits, it is fit accordlyng with limit nearest
        self.fit(individual)

    def find_chill_more_apt(self):

        """
            Search the individual with the better evaluation get in of population
        """

        # Cluester the individuals with their evaluation to create the candidates
        candidates = zip(self.population, self.evaluation)

        # Return the candidate with better evaluation, that is, the more apt to population
        return max(candidates, key=lambda elemento: elemento[1])


def main():

    # Create a genetic algorithm's instance with the enunciated configuration
    genetic_a = GeneticAlgorithm(-20, 20, 60, 2, 75, 50)

    # Do the initial population evaluation  
    genetic_a.evaluate()

    # Runing the algorithm by "generation_numb"
    for i in range(genetic_a.generation_numb):

        # Print the result of each generation, starting the original population
        print( 'Result of Generation {}: {}'.format(i, genetic_a.find_chill_more_apt()) )

        # Create  new population and write it while do not had been complete
        new_population = []

        while len(new_population) < genetic_a.population_size:

            # Select the parents
            dad = genetic_a.select()
            mom = genetic_a.select()

            # Do the crossover about the parents to create the children
            chill_1, chill_2 = genetic_a.crossover(dad, mom)

            # Do the mutation for children and add their to new population
            genetic_a.mutation(chill_1)
            genetic_a.mutation(chill_2)
            new_population.append(chill_1)
            new_population.append(chill_2)

        # Change the old population for new pulation and do the evaluation 
        genetic_a.population = new_population
        genetic_a.evaluate()

    # Research the chill more apt get in of population and show the genetic algorithm result
    print( 'Result {}: {}'.format(i+1, genetic_a.find_chill_more_apt()) )

    # Finish the main file execution
    return 0

if __name__ == '__main__':
    main()


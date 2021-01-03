# GENETIC ALGORITHM TO MAXIMIZE A FUNCTION 

Author: Douglas Sales A. Amante 

[![Genetic Algorithm Overview](https://www.sciencedirect.com/topics/engineering/genetic-algorithm-method)]

This implementation is based on the use of the Algorithms Genetics approaches to find a better value of x using two limits(maximum and minimum). A functions that we are use is *f(x) = x² +7x -3*. In which, we must stay careful about the following parameters to algorithms: 

- Limits to x values [-20, 20];

- Population equal the 60 individuals;

- Mutation Rate = 2%;

- Crossover Rate = 75%; 

- Quantity of generation used with 50 generation.

It is necesseray to be that it was used some concepts as: 

- The selection was done by the tournament.   [![Tournament Selection GA](https://www.geeksforgeeks.org/tournament-selection-ga/)]

- The value of x was used in binary format with the signal.  [![Introduction to GA](https://www.whitman.edu/Documents/Academics/Mathematics/2014/carrjk.pdf)]


# Running

To run this implementation is very simple, it is created in docker-compose. However, to run this file you do not need the docker-compose installation. Only, do the following commands in the command line: 

First Command: 
```sh
$ cd && mkdir build && cd build
```

Next Command (1):
```sh
$ git clone https://github.com/douglasamante/genetic_algorithm
```
If you not have been git command, you must do the installation.   [![Instalation Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)]

Next Command (2): 
```sh
$ py genetic_algorithm.py
```

Maybe, the use of this file in an API could do not works.

You will see the results after the generation quantity that is equal to 50, in this case. Remember this case, the out would be in binary format: 

> Decimal Value to out = + 537

> Binary Value to out =  + 10100

You can do new changes to understood what is happiness and, good luck!


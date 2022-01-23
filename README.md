# Project Euler :atom:
![Image of Euler](https://vedicmathschool.org/wp-content/uploads/2020/06/leonhard_1-1024x538.jpg)

A collection of my program code solutions for Project Euler. Project Euler is described as "A series of challenging mathematical/computer programming problems that will require more than just mathematical insights to solve". The original problems can be found at [Project Euler](https://projecteuler.net/archives).

## Contents
- [Problems](https://github.com/torjusn/project_euler#problems)
- [Assorted solutions](https://github.com/snoofalus/glitre#datasett)

## Problems
- [x] 1
- [x] 2
- [x] 3
- [x] 4
- [x] 5
- [x] 6
- [x] 7
- [x] 8
- [x] 9
- [x] 10  

I will from now on only be updating the list for some of the thougher problems.

## Assorted solutions 
Below are some solutions to problems I found particularly interesting.

### 5 Smallest multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.  
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?  

Primes are only divisible by themselves and 1. We can start with factoring out a prime base for the example by multiplying all primes from 1 to 10 together, i.e. 
```
2*3*5*7 = 210
```
and we see that the factor left out to make 2520 is 12. An explanation is found by checking which of the missing non-prime factors are included in our prime base:
```
210 / 2 = 105
210 / 3 = 70 
210 / 6 = 35
```  
The non-primes from 1-10 we need to be concerned about are the ones that cant be factored out of our prime-base, i.e. 4, 8 and 9. We need to add factors that can create 4, 8 and 9 together with our base. Missing factors are therefore 2^2, 3. The example answer is obtained by multiplying the prime-base 210 with missing factors as below:
```
210 * (2*2*3) = 210 * 12 = 2520
``` 
Repeating the same process for numbers 1 to 20 results in 24 times the prime base up to 20.

### 9 Special Pythagorean triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

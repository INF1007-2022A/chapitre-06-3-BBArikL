#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math
import copy
import itertools


def get_maximums(numbers: list[list[int]]):
	return [max(lst_nb) for lst_nb in numbers]


def join_integers(numbers: list[int]):
	return int("".join([str(nb) for nb in numbers]))


def generate_prime_numbers(limit):
	primes = [2]

	for i in range(3, limit+1, 2):
		is_prime = True
		j = 0
		while is_prime and j < len(primes):
			if i % primes[j] == 0:
				is_prime = False
			j += 1

		if is_prime:
			primes.append(i)

	return primes


def combine_strings_and_numbers(strings, num_combinations, excluded_multiples):
	res = []

	def exclude_multiple(x: int) -> bool:
		return x % excluded_multiples != 0

	if excluded_multiples is None:
		exclude_multiple = (lambda x: True)

	for i in range(1, num_combinations+1):
		if exclude_multiple(i):
			for s in strings:
				res.append(f"{s}{i}")
	return res

if __name__ == "__main__":
	print(get_maximums([[1, 2, 3], [6, 5, 4], [10, 11, 12], [8, 9, 7]]))
	print("")
	print(join_integers([111, 222, 333]))
	print(join_integers([69, 420]))
	print("")
	print(generate_prime_numbers(17))
	print("")
	print(combine_strings_and_numbers(["A", "B"], 2, None))
	print(combine_strings_and_numbers(["A", "B"], 5, 2))

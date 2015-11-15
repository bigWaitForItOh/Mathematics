#################################################################################################################
#THE PROBABILITY TREE METHOD - A Recursive Solution:
#We have a set of N different objects. We have to pick out K of those N objects, 1-by-1, randomly (with uniform probability distribution) without replacing any object.
#If T objects of type TARGET exist whatis the probability that at least 1 of K picked objects is of type TARGET?
#refer to this question for example: https://www.hackerrank.com/contests/pythonist3/challenges/iterables-and-iterators
#################################################################################################################

def get_p (a_count, size, draws):
	if (draws == 0):
		if (a_count == a_count_original):
			return (0);
		return (1);

	a_found = (a_count / size) * get_p (a_count - 1, size - 1, draws - 1);
	a_nfound = ( (size - a_count) / size) * get_p (a_count, size - 1, draws - 1);

	return (a_found + a_nfound);

#sample input collection and call to function
size, target_count_original, draws = int (input ()), int (input ()), int (input ());
print (get_p (a_count_original, size, draws);

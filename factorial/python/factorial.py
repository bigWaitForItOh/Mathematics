from functools import reduce;
factorial = lambda i : reduce (lambda x, y : x * y, range (2, i + 1));

#Sample call to function factorial ()
print (factorial (int (input ())));

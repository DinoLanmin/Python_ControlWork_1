
#Python Control Work

library_a = ['1', '2', '3', '4', '5']
library_b = ['a', 'b', 'c', 'd', 'e']
library_c = ''

for a, b in zip(library_a, library_b):
    library_c += (a + b + ' ')

print(library_c)
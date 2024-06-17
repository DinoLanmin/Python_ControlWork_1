
#Python Control Work

library_a = ['1', '2', '3', '4', '5']
library_b = ['a', 'b', 'c', 'd', 'e']
library_c = ''

for a, b in zip(library_a, library_b):
    library_c += (a + b + ' ')

print(library_c)

section_a = [2, 0, 509, 23]
section_b = [45, 0, 14, 8, 1]
section_c = []

section_c.append(''.join(map(str, sorted(section_a))))
section_c.append(''.join(map(str, sorted(section_a, reverse=True))))
section_c.append(''.join(map(str, sorted(section_b))))
section_c.append(''.join(map(str, sorted(section_b, reverse=True))))

print(*section_c)
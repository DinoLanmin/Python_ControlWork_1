
#Python Control Work

section_a = [2, 0, 509, 23]
section_b = [45, 0, 14, 8, 1]
section_c = []

section_c.append(''.join(map(str, sorted(section_a))))
section_c.append(''.join(map(str, sorted(section_a, reverse=True))))
section_c.append(''.join(map(str, sorted(section_b))))
section_c.append(''.join(map(str, sorted(section_b, reverse=True))))

print(*section_c)
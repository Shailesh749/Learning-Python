s1 = {1, 2, 4, 0}
s1.add(-1)
print(s1)


# Frozen sets - Immutable sets
fs1 = frozenset({10, 20, 30})
print(fs1, type(fs1))

# fs1.add(40)  cannot work 
print(fs1)

fs2 = ({10, 50, 100, 200})
print(fs1 & fs2)
print(fs1 | fs2)
print(fs2 - fs1)
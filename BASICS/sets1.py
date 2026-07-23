# --- 1. SET CREATION & UNION/UPDATE ---
s1 = {1, 2, 5, 6}
s2 = {3, 6, 7}

# union() returns a new set
s3 = s1.union(s2)
print(f"Union of s1 and s2: {s3}")

# update() modifies the original set
s1.update(s2)
print(f"s1 after update(s2): {s1}")

# --- 2. INTERSECTION & DIFFERENCE ---
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}

# intersection(): Items present in both
intersect = cities.intersection(cities2)
print(f"Intersection: {intersect}")

# symmetric_difference(): Items NOT common to both
sym_diff = cities.symmetric_difference(cities2)
print(f"Symmetric Difference: {sym_diff}")

# difference(): Items in cities but NOT in cities2
diff = cities.difference(cities2)
print(f"Difference (cities - cities2): {diff}")

# --- 3. SET RELATIONSHIPS (BOOLEAN) ---
c1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
c2 = {"Tokyo", "Madrid"}
c3 = {"Seoul", "Kabul"}

print(f"Is c1 a superset of c2?: {c1.issuperset(c2)}")
print(f"Is c2 a subset of c1?: {c2.issubset(c1)}")
print(f"Are c1 and c3 disjoint? (No common items): {c1.isdisjoint(c3)}")

# --- 4. ADDING & REMOVING ITEMS ---
# add(): To add one item
c1.add("Helsinki")

# remove() vs discard()
c1.remove("Berlin")   # Raises KeyError if item is missing
c1.discard("London")  # Does NOT raise error if item is missing

# pop(): Removes and returns a random item
popped_item = c1.pop()
print(f"Popped item: {popped_item}")
print(f"Set after pop: {c1}")

# --- 5. CHECKING & CLEARING ---
info = {"Carla", 19, False, 5.9}

# Check existence
if "Carla" in info:
    print("Carla is present in the set.")

# clear(): Removes all elements but keeps the set object
info.clear()
print(f"Set after clear: {info}")

# del: Deletes the set entirely (printing it after this would cause an error)
del info
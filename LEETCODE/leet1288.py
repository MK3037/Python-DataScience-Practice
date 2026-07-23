intervals = [[1, 4], [3, 6], [2, 8]]

# Iterate backwards from the last index to 0
for i in range(len(intervals) - 1, -1, -1):            #(start, stop, step)
    for j in range(len(intervals)):
        if i == j:
            continue

        if intervals[j][0] <= intervals[i][0] and intervals[j][1] >= intervals[i][1]:
            del intervals[i]
            break 

print(intervals)


# The Problem with Forward Iteration
# When you iterate forward (0, 1, 2, ...), deleting an item causes a "shift" that pulls all subsequent items one spot to the left.

# Imagine intervals = [A, B, C]:

# Loop i=0: You delete A.

# The list shrinks: [B, C].

# Loop i=1: The list now only has index 0 (B) and index 1 (C). The loop logic is looking for index 1, so it skips over the new item at index 0 (B) and goes straight to C. You skipped B entirely.

# Loop i=2: The list is [B, C]. The loop tries to access index 2, but it doesn't exist! IndexError.



# The Solution: Backward Iteration
# When you iterate backward (2, 1, 0), deleting an item only affects the indices to the right of the current one. The indices of the items you have not yet checked remain exactly the same.

# Imagine intervals = [A, B, C] and we want to delete A and B:

# Step 1: i = 2

# You check intervals[2] (which is C). It's fine, keep it.

# List is still [A, B, C].

# Step 2: i = 1

# You check intervals[1] (which is B). Let's say B is covered and needs to be deleted.

# You del intervals[1].

# The list is now [A, C].

# Notice: The index 0 (where A is) was not affected by deleting index 1.

# Step 3: i = 0

# The loop proceeds to i = 0.

# It checks intervals[0] (which is A). Everything is still in its correct place.
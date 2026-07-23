n = int(input("Total versions: "))
bad_version_threshold = int(input("Enter the bad version: "))

def findFirstBadVersion(n, bad):
    low = 1
    high = n
    first_bad = n  

    while low <= high:
        mid = (low + high) // 2

        if bad<=mid: 
            first_bad = mid
            high = mid - 1
        else:
            low = mid + 1
            
    return first_bad

print(f"The first bad version is: {findFirstBadVersion(n, bad_version_threshold)}")
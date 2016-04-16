# binary search
#err: waffling around

def chop(needle, haystack):
    # err: forgot colon
    if len(haystack) == 0:
        return -1
    low = 0
    high = len(haystack) - 1
    # err: referenced high before assignment
    mid = (low + high) / 2
    # proper For Loops nonexistent... I'd have to make an iterable

    while low <= high:
        if haystack[low] == needle:
            return low
        elif haystack[high] == needle:
            return high
        elif haystack[mid] == needle:
            return mid
        elif needle < haystack[mid]:
            low == low + 1
            high == mid - 1
            mid == (low + high) / 2
            # err: tried to double else
            # err: else if syntax error?
        elif needle > haystack[mid]:
                low == mid + 1
                high == high - 1
                mid == (low + high) / 2
        else:
            raise Error("How did you even get to this part?")

    return -1

# err: forget to print
print chop(1, [-1, 0, 1, 3, 5, 10])
    # err: over time, no time to test

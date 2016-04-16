def complement(s):
""" Take a DNA string and return the reverse complement.
    print out any characters that do not print the pattern with an error. """
    string = list(s)
    for i, char in enumerate(string):
        if char == "G":
            string[i] = 'C'
        elif char == "T":
            string[i] = 'A'
        elif char == "C":
            string[i] = 'G'
        elif char == "A":
            string[i] = 'T'
        else:
            print "err: " + str(char)

    return "".join(string[::-1])

if __name__ == "__main__":
    with open("temp.txt", "r") as f:
        s = f.readline()[:-1]
        s_complement = complement(s)
        print s_complement


"""2015-02-15 errors"""
#err: tried to put assignment inside for loop
#err: lah recommends using enumerate
#err: changed one var but used older version as reference for it
#err: erased local assignment, still needed
#err: fixed indentation wrong
#err: don't know much pypy
#err: don't know when to expect function vars change external stuff
#err: apparently strings don't list
#err: forgot to update my remapping when I realized output example is reversed
#err: the real problem is that I never tested with the test case I DO HAVE
#err: lots of print statements. lahwran suggests pdb, I squirm
#err: tried to assign with ==
#err: waffle about whether to str() in return or where fn used
#err: ran out of time after downloading file
#err: tried to str() instead of .join()
#err: messed up join syntax, is an instance method
#err: used reverse(), should have used reverse()
#err: tried to call reversed on list, didn't work?
#err: reversed didn't work on string either.
#err: tried to add too many ')'s
#err: taking much longer than I should for simple problem, start to hate self.
#err: tried again, still wrong don't know why
#err: idk how to make this a library
#err: feel like this too long to set up
#err: idk how to check if python is main script..
#err: wish I could do easy argparse to run particular function
#err: should use argparse to get filename, squirmy feels
#err: tried to run a .txt file as python
#err: tried to use python keyword as varname
#err: idr syntax for reading whole file
#err: tried to .pop() a string
#err: did slices wrong, forgot 2nd is exclusive
#err: forgot to put printing result back after testing tangent
#err: forgot that ipython notebook was *made* for piecemeal editing


def highestGC(dna_dict):
    """ Given a dictionary of IDs to DNA string pairs, return a tuple containing:
         - the ID of the string with the highest percentage of C and G symbols
         - the percentage of C ang G symbols in the string out of 100
    No ordered behavior on exact percentage matches, if strings empty fn will
    return (-1, 0)"""

    top = (-1, 0) #just in case none have GC content

    for key, value in dna_dict.items():
        if len(value) == 0:
            pass
        gc = (value.count('G') + value.count('C')) * 100.0 / len(value)

        if gc >= top[1]:
            top = (key, gc)

    return top



if __name__ == "__main__":
    with open('temp.txt', 'r') as f:
        strings = {}
        while True:
            line = f.readline()[:-1] # chop off newline
            if line == "":
                break
            if line[0] == ">":
                label = line[1:]
                strings[label] = f.readline()[:-1]
            else:
                strings[label] = strings[label] + line
        top = highestGC(strings)
        print top[0]
        print top[1]




"""2015-02-16 errors"""

    #e couldn't remember if .items() for dictionary key AND value list
        #e not sure proper Type Assertion method
        #e guilty about not knowing how to do this low-level way
        #e forgot to actually calculate the gc
        #e got parentheses in (x + y) * w / z wrong
# e had to look up pdb thing
        #e itch, want to make a library that loads stuff.
        #e how do I check for last next() in iterator?
            #e uncertainty what architecture best for solving problem
                #e chopped off end char because forgot slice is noninclusive
                #e apparently readline in assign doesn't call the next()?
        #e left off plural in varname
        #e top[gc] i don't even know how I thought that was right
       #e tried to cat "text to append" instead of echo
       #e echoed text came out weirdly in debug print
       #e AAAGGGH the test example had newlines where it wrapped in the window
       #e forgot to take out pdb before I ran again for real
       #e iterm window too small really
       #e aaggh apparently the actual format includes newline wraps as valid

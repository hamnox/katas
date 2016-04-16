import numpy as np

class fibonacci:
    def __init__(self, k):
        self.k = k
        self.ref = {1: 1}
    def get(self, n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in self.ref:
            return self.ref[n]
        if n-1 not in self.ref:
            f1 = self.get(n - 1)
            self.ref[n-1] = f1
        else:
            f1 = self.ref[n-1]
        if n-2 not in self.ref:
            f2 = self.get(n - 2)
            self.ref[n-2] = f2
        else:
            f2 = self.ref[n-2]
        self.ref[n] = f1 + f2 * self.k
        return self.ref[n]


def parse_nk(line):
    n, k = line.split()
    n = int(n)
    k = int(k)
    return n, k

def parse_kmData(f):
    k, m = f.readline()[:-1].split()
    k = int(k)
    m = int(m)
    data = []
    while True:
        line = f.readline()
        if line == "":
            break
        # err: went to bathroom, forgot to pause timer
        # err: not getting to meat of problem because of parsing shit.
        subdata = []
        for x in line[:-1].split():
            subdata.append(float(x))
        data.append(subdata)
    data = np.matrix(data) 
    return k, m, data


def calculate_centers(centers, dimensions, data_matrix):
    # err: been forgetting docstrings
    # assert data_matrix has dimensions
# FarthestFirstTraversal(Data, k) 
#  Centers ← the set consisting of a single randomly chosen point from Data
#   while |Centers| < k 
#    DataPoint ← the point in Data maximizing d(DataPoint, Centers) 
#    add DataPoint to Centers 
#  return Centers 
    pass


if __name__ == "__main__":
    with open('temp.txt', 'r') as f:
        k, m, data = parse_kmData(f)
        # err: ran out of time to test



# err: hnew is not a vim command
        # err: would be simpler if I had numpy matrix, no time to look up
    # err: ycm tried to change 'line' to readline

    # err: pdb too slow
    # err: messed up noh statement
        # err: indeed needed to knock off the newline
        # err: don't remember if readline gives you \n
        # err: regex too hard to learn right now
            # err: returned key instead of value
            # tried to %s () instead of % ()
        # err: used a global k instead of instance

    # err: forgot to call recursive with all arguments
    # err: wish knew math better to do formulaically
    # err: didn't connect fib instructions to the problem
    # err: forgot to stop printing the intermediate steps
    # err: multiplied by a constant instead of 

    # err: accidentally opened a weird miniwindow in vim
    # err: Ran out of time right before testing

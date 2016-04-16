# err don't remember argparse
import argparse
from datetime.

parser = argparse.ArgumentParser(description='Average some nums in a logfile')
parser.add_argument('fileobject', type=open, help='input file')

# err: had to look up parse_args()
args = parser.parse_args()

lines = args.fileobject.readlines()

#err can't remember how to parse dates
# err out of time
#err fiddling with windows

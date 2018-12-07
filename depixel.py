import os
import sys

PotraceTrans = lambda x : os.system('potrace -b svg -b pdf '+x))
map(PotraceTrans, sys.argv[1:])

import os
import sys

Args=[]

Args.extend(sys.argv[1:])

PotraceTrans = lambda x : os.system('potrace -b svg -b pdf {0} -o {1}.pdf'.format(x, x[:-4]))
map(PotraceTrans, Args)

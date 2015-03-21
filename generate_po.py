#!/ve/premier/bin/python

import sys, getopt
from purchase.models import PurchaseOrder

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      # import pdb; pdb.set_trace();
      opts, args = getopt.getopt(argv,"p:f:")
   except getopt.GetoptError:
      print 'test.py -i <inputfile> -o <outputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-p':
      	print arg


if __name__ == "__main__":
   main(sys.argv[1:])
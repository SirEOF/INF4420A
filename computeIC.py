#!/usr/bin/env python

import sys
import collections

# Bag em
cipher_file  = open( sys.argv[ 1 ], 'rb')  
cipher_text  = cipher_file.read()

# remove all non alpha and whitespace and force uppercase
# SOTHATCIPHERTEXTLOOKSLIKETHIS
cipher_flat  = "".join( 
                        [x.upper() for x in cipher_text.split() \
                                   if  x.isalpha() ]
                     )

# Tag em
N            = len(cipher_flat)
freqs        = collections.Counter( cipher_flat )
alphabet     =  map(chr, range( ord('A'), ord('Z')+1))
freqsum      = 0.0

# Do the math
for letter in alphabet:
    freqsum += freqs[ letter ] * ( freqs[ letter ] - 1 )

IC = freqsum / ( N*(N-1) )

print "%.3f" % IC, "({})".format( IC )

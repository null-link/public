#Python module for converting hex to base64

import binascii   # useful methods for binary ascii shinanigans

#take this string from the cryptopals challenge.  interpret it as hex.

hex = binascii.a2b_hex("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")

#print if want to see what it reads, then this convert the hex to ascii
#print(bytes.decode(hex))

#convert the hex to base64
base = binascii.b2a_base64(hex)

#print final output
print(bytes.decode(base))



# In this problem, you will see how to exploit the malleability of one-time pad.encryption to change the meaning of an encrypted message. 
# Suppose you are told that theone-time pad encryption of the message:
  # “final grade: 20% (F-)” is ==> 0x09ea81c5f7b0a6653ac6519458e7e53f36ab0f232c, where each plaintext letter is encoded as 8-bit ASCII 
# and the given ciphertext is written in hexadecimal notation. What would be the one-time pad encryption of the message:
# “finalgrade: 99% (A+)” under the same pad?

import utils

def main():
    #plaintext m1
    m1 = "final grade: 20% (F-)";
    #one time pad encryption of plaintext m1
    c1 = "09ea81c5f7b0a6653ac6519458e7e53f36ab0f232c";
    #plaintext m2
    m2 = "final grade: 99% (A+)";
    
    m1_bin = utils.ascii2Bin(m1);
    c1_bin = utils.hex2Bin(c1);
    m2_bin = utils.ascii2Bin(m2);
    
    assert(len(m1_bin) == len(c1_bin) == len(m2_bin))
    
    result = utils.xor(utils.xor(m1_bin, c1_bin), m2_bin);
    print(utils.bin2Hex(result))

if(__name__ == "__main__"):
    main();

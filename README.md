# IntroductionToCryptography
Programming assignments as part of the course "CSCI-B504 Introduction to Cryptography"

## Crib Dragging:
Reference: http://travisdazell.blogspot.com/2012/11/many-time-pad-attack-crib-drag.html

Follow the steps below:

i)   Guess a word that might appear in one of the messages<br>
ii)  Encode the word from step 1 to a hex string<br>
iii) XOR the two cipher-text messages<br>
iv)  XOR the hex string from step 2 at each position of the XOR of the two cipher-texts (from step 3)<br>
v)   When the result from step 4 is readable text, we guess the English word and expand our crib search.<br>
     If the result is not readable text, we try an XOR of the crib word at the next position.<br>
     
The plaintexts deciphered by the process are:

**plaintext1:**<br>
Physalis acutifolia is a species of flowering plant in the nightshade family known by the common names sharpleaf groundcherry and Wright groundcherry. It is native to the southwestern United States from California to Texas, and northern Mexico, where it can be found in many types of habitat, includi

**plaintext2:**<br>
It is a small, unnamed headland, some 2.5 km east of Nelly Point, which has been referred to unofficially as Chinstrap Camp. The site has been identified as an Important Bird Area (IBA) by BirdLife International because it supports a large breeding colony of about 24,000 pairs of Chinstrap Penguins.

## CTR ciphertext decryption:
**ciphertext properties**<br>
'ctr-ciphertext' file is encrypted using the 128-bit AES block cipher in CTR mode with a random 128-bit key. The first block (16 bytes) of the ciphertext is the random IV.

**server(oracle) properties**<br>
The server at *burrow.soic.indiana.edu:33336* exhibits the following behaviour:<br>
given a CTR mode encrypted ciphertext it decrypts the ciphertext and checks the padding (that is, it inspects the last byte of the resulting plaintext to determine *d−1*, and then it checks that each of the preceding *d−1* bytes are equal to *d−1*). If the padding is invalid, it returns 0; otherwise, it returns1.


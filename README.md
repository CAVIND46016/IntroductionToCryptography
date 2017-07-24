# IntroductionToCryptography
Programming assignments as part of the course "CSCI-B504 Introduction to Cryptography"

## Crib Dragging:
Reference: http://travisdazell.blogspot.com/2012/11/many-time-pad-attack-crib-drag.html

Follow the steps below:

i)   Guess a word that might appear in one of the messages
ii)  Encode the word from step 1 to a hex string
iii) XOR the two cipher-text messages
iv)  XOR the hex string from step 2 at each position of the XOR of the two cipher-texts (from step 3)
v)   When the result from step 4 is readable text, we guess the English word and expand our crib search.
     If the result is not readable text, we try an XOR of the crib word at the next position.
     
The plaintexts deciphered by the process are:

**plaintext1:**
Physalis acutifolia is a species of flowering plant in the nightshade family known by the common names sharpleaf groundcherry and Wright groundcherry. It is native to the southwestern United States from California to Texas, and northern Mexico, where it can be found in many types of habitat, includi

**plaintext2:**
It is a small, unnamed headland, some 2.5 km east of Nelly Point, which has been referred to unofficially as Chinstrap Camp. The site has been identified as an Important Bird Area (IBA) by BirdLife International because it supports a large breeding colony of about 24,000 pairs of Chinstrap Penguins.

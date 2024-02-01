Enigma Crib Analysis 

This is a a solution to a simple python cryptography challenge. The Enigma code was a method of encryption used 
by Germany during WW2. One of its weaknesses was the fact that a letter cannot be encoded as itself. Given that a common word 
can be guessed and brute forced to find locations in the text where no letter in the common word matches letters in the encrypted text. These locations are
known as cribs. This script performs that function using the keyword secretmessage and iterates through to find possible cribs.

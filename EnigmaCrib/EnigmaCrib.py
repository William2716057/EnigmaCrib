ciphertext = "HQEYSAWQSTNTLGKPESREVL"
plaintext  = "SECRETMESSAGE"
#Complete the code here to output all possible valid cribs using the ciphertext and the plaintext to use for the crib
#You will need to test all posible positions of the crib and discard cribs containing at least one letter encoded as itself.
#initialise an empty list for storing valid cribs
valid = []

#iterate through all possible starting position of crib

for i in range(len(ciphertext) - len(plaintext) +1):
    #extract possible cribs from ciphertext
    possible = ciphertext[i:i+len(plaintext)]
    #search for characters encoded as themselves
    if all(c != p for c, p in zip(possible, plaintext)):
        #if no matches found add to list
        valid.append(possible)
        
#print all valid cribs
print("valid cribs: ", valid)

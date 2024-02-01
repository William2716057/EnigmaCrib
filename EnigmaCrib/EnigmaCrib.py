ciphertext = "HQEYSAWQSTNTLGKPESREVL"
plaintext  = "SECRETMESSAGE"

#Complete the code here to output all possible valid cribs using the ciphertext and the plaintext to use for the crib
#You will need to test all posible positions of the crib and discard cribs containing at least one letter encoded as itself.

#iterate through each index of each string if indexes contain the same letter
#shift character in position 0 of plaintext by one padding 
#plaintext with 0 in front
#print results that do not contain matches 

#add cipher and plaintext to lists 
#if not print result
#"H","Q","E","Y","S","A","W","Q","S","T","N","T","L","G","K","P","E","S","R","E","V","L"
list1, list2 = ["H","Q","E","Y","S","A","W","Q","S","T","N","T","L","G","K","P","E","S","R","E","V","L"], ["S","E","C","R","E","T","M","E","S","S","A","G","E"]

print([index for index, (e1, e2) in enumerate(zip(list1, list2)) if e1 == e2])
#match at [8]
#list2 = ["0","S","E","C","R","E","T","M","E","S","S","A","G","E"]
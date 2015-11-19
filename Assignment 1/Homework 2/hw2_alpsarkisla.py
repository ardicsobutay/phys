

word = raw_input("Please enter a string: ")
sumbob = 0
i = 0
while i+2 < len(word):
    if word[i:i+3] == "bob" :
        i = i+3 
        sumbob += 1
    else :
        i += 1 
print "Number of non-intersecting bobs are: " + str(sumbob)           

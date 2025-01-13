#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACE_HOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as letters:
    names = [name.rstrip() for name in letters] #strip \n in each name
    # print(names)
    with open("./Input/Letters/starting_letter.txt") as letter_template:
        letter_temp = letter_template.read()
        # search_text = "[name]"
        for name in names:
            print(name)    
            
            custom_letter = letter_temp.replace(PLACE_HOLDER, name)
            
            print(custom_letter)
            
            with open(f"./Output/ReadyToSend/{name}_letter.txt", mode="w") as letter_to_mail:
                letter_to_mail.write(custom_letter)                       
        
        # print(letter_temp)
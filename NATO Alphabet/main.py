student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas as pd
student_data_frame = pd.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    print(index)
    print(row)
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
nato_df = pd.read_csv("nato_phonetic_alphabet.csv")
print(nato_df)

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_dict = {row.letter:row.code for (index,row) in nato_df.iterrows()}
print(nato_dict)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("What do you want to spell out? ").upper()
# nato_list = [value for (key,value) in nato_dict ]
# nato_list = []
# for c in word:
#     nato_list.append(nato_dict[c])

nato_list = [nato_dict[c] for c in word]
    
print(nato_list)
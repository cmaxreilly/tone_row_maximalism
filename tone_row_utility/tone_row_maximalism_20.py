# My objective with this program is to create a piece that performs every single tone row possible in a row without repetition.
# This second version has come about because of my realization that my final system of notating pitches must be a duodecimal system. 
# After consideration, I have decided to do this at the last possible moment, when the pitches are transfered to the repository.
# 
# To Do:
# 1: Re-make tone row repository writer, because I erased that for some fucking reason.
# 2: While re-making repository writer, incorporate in conversion to duodecimal system
# 3: Test repository writer
# 4: Make midi file writer program with minmal repetition of code.
# 5: Test midi file writer program.
# 6: Import midi files to a new Ableton project. 
# 7: Do mixing and arranging.

from os import lseek
import random



#Function that generates tone rows

pitch_integers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ]
def tone_row_generator():

    random.shuffle(pitch_integers)

    tone_row = []

    for pitch in pitch_integers:
        tone_row.append(pitch)
    return(tone_row)

def transpose_function(notes, transposition):
    transposed_notes = []
    for note in notes:
        if note + transposition <= 11:
            transposed_notes.append(note + transposition)
        else:
            transposed_notes.append(note + transposition - 12)
    return transposed_notes


#function that transposes a tone row into every key
def total_tone_row_transposer(tone_row):
    list_of_tranposed_tone_rows = []
    for pitch in pitch_integers:
        list_of_tranposed_tone_rows.append(transpose_function(tone_row, pitch))
    return list_of_tranposed_tone_rows

#testing that function
#print(total_tone_row_transposer(tone_row_generator()))
    

#function to generate non repeating tone row list
def non_repeating_tone_row_list(length):
    list_length = list(range(0, length))
    non_repeating_list = []
    unbroken_list = []
    for number in list_length:
        tone_row = tone_row_generator()
        tone_row_transposed = total_tone_row_transposer(tone_row)
        for row in tone_row_transposed:
            if row in non_repeating_list:
                break
            else:
                non_repeating_list.append(row)
                break
            #This row is a problem, because the midi reads it 10 and 11 as 1 0 1 1, which
            #compromises the integrity of the tone rows. I will have to edit this before 
            #I go on. This is a serious logistical problem.
    return non_repeating_list

# print(non_repeating_tone_row_list(10))

# Creates the hyper row. Number controls the length.

hyper_row = non_repeating_tone_row_list(5000)

# data to go into tone_row_repository.txt
repository_data = ""

# concentates data to repository in a duodecimal system
for row in hyper_row:
    for note in row:
        if note == 10:
            repository_data += "T"
        elif note == 11:
            repository_data += "E"
        else:
            repository_data += str(note)

# Testing hyper row generator and repository generator
# print(hyper_row)
# print(repository_data)

# Adds data to tone_row_repository.txt

with open('Documents/the_vault/Code/tone_row_maximalism/tone_row_repository.txt', 'w') as repository:
    repository.write(repository_data)

# Great Success! Now I will move on to making the midi writer that does it all in a bunch of octaves

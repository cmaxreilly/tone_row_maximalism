#Copied from midi_function_writer.py

def midi_file_writer_writer (octave, duration):
    
    

    for note in :
        around_C1.append(int(note) + (12 * octave))
    
    degrees  = 
    track    = 0
    channel  = 0
    time     = 0   
    duration = 1/14
    tempo    = 200  
    volume   = 100 

    C7_track = MIDIFile(1)

    C7_track.addTempo(track, time, tempo)

    for pitch in degrees:
        C7_track.addNote(track, channel, pitch, time, duration, volume)
        time = time + 1

    with open("C7_track.mid", "wb") as output_file:
        C7_track.writeFile(output_file)


# Copied from midi_writer.py

from midiutil import MIDIFile

import random

with open("tone_row_repository.txt", 'r') as repository:
    string_of_notes = repository.read()

list_of_notes = list(string_of_notes)

around_C1 = []
around_C2 =[]
around_C3 = []
around_C4 = []
around_C5 = []
around_C6 = []
around_C7 = []

for note in list_of_notes:
    
    around_C1.append(int(note) + 12)
    around_C2.append(int(note) + 24)
    around_C3.append(int(note) + 36)
    around_C4.append(int(note) + 48)
    around_C5.append(int(note) + 60)
    around_C6.append(int(note) + 72)
    around_C7.append(int(note) + 84)

#hyper_row = []
#for note in list_of_notes:
#    index_number = 0
#    octave_randomizer = list(range(0, 12))
#    random.shuffle(octave_randomizer)
#    if index_number < 12:
#        hyper_row.append(note * (12 * octave_randomizer[index_number]))
#        index_number += 1
#    else:
#        hyper_row.append(note * (12 * octave_randomizer(index_number)))
    

#print(hyper_row)

degrees  = around_C7
track    = 0
channel  = 0
time     = 0   
duration = 1/14
tempo    = 200  
volume   = 100 

C7_track = MIDIFile(1)

C7_track.addTempo(track, time, tempo)

for pitch in degrees:
    C7_track.addNote(track, channel, pitch, time, duration, volume)
    time = time + 1

with open("C7_track.mid", "wb") as output_file:
    C7_track.writeFile(output_file)


# Copied from midi_writer_1.0.py


from midiutil import MIDIFile


with open("Documents/the_vault/Code/tone_row_maximalism/tone_row_repository.txt", 'r') as repository:
    string_of_notes = repository.read()

list_of_notes = list(string_of_notes)

around_C1 = []
around_C2 =[]
around_C3 = []
around_C4 = []
around_C5 = []
around_C6 = []
around_C7 = []

for note in list_of_notes:
    if note == 'T':
        around_C1.append(10 + 12)
        around_C2.append(10 + 24)
        around_C3.append(10 + 36)
        around_C4.append(10 + 48)
        around_C5.append(10 + 60)
        around_C6.append(10 + 72)
        around_C7.append(10 + 84)
    elif note == 'E':
        around_C1.append(11 + 12)
        around_C2.append(11 + 24)
        around_C3.append(11 + 36)
        around_C4.append(11 + 48)
        around_C5.append(11 + 60)
        around_C6.append(11 + 72)
        around_C7.append(11 + 84)
    else:
        around_C1.append(int(note) + 12)
        around_C2.append(int(note) + 24)
        around_C3.append(int(note) + 36)
        around_C4.append(int(note) + 48)
        around_C5.append(int(note) + 60)
        around_C6.append(int(note) + 72)
        around_C7.append(int(note) + 84)


# Testing of the list of notes appendor thing
#print(list_of_notes)
#print(around_C1)



#print(hyper_row)

# Around C1 midifile creator
degrees  = around_C1
track    = 0
channel  = 0
time     = 0   
duration = 1
tempo    = 200  
volume   = 100 

C1_track = MIDIFile(1)

C1_track.addTempo(track, time, tempo)

for pitch in degrees:
    C1_track.addNote(track, channel, pitch, time, duration, volume)
    time = time + 1

with open("Documents/the_vault/Code/tone_row_maximalism/C1_track.mid", "wb") as output_file:
    C1_track.writeFile(output_file)


# Around C2

degrees  = around_C2
track    = 0
channel  = 0
time     = 0   
duration = 1/2
tempo    = 200  
volume   = 100 

C2_track = MIDIFile(1)

C2_track.addTempo(track, time, tempo)

for pitch in degrees:
    C2_track.addNote(track, channel, pitch, time, duration, volume)
    time = time + 1/2

with open("Documents/the_vault/Code/tone_row_maximalism/C2_track.mid", "wb") as output_file:
    C2_track.writeFile(output_file)

# Around C3

degrees  = around_C3
track    = 0
channel  = 0
time     = 0   
duration = 1
tempo    = 200  
volume   = 100 

C3_track = MIDIFile(1)

C3_track.addTempo(track, time, tempo)

for pitch in degrees:
    C3_track.addNote(track, channel, pitch, time, duration, volume)
    time = time + 1/3

with open("Documents/the_vault/Code/tone_row_maximalism/C3_track.mid", "wb") as output_file:
    C3_track.writeFile(output_file)

# Around C4

degrees  = around_C4
track    = 0
channel  = 0
time     = 0   
duration = 1/3
tempo    = 200  
volume   = 100 

C4_track = MIDIFile(1)

C4_track.addTempo(track, time, tempo)

for pitch in degrees:
    C4_track.addNote(track, channel, pitch, time, duration, volume)
    time = time + 1/3

with open("Documents/the_vault/Code/tone_row_maximalism/C4_track.mid", "wb") as output_file:
    C4_track.writeFile(output_file)

# Around C5

degrees  = around_C5
track    = 0
channel  = 0
time     = 0   
duration = 1/4
tempo    = 200  
volume   = 100 

C5_track = MIDIFile(1)

C5_track.addTempo(track, time, tempo)

for pitch in degrees:
    C5_track.addNote(track, channel, pitch, time, duration, volume)
    time = time + 1/4

with open("Documents/the_vault/Code/tone_row_maximalism/C5_track.mid", "wb") as output_file:
    C5_track.writeFile(output_file)

# Around C6

degrees  = around_C6
track    = 0
channel  = 0
time     = 0   
duration = 1/5
tempo    = 200  
volume   = 100 

C6_track = MIDIFile(1)

C6_track.addTempo(track, time, tempo)

for pitch in degrees:
    C6_track.addNote(track, channel, pitch, time, duration, volume)
    time = time + 1/5

with open("Documents/the_vault/Code/tone_row_maximalism/C6_track.mid", "wb") as output_file:
    C6_track.writeFile(output_file)

# Around C7

degrees  = around_C7
track    = 0
channel  = 0
time     = 0   
duration = 1/6
tempo    = 200  
volume   = 100 

C7_track = MIDIFile(1)

C7_track.addTempo(track, time, tempo)

for pitch in degrees:
    C7_track.addNote(track, channel, pitch, time, duration, volume)
    time = time + 1/6

with open("Documents/the_vault/Code/tone_row_maximalism/C7_track.mid", "wb") as output_file:
    C7_track.writeFile(output_file)


# Copied from tone_row_maximalism_1.0.py

#My objective with this program is to create a piece that performs every single tone row possible in a row without repetition.

from os import lseek
import random
from midiutil import MIDIFile


#Function that generates tone rows

pitch_integers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, T, E, ]
def tone_row_generator():

    random.shuffle(pitch_integers)

    tone_row = []

    for pitch in pitch_integers:
        tone_row.append(pitch)
    return(tone_row)

#function to generate tone row list
def tone_row_list(length):
    list_length = list(range(0, length))
    list_of_tone_rows = []
    for number in list_length:
        tone_row = tone_row_generator()
        list_of_tone_rows.append(tone_row)
    return list_of_tone_rows

#function that transposes a tone row into a key

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

#print(non_repeating_tone_row_list(10))


# Now I need to append the tone row list to lists that designate different octaves
list_of_tone_rows = non_repeating_tone_row_list(500)

around_C1 = []
around_C2 =[]
around_C3 = []
around_C4 = []
around_C5 = []
around_C6 = []
around_C7 = []

for row in list_of_tone_rows:
    for note in row:
        
        around_C1.append(int(note) + 12)
        around_C2.append(int(note) + 24)
        around_C3.append(int(note) + 36)
        around_C4.append(int(note) + 48)
        around_C5.append(int(note) + 60)
        around_C6.append(int(note) + 72)
        around_C7.append(int(note) + 84)


#  This is a failed attmept at making a tone row with randomized octaves
#hyper_row = []
#for note in list_of_notes:
#    index_number = 0
#    octave_randomizer = list(range(0, 12))
#    random.shuffle(octave_randomizer)
#    if index_number < 12:
#        hyper_row.append(note * (12 * octave_randomizer[index_number]))
#        index_number += 1
#    else:
#        hyper_row.append(note * (12 * octave_randomizer(index_number)))
    

#print(hyper_row)

degrees  = around_C7
track    = 0
channel  = 0
time     = 0   
duration = 1/14
tempo    = 200  
volume   = 100 

C7_track = MIDIFile(1)

C7_track.addTempo(track, time, tempo)

for pitch in degrees:
    C7_track.addNote(track, channel, pitch, time, duration, volume)
    time = time + 1

with open("C7_track.mid", "wb") as output_file:
    C7_track.writeFile(output_file)


# Copied from tone_row_maximalism_20.py

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

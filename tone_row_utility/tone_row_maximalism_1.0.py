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
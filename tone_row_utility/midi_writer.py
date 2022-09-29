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

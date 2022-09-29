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
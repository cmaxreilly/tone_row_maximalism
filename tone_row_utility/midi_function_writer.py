

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

import random
from midiutil import MIDIFile

# This may be way easier to use if I just make a gui, but still going to 
# make a command line option with an interactive prompt


# Global constants
pitch_integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
#from helpers import tone_row_generator

# A function that takes user input from the command line
#   * How many tone rows
#   * In Midi or on the command line
#   * What octaves
#   * All transpositions?
#   * Inversion?
#   * Retrograde?
#   * What directory
#   * Rhythmic information
#       * serialized rhythmn
#       * Pick Rhythmn
# A function that creates tone rows

def tone_row_generator():
    global pitch_integers
    random.shuffle(pitch_integers)

    tone_row = []

    for pitch in pitch_integers:
        tone_row.append(pitch)
    # initialize pitch integers
    pitch_integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    return(tone_row)

# A function that creates a list of tone  rows of a given length

def tone_row_list(length):
    list_length = list(range(0, length))
    list_of_tone_rows = []
    for number in list_length:
        tone_row = tone_row_generator()
        list_of_tone_rows.append(tone_row)
    return list_of_tone_rows

# A function that creates a non repeating list of tone rows

def non_repeating_tone_row_list(length):
    list_length = list(range(0, length))
    list_of_tone_rows = []
    for number in list_length:
        tone_row = tone_row_generator()
        if tone_row in list_of_tone_rows:
            pass
        else:
            list_of_tone_rows.append(tone_row)
    return list_of_tone_rows

# Function to transpose a single pitch

def tranpose_pitch_by_interval(pitch, transposition):
    if pitch + transposition < 12:
        new_pitch = (pitch + transposition)
    else:
        new_pitch = (pitch + transposition) % 12
    return new_pitch


# A function that transposes tone rows to different octaves

def transpose_by_octave_up(pitches, octave):
    new_list = []
    for pitch in pitches:
        new_list.append(pitch + (octave * 12))
    return new_list
        
# A function that transposes tone rows into all 12 keys

def tranpose_row_by_interval(row, transposition):
    new_row = []
    for pitch in row:
        transposed_pitch = tranpose_pitch_by_interval(pitch, transposition)
        if transposed_pitch < 12:
            new_row.append(transposed_pitch) 
        else: 
            new_row.append(transposed_pitch % 12)
    return new_row


# A function that transposes all tone rows into all 12 keys

def transpose_to_all_keys(pitches):
    tranpositions = []
    for number in pitch_integers:
        tranpositions.append(tranpose_row_by_interval(pitches, number))
    return tranpositions   
# A function that does inversion
def invert_pitch_content(pitches):
    inverted_pitches = []
    for pitch in pitches:
        inverted_pitches.append((pitch + 11) - (pitch * 2))
    return inverted_pitches
     
# A function that does retrograde

def retrograde_pitch_content(pitches):
    pitches.reverse()
    return pitches 
# A function that generates midi files in the given directory from a given set of pitches

def write_midi_file(pitches, desired_duration, usrpath):
    degrees  = pitches 
    track    = 0
    channel  = 0
    time     = 0   
    duration = desired_duration 
    tempo    = 200  
    volume   = 100 

    midi_track = MIDIFile(1)

    midi_track.addTempo(track, time, tempo)

    for pitch in degrees:
        midi_track.addNote(track, channel, pitch, time, duration, volume)
        time = time + 1

    with open("{}.mid".format(usrpath), "wb") as output_file:
        midi_track.writeFile(output_file)

 

# A __name__ == "__main__" conditional statement for testing function execution.

if __name__ == "__main__":
    print(pitch_integers) 
    test_row = tone_row_generator()
    print("test row: " + str(test_row))
    print('transpose up five octaves: ' + str(transpose_by_octave_up(test_row, 5)))
    print('transpose up 5 half steps: ' + str(tranpose_row_by_interval(test_row, 5)))
    print('transpose to all keys: ' + (str(transpose_to_all_keys(test_row))))
    print('invert: ' + str(invert_pitch_content(test_row)))
    print(pitch_integers)
    write_midi_file(test_row, 1/16, "../test") 

# Congratulations! Looks like all of the functionality works well. Now I will start work on the driver
# code in ../__main__.py to make a command line tool that makes use of these functions. 
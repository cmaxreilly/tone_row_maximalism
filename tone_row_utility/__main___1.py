import random

# This may be way easier to use if I just make a gui, but still going to 
# make a command line option with an interactive prompt


# Global constants
pitch_integers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ]
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

    random.shuffle(pitch_integers)

    tone_row = []

    for pitch in pitch_integers:
        tone_row.append(pitch)
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
# A function that transposes tone rows to different octaves

# A function that transposes tone rows into all 12 keys

# A function that transposes all tone rows into all 12 keys

# A function that does inversion

# A function that does retrograde

# A function that generates midi files in the given directory

# A __name__ == "__main__" conditional statement for execution.

if __name__ == "__main__":
    print(tone_row_generator())
    print(non_repeating_tone_row_list(20))
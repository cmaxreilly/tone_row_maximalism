from tonerowutils import tonerowutils as t
from sys import argv 

# print(t.pitch_integers)
# print (t.tone_row_generator())
# print (t.pitch_integers)

message = "Greetings! I will put a dumb help message here."

# Driver code for the tone row utility

if len(argv) == 1:
    print(message) 
elif len(argv) == 2:
    if argv[1] == '-s':
        print("Your tone row is {}".format(t.tone_row_generator()))
    elif argv[1] == '-sm' or argv[1] == '-ms':
        tone_row = t.tone_row_generator()
        print("Your tone row is {}, and has been printed to a midi file in this directory".format(tone_row))
        t.write_midi_file(tone_row, 1, "tone_row")
else:
    print("Invalid options.")

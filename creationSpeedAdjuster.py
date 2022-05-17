from musicPlayer import song_reader

# This program will be used only by me in order to adjust the speed of the song.
# This is useful because I will create some songs in a slowed state (probably 50% speed or so) in order to
# accurately make the notes spawn at the right time.

name = input("Song: ")  # get the song choice

notes = song_reader(name)  # put the existing notes into a list to be changed

speedAdj = float(input("Enter the decimal percentage at which you would like to adjust the song's speed "
                       "(0-1 to decrease, > 1 to increase): "))

# open the file again to replace the lines at new speed
file = open("song txts/{}.txt".format(name), "w")
file.writelines("{} {}\n".format(notes[0][0], notes[0][1]))  # write the starting time

for i in range(1, len(notes)):
    notes[i][1] = round(notes[i][1] / speedAdj)  # will make notes play quicker if they want speed increased, slower if decreased
    file.writelines("{} {}\n".format(notes[i][0], notes[i][1]))

file.close()

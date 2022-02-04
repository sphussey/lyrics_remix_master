"""
    CS5001
    Fall 2021
    HW5 - ♫♫♫♫ remix_master.py ♫♫♫♫
    Shane Hussey

    Program for remixing selected songs from music.py ♫♫♫♫♫♫♫♫♫♫♫♫♫♫♫♫
"""

import music

# import song name and song lists from music.py in same directory
PLAYLIST = music.PLAYLIST
SONGS = music.SONGS

SONGLISTTXT = '''
            Choose the number for song you want to load:
            1: Old MacDonald
            2: Row Your Boat
            3: Happy
            
            Your Choice: '''

# create a single list of all available song names and their respective
# lyrics in the format [[lyrics, more lyrics], name], [etc.]]
MUSIC = [list(jam) for jam in zip(SONGS, PLAYLIST)]


WELCOME = '''Welcome to Remix-Master. You can remix the greatest hits!
Turn up the 808's and drop the beat! Here's your remix:'''

# define user choices for mix
USER_CHOICES ='''
    Remix-Master:
     L: Load a different song
     T: Title of current song
     S: Substitute a word
     P: Playback your song
     R: Reverse it!
     X: Reset to original song
     Q: Quit?
     Your Choice:  '''

# actionable valid entries for USER_CHOICES
REMIX_ENTRIES = ['l', 't', 's', 'p', 'r', 'x']


def load_song(selection: int) -> list:
    """

    Description - selects song to load based on user input
    Inputs - selection is an integer reprsenting a song in SONGLISTTXT
    Returns - list of chosen song data [[lyrics, more lyrics], name], [etc.]]

    """
    
    if (1 <= selection <= len(PLAYLIST)):
        song_data = MUSIC[(selection - 1)]
    else:
        song_data = []
    return song_data


def substitute(song: list, old_word: str, new_word: str ) -> list:
    """

    Description - replaces desired words into new words
    Inputs -
    songs - song lyric strings in list form ['line 1 lyrics', 'line2']
    old_word - desired word to change from
    new_word - desired word to change to
    Returns - if the word is in the song, it returns a word substituted
        song. the old_word is not present in the song, it returs the song
        unmutagenized. 

    """
    # iterate through the lines, then through the words, and replace the
    # old_word with the new_word if the old_word is present in the lyrics
    for line in song:
        lsplit = line.split(' ')
        for word in lsplit:
            while word != old_word:
                subbed_song = []
                for line in song:
                    subbed_song.append(line.replace(old_word, new_word))
                return subbed_song
                
        return song


def reverse_it(song: list) -> list:
    """

    Description - reverses order of words on a given line in a song's lyrics    
    Inputs - song - list of lyrics in format ['line 1 lyrics', 'line2']
    Returns - list containing reversed words from individual lines of song

    """
    reversed_song = []
    # iterate through lines in song, split to words, strip and rejoin reversed
    for line in song:
        words = line.split(' ')
        stripped = []
        for word in words:
            # strip punctuation
            stripped.append(word.strip('(!?,.;:)'))
        # join reversed words on the same line
        reversed_words = ' '.join(stripped[::-1])
        reversed_song.append(reversed_words)
    return reversed_song    


def starting_song() -> list:
    """

    Description - initiates song selection with the first song on playlist
    Inputs - none
    Returns - list with song data in form [lyrics, more lyrics], name]

    """
    #Greet user with message 
    print(WELCOME)
    # auto-load first song
    song_data = MUSIC[0].copy()
    print('starting_song',song_data)
    # print autoloading song to user
    for line in song_data[0]:
        print(line)
    print('\n')
    return song_data


def remix_manager(user_input: int, song_data: list) -> list:
    """

    Description - function to manage user input and direct action functions
    Inputs -
    user_input - integer selection correlating with SONGLISTTXT
    song_data - list with song data in form [lyrics, more lyrics], name]
    Returns - mutated list with song data in form [lyrics, more lyrics], name]

    """

    # load song selection
    if user_input == 'l':
        selection = int(input(SONGLISTTXT))
        song_data = load_song(selection)
    # names song
    elif user_input == 't':
        print('-♫' * 20, '\nYou are mixing the song: ', song_data[1], sep='')
    # Asks for user input to substitute a word
    elif user_input == 's':
        old_word = input('What word do you want to replace in the song? ')
        new_word = input('What new word do you want to use for the song? ')
        song_data[0] = substitute(song_data[0],old_word, new_word)
    # prints song lyrics if p is entered by user
    elif user_input == 'p': # Playback the song
        print("Turn up the 808's and drop the beat! Here's your remix:")
        if song_data != []:
            song = song_data[0]
            for line in song:
                print(line)

    # reverses words in idividual lyric lines
    elif user_input == 'r': 
        song_data[0] = reverse_it(song_data[0])
    # for 'x' reset to orignial song
    elif user_input == 'x':
        song_data = MUSIC[0]
    return song_data


def ui():
    """

    Description - Responsible for User interaction with mixing choices
    and utilizes remix manager function to organize task functions
    Inputs - none
    Returns - 

    """
    # Greet user and print first song in list
    song_data = starting_song()
    # Ask User how they would like to mix their song
    user_input = input(USER_CHOICES).lower()
    song_data = remix_manager(user_input, song_data)
    # loop through actionable remix inputs
    while user_input != 'q':
        user_input = input(USER_CHOICES).lower()
        print('\n')
        # Run User input manager to perform task requested by user
        song_data = remix_manager(user_input, song_data)
    if user_input == 'q':
        print('Bravo! Your Grammy Award is being shipped to you now!')


def main():
    ui()


if __name__ == '__main__':
    main()

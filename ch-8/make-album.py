# Exercise 8-7, p142
# Write a function called make_album() that builds a dictionary describing a 
# music album. The function should take in an artist name and an album title,
# and it should return a dictionary containing these two pieces of information.
# Use the function to make three dictionaries representing different albums.
# Use "None" to add an optional paramter to make_album() that allows your to store
# the number of songs on an album. If the calling line includes a value for the
# number of songs, add that value to the album's dictionary. Make at least one
# new function call that includes the number of songs on an album.

def make_album(artist, album_name, tracks = None):
    """Returns information about an album in a dictionary that contains the name of the album, the artist, and the number of tracks (if available)"""
    album = {'album': album_name, 'artist': artist}
    if tracks == None:
        return(album)
    else:
        album['tracks'] = tracks
        return(album)

#album_a=make_album(artist='ween', album_name='quebec')
#album_b=make_album(artist='horronauts', album_name='a night with the horrornauts')
#album_c=make_album(artist="sinead o'connor", album_name="i do not want what i haven't got")
#album_d=make_album(artist='pertubator', album_name="dangerous days", tracks = 13)
#print(album_a)
#print(album_b)
#print(album_c)
#print(album_d)

# Exercise 8-8, p142
# Start with your program from exercise 8-7. Write a while loop that allows users
# to enter an album's artist and title. Once you have that information, call
# make_album() with the user's input and print the dictionary that is created.
# Be sure to include a quit value in the while loop.

def user_album():
    """Collects information about an album from the user that is then fed to make_album to create a dictionary."""
    while True:
        print("\nLet's get some information about one of your favorite albums.")
        print("Enter 'q' at any time to quit.")
        user_title=input("\nWhat is the name of the album? ")
        if user_title == 'q':
            break
        user_artist=input("What is the name of the artist? ")
        if user_artist == 'q':
            break
        generated_album=make_album(user_artist, user_title)
        print(generated_album)
        continue

user_album()


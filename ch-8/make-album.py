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

album_a=make_album(artist='ween', album_name='quebec')
album_b=make_album(artist='horronauts', album_name='a night with the horrornauts')
album_c=make_album(artist="sinead o'connor", album_name="i do not want what i haven't got")
album_d=make_album(artist='pertubator', album_name="dangerous days", tracks = 13)
print(album_a)
print(album_b)
print(album_c)
print(album_d)

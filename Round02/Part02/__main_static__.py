from analysis import Unidentified  # type: ignore[reportUnusedImports]
from os import chdir
from os.path import dirname
from io import open

# Store expected name of CSV file as a constant
FILENAME: str = "Anomalous - Anomalous.csv"

# Get directory of the folder
# this file resides in
path: str = dirname(__file__)

# Change current working directory
# to that of the python file
chdir(path)

# Open file and read content to dictionary
#
# Using python's content manager protocol
# So that we can rest assured that the file
# is handled cleanly
#
# Adding parameter `newline=""` to `open()`
# as suggested by documentation of module `csv`
with open(FILENAME, newline="") as file:
    # Retrieve the data
    data = Unidentified(file)
    artist_dict = data.artist_songs()

# Retrieve top artist information
#
# Passing `artists_dict` instead of letting the function
# so that we don't need to call `Unknown.artist_songs()`
# again and waste compute time
artist_top = data.top_artist(artist_dict)

# TASK 01: Find top artist

print(f"Top artist: {artist_top[0]}")
print(f"Songs: {artist_top[1]}")
print()

# TASK 02: Print songs by "Sophia Hall"

name = "Sophia Hall"
print(f"Artist: {name}")
print(f"Songs: {artist_dict[name]}")
print()

# TASK 03: Find words in song names that
# occur at least 15 times in total

# Initialize a dictionary to store word occurrence count
song_word_count_dict: dict[str, int] = {}
# Get a tuple of all names
song_names_list_tuple: tuple[list[str], ...] = tuple(artist_dict.values())
# Iterate through lists in the tuple
for song_names_list in song_names_list_tuple:
    # Iterate through the names in the list
    for song_names in song_names_list:
        # Iterate through the words in the name
        for word in song_names.split(" "):
            # Initialize counter for word if not already initialized
            if word.capitalize() not in song_word_count_dict:
                song_word_count_dict[word.capitalize()] = 0
            # Increment counter for word
            song_word_count_dict[word.capitalize()] += 1
# Convert dict to list for ease of processing
song_word_count_list: list[tuple[str, int]] = list(song_word_count_dict.items())
# Sort them in descending order
song_word_count_list.sort(
    key=lambda item: item[1],  # So that we sort in order of count and not word
    reverse=True,  # We want it to be descending, hence reverse order
)
# Output header
print("Words that occurred more than 15 times: ")
# Output words only if they occurred >=15 times
for index, word in enumerate(song_word_count_list):
    # We can break out of the loop if count is less than 15
    # We don't need to iterate further if this condition's met
    if word[1] < 15:
        break
    # If the loop's still going, print it out
    print(f"{index+1}] ({word[1]}) {word[0]}")
print()

# TASK 04: Print songs by "The unidentified"

name = "The unidentified"
print(f"Artist: {name}")
print(f"Songs: {artist_dict[name]}")
print()

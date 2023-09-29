import csv
import os

# Store expected name of CSV file as a constant
FILENAME: str = "Anomalous - Anomalous.csv"

# Get directory of the folder
# this file resides in
path: str = os.path.dirname(__file__)

# Change current working directory
# to that of the python file
os.chdir(path)


def extract_dict(filename: str) -> dict[str, list[str]]:
    """Extracts artists and their songs into a structured dictionary

    ### Args:
        `filename` (`str`):
            The name of the CSV file to open. CSV must
            store file in the format `key, artist_name`

    ### Returns:
        `dict[str, list[str]]`:
            Keys are artists, and key values are a list of their songs
    """

    # Open the given file using the content manager protocol
    with open(filename, newline="") as file:
        # Retrieve CSV data from file
        # TODO: Move data retrieval to class attribute
        data_raw = csv.DictReader(file)
        
        # Initialize variable to hold clean data
        data_clean: dict[str, list[str]] = {}
        
        # Iterate through every row of data
        for row in data_raw:
            # Store artist name in a variable
            artist: str = row["artist_name"]
            
            # If it's not already there, initialize a key
            # that goes by the artist's name with a blank list
            if not data_clean.get(artist, 0):
                data_clean[artist] = []
            
            # Append song name to list
            data_clean[artist].append(row["key"])
        
        # Return 
        return data_clean


print(extract_dict(FILENAME))

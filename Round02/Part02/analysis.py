from csv import DictReader
from io import TextIOWrapper


class Unidentified:
    """Making this a class yet again so that I don't have to
    keep the file open for longer than we need to, and so that
    we can granularly handle file initialization"""

    def __init__(self, file: TextIOWrapper) -> None:
        """Initialize data for deciphering data from
        the unknown file given to us by `The Unidentified`

        ### Args:
            `file` (`str`):
                The name of the file we need to open

        ### Raises:
            `TypeError`:
                Raised only if file's name does not
                end in `.CSV` (case insensitive)
                - we then assume that the file is
                not a valid CSV file

        ### Attributes:
            `data` (`csv.DictReader`):
                Contains a `DictReader` generator object which
                holds all of CSV data in an optimized manner
        """

        # First, make sure that the file's actually
        # a CSV and nothing else
        #
        # We just check the file extension for this
        # and convert the slice to lowercase
        # to account for unconventional file naming
        if file.name[-4:].lower() != ".csv":
            raise TypeError(
                "Invalid file type - make sure the file name ends in `.csv`"
            )

        # Extract raw data from CSV file
        self.__data = DictReader(file)

    def artist_songs(self) -> dict[str, list[str]]:
        """Extracts artists and their songs into a structured dictionary

        ### Returns:
            `dict[str, list[str]]`:
                Keys are artists, and key values are a list of their songs
        """

        # Initialize variable to hold clean data
        data_clean: dict[str, list[str]] = {}

        # Iterate through every row of data
        for row in self.__data:
            # Store artist name in a variable
            artist: str = row["artist_name"]

            # If it's not already there, initialize a key
            # that goes by the artist's name with a blank list
            if artist not in data_clean:
                data_clean[artist] = []

            # Append song name to list
            data_clean[artist].append(row["key"])

        # Return processed data
        #
        # We're returning a dictionary here - while it would've been
        # absolutely fine to return a list (that would've been easier
        # to work with too), considering how large our dataset can get,
        # and how we can refer to a particular artist here by key value
        # instead of having to implement a searching algorithm, the
        # performance and functional aspects of dictionaries can be
        # utilized effectively in the long run
        return data_clean

    def top_artist(
        self, artist_songs: dict[str, list[str]] | None = None
    ) -> list[str | list[str]]:
        """Find the artist with the most amount of songs

        ### Args:
            artist_songs (`dict[str, list[str]]` | `None`, optional):
                You can pass a dictionary that contains artists
                and their songs as a key-value pair in a dictionary,
                where the value contains a list of their songs. If
                value for this argument is not provided, then
                `self.artist_songs()` will be run to retrieve the data

        ### Returns:
            `list[str | list[str]]`:
                A list with a two values. The first element of the list
                is a string containing the artist's name, and the latter
                element is a list of the songs published by the artist
        """

        # Retrieve dictionary of all artists and
        # their songs if user did not provide any
        if artist_songs == None:
            artist_songs = self.artist_songs()

        # Find the artist with the most songs
        top_artist = max(
            # Iterate through the keys of `artist songs`
            artist_songs,
            # Consider largest based on the length of list stored as value
            key=lambda artist: len(artist_songs[artist]),
        )

        # Return a list with solely
        # the top artist and their songs
        return [top_artist, artist_songs[top_artist]]

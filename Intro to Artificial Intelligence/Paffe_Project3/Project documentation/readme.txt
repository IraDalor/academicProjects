This program is easily operated by assembling the python source code in the environment of your choice to run the program.

Temporary files will be created automatically, while any file that you wish to use must be a .txt file contained in the same
directory as the source code.

CLASP MUST BE PRESENT IN THE SOURCES DIRECTORY FOR THIS PROGRAM TO FUNCTION!

When the program is first opened all fields will be blank. Simply enter .txt filenames of your choice and click "Show Results",
simple as that. If manual entry is preferable simply type (or copy paste) it into the appropriate fields in the below format
and click "Show Results"

Required formats for .txt files and manual entry:

Attributes:
appetizer: soup, salad
entree: beef, fish
drink: beer, wine
dissert: cake, ice-cream

Hard Constraints:
NOT soup OR NOT beer
NOT soup OR NOT wine

Preferences:
fish AND wine, 10
wine OR cake, 6
beer OR beer AND beef OR NOT soup, 7

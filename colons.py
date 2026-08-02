from errors import InvalidColonsFile
import sys
from interpreter import interpret_file

if not len(sys.argv) == 2:
    raise ValueError(
        "No file was passed, aborting..."
    )
file = sys.argv[1]

if not file.endswith(".colons"):
    raise InvalidColonsFile(
        f"File {file} is not a colond file."
    )

interpret_file(file)
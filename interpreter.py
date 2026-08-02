from errors import ColonsSyntaxError

def interpret_file(file: str):
    end = ""
    with open(file, 'r') as f:
        lines = f.read().split("\n")

    for i, line in enumerate(lines, start=1):
        if not all(char == ":" for char in line) and not line.endswith(";"):
            raise ColonsSyntaxError(
                f'Line {i}; "{line}", all characters in line must be colons and end withe a semicolon.'
            )

        if ":" in line and line.endswith(";"):
            colons = line.count(":")
            char = chr(colons)

            end += char

        if not line.endswith(
            ";"
        ) and line:
            raise ColonsSyntaxError(
                f'Line {i}; "{line}": Line does not end with a semicolon (;).'
            )

        if line.startswith(";;"):
            print(end)
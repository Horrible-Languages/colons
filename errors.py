class ColonsError(Exception):
    pass

class ColonsSyntaxError(ColonsError):
    pass

class ColonsFileError(Exception):
    pass

class InvalidColonsFile(ColonsFileError):
    pass
class FileNotPassedError(ColonsFileError):
    pass
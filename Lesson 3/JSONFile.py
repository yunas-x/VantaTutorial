from File import File


class JSONFile(File):

    def __init__(self, file_name: str) -> None:
        if not isinstance(file_name, str):
            raise TypeError("Only strings are allowed")
        if not file_name.endswith(".json"):
            raise ValueError("Wrong extension")
        
        super().__init__(file_name)
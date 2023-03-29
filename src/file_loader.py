from ansi_colors import AnsiColors

class FileLoader():
    def __init__(self, path: str, is_encrypted: bool) -> None:
        self.path = path
        self.is_encrypted = is_encrypted

    def get_printable_message(self) -> str:
        if self.is_encrypted is True:
            return f'Loading encrypted content from {self.path}'
        else:
            return f'Loading content from {self.path}'

    def get_contents(self):
        if self.is_encrypted:
            print(AnsiColors.WARNING, end = "")
        else:
            print(AnsiColors.OKGREEN, end = "")
        message = self.get_printable_message()
        print(message)
        lines = []
        with open(self.path, 'r') as my_file:
            for i in my_file:
                line = i.strip()
                lines.append(line)
        print(AnsiColors.ENDC, end = "")
        return lines
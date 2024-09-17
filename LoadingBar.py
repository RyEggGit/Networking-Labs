import sys

class LoadingBar:
    def __init__(self, total: float, length: int = 50, char: str = '█'):
        self.total = total
        self.length = length
        self.char = char
        self.progress = 0

    def update(self):
        percent = (self.progress / self.total)
        filled_length = int(self.length * percent)
        bar = self.char * filled_length + '-' * (self.length - filled_length)
        sys.stdout.write(f'\r[{bar}] {int(percent * 100)}%')
        sys.stdout.flush()

    def set_progress(self, progress: float):
        self.progress = progress
        self.update()

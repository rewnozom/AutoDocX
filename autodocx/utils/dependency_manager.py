# src/utils/dependency_manager.py
from ..scanners.dependency_tracker import DependencyTracker
from ..helpers.file_operations import read_file


class DependencyManager:
    """
    Hanterar beroendeanalys för filer.
    """

    def __init__(self):
        self.tracker = DependencyTracker()

    def get_dependencies(self, file_path):
        content = read_file(file_path)
        if content:
            return self.tracker.track(content)
        return []


if __name__ == "__main__":
    manager = DependencyManager()
    deps = manager.get_dependencies(__file__)
    print("Beroenden:", deps)

# src/scanners/dependency_tracker.py
import re

class DependencyTracker:
    """
    Identifierar beroenden mellan moduler genom att analysera filinnehåll.
    Denna placeholder använder ett enkelt regex för att hitta Python-importsatsningar.
    """

    IMPORT_REGEX = r"^\s*(?:import|from)\s+([\w\.]+)"

    def track(self, file_content):
        """
        Returnerar en lista med identifierade beroenden i filinnehållet.
        """
        dependencies = set()
        for line in file_content.splitlines():
            match = re.match(self.IMPORT_REGEX, line)
            if match:
                dependencies.add(match.group(1))
        return list(dependencies)

if __name__ == "__main__":
    sample_content = """
    import os
    import sys
    from collections import defaultdict
    # from random import randint
    """
    tracker = DependencyTracker()
    deps = tracker.track(sample_content)
    print("Identifierade beroenden:", deps)

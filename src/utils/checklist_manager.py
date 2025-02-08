class ChecklistManager:
    """
    Hanterar vilka filer/uppgifter som är färdiga.

    Funktionalitet:
      - add_task(task_name): Lägg till en ny uppgift i checklistan.
      - mark_done(task_name): Markerar en uppgift som färdig.
      - all_done(): Returnerar True om alla uppgifter är klara.
      - report(): Returnerar checklistans innehåll.
    """

    def __init__(self):
        self.checklist = {}

    def add_task(self, task_name):
        self.checklist[task_name] = False
        print(f"[CHECKLIST] Uppgift '{{task_name}}' tillagd.")

    def mark_done(self, task_name):
        if task_name in self.checklist:
            self.checklist[task_name] = True
            print(f"[CHECKLIST] Uppgift '{{task_name}}' markerad som klar.")
        else:
            print(f"[ERROR] Uppgift '{{task_name}}' hittades inte i checklistan.")

    def all_done(self):
        return all(status for status in self.checklist.values())

    def report(self):
        return self.checklist


if __name__ == "__main__":
    manager = ChecklistManager()
    manager.add_task("Analysera fil A")
    manager.add_task("Generera docs för fil A")
    manager.mark_done("Analysera fil A")
    print("Checklist rapport:", manager.report())

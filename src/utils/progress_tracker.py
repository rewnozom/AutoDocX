# src/utils/progress_tracker.py
import time

class ProgressTracker:
    """
    Spårar processens framsteg.

    Metoder:
        start(task_name): Startar en ny uppgift.
        update(task_name, progress): Uppdaterar uppgiftens progress.
        finish(task_name): Markerar uppgiften som klar.
        report(): Returnerar en sammanfattning av all progress.
    """
    def __init__(self):
        self.tasks = {}

    def start(self, task_name):
        self.tasks[task_name] = {"start": time.time(), "progress": 0, "finished": False}
        print(f"[START] '{task_name}' har startat.")

    def update(self, task_name, progress):
        if task_name in self.tasks:
            self.tasks[task_name]["progress"] = progress
            print(f"[UPDATE] '{task_name}': progress = {progress}%")
        else:
            print(f"[ERROR] Uppgift '{task_name}' hittades inte.")

    def finish(self, task_name):
        if task_name in self.tasks:
            self.tasks[task_name]["finished"] = True
            elapsed = time.time() - self.tasks[task_name]["start"]
            print(f"[FINISH] '{task_name}' klar. Tidsåtgång: {elapsed:.2f} sekunder.")
        else:
            print(f"[ERROR] Uppgift '{task_name}' hittades inte.")

    def report(self):
        return self.tasks

if __name__ == "__main__":
    tracker = ProgressTracker()
    tracker.start("TestTask")
    tracker.update("TestTask", 50)
    tracker.finish("TestTask")
    print("Rapport:", tracker.report())

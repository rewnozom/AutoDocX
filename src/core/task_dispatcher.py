from ..helpers.logger import Logger
from ..ai.prompt_engine import PromptEngine
from ..generators.doc_generator import DocGenerator


class TaskDispatcher:
    def __init__(self):
        self.prompt_engine = PromptEngine()
        self.doc_generator = DocGenerator()
        self.tasks = []

    def create_task(self, file_path, prompt_variant):
        Logger.log(f"Skapar uppgift för fil: {file_path}", "INFO")
        prompt = self.prompt_engine.get_prompt("developer", prompt_variant)
        task = {"file_path": file_path, "prompt": prompt}
        self.tasks.append(task)
        Logger.log(f"Uppgift skapad för: {file_path}", "SUCCESS")

    def execute_tasks(self):
        Logger.log("Utför alla uppgifter...", "INFO")
        for task in self.tasks:
            Logger.log(
                f"Bearbetar uppgift för {task['file_path']} med prompt: {task['prompt'][:30]}...",
                "INFO",
            )
            # Placeholder: Här anropas AI-moduler och dokumentationsgenerering för varje fil.
        Logger.log("Alla uppgifter bearbetade.", "SUCCESS")

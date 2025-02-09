# src/core/task_dispatcher.py
import asyncio
from ..helpers.logger import Logger
from ..ai.prompt_engine import PromptEngine
from ..generators.doc_generator import DocGenerator
from ..ai.text_generator import TextGenerator


class TaskDispatcher:
    def __init__(self):
        self.prompt_engine = PromptEngine()
        self.text_generator = TextGenerator()
        self.tasks = []
        # Skapa en DocGenerator för varje dokumentationstyp
        self.doc_generators = {
            "developer": DocGenerator(),
            "user": DocGenerator(),
            "ai": DocGenerator(),
        }

    def create_tasks_for_file(self, file_path, prompt_variant):
        """Skapar en task per dokumentationstyp för en given fil."""
        for doc_type in ["developer", "user", "ai"]:
            prompt = self.prompt_engine.get_prompt(doc_type, prompt_variant)
            task = {
                "file_path": file_path,
                "doc_type": doc_type,
                "prompt": prompt,
                "response": None,
            }
            self.tasks.append(task)
            Logger.log(
                f"Uppgift skapad för {doc_type} dokumentation: {file_path}", "SUCCESS"
            )

    async def execute_tasks(self):
        Logger.log("Utför alla uppgifter...", "INFO")

        async def process_task(task):
            Logger.log(
                f"Bearbetar {task['doc_type']} uppgift för {task['file_path']}...",
                "INFO",
            )
            # Anropa LLM‑anropet och vänta på svar (simulerat asynkront)
            response = await self.text_generator.generate_text(task["prompt"])
            task["response"] = response
            # Lägg till dokumentationen i rätt DocGenerator
            self.doc_generators[task["doc_type"]].add_document(
                task["file_path"], response
            )
            Logger.log(
                f"Uppgift klar för {task['doc_type']} dokumentation: {task['file_path']}",
                "SUCCESS",
            )

        # Kör alla tasks parallellt
        await asyncio.gather(*(process_task(task) for task in self.tasks))
        Logger.log("Alla uppgifter bearbetade.", "SUCCESS")

    def run_all_tasks(self):
        asyncio.run(self.execute_tasks())

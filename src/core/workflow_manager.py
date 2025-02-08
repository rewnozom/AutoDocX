# src/core/workflow_manager.py
import os
from ..helpers.logger import Logger
from .process_controller import ProcessController
from .task_dispatcher import TaskDispatcher
from ..utils.progress_tracker import ProgressTracker
from ..utils.checklist_manager import ChecklistManager

class WorkflowManager:
    def __init__(self, base_path, update=False, review=False, prompt_variant="full"):
        self.base_path = base_path
        self.update = update
        self.review = review
        self.prompt_variant = prompt_variant
        self.process_controller = ProcessController()
        self.task_dispatcher = TaskDispatcher()
        self.progress_tracker = ProgressTracker()
        self.checklist_manager = ChecklistManager()

    def run(self):
        Logger.log("Workflow startar...", "INFO")
        files = self.process_controller.scan_codebase(self.base_path)
        Logger.log(f"Antal filer skannade: {len(files)}", "INFO")
        
        # Starta en övergripande uppgift med ProgressTracker
        self.progress_tracker.start("Total files")
        
        for file in files:
            self.checklist_manager.add_task(file)
            self.task_dispatcher.create_tasks_for_file(file, self.prompt_variant)
        
        # Kör alla tasks (använder asynkrona LLM-anrop)
        self.task_dispatcher.run_all_tasks()

        # Markera alla filer som färdigbehandlade
        for file in files:
            self.checklist_manager.mark_done(file)
        self.progress_tracker.update("Total files", 100)
        self.progress_tracker.finish("Total files")

        # Aggregera och spara dokumentationen per typ
        self.aggregate_documents()

        Logger.log("Workflow avslutat.", "SUCCESS")

    def aggregate_documents(self):
        # Definiera utgångssökvägar – dessa kan justeras via config
        output_paths = {
            "developer": os.path.join("docs", "Developer-Docs", "aggregate.md"),
            "user": os.path.join("docs", "User-Docs", "aggregate.md"),
            "ai": os.path.join("docs", "AI-Docs", "aggregate.md")
        }
        # Importera syntax-checkern
        from ..validators.syntax_checker import check_syntax

        for doc_type, output_path in output_paths.items():
            aggregated_content = self.task_dispatcher.doc_generators[doc_type].generate_aggregate(output_path)
            Logger.log(f"Aggregerad {doc_type} dokumentation sparad i {output_path}", "SUCCESS")
            # Validera syntaxen i den aggregerade dokumentationen
            valid, message = check_syntax(output_path)
            if not valid:
                Logger.log(f"Syntaxfel i {doc_type} dokumentation: {message}", "ERROR")
            else:
                Logger.log(f"Syntaxcheck OK för {doc_type} dokumentation.", "SUCCESS")

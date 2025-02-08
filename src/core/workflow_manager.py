from ..helpers.logger import Logger
from .process_controller import ProcessController
from .task_dispatcher import TaskDispatcher

class WorkflowManager:
    def __init__(self, base_path, update=False, review=False, prompt_variant="full"):
        self.base_path = base_path
        self.update = update
        self.review = review
        self.prompt_variant = prompt_variant
        self.process_controller = ProcessController()
        self.task_dispatcher = TaskDispatcher()
    
    def run(self):
        Logger.log("Workflow startar...", "INFO")
        files = self.process_controller.scan_codebase(self.base_path)
        Logger.log(f"Antal filer skannade: {len(files)}", "INFO")
        for file in files:
            self.task_dispatcher.create_task(file, self.prompt_variant)
        self.task_dispatcher.execute_tasks()
        Logger.log("Workflow avslutat.", "SUCCESS")

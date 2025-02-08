import sys
import argparse
from .initialize import initialize_system
from .workflow_manager import WorkflowManager
from ..helpers.logger import Logger

def main():
    parser = argparse.ArgumentParser(description="AutoDocX - Automatiserad Dokumentationsgenerator")
    parser.add_argument("path", nargs="?", default=None, help="Sökväg till kodbasen (default: ./Workspace/)")
    parser.add_argument("-update", action="store_true", help="Uppdatera dokumentation")
    parser.add_argument("-review", action="store_true", help="Granska dokumentation")
    parser.add_argument("-full", action="store_true", help="Använd fullständiga promptar")
    parser.add_argument("-sum", action="store_true", help="Använd sammanfattande promptar")
    parser.add_argument("-short", action="store_true", help="Använd kortfattade promptar")
    args = parser.parse_args()
    
    base_path = args.path if args.path else "./Workspace/"
    Logger.log(f"Startar AutoDocX med sökväg: {base_path}", "INFO")
    
    initialize_system()
    
    prompt_variant = "full" if args.full else ("sum" if args.sum else ("short" if args.short else "full"))
    workflow_manager = WorkflowManager(base_path, update=args.update, review=args.review, prompt_variant=prompt_variant)
    workflow_manager.run()

if __name__ == "__main__":
    main()

# main.py
import argparse
import os
from autodocx.core.initialize import initialize_system
from autodocx.core.workflow_manager import WorkflowManager
from autodocx.helpers.logger import Logger

def main(args=None):
    # Om inget argumentobjekt skickats med (t.ex. vid direkt anrop) görs parsing lokalt.
    if args is None:
        parser = argparse.ArgumentParser(
            description="""
            AutoDocX - Automatiserad Dokumentationsgenerator
            -----------------------------------------------
            AutoDocX genererar dokumentation för din kod automatiskt genom att analysera kodstrukturen och 
            använda en LLM (Large Language Model) för att skapa både utvecklardokumentation och användarguider.

            Exempel på användning:
              - Generera fullständig dokumentation:
                python main.py ./ --update --full

              - Generera kortfattad dokumentation:
                python main.py ./ --update --short

              - Granska existerande dokumentation:
                python main.py ./ --review
            """,
            formatter_class=argparse.RawTextHelpFormatter,
        )

        parser.add_argument(
            "path",
            nargs="?",
            default="./Workspace/",
            help="Sökväg till kodbasen som ska dokumenteras (default: ./Workspace/).",
        )
        parser.add_argument(
            "--update",
            action="store_true",
            help="Skapa eller uppdatera dokumentationen för kodbasen.",
        )
        parser.add_argument(
            "--review",
            action="store_true",
            help="Granska existerande dokumentation för att identifiera förbättringar.",
        )
        parser.add_argument(
            "--full",
            action="store_true",
            help="Använd fullständiga, detaljerade promptar för att generera omfattande dokumentation.",
        )
        parser.add_argument(
            "--sum",
            action="store_true",
            help="Använd sammanfattande promptar för att generera kortare dokumentation.",
        )
        parser.add_argument(
            "--short",
            action="store_true",
            help="Använd en ultrakort version av dokumentationen, endast med de viktigaste detaljerna.",
        )

        args = parser.parse_args()

    # Use the provided path or default to "./Workspace/"
    base_path = args.path
    Logger.log(f"Startar AutoDocX med sökväg: {base_path}", "INFO")

    initialize_system()

    prompt_variant = (
        "full"
        if args.full
        else ("sum" if args.sum else ("short" if args.short else "full"))
    )
    workflow_manager = WorkflowManager(
        base_path, update=args.update, review=args.review, prompt_variant=prompt_variant
    )
    workflow_manager.run()


if __name__ == "__main__":
    main()
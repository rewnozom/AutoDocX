import argparse
from argparse import ArgumentParser
from ..core.main import main as core_main
import os


def main():
    parser = ArgumentParser(
        description="""
        AutoDocX CLI - Automatiserad dokumentationsgenerator
        ---------------------------------------------------
        Använd detta CLI-verktyg för att generera, uppdatera och granska dokumentation 
        direkt från kommandoraden.

        📌 Path (sökväg):
          - "." (punkt) = Skannar hela projektet i ./Workspace/
          - Du kan också ange en specifik katalog, t.ex.:
            docx "C:\\User\\ExampleProject"

        📌 Exempel på användning:
          - Skanna hela standardkatalogen:
            docx . --update

          - Skanna en specifik katalog:
            docx "C:\\User\\ExampleProject" --update --sum

        Exempel på användning:
          - Uppdatera dokumentationen:
            docx ./ --update

          - Generera en detaljerad version:
            docx ./ --update --full

          - Generera en sammanfattad version:
            docx ./ --update --sum

          - Generera en ultrakort version:
            docx ./ --update --short

          - Granska existerande dokumentation:
            docx ./ --review
        """,
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.add_argument(
        "path",
        nargs="?",
        default="./Workspace/",
        help="Sökväg till kodbasen som ska dokumenteras (default: ./Workspace/).",
    )
    parser.add_argument("--update", action="store_true", help="Skapa eller uppdatera dokumentationen.")
    parser.add_argument("--review", action="store_true", help="Granska existerande dokumentation.")
    parser.add_argument("--full", action="store_true", help="Använd fullständiga promptar.")
    parser.add_argument("--sum", action="store_true", help="Använd sammanfattande promptar.")
    parser.add_argument("--short", action="store_true", help="Använd kortfattade promptar.")
    parser.add_argument("-v", "--verbose", action="store_true", help="Visa detaljerad debug-information.")

    args = parser.parse_args()

    if args.verbose:
        print(f"DEBUG: Raw path argument: {args.path}")
        print(f"DEBUG: Absolute path: {os.path.abspath(args.path)}")
        print(f"DEBUG: Path exists: {os.path.exists(args.path)}")

    # Normalisera sökvägen och gör den absolut
    args.path = os.path.abspath(os.path.normpath(args.path))

    if args.verbose:
        print(f"DEBUG: Normalized path: {args.path}")

    # Vidarebefordra de tolkade argumenten till core_main
    core_main(args)


if __name__ == "__main__":
    main()
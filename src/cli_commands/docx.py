# src/cli_commands/docx.py
from argparse import ArgumentParser
from ..core.main import main as core_main
import os


def main():
    parser = ArgumentParser(
        description="AutoDocX CLI - Automatiserad dokumentationsgenerator"
    )
    parser.add_argument(
        "path",
        nargs="?",
        default="./Workspace/",
        help="Sökväg till kodbasen (default: ./Workspace/)",
    )
    parser.add_argument("-update", action="store_true", help="Uppdatera dokumentation")
    parser.add_argument("-review", action="store_true", help="Granska dokumentation")
    parser.add_argument(
        "-full", action="store_true", help="Använd fullständiga promptar"
    )
    parser.add_argument(
        "-sum", action="store_true", help="Använd sammanfattande promptar"
    )
    parser.add_argument(
        "-short", action="store_true", help="Använd kortfattade promptar"
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Visa detaljerad debug-information"
    )
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

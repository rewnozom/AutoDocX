import sys
from argparse import ArgumentParser
from ..core.main import main as core_main


def main():
    parser = ArgumentParser(
        description="AutoDocX CLI - Automatiserad dokumentationsgenerator"
    )
    parser.add_argument(
        "path",
        nargs="?",
        default=None,
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

    args = parser.parse_args()
    sys.argv = sys.argv[1:]  # ta bort kommandots namn
    core_main()


if __name__ == "__main__":
    main()

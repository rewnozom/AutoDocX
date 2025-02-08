import os


def create_file(file_path, content):
    """Skapar nödvändig mappstruktur och skriver innehållet till filen."""
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[CREATED] {file_path}")


def main():
    # --- Skapa mappen scripts/ och dess filer ---
    scripts_dir = "scripts"
    scripts_files = {
        os.path.join(
            scripts_dir, "setup_env.py"
        ): '''#!/usr/bin/env python3
"""
setup_env.py - Script för att sätta upp utvecklingsmiljön för AutoDocX.
Exempel:
    python scripts/setup_env.py
"""
import os
import subprocess

def main():
    print("Sätter upp utvecklingsmiljön för AutoDocX...")
    # Exempel: Installera beroenden
    subprocess.run(["pip", "install", "-r", "requirements.txt"])
    print("Utvecklingsmiljön är nu inställd.")

if __name__ == "__main__":
    main()
''',
        os.path.join(
            scripts_dir, "run_tests.py"
        ): '''#!/usr/bin/env python3
"""
run_tests.py - Kör enhetstester för AutoDocX.
"""
import subprocess

def main():
    print("Kör tester med pytest...")
    subprocess.run(["pytest", "--maxfail=1", "--disable-warnings", "-q"])

if __name__ == "__main__":
    main()
''',
        os.path.join(
            scripts_dir, "deploy.py"
        ): '''#!/usr/bin/env python3
"""
deploy.py - Script för att distribuera AutoDocX.
Exempel:
    python scripts/deploy.py
"""
import subprocess

def main():
    print("Distribuerar AutoDocX...")
    # Placeholder: Lägg till distributionslogik här (t.ex. bygga distributionspaket med setup.py)
    subprocess.run(["python", "setup.py", "sdist"])
    print("Distribueringen är klar.")

if __name__ == "__main__":
    main()
''',
    }

    for path, content in scripts_files.items():
        create_file(path, content)

    # --- Skapa root-filer ---
    root_files = {
        "requirements.txt": """# requirements.txt
pyyaml
python-dotenv
pytest
flake8
""",
        "setup.py": """from setuptools import setup, find_packages

setup(
    name="AutoDocX",
    version="0.1.0",
    description="Automatiserad Dokumentationsgenerator",
    author="Ditt Namn",
    packages=find_packages(),
    install_requires=[
        "pyyaml",
        "python-dotenv",
    ],
    entry_points={
        "console_scripts": [
            "docx=src.cli_commands.docx:main",
        ],
    },
)
""",
        "README.md": """# AutoDocX – Automatiserad Dokumentationsgenerator

AutoDocX är ett fullständigt automatiserat verktyg för att generera dokumentation för din kodbas. 
Verktyget skannar igenom alla mappar och filer i angiven sökväg (standard: ./Workspace/) och genererar tre typer av dokumentation:
- **User-Docs:** Användarvänliga sammanfattningar.
- **Developer-Docs:** Teknisk och detaljerad dokumentation.
- **AI-Docs:** Optimerade sammanfattningar för LLM-chat (för att spara tokens).

## Installation

Installera beroenden:
```bash
pip install -r requirements.txt
```

## Användning

Kör AutoDocX med:
```bash
python -m src.core.main
```
eller via CLI:
```bash
docx "./" -update -full
```

## CI/CD

Se .github/workflows/auto-docs.yml för CI/CD-pipeline-konfiguration.

## Övrigt

AutoDocX använder LM Studio (lokal LLM) som primär leverantör. 
Stöd för alternativa LLM-leverantörer finns i `model/llm_models.py`.

Happy documenting!
""",
        ".gitignore": """# .gitignore

# Bytekompilat
__pycache__/
*.py[cod]
*.egg-info/

# Miljöfiler
.env

# Distribution
dist/
build/
""",
        ".env": """# .env
# Exempel på miljövariabler för AutoDocX
ANTHROPIC_API_KEY=din_anthropic_api_key
OPENAI_API_KEY=din_openai_api_key
# Lägg till övriga API-nycklar och miljövariabler här.
""",
        "config.yaml": """# config.yaml - Huvudinställningar för AutoDocX
default_llm: lmstudio
llm:
  lmstudio:
    context_tokens: 60000
    temperature: 0.7
    base_url: "http://localhost:1234/v1"
  openai:
    context_tokens: 4000
    temperature: 0.8
    base_url: "https://api.openai.com/v1"
default_path: "./Workspace/"   # Standard sökväg om inget annat anges
ignore_paths:                  # Lista på mappar att ignorera under skanning
  - "node_modules"
  - ".git"
  - "venv"
prompt_templates:
  developer:
    full: "Developer-Full-Prompt-Template"
    sum: "Developer-Summary-Prompt-Template"
    short: "Developer-Short-Prompt-Template"
  user:
    full: "User-Full-Prompt-Template"
    sum: "User-Summary-Prompt-Template"
    short: "User-Short-Prompt-Template"
  ai:
    full: "AI-Full-Prompt-Template"
    sum: "AI-Summary-Prompt-Template"
    short: "AI-Short-Prompt-Template"
""",
    }

    for path, content in root_files.items():
        create_file(path, content)


if __name__ == "__main__":
    main()

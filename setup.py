import os
from setuptools import setup, find_packages
from setuptools.command.install import install

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Core dependencies required for the application
INSTALL_REQUIRES = [
    "pyyaml>=6.0.1",
    "python-dotenv>=1.0.0",
    "requests>=2.31.0",
    "aiohttp>=3.9.1",
    # LLM dependencies
    "anthropic>=0.18.1",
    "openai>=1.12.0",
    "langchain-anthropic>=0.0.4",
    "langchain-openai>=0.0.2",
    "langchain-groq>=0.0.1",
    "pydantic>=2.6.1",
]

# Development dependencies
DEV_REQUIRES = [
    "pytest>=7.4.0",
    "flake8>=6.1.0",
    "black>=23.9.1",
    "isort>=5.12.0",
    "autoflake>=2.2.0",
    "mypy>=1.8.0",
    "types-PyYAML>=6.0.12.12",
    "types-requests>=2.31.0.20240106"
]

class CustomInstallCommand(install):
    """Custom install command för att skapa nödvändiga mappar och en .env-fil om den inte finns."""

    def run(self):
        install.run(self)  # Kör standardinstallationen

        # Skapa nödvändiga mappar om de inte finns
        directories = [
            "Workspace",
            "docs/User-Docs",
            "docs/Developer-Docs",
            "docs/AI-Docs",
            "logs",
        ]
        for directory in directories:
            if not os.path.exists(directory):
                os.makedirs(directory)
                print(f"[SETUP] Skapade mapp: {directory}")

        # Skapa .env-fil om den inte redan finns
        env_path = ".env"
        if not os.path.exists(env_path):
            with open(env_path, "w", encoding="utf-8") as env_file:
                env_file.write(
                    "# =======================================\n"
                    "#  .env - Miljövariabler för AutoDocX     \n"
                    "# =======================================\n\n"
                    "# API-nycklar\n"
                    "ANTHROPIC_API_KEY=\n"
                    "OPENAI_API_KEY=\n"
                    "AZURE_OPENAI_API_KEY=\n"
                    "GROQ_API_KEY=\n\n"
                    "# Vilken provider som ska vara standard\n"
                    "DEFAULT_MODEL=lmstudio\n\n"
                    "# Standard-sökväg till projektets kod\n"
                    "DEFAULT_PATH=./Workspace/\n\n"
                    "# Ignorerade sökvägar (kommaseparerad lista)\n"
                    "IGNORE_PATHS=node_modules,.git,venv\n\n"
                    "# Gemensamma LLM-parametrar\n"
                    "TEMPERATURE=0.7\n"
                    "MAX_TOKENS=60000\n"
                    "TOP_P=0.9\n\n"
                    "# LM Studio-specifika inställningar\n"
                    "LM_STUDIO_BASE_URL=http://localhost:1234/v1\n"
                    "LM_STUDIO_MODEL=model-identifier\n\n"
                    "# Anthropic inställningar\n"
                    "CLAUDE_HAIKU_MODEL=claude-3-haiku-20240307\n"
                    "CLAUDE_SONNET_MODEL=claude-3-sonnet-20240229\n"
                    "CLAUDE_OPUS_MODEL=claude-3-opus-20240229\n\n"
                    "# OpenAI inställningar\n"
                    "GPT4_MODEL=gpt-4\n"
                    "GPT35_MODEL=gpt-3.5-turbo\n\n"
                    "# Azure OpenAI inställningar\n"
                    "AZURE_BASE_URL=https://your-resource.openai.azure.com\n"
                    "AZURE_API_VERSION=2024-02-15-preview\n"
                    "AZURE_GPT4_MODEL=gpt-4\n"
                    "AZURE_GPT35_MODEL=gpt-3.5-turbo\n\n"
                    "# Groq inställningar\n"
                    "GROQ_MODEL=mixtral-8x7b-32768\n"
                )
                print("[SETUP] Skapade en ny .env-fil med standardinställningar.")

setup(
    name="AutoDocX",
    version="0.2.6",
    description="Automatiserad Dokumentationsgenerator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Tobias Raanaes",
    url="https://github.com/rewnozom/AutoDocX",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=INSTALL_REQUIRES,
    extras_require={
        "dev": DEV_REQUIRES,
    },
    python_requires=">=3.10",
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "docx=src.cli_commands.docx:main",
        ],
    },
    cmdclass={
        "install": CustomInstallCommand,
    },
    include_package_data=True,
)
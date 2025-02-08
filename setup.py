import os
from setuptools import setup, find_packages
from setuptools.command.install import install

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

class CustomInstallCommand(install):
    """Custom install command för att skapa nödvändiga mappar vid installation."""
    def run(self):
        install.run(self)  # Kör standardinstallationen

        # Skapa nödvändiga mappar om de inte finns
        directories = [
            "Workspace",
            "docs/User-Docs",
            "docs/Developer-Docs",
            "docs/AI-Docs",
            "logs"
        ]

        for directory in directories:
            if not os.path.exists(directory):
                os.makedirs(directory)
                print(f"[SETUP] Skapade mapp: {directory}")

setup(
    name="AutoDocX",
    version="0.2.3",
    description="Automatiserad Dokumentationsgenerator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Tobias Raanaes",
    url="https://github.com/rewnozom/AutoDocX",
    packages=find_packages(),
    install_requires=[
        "pyyaml",
        "python-dotenv",
        "pytest",
        "flake8",
        "requests",
        "aiohttp",
    ],
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
    cmdclass={  # Kopplar `CustomInstallCommand` till `install`
        "install": CustomInstallCommand,
    },
)

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="AutoDocX",
    version="0.2.3",
    description="Automatiserad Dokumentationsgenerator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Tobias Raanaes",
    url="https://github.com/rewnozom/AutoDocX",  # Uppdatera om repo finns
    packages=find_packages(),
    install_requires=[
        "pyyaml",
        "python-dotenv",
        "pytest",
        "flake8",
        "requests",
        "aiohttp",
    ],
    python_requires=">=3.9",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "docx=src.cli_commands.docx:main",
        ],
    },
)

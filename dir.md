
AutoDocX/
│
├── config.yaml                      # Huvudkonfiguration (inställningar, prompt-alternativ, ignorerade mappar etc.)
│
├── model/                           # LLM-modeller och konfiguration
│   ├── __init__.py
│   └── llm_models.py                # Standard: LM Studio med context_tokens=60000, temperature=0.7, base_url="http://localhost:1234/v1"
│
├── docs/                            # Slutgiltig dokumentation
│   ├── User-Docs/                   # Användarvänliga dokument
│   ├── Developer-Docs/              # Utvecklardokumentation
│   └── AI-Docs/                     # AI-optimerade sammanfattningar
│
├── docs/
│   └── Temp/                        # Temporär lagring under processen (mappstruktur speglar källkoden)
│       ├── User-Docs/
│       ├── Developer-Docs/
│       └── AI-Docs/
│
├── src/                             # Kärnkodbasen
│   ├── __init__.py
│   │
│   ├── core/                        # Systemets workflow och styrning
│   │   ├── __init__.py
│   │   ├── main.py                  # Entrypoint – kör hela workflowet
│   │   ├── initialize.py            # Initiering (läser in config.yaml, miljö, konfiguration, mappscan)
│   │   ├── workflow_manager.py      # Styr och koordinerar hela processen
│   │   ├── process_controller.py    # Ansvarar för kodskanning och analys
│   │   └── task_dispatcher.py       # Skapar och hanterar dokumentationsuppgifter
│   │
│   ├── ai/                          # LLM-anknutna moduler
│   │   ├── __init__.py
│   │   ├── text_generator.py        # Skickar filinnehåll med prompt till LLM (sammanfattar)
│   │   ├── prompt_engine.py         # Bygger och hanterar prompt-templates (27 varianter)
│   │   └── token_optimizer.py       # Optimerar LLM-svar för tokenanvändning
│   │
│   ├── generators/                  # Dokumentgenerering och formatering
│   │   ├── __init__.py
│   │   ├── doc_generator.py         # Sammanställer enskilda fil-dokumentationer
│   │   ├── structure_validator.py   # Validerar kodstruktur och dokumentationssammanhang
│   │   └── formatters/              # Formaterar utdata till olika format
│   │       ├── __init__.py
│   │       ├── markdown_formatter.py
│   │       ├── html_formatter.py
│   │       └── json_formatter.py
│   │
│   ├── parsers/                     # Kodanalys och parsing
│   │   ├── __init__.py
│   │   ├── code_parser.py           # Läser och tolkar kod
│   │   ├── comment_extractor.py     # Extraherar kommentarer från koden
│   │   └── metadata_parser.py       # Samlar metadata om filerna
│   │
│   ├── validators/                  # Validering av dokumentation och kod
│   │   ├── __init__.py
│   │   ├── syntax_checker.py        # Kontrollerar syntaxen i genererad dokumentation
│   │   └── doc_consistency.py       # Säkerställer att dokumentationen överensstämmer med koden
│   │
│   ├── helpers/                     # Diverse hjälpfunktioner
│   │   ├── __init__.py
│   │   ├── file_operations.py       # Hanterar filsystemoperationer (läsa, skriva, spara etc.)
│   │   ├── string_utils.py          # Verktyg för textmanipulation
│   │   └── logger.py                # Loggning av workflow-aktivitet (skriver ut progress i terminalen)
│   │
│   ├── utils/                       # Verktygsmoduler
│   │   ├── __init__.py
│   │   ├── progress_tracker.py      # Spårar processens framsteg
│   │   ├── checklist_manager.py     # Hanterar vilka filer/uppgifter som är färdiga
│   │   └── state_manager.py         # Övervakar systemets tillstånd och framsteg
│   │
│   ├── scanners/                    # Skanning av hela kodbasen
│   │   ├── __init__.py
│   │   ├── workspace_scanner.py     # Genomsöker angiven sökväg och identifierar mappar/filer
│   │   ├── file_analyzer.py         # Analyserar enskilda filer (funktioner, klasser, m.m.)
│   │   └── dependency_tracker.py    # Identifierar beroenden mellan moduler
│   │
│   └── cli_commands/                # Custom CLI-kommandon för AutoDocX
│       ├── __init__.py
│       └── docx.py                # Implementerar kommandon som: 
│                                     #   docx "path" 
│                                     #   docx "path" -update 
│                                     #   docx "path" -review 
│                                     # Med ytterligare flaggor (-full, -sum, -short)
│
├── scripts/                         # Hjälpskript (setup, tester, distribution)
│   ├── setup_env.py
│   ├── run_tests.py
│   └── deploy.py
│
├── requirements.txt
├── setup.py
├── README.md
├── .gitignore
└── .env

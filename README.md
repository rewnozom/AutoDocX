
# **AutoDocX – Automatiserad Dokumentationsgenerator**

### ✨ _Låt din lokala LLM(AI) dokumentera din kodbas åt dig_

**AutoDocX** skapar **automatiskt dokumentation** för din kodbas utan att du behöver skriva den manuellt. Genom att analysera **kod och kommentarer**, genererar den **två olika typer av dokumentation**, anpassade både för slutanvändare och utvecklare.

Verktyget skannar igenom alla mappar och filer i angiven sökväg (standard: `./Workspace/`) och genererar tre olika typer av dokumentation:

- **User-Docs:** Användarvänliga sammanfattningar  
- **Developer-Docs:** Teknisk och detaljerad dokumentation  
- **AI-Docs:** Optimerade sammanfattningar för LLM-chat (för att spara tokens)

---

## 🔹 **Vad gör AutoDocX?**

**1. Automatisk skanning och analys**  
- Går igenom varje fil i den angivna sökvägen (standard: `DEFAULT_PATH` i .env)  
- Möjlighet att ignorera specifika mappar via `IGNORE_PATHS` i .env (standard: node_modules, .git, venv)  
- Extraherar kod, kommentarer och metadata för komplett analys

**2. Tre olika typer av dokumentation**  
- **Användardokumentation (User-Docs)** – Enkel och lättförståelig information för icke-tekniska användare, fokuserar på hur man använder systemet och dess funktioner
- **Utvecklardokumentation (Developer-Docs)** – Teknisk och djupgående dokumentation för utvecklare, innehåller kodanalys, arkitektur och implementationsdetaljer
- **AI-Docs** – Token-optimerade sammanfattningar specifikt anpassade för LLM-chat, perfekt för AI-assistenter och automatiserad kodanalys

**3. Dokumentgenereringsworkflow**  
- **Steg 1:** Skicka filens innehåll med en Developer-prompt till LLM för att generera detaljerad teknisk dokumentation
- **Steg 2:** Skicka samma fil med en User-friendly prompt för att skapa lättförståelig användardokumentation
- **Steg 3:** Skicka samma fil med en AI-optimerad prompt för att generera en effektiv LLM-anpassad sammanfattning

**4. Strukturerad output**  
Under processen sparas all dokumentation först i `docs/Temp/` med en mappstruktur som exakt speglar källkodens struktur. När alla filer är färdigprocessade sammanställs den kompletta dokumentationen per kategori och exporteras till:
- `docs/Developer-Docs/` – För utvecklare och teknisk personal
- `docs/User-Docs/` – För slutanvändare och icke-teknisk personal
- `docs/AI-Docs/` – För AI-assistenter och LLM-integrationer

**5. Konfiguration via .env**
- All konfiguration hanteras enkelt via miljövariabler i .env-filen
- Stöd för flera LLM-providers:
  - LM Studio (lokal LLM)
  - Anthropic (Claude)
  - OpenAI (GPT-4/3.5)
  - Azure OpenAI
  - Groq

---

## 🔧 **Användning och Argument**

### **Sökvägar (Paths)**
Du kan specificera vilken sökväg AutoDocX ska skanna:

- `.` eller `./` – Skannar hela projektet från nuvarande katalog  
- `./Workspace/` – Standardsökvägen om ingen annan anges  
- Absolut sökväg – t.ex. `C:/User/MittProjekt` eller `/home/user/projekt`  

### **Tillgängliga Argument**

| Argument        | Beskrivning                                                | Exempel                     |
|-----------------|------------------------------------------------------------|-----------------------------|
| `path`          | Sökväg till kodbasen som ska dokumenteras                  | `docx ./mitt-projekt`       |
| `--update`      | Skapar eller uppdaterar dokumentationen                    | `docx . --update`           |
| `--review`      | Granskar existerande dokumentation                         | `docx . --review`           |
| `--full`        | Använder fullständiga, detaljerade promptar                | `docx . --update --full`    |
| `--sum`         | Använder sammanfattande promptar för kortare dokumentation | `docx . --update --sum`     |
| `--short`       | Genererar ultrakort version med endast viktiga detaljer    | `docx . --update --short`   |
| `-v, --verbose` | Visar detaljerad debug-information                         | `docx . --update --verbose` |

### **Exempel på Användning**

**Grundläggande användning – standardsökväg**  
```bash
docx . --update
````

**Specifik sökväg med full dokumentation**

```bash
docx "C:/User/MittProjekt" --update --full
```

**Sammanfattad dokumentation med verbose-läge**

```bash
docx ./mitt-projekt --update --sum --verbose
```

**Granska befintlig dokumentation**

```bash
docx . --review
```

### **Kombinera Argument**

Du kan kombinera olika argument för att anpassa dokumentationsgenereringen:

- `--update --full` för detaljerad dokumentation
- `--update --sum` för sammanfattad version
- `--update --short` för ultrakort version
- Lägg till `--verbose` till valfri kombination för debugging

---

## **Installation**

### **Installera och köra som ett paket**

För att installera **AutoDocX** som ett globalt CLI-verktyg:

```bash
pip install .
```

Efter installation kan du köra `docx` direkt från terminalen:

```bash
docx "./" --update --full
```

---

### **Bygga och distribuera AutoDocX**

Om du vill bygga ett distributionspaket:

```bash
python setup.py sdist
```

Detta skapar en `.tar.gz`-fil i `dist/`-mappen.

För att installera paketet lokalt från din skapade fil:

```bash
pip install dist/AutoDocX-0.1.0.tar.gz
```

---

### **Installera beroenden**

Om du klonat projektet från källkod:

```bash
pip install -r requirements.txt
```

---

## **Användning**

Du kan antingen köra verktyget direkt via CLI-verktyget `docx` (om du installerat det), eller köra huvudmodulen:

```bash
python -m src.core.main
```

**Exempelvis:**

```bash
docx "./" --update --full
```

eller

```bash
python -m src.core.main --update --sum
```

---

## **CI/CD**

Se `.github/workflows/auto-docs.yml` för konfiguration av CI/CD-pipelinen. Här kan du automatisera körningen av AutoDocX vid varje commit eller pull request.

---

## **Övrigt**

- **Primär LLM**: AutoDocX använder LM Studio (lokal LLM) som standard.
- **Alternativa LLM-leverantörer**: Stöd finns i `model/llm_models.py`.

---

🚀 _Perfekt för både utvecklare och användare som vill ha aktuell dokumentation utan extra arbete!_
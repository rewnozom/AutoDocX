

# **AutoDocX – Automatiserad Dokumentationsgenerator**  

### ✨ _Låt din lokala LLM(AI) dokumentera din kodbas åt dig_  

**AutoDocX** skapar **automatiskt dokumentation** för din kodbas utan att du behöver skriva den manuellt. Genom att analysera **kod och kommentarer**, genererar den **två olika typer av dokumentation**, anpassade både för slutanvändare och utvecklare.  


Verktyget skannar igenom alla mappar och filer i angiven sökväg (standard: `./Workspace/`) och genererar tre olika typer av dokumentation:

- **User-Docs:** Användarvänliga sammanfattningar.

- **Developer-Docs:** Teknisk och detaljerad dokumentation.

- **AI-Docs:** Optimerade sammanfattningar för LLM-chat (för att spara tokens).


-----


## 🔹 **Vad gör AutoDocX?**  

📌 **Automatiserad dokumentation**  
   - Läser av din kod och skapar dokumentation automatiskt.  

1. **Automatisk skanning och analys**  

   - Går igenom varje fil i den angivna sökvägen (med möjlighet att ignorera specifika mappar, se `config.yaml`).

   - Extraherar kod, kommentarer och metadata.



📌 **Två olika typer av dokumentation**  
   - 📝 **Användardokumentation** – Enkel och lättförståelig information för slutanvändare.  
   - 🛠 **Utvecklardokumentation** – Teknisk och djupgående information för utvecklare.  

2. **Dokumentgenereringsworkflow**  

   För varje fil sker tre steg:

   - **Steg 1:** Skicka filens innehåll med en Developer-prompt till LLM för att generera detaljerad dokumentation.

   - **Steg 2:** Skicka samma fil med en User-friendly prompt för att skapa användardokumentation.

   - **Steg 3:** Skicka samma fil med en AI-optimerad prompt för att generera en sammanfattning för LLM-chat.

  

   Under processen sparas utdata först i `docs/Temp/` med en mappstruktur som speglar källkoden.

  

3. **Sammanställning**  

   När alla filer har processats sammanställs dokumentationen per mapp och exporteras till:

   - `docs/User-Docs/`

   - `docs/Developer-Docs/`

   - `docs/AI-Docs/`



📌 **Alltid uppdaterad**  
   - Dokumentationen uppdateras automatiskt varje gång koden ändras.  

📌 **Passar alla typer av projekt**  
   - Kan användas oavsett storlek eller teknikstack.  


4. **CLI-kommandon**  

   Kör AutoDocX via terminalen med följande exempel:

   - `docx "./" -update`  

     Processar sökvägen `./` (eller standardvägen om inget anges) och uppdaterar dokumentationen.

   - `docx "./" -update -full`  

     Använder fullständiga (detaljerade) promptar.

   - `docx "./" -update -sum`  

     Använder sammanfattande promptar.

   - `docx "./" -update -short`  

     Använder kortfattade promptar.

  

   Ytterligare flaggor och inställningar (t.ex. ignorerade mappar) konfigureras via `config.yaml`.




## Installation


### **Installera och köra som ett paket**

För att installera **AutoDocX** som ett globalt CLI-verktyg:

```bash
pip install .
```

Efter installation kan du köra `docx` från terminalen:

```bash
docx "./" -update -full
```


---

### **Bygga och distribuera AutoDocX**
Om du vill bygga ett distributionspaket:

```bash
python setup.py sdist
```

Detta skapar en `.tar.gz`-fil i `dist/`-mappen.

För att installera paketet lokalt:

```bash
pip install dist/AutoDocX-0.1.0.tar.gz
```

---

  

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

  

AutoDocX använder LM Studio (lokal LLM) som primär.

Stöd för alternativa LLM-leverantörer finns i `model/llm_models.py`.


🚀 _Perfekt för både utvecklare som vill ha aktuell dokumentation utan extra arbete!_  

# src/ai/prompt_engine.py
"""
PromptEngine - Bygger och hanterar promptmallar för AutoDocX.
Innehåller mallar för:
  - Developer-dokumentation
  - User-dokumentation
  - AI-optimerad dokumentation

Varje kategori har:
  - full: Genererar en detaljerad och utförlig dokumentation.
  - sum: Genererar en kortfattad sammanfattning.
  - short: Ger en ultrakort version.
  - aggregate_full/sum/short: Liknande varianter för att sammanfatta aggregerad dokumentation.
"""


class PromptEngine:
    def __init__(self):
        # Definierar promptmallar för varje dokumentationstyp och variant.
        self.templates = {
            "developer": {
                "full": (
                    "Du är en expertutvecklare. Analysera följande kod och skapa en detaljerad dokumentation som "
                    "beskriver alla funktioner, klasser, logik och eventuella designmönster. Inkludera exempel och "
                    "motiveringar. Koden:\n{code}"
                ),
                "sum": (
                    "Sammanfatta koden för en utvecklare. Fokusera på huvudfunktioner, viktiga metoder och struktur. "
                    "Koden:\n{code}"
                ),
                "short": (
                    "Ge en kort översikt av koden med de mest centrala punkterna för en utvecklare. Koden:\n{code}"
                ),
                "aggregate_full": (
                    "Granska den samlade utvecklardokumentationen och ge en övergripande, detaljerad sammanfattning med "
                    "fokus på kritiska funktioner och möjliga förbättringsområden. Dokumentationen:\n{docs}"
                ),
                "aggregate_sum": (
                    "Sammanfatta den aggregerade utvecklardokumentationen med en kortfattad översikt som lyfter fram huvudteman. "
                    "Dokumentationen:\n{docs}"
                ),
                "aggregate_short": (
                    "Ge en ultrakort översikt av den aggregerade utvecklardokumentationen, med de mest väsentliga punkterna. "
                    "Dokumentationen:\n{docs}"
                ),
            },
            "user": {
                "full": (
                    "Du är expert på att skapa användarvänlig dokumentation. Förklara koden på ett enkelt och begripligt "
                    "sätt för icke-tekniska användare. Beskriv syfte, funktion och hur man använder koden. Koden:\n{code}"
                ),
                "sum": (
                    "Sammanfatta koden för användare på ett lättförståeligt sätt. Ge en kort översikt över kodens syfte och funktion. "
                    "Koden:\n{code}"
                ),
                "short": (
                    "Ge en mycket kort sammanfattning av koden, med fokus på huvudsyftet, anpassat för en icke-teknisk publik. "
                    "Koden:\n{code}"
                ),
                "aggregate_full": (
                    "Granska den aggregerade användardokumentationen och skapa en detaljerad, men lättförståelig, översikt över "
                    "applikationens funktionalitet och användarflöden. Dokumentationen:\n{docs}"
                ),
                "aggregate_sum": (
                    "Sammanfatta den aggregerade användardokumentationen med en kort översikt som lyfter fram de centrala delarna. "
                    "Dokumentationen:\n{docs}"
                ),
                "aggregate_short": (
                    "Ge en ultrakort översikt av den aggregerade användardokumentationen med de mest väsentliga punkterna. "
                    "Dokumentationen:\n{docs}"
                ),
            },
            "ai": {
                "full": (
                    "Generera en omfattande, AI-optimerad sammanfattning av koden. Fokusera på att extrahera kärnkoncepten "
                    "med minimal tokenanvändning, men bevara all viktig information. Koden:\n{code}"
                ),
                "sum": (
                    "Sammanfatta koden på ett kompakt sätt optimerat för tokenbesparing utan att förlora kritiska detaljer. "
                    "Koden:\n{code}"
                ),
                "short": (
                    "Ge en ultrakort sammanfattning av koden med de viktigaste punkterna, optimerad för LLM-chat. "
                    "Koden:\n{code}"
                ),
                "aggregate_full": (
                    "Granska den samlade AI-dokumentationen och skapa en detaljerad, men token-effektiv, övergripande sammanfattning. "
                    "Dokumentationen:\n{docs}"
                ),
                "aggregate_sum": (
                    "Sammanfatta den aggregerade AI-dokumentationen med en kompakt översikt som bevarar de viktigaste punkterna. "
                    "Dokumentationen:\n{docs}"
                ),
                "aggregate_short": (
                    "Ge en extremt kort sammanfattning av den aggregerade AI-dokumentationen, med fokus på kärninnehållet. "
                    "Dokumentationen:\n{docs}"
                ),
            },
        }

    def get_prompt(self, doc_type, variant):
        """
        Hämtar promptmallen för en given dokumentationstyp och variant.

        Args:
            doc_type (str): 'developer', 'user' eller 'ai'
            variant (str): Exempelvis 'full', 'sum', 'short', 'aggregate_full', 'aggregate_sum' eller 'aggregate_short'

        Returns:
            str: Den valda promptmallen.
        """
        return self.templates.get(doc_type, {}).get(variant, "")


if __name__ == "__main__":
    engine = PromptEngine()

    # Exempel: Hämta och skriv ut promptar för utvecklardokumentation
    dev_full = engine.get_prompt("developer", "full")
    dev_sum = engine.get_prompt("developer", "sum")
    dev_short = engine.get_prompt("developer", "short")
    dev_agg_full = engine.get_prompt("developer", "aggregate_full")

    print("Developer Full Prompt:\n", dev_full)
    print("\nDeveloper Summary Prompt:\n", dev_sum)
    print("\nDeveloper Short Prompt:\n", dev_short)
    print("\nDeveloper Aggregate Full Prompt:\n", dev_agg_full)

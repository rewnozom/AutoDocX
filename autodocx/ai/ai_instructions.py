# src/ai/ai_instructions.py
"""
Ytterligare AI-instruktioner för att styra LLM:s beteende.
Exempelvis kan man ange instruktioner för att:
- Optimera svar för tokenanvändning.
- Fokusera på specifika delar av koden.
- Generera sammanfattningar med ett särskilt fokus.
"""


def get_additional_instructions(doc_type):
    instructions = {
        "developer": "Fokusera på tekniska detaljer, designmönster och kodstruktur.",
        "user": "Förklara kodens funktion och användning på ett enkelt och begripligt sätt.",
        "ai": "Ge en extremt kompakt sammanfattning med minimalt tokenanvändande men maximal informationsutbyte.",
    }
    return instructions.get(doc_type, "")


if __name__ == "__main__":
    for dt in ["developer", "user", "ai"]:
        print(f"{dt}: {get_additional_instructions(dt)}")

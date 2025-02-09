# src/ai/text_generator.py
import asyncio
from ..helpers.logger import Logger

# Placeholder: Importera LLM-modellhanteraren (ex. från model/llm_models.py) när den är implementerad


class TextGenerator:
    """
    Skickar filinnehåll tillsammans med en prompt till LLM (t.ex. LM Studio) för att generera en sammanfattning.

    Metoder:
      - generate_text(prompt: str) -> str: Skickar prompten till LLM och returnerar genererad text.
    """

    def __init__(self, llm_client=None):
        # llm_client kan sättas till en instans av en LLM-klient (t.ex. LM Studio)
        self.llm_client = llm_client

    async def generate_text(self, prompt):
        """
        Asynkront skickar prompten till LLM och returnerar svaret.
        Placeholder-implementation: Returnerar en simulerad sammanfattning.
        """
        Logger.log("Skickar prompt till LLM...", "INFO")
        # Här skulle du anropa self.llm_client med prompten, ex:
        # response = await self.llm_client.chat.completions.create(prompt=prompt, ...)
        await asyncio.sleep(1)  # Simulerar väntetid
        simulated_response = f"Simulerad LLM-sammanfattning för prompt: {prompt}"
        Logger.log("Svar mottaget från LLM.", "SUCCESS")
        return simulated_response


if __name__ == "__main__":
    import asyncio

    generator = TextGenerator()
    prompt = "Exempelprompt för att generera dokumentation."
    response = asyncio.run(generator.generate_text(prompt))
    print("Genererat svar:", response)

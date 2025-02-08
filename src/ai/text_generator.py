# src/ai/text_generator.py
import asyncio
from ..helpers.logger import Logger
from ..helpers.config_manager import ConfigManager
from model.llm_models import llm_manager, ModelProvider

class TextGenerator:
    """
    Skickar filinnehåll tillsammans med en prompt till vald LLM för att generera en sammanfattning.
    Stödjer dynamiskt alla konfigurerade LLM providers.
    """

    def __init__(self, provider=None):
        """
        Initierar TextGenerator med specifik provider eller default från miljövariabler.
        
        Args:
            provider (str, optional): Specifik provider att använda.
                                      Om None, används värdet från .env (default_llm).
        """
        # Hämta konfigurationen från miljövariabler via ConfigManager
        self.config = ConfigManager().config
        
        # Använd angiven provider eller default från konfigurationen
        self.provider = provider or self.config.get('default_llm')
        
        try:
            # Mappa provider-namn till (modellnamn, ModelProvider)
            provider_model_map = {
                'lmstudio': ('lm-studio-local', ModelProvider.LM_STUDIO),
                'anthropic': ('claude-3-opus', ModelProvider.ANTHROPIC),
                'openai': ('gpt-4-turbo', ModelProvider.OPENAI),
                'azure': ('gpt-4', ModelProvider.AZURE),
                'groq': ('mixtral-8x7b-32768', ModelProvider.GROQ)
            }
            
            if self.provider not in provider_model_map:
                raise ValueError(f"Okänd provider: {self.provider}")
            
            model_name, _ = provider_model_map[self.provider]
            llm_manager.set_current_model(model_name)
            
            # Hämta provider-specifika inställningar (från .env-konfigurationen)
            self.provider_config = self.config['llm'].get(self.provider, {})
            
            Logger.log(f"Använder {self.provider.upper()} som LLM provider", "INFO")
            
        except Exception as e:
            Logger.log(f"Kunde inte initiera LLM provider: {str(e)}", "ERROR")
            raise

    async def generate_text(self, prompt):
        """
        Asynkront skickar prompten till vald LLM och returnerar svaret.
        """
        try:
            Logger.log(f"Skickar prompt till {self.provider.upper()}...", "INFO")
            
            # Om prompten innehåller "file_path:" försök läsa in filens innehåll
            file_content = None
            if "file_path:" in prompt:
                try:
                    file_path = prompt.split("file_path:")[1].split("\n")[0].strip()
                    with open(file_path, 'r', encoding='utf-8') as f:
                        file_content = f.read()
                except Exception as file_error:
                    Logger.log(f"Kunde inte läsa fil: {str(file_error)}", "ERROR")

            # Formatera meddelandet enligt ChatML-format
            messages = [
                {
                    "role": "system", 
                    "content": "Du är en expert på att analysera och dokumentera kod."
                },
                {
                    "role": "user", 
                    "content": prompt + (f"\n\nFilinnehåll:\n```\n{file_content}\n```" if file_content else "")
                }
            ]
            
            # Hämta inställningar för den valda providern
            temperature = self.provider_config.get('temperature', 0.7)
            max_tokens = self.provider_config.get('context_tokens', 60000)
            top_p = self.provider_config.get('top_p', 0.9)
            
            # Anropa LLM‑manager för att generera svar
            response = await llm_manager.generate_response(
                messages,
                temperature=temperature,
                max_tokens=max_tokens,
                top_p=top_p
            )
            
            if response and response.content:
                Logger.log(
                    f"Svar mottaget från {self.provider.upper()}. Tokens använt: {response.total_tokens} "
                    f"(prompt: {response.prompt_tokens}, completion: {response.completion_tokens})", 
                    "SUCCESS"
                )
                return response.content
            else:
                Logger.log(f"Inget innehåll i svaret från {self.provider.upper()}.", "ERROR")
                return f"Kunde inte generera dokumentation - tomt svar från {self.provider.upper()}."
                
        except Exception as e:
            Logger.log(f"Fel vid generering av text: {str(e)}", "ERROR")
            return f"Fel vid generering av dokumentation: {str(e)}"

    def change_provider(self, new_provider):
        """
        Byter till en annan LLM provider.
        
        Args:
            new_provider (str): Namnet på den nya providern att använda.
        """
        try:
            # Återanvänd __init__-logiken för att byta provider
            self.__init__(new_provider)
            Logger.log(f"Bytte till provider: {new_provider}", "SUCCESS")
        except Exception as e:
            Logger.log(f"Kunde inte byta provider: {str(e)}", "ERROR")
            raise

if __name__ == "__main__":
    async def test():
        # Testa med explicit provider "lmstudio" (som standard)
        try:
            generator = TextGenerator("lmstudio")
            prompt = "Exempelprompt för att generera dokumentation."
            response = await generator.generate_text(prompt)
            print("\nLMSTUDIO svar:", response)
        except Exception as e:
            print("Fel vid test av lmstudio:", str(e))

    asyncio.run(test())

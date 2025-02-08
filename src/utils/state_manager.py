class StateManager:
    """
    Övervakar systemets tillstånd och framsteg.
    
    Funktionalitet:
      - update_state(key, value): Uppdaterar ett specifikt tillstånd.
      - get_state(key): Returnerar värdet för ett givet tillstånd.
      - report_state(): Returnerar en sammanfattning av hela systemets tillstånd.
    """
    def __init__(self):
        self.state = {}
    
    def update_state(self, key, value):
        self.state[key] = value
        print(f"[STATE] Uppdaterat '{{key}}' till '{{value}}'.")
    
    def get_state(self, key):
        return self.state.get(key, None)
    
    def report_state(self):
        return self.state

if __name__ == "__main__":
    state_manager = StateManager()
    state_manager.update_state("Filer processade", 10)
    state_manager.update_state("Fel", 0)
    print("Systemstatus:", state_manager.report_state())

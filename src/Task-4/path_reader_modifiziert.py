import os
 
def umgebungsvariable_lesen():
    """Die System-PATH auslesen und formatiert ausgeben"""
    pfad_variable = os.environ.get("PATH")
    if not pfad_variable:
        print("System-PATH nicht gefunden.")
        return
    pfad_trenner = ";" if os.name == "nt" else ":"
    pfad_liste = pfad_variable.split(pfad_trenner)
    print("Inhalt der System-PATH:")
    print("="*40)
    for i, path in enumerate(pfad_liste, 1):
        print(f"{i}. {path}")
    print("="*40)
    print(f"Gesamt: {len(pfad_liste)} Pfade gefunden.")
 
if __name__ == "__main__":
    umgebungsvariable_lesen()
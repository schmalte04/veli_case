import pandas as pd
import pytest

values = [8, 9, 8, 7, 9, 8, 8 ,7, 8, 22, 9]

def detect_spike(values, k=3):
  
    if len(values) < 6:  ## Berechnung erst ab 6. Wert sinnvoll davor n zu klein - macht keinen Sinn
        print("Zu wenige Werte für Anomalieerkennung")

        return None
    
    # Ab dem 6. Wert (Index 5) erst loop starten
    for i in range(5, len(values)):
        # Vorangehende 5 Werte
        previous_five = values[i-5:i]
        
        # Mittelwert und Stdabw der vorangehenden 5 Werte
        prev_series = pd.Series(previous_five)
        mean_prev = prev_series.mean()
        std_prev = prev_series.std(ddof=0)

        # Prüfen ob aktueller Wert eine Anomalie ist (mehr als k Standardabweichungen ÜBER dem Mittelwert!!)
        if std_prev > 0 and values[i] > mean_prev + k * std_prev:
            return i
    return None

# Test der Funktion
result = detect_spike(values)
print(f"Ergebnis für {values}: Index {result}")

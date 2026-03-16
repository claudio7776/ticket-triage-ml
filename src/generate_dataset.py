import random
import pandas as pd

N_SAMPLES = 300

categories = ["Amministrazione", "Tecnico", "Commerciale"]
priorities = ["bassa", "media", "alta"]

titles = [
    "Errore accesso sistema",
    "Richiesta informazioni fattura",
    "Problema con preventivo",
    "Sistema bloccato",
    "Richiesta aggiornamento cliente"
]

bodies = [
    "Il sistema non funziona correttamente",
    "Ho bisogno di chiarimenti sulla fattura",
    "Il cliente chiede aggiornamenti",
    "Il software restituisce errore",
    "Serve assistenza tecnica"
]

rows = []

for i in range(N_SAMPLES):

    title = random.choice(titles)
    body = random.choice(bodies)
    category = random.choice(categories)
    priority = random.choice(priorities)

    rows.append({
        "title": title,
        "body": body,
        "category": category,
        "priority": priority
    })

df = pd.DataFrame(rows)

df.to_csv("tickets_dataset.csv", index=False)

print("Dataset generato")

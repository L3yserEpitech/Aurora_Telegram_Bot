import pandas as pd

# Créer un DataFrame avec "Bonjour" dans la cellule A1
df = pd.DataFrame(data={"A": ["Bonjour"]})

# Ajouter "Au revoir" dans la cellule A15
df.at[1, 'A'] = "Jules"

# Écrire le DataFrame dans un fichier Excel
df.to_excel('mon_fichier.xlsx', index=False)

print(df)
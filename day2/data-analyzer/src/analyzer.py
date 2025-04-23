# Créer une classe DataAnalyzer qui :
# - Fait des statistiques (moyenne, médiane, std) par catégorie
# - Analyse dans le temps
# - Trouve les catégories les plus dépensières
# - Classe les clients selon leurs habitudes

import pandas as pd

class DataAnalyzer:
    def __init__(self, data):
        self.data = data

    def summary_stats(self):
        # Retourne les statistiques descriptives
        return self.data.describe()

    def time_series(self):
        # Exemple : Retourne une série temporelle agrégée par mois
        if 'date' not in self.data.columns:
            raise ValueError("La colonne 'date' est manquante dans les données.")
        self.data['date'] = pd.to_datetime(self.data['date'], errors='coerce')
        return self.data.groupby(self.data['date'].dt.to_period('M')).size()

    def top_categories(self):
        # Exemple : Retourne les 5 catégories les plus fréquentes
        if 'category' not in self.data.columns:
            raise ValueError("La colonne 'category' est manquante dans les données.")
        return self.data['category'].value_counts().head(5)

    def segment_customers(self):
        pass

# Exemple d'utilisation     
if __name__ == "__main__":
    data = {
        'date': ['2023-01-01', '2023-01-02', '2023-01-03'],
        'category': ['Electronics', 'Clothing', 'Electronics'],
        'price': [100, 50, 150]
    }
    df = pd.DataFrame(data)
    analyzer = DataAnalyzer(df)
    print(analyzer.summary_stats())
    print(analyzer.time_series())
    print(analyzer.top_categories())
    print(analyzer.segment_customers())
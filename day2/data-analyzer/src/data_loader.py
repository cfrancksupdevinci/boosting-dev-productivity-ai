# Créer une classe DataLoader qui :
# - Charge un fichier CSV dans un DataFrame
# - Vérifie les colonnes obligatoires
# - Gère les valeurs manquantes
# - Convertit les types (date, float)
# - Filtre par date ou catégorie

import pandas as pd

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = pd.read_csv(file_path)
        self.clean_data()

    def clean_data(self):
        pass

    def filter_by_date(self, start, end):
        pass

    def filter_by_category(self, category):
        pass

    def check_required_columns(self, required_columns):
        missing_columns = [col for col in required_columns if col not in self.df.columns]
        if missing_columns:
            raise ValueError(f"Missing required columns: {missing_columns}")
        return True

    def handle_missing_values(self, strategy='drop'):
        if strategy == 'drop':
            self.df.dropna(inplace=True)
        elif strategy == 'fill':
            self.df.fillna(0, inplace=True)
        else:
            raise ValueError("Invalid strategy. Use 'drop' or 'fill'.")

    def convert_types(self, date_cols=None, float_cols=None):
        if date_cols:
            for col in date_cols:
                self.df[col] = pd.to_datetime(self.df[col], errors='coerce')
        if float_cols:
            for col in float_cols:
                self.df[col] = pd.to_numeric(self.df[col], errors='coerce')

    def filter_by_date(self, start_date, end_date):
        self.df = self.df[(self.df['date'] >= start_date) & (self.df['date'] <= end_date)]

    def filter_by_category(self, category):
        self.df = self.df[self.df['category'] == category]

    def load_data(self):
        # Charger le fichier CSV dans un DataFrame
        self.df = pd.read_csv(self.file_path)
        # Vérifier les colonnes obligatoires
        self.check_required_columns(['date', 'category'])
        # Gérer les valeurs manquantes
        self.handle_missing_values(strategy='drop')
        # Convertir les types de colonnes
        self.convert_types(date_cols=['date'], float_cols=['price'])
        # Filtrer par date et catégorie si nécessaire
        self.filter_by_date('2023-01-01', '2023-12-31')
        self.filter_by_category('Electronics')

# Exemple d'utilisation
if __name__ == "__main__":
    loader = DataLoader('data.csv')
    loader.check_required_columns(['date', 'category'])
    loader.handle_missing_values(strategy='fill')
    loader.convert_types(date_cols=['date'], float_cols=['price'])
    loader.filter_by_date('2023-01-01', '2023-12-31')
    loader.filter_by_category('Electronics')
    print(loader.df.head())
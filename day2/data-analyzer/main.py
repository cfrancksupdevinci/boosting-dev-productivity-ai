# Interface CLI :
# - Prend un fichier CSV en paramètre
# - Demande quelle analyse faire
# - Demande quelle visualisation afficher
# - Sauvegarde les résultats

import argparse
from src.data_loader import DataLoader
from src.analyzer import DataAnalyzer
from src.visualizer import DataVisualizer

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyseur de données CSV")
    parser.add_argument("file", help="Chemin vers le fichier CSV")
    parser.add_argument("--analysis", choices=["summary", "time-series", "category"], required=True, help="Type d'analyse à effectuer")
    parser.add_argument("--plot", choices=["bar", "line", "pie"], required=True, help="Type de visualisation à afficher")
    parser.add_argument("--output", help="Chemin du fichier de sortie pour sauvegarder le graphique")

    args = parser.parse_args()

    # Chargement des données
    data_loader = DataLoader(args.file)
    data = data_loader.df

    # Analyse des données
    data_analyzer = DataAnalyzer(data)
    if args.analysis == "summary":
        result = data_analyzer.summary_stats()
    elif args.analysis == "time-series":
        result = data_analyzer.time_series()
    elif args.analysis == "category":
        result = data_analyzer.top_categories()
    else:
        result = None

    print("Résultat de l'analyse :", result)  # Ajoutez cette ligne pour vérifier le résultat

    # Visualisation des données
    data_visualizer = DataVisualizer()
    if args.plot == "bar":
        data_visualizer.bar_chart(result, title="Bar Chart")
    elif args.plot == "line":
        data_visualizer.line_chart(result, title="Line Chart")
    elif args.plot == "pie":
        data_visualizer.pie_chart(result, title="Pie Chart")

    # Sauvegarde ou affichage du graphique
    if args.output:
        data_visualizer.save(args.output)
    else:
        data_visualizer.show()

    # Affichage des résultats de l'analyse
    print(result)
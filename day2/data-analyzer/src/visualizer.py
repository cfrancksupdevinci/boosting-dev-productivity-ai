# Classe DataVisualizer qui :
# - Crée des bar charts, line charts, pie charts, heatmaps
# - Permet de personnaliser le style
# - Peut afficher ou sauvegarder le graphique

import matplotlib.pyplot as plt
import seaborn as sns

class DataVisualizer:
    def __init__(self):
        pass

    def bar_chart(self, data, title="Bar Chart"):
        data.plot(kind='bar')
        plt.title(title)
        plt.show()

    def line_chart(self, data, title="Line Chart"):
        pass
    def pie_chart(self, data, title="Pie Chart"):
        pass
    def heatmap(self, data, title="Heatmap"):
        pass
    def customize_style(self, style): 
        sns.set_style(style)
    def show(self):
        plt.show()
    def save(self, path):
        plt.savefig(path)
# Exemple d'utilisation 
if __name__ == "__main__":
    import pandas as pd
    data = {
        'category': ['Electronics', 'Clothing', 'Electronics'],
        'price': [100, 50, 150]
    }
    df = pd.DataFrame(data)
    visualizer = DataVisualizer()
    visualizer.bar_chart(df.groupby('category')['price'].sum(), title="Total Price by Category")
    visualizer.show()
    visualizer.save("bar_chart.png")
import pandas as pd


class ExperimentResults():
    def __init__(self):
        cols = ['Liczba kultur', 'Max. rozmiar kultury',
                'Średni rozmiar kultury']
        self.df = pd.DataFrame(columns=cols)
        self.df.index.name = "Iteracja"

    def add(self, i, no_cultures, avg_culture_size, max_culture_size):
        self.df.loc[i + 1] = [int(no_cultures), int(max_culture_size), avg_culture_size]

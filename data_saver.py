import copy
import pandas as pd
import csv


class DataSaver:

    def __init__(self, repetition, experiment_no):
        self.repetition = repetition
        self.experiment_no = experiment_no
        self.detailed_state = []
        self.final_state = []

    def save_curr_state(self, grid):
        for ind, agent in enumerate(grid.cells):
            nbrs = grid.neighbours_indices(ind)
            self.detailed_state.append({'Kultura': copy.deepcopy(agent.culture),
                                      'Wagi': copy.deepcopy(agent.weights),
                                      'Sąsiedzi': nbrs,
                                      'Wybrany sąsiad': '',
                                      'Podobieństwo': '',
                                      'L. pseudolosowa': '',
                                      'Cecha': '',
                                      'Interakcja': '0'})

    def update_neighbour(self, index, nb_index):
        self.detailed_state[index].update({'Wybrany sąsiad': str(nb_index)})

    def update_probability(self, index, probability):
        rounded_prob = round(probability, 2)
        self.detailed_state[index].update({'Podobieństwo': str(rounded_prob)})

    def update_rnd(self, index, rnd):
        rounded_rnd = round(rnd, 2)
        self.detailed_state[index].update({'L. pseudolosowa': str(rounded_rnd)})

    def update_feature(self, index, feature):
        self.detailed_state[index].update({'Cecha': str(feature + 1)})

    def update_interaction(self, index, interaction):
        self.detailed_state[index].update({'Interakcja': str(interaction)})

    def save_all_data(self, i):
        experiment_data = pd.DataFrame(self.detailed_state)
        experiment_data.index.name = 'Agent'
        filename = './iterations/' + str(self.experiment_no) + '/rep_' \
                   + str(self.repetition) + '_iter_' + str(i) + '.csv'
        experiment_data.to_csv(filename, sep='\t',
                               quoting=csv.QUOTE_NONE)
        self.detailed_state = []

    def save_final_state(self, grid):
        for agent in grid.cells:
            row = {'Kultura': copy.deepcopy(agent.culture),
                   'Wagi': copy.deepcopy(agent.weights)}
            self.final_state.append(row)
        self.final_state = pd.DataFrame(self.final_state)
        self.final_state.index.name = 'Agent'
        self.final_state.to_csv('./summary/exp_' + str(self.experiment_no) +
                                  '_rep_' + str(self.repetition) +
                                  '_final_state.csv', sep='\t',
                                quoting=csv.QUOTE_NONE)

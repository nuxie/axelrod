import random
import math
import copy

from cell import Cell
from moore_grid_full import MooreGridFull
from neumann_grid_full import NeumannGridFull
from experiment_results import ExperimentResults
from gif_saver import GIFSaver
from data_saver import DataSaver


class Simulation:

    def __init__(self, rep, max_iter, population, features, traits, grid_type,
                 max_weight, save_gif, save_all_data, experiment_no):
        self.max_iter = max_iter
        self.population = population
        self.features = features
        self.traits = traits
        self.rows_list = []
        self.save_all_data = save_all_data
        self.save_gif = save_gif
        if self.save_gif:
            self.gif_saver = GIFSaver(rep, experiment_no, traits)
        self.data_saver = DataSaver(rep, experiment_no)
        self.experiment_no = experiment_no
        grid_size = int(math.sqrt(population))
        cells = []
        for i in range(int(grid_size ** 2)):
            cells.append(Cell(traits, features, max_weight))
        if grid_type == 'Moore':
            self.grid = MooreGridFull(grid_size, cells)
        else:
            self.grid = NeumannGridFull(grid_size, cells)
        self.results = ExperimentResults()

    def run(self):
        i: int = 0
        end = False
        while (not end) & (i < self.max_iter):
            i += 1
            if self.save_all_data:
                self.data_saver.save_curr_state(self.grid)
            if self.save_gif:
                self.gif_saver.generate_animation(i, self.grid)
            self.iteration()
            no_cultures = self.grid.distinct_cultures()
            avg_culture_size, max_culture_size = self.grid.culture_size_stats()
            self.results.add(i, no_cultures, avg_culture_size,
                             max_culture_size)
            if self.save_all_data:
                self.data_saver.save_all_data(i)
            end = self.check_end()
        if self.save_all_data:
            self.data_saver.save_final_state(self.grid)
        if self.save_gif:
            self.gif_saver.save_gif()
        final_cultures = set()
        for agent in self.grid.cells:
            final_cultures.add(copy.deepcopy(agent.culture_id))
        return self.results, i, final_cultures

    def iteration(self):
        cells_to_iterate = [i for i in range(self.grid.size ** 2)]
        random.shuffle(cells_to_iterate)
        while len(cells_to_iterate) > 0:
            ind = cells_to_iterate.pop(0)
            agent = self.grid.cells[ind]
            if self.grid.neighbours_same(ind):
                continue
            neighbour = agent
            nb_ind = -1
            while neighbour == agent:
                nb_ind, neighbour = self.grid.random_neighbour(ind)
            prob = agent.similarity(neighbour)
            rnd = random.uniform(0, 1)
            if self.save_all_data:
                self.data_saver.update_neighbour(ind, nb_ind)
                self.data_saver.update_probability(ind, prob)
                self.data_saver.update_rnd(ind, rnd)
            if prob != 1 and rnd < prob:
                while True:
                    feature = random.randint(0, self.features - 1)
                    if neighbour.culture[feature] != agent.culture[feature]:
                        break
                if self.save_all_data:
                    self.data_saver.update_feature(ind, feature)
                if prob >= agent.weights[feature]:
                    agent.update_feature(feature, neighbour.culture[feature])
                    if self.save_all_data:
                        self.data_saver.update_interaction(ind, 1)

    def check_end(self):
        counter = 0
        for ind, agent in enumerate(self.grid.cells):
            if self.grid.neighbours_same(ind):
                counter += 1
                if counter == self.grid.size ** 2:
                    return True
            else:
                nbrs = self.grid.neighbours(ind)
                agent_culture = str(agent.culture_id)
                for neighbour in nbrs:
                    if neighbour.culture_id == agent.culture_id:
                        continue
                    similarity = agent.similarity(neighbour)
                    different_features_weights = []
                    neighbour_culture = str(neighbour.culture_id)
                    for index, c in enumerate(agent_culture):
                        if c != neighbour_culture[index]:
                            different_features_weights.append(
                                agent.weights[index])
                    if similarity >= min(different_features_weights):
                        return False
        return True

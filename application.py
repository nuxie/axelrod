import multiprocessing
import shutil
import os
import pandas as pd
from functools import partial
from simulation import Simulation
from visualization import Visualization


def run_simulation(rep, max_iter, pop, features, traits, grid_type,
                   max_weight, save_gif, save_all_data, experiment_no):
    s = Simulation(rep, max_iter, pop, features, traits, grid_type,
                   max_weight, save_gif, save_all_data, experiment_no)
    return s.run()


def process_results(experiment_no, results_list, max_simulation_len,
                    final_cult):
    final = []
    for i, res in enumerate(results_list):
        to_add = max_simulation_len - res.df.shape[0]
        results_list[i] = res.df.append([res.df.tail(1)] * to_add,
                                     ignore_index=True)
        final.append(res.df.tail(1))
        final[i]['Kultury końcowe'] = ", ".join(map(str, final_cult[i]))
    results_concat = pd.concat(tuple(results_list))
    final_states = pd.concat(tuple(final))
    final_states.index.name = "Czas trwania"
    results_concat.index.name = "Iteracja"
    concat_by_index = results_concat.groupby(results_concat.index)
    results_means = concat_by_index.mean()
    results_stddev = concat_by_index.std(ddof=0)
    results_concat.to_csv('./summary/exp_' + str(experiment_no)
                          + '_results_concat.csv')
    filename = './summary/exp_' + str(experiment_no) + '_final_states.csv'
    final_states.to_csv(filename)
    return results_means, results_stddev


class Application:
    def __init__(self, experiments_list, experiments_repeats):
        self.experiments_list = experiments_list
        self.experiments_repeats = experiments_repeats

    def cleanup_dirs(self):
        shutil.rmtree('./iterations', ignore_errors=True)
        shutil.rmtree('./viz', ignore_errors=True)
        shutil.rmtree('./summary', ignore_errors=True)
        os.mkdir('./summary/')
        os.mkdir('./viz/')
        os.mkdir('./iterations/')
        for ind, e in enumerate(self.experiments_list):
            os.mkdir('./viz/' + str(ind))
            os.mkdir('./iterations/' + str(ind))

    def save_experiment_details(self):
        for ind, e in enumerate(self.experiments_list):
            data = 'Agents = ' + str(e[1])
            data += '\n Features = ' + str(e[2])
            data += '\n Traits = ' + str(e[3])
            data += '\n Grid type = ' + str(e[4])
            data += '\n Max weight = ' + str(e[5])
            text_file = open('./summary/exp_' + str(ind) + '_details.txt', "w")
            text_file.write(data)
            text_file.close()

    def execute_experiment(self, experiment, exp_no):
        partial_run_sim = partial(run_simulation,
                                  max_iter=experiment[0],
                                  pop=experiment[1],
                                  features=experiment[2],
                                  traits=experiment[3],
                                  grid_type=experiment[4],
                                  max_weight=experiment[5],
                                  save_gif=experiment[6],
                                  save_all_data=experiment[7],
                                  experiment_no=exp_no)
        with multiprocessing.Pool() as pool:
            res, iters, cult = zip(*pool.map(partial_run_sim,
                                             range(self.experiments_repeats)))
            results = list(res)
            max_sim_len = max(iters)
            iterations = list(iters)
            cultures = []
            for c in cult:
                cultures.append(len(c))
        results_means, results_stddev = process_results(exp_no, results,
                                                        max_sim_len, cult)
        visualization = Visualization(self.experiments_repeats, cultures,
                                      exp_no, iterations, results_means,
                                      results_stddev)
        visualization.visualize_all()

    def run(self):
        self.cleanup_dirs()
        self.save_experiment_details()
        print("Parallel execution on", multiprocessing.cpu_count(), "cores...")
        for exp_no, experiment in enumerate(self.experiments_list):
            self.execute_experiment(experiment, exp_no)

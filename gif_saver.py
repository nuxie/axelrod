import time
import imageio
import os
from glob import glob
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt


class GIFSaver:

    def __init__(self, repetition, experiment_no, traits):
        self.repetition = repetition
        self.experiment_no = experiment_no
        self.traits = traits

    def save_gif(self):
        gif_name = './viz/exp_' + str(self.experiment_no) + '_rep_' + \
                   str(self.repetition) + '.gif'
        time.sleep(20)
        with imageio.get_writer(gif_name, mode='I', fps=50) as writer:
            for filename in sorted(glob('./viz/' + str(self.experiment_no) +
                                        '/rep_' + str(self.repetition) +
                                        '*_gif.png'), key=os.path.getmtime):
                image = imageio.imread(filename)
                for x in range(3):
                    writer.append_data(image)
            for x in range(50):
                writer.append_data(image)

    def generate_animation(self, i, grid):
        sample_agent = grid.cells[0]
        features = len(sample_agent.culture)
        v_min = '1' * features
        v_max = str(self.traits) * features
        culture_ids = np.asarray([a.culture_id for a in grid.cells])
        culture_ids_grid = culture_ids.reshape(grid.size, grid.size)
        colormap = sb.color_palette('Set2', as_cmap=True)
        sb.heatmap(culture_ids_grid, vmin=int(v_min), vmax=int(v_max),
                   cbar=False, square=True, cmap=colormap).set_title(str(i))
        plt.xticks([], [])
        plt.yticks([], [])
        plt.savefig('./viz/' + str(self.experiment_no) + '/rep_' +
                    str(self.repetition) + "_" + str(i) + '_gif.png')
        plt.close()

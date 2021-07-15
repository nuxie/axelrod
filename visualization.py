import seaborn as sb
import matplotlib.pyplot as plt
import matplotlib as mpl


class Visualization:
    def __init__(self, repetitions, cultures, experiment_no, iterations,
                 results_means, results_stddev):
        self.repetitions = repetitions
        self.cultures = cultures
        self.experiment_no = experiment_no
        self.iterations = iterations
        self.results_means = results_means
        self.results_stddev = results_stddev
        mpl.rcParams['savefig.dpi'] = 300
        mpl.rcParams["figure.dpi"] = 300
        sb.set_style("whitegrid")
        plt.style.use('./style.mplstyle')
        mpl.rcParams['text.latex.preamble'] = r'\usepackage[T1]{fontenc}'

    def save_plot(self, filename):
        plt.savefig(filename, bbox_inches="tight")
        plt.show()
        plt.close()

    def name_axes(self, x, y):
        plt.xlabel(x, labelpad=10)
        plt.ylabel(y, labelpad=10)

    def relplot_details(self, plot, legend_loc, x, y):
        plot.legend.remove()
        plt.legend(loc=legend_loc)
        self.name_axes(x, y)

    def visualize_all(self):
        self.time_histogram()
        self.time_histogram2()
        self.time_histogram3()
        self.final_cultures_histogram()
        self.avg_results()
        self.stddev_results()

    def time_histogram(self):
        sb.histplot(x=self.iterations, bins='auto', kde=True, color='teal',
                    stat="density")
        self.name_axes('Liczba iteracji', 'Density')
        self.save_plot(
            './viz/exp_' + str(self.experiment_no) + '_hist_time.png')

    def time_histogram2(self):
        sb.histplot(x=self.iterations, bins='auto', kde=True, color='teal',
                    stat="probability")
        self.name_axes('Liczba iteracji', 'Probability')
        self.save_plot(
            './viz/exp_' + str(self.experiment_no) + '_hist_time2.png')

    def time_histogram3(self):
        sb.histplot(x=self.iterations, bins='auto', kde=True, color='teal',
                    stat="count")
        self.name_axes('Liczba iteracji', 'Count')
        self.save_plot(
            './viz/exp_' + str(self.experiment_no) + '_hist_time3.png')

    def final_cultures_histogram(self):
        culture_dict = {}
        for c in range(len(self.cultures)):
            culture_dict[self.cultures[c]] = self.cultures.count(
                self.cultures[c])
        h = sb.histplot(x=self.cultures, bins=len(set(self.cultures)),
                        color='teal',
                        stat="probability", discrete=True)
        for p in h.patches:
            key = int(p.get_x() + 0.5)
            if key in culture_dict:
                h.annotate(culture_dict[key],
                           (p.get_x() + p.get_width() / 2., p.get_height()),
                           ha='center', va='center', fontsize=11, color='gray',
                           xytext=(0, 5), textcoords='offset points')
        self.name_axes('Liczba kultur', 'Prawdopodobieństwo')
        self.save_plot(
            './viz/exp_' + str(self.experiment_no) + '_hist_cultures.png')

    def avg_results(self):
        df = self.results_means.melt(var_name='cols',
                                     value_name='vals',
                                     ignore_index=False)
        plot = sb.relplot(x=df.index, y="vals", hue='cols', data=df,
                          kind="line", palette='Set2')
        self.relplot_details(plot, 'upper left', 'Iteracja', 'Średnia')
        self.save_plot(
            './viz/exp_' + str(self.experiment_no) + '_stats_avg.png')

    def stddev_results(self):
        self.results_stddev = self.results_stddev.drop(
            'Średni rozmiar kultury',
            axis=1)
        df = self.results_stddev.melt(var_name='cols',
                                      value_name='vals',
                                      ignore_index=False)
        plot = sb.relplot(x=df.index, y="vals", hue='cols', data=df,
                          kind="line", palette='Set2')
        self.relplot_details(plot, 'upper right', 'Iteracja', 'Odchylenie standardowe')
        self.save_plot(
            './viz/exp_' + str(self.experiment_no) + '_stats_stddev.png')

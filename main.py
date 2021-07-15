from application import Application

# format:
# [max_iterations, population, features, traits,
#  grid_type, maximum_weight, save_gif, save_all_data]
EXPERIMENTS = [
    [10000, 25, 5, 4, 'Neumann', 0.5, False, False]
]
EXPERIMENT_REPEATS = 5


def main():
    app = Application(EXPERIMENTS, EXPERIMENT_REPEATS)
    app.run()


if __name__ == "__main__":
    main()

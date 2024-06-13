import Genetic_Algorithm as GA
import Chromosome as Ch
import numpy as np
import matplotlib.pyplot as plt

numbers_of_generations = 200
population_size = 500
mut_rate = 0.2

dataset = Ch.dataset


def genetic_algorithm(num_of_generations, pop_size, mutation_rate, data_list):
    new_gen = GA.initialization(data_list, pop_size)

    costs_for_plot = []

    for iteration in range(0, num_of_generations):
        new_gen = GA.create_new_generation(new_gen, mutation_rate)

        print(f"Generation: {str(iteration)}" + "\n" + f"Cost in the Generation {str(iteration)}: {str(new_gen[0].cost)}")

        costs_for_plot.append(GA.find_best(new_gen).cost)

    return new_gen, costs_for_plot


def draw_cost_generation(y_list):
    x_list = np.arange(1, len(y_list) + 1)

    plt.plot(x_list, y_list)

    plt.title("Route Cost through Generations")
    plt.xlabel("Generations")
    plt.ylabel("Cost")

    plt.show()


def draw_path(solution):
    x_list = []
    y_list = []
    name_list = []

    for m in range(0, len(solution.chromosome)):
        x_list.append(solution.chromosome[m].x)
        y_list.append(solution.chromosome[m].y)
        name_list.append(solution.chromosome[m].name)

    fig, ax = plt.subplots()

    plt.scatter(y_list, x_list)

    ax.plot(y_list, x_list, '-', lw=2, color='black', ms=10)
    ax.set_title("Best Solution")

    for i, name in enumerate(name_list):
        ax.annotate(name, (y_list[i], x_list[i]))

    plt.show()


last_generation, y_axis = genetic_algorithm(
    num_of_generations=numbers_of_generations, pop_size=population_size, mutation_rate=mut_rate, data_list=dataset
)

best_solution = GA.find_best(last_generation)

draw_cost_generation(y_axis)

draw_path(best_solution)

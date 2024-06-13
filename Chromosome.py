import math


class City:
    def __init__(self, id, x, y, name):
        self.x = float(x)
        self.y = float(y)
        self.id = int(id)
        self.name = str(name)


file_name = input("Please enter the file name you want to open (If the file is not in the same folder please give the "
                  "path): ")

dataset = []
N_of_cities = int(input("Please enter how many cities does the file contains: "))

with open(file_name, "r") as f:
    for line in f:
        new_line = line.strip()
        new_line = new_line.split(" ")

        id, x, y, name = new_line[0], new_line[1], new_line[2], new_line[3]

        dataset.append(City(id=id, x=x, y=y, name=name))


def create_distance_matrix(city_list):
    matrix = [[0 for _ in range(N_of_cities)] for _ in range(N_of_cities)]

    for i in range(0, len(matrix)-1):
        for j in range(0, len(matrix[0])-1):
            matrix[city_list[i].id][city_list[j].id] = math.sqrt(pow((city_list[i].x - city_list[j].x), 2)
                                                                 + pow((city_list[i].y - city_list[j].y), 2))
    return matrix


matrix = create_distance_matrix(dataset)


class Chromosome:
    def __init__(self, node_list):
        self.chromosome = node_list

        chr_representation = []
        for i in range(0, len(node_list)):
            chr_representation.append(self.chromosome[i].id)
        self.chr_representation = chr_representation

        distance = 0
        for j in range(1, len(self.chr_representation) - 1):
            distance += matrix[self.chr_representation[j]-1][self.chr_representation[j + 1]-1]
        self.cost = distance

        self.fitness_value = 1 / self.cost

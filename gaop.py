import math
import random

# --- GA PARAMETERS ---
POPULATION_SIZE = 50
GENERATIONS = 100
CROSSOVER_RATE = 0.8
MUTATION_RATE = 0.2  # Higher mutation rate helps avoid local optima in TSP

# Map of cities represented by 2D coordinates (x, y)
CITIES = {
    0: (0, 0),
    1: (1, 5),
    2: (5, 8),
    3: (8, 3),
    4: (4, 1),
    5: (7, 7),
    6: (2, 9),
    7: (9, 0),
    8: (6, 4),
    9: (3, 3),
}
NUM_CITIES = len(CITIES)


# --- UTILITY & FITNESS FUNCTIONS ---
def euclidean_distance(city1, city2):
    """Calculates straight-line distance between two city coordinates."""
    x1, y1 = CITIES[city1]
    x2, y2 = CITIES[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def calculate_total_distance(route):
    """Calculates total round-trip distance for a given route."""
    dist = 0
    for i in range(len(route)):
        from_city = route[i]
        to_city = route[(i + 1) % len(route)]  # Return to starting city
        dist += euclidean_distance(from_city, to_city)
    return dist


def calculate_fitness(route):
    """Fitness is inversely proportional to total distance."""
    distance = calculate_total_distance(route)
    return 1.0 / distance if distance > 0 else 0


# --- GA OPERATORS ---
def create_individual():
    """Generates a random valid route visiting all cities once."""
    route = list(CITIES.keys())
    random.shuffle(route)
    return route


def create_population(size):
    return [create_individual() for _ in range(size)]


def select_parent(population, fitnesses):
    """Tournament selection."""
    candidates = random.sample(list(zip(population, fitnesses)), k=3)
    candidates.sort(key=lambda x: x[1], reverse=True)
    return candidates[0][0]


def ordered_crossover(parent1, parent2):
    """Ordered Crossover (OX) to preserve unique city sequences without duplicates."""
    if random.random() > CROSSOVER_RATE:
        return parent1.copy(), parent2.copy()

    size = len(parent1)
    a, b = sorted(random.sample(range(size), 2))

    def mate(p1, p2):
        child = [None] * size
        # Copy segment from p1
        child[a : b + 1] = p1[a : b + 1]

        # Fill remaining spots in order from p2
        p2_idx = 0
        for i in range(size):
            if child[i] is None:
                while p2[p2_idx] in child:
                    p2_idx += 1
                child[i] = p2[p2_idx]
        return child

    return mate(parent1, parent2), mate(parent2, parent1)


def mutate(route):
    """Swap Mutation: swaps two random cities in the route."""
    route = route.copy()
    if random.random() < MUTATION_RATE:
        idx1, idx2 = random.sample(range(len(route)), 2)
        route[idx1], route[idx2] = route[idx2], route[idx1]
    return route


# --- MAIN ALGORITHM FLOW ---
def run_tsp_genetic_algorithm():
    population = create_population(POPULATION_SIZE)

    print(f"--- Running GA for Vehicle Route Optimization ({NUM_CITIES} Cities) ---")

    best_overall_route = None
    best_overall_distance = float("inf")

    for generation in range(GENERATIONS):
        # Calculate fitnesses
        fitnesses = [calculate_fitness(route) for route in population]

        # Find best route in current generation
        best_fitness = max(fitnesses)
        best_route = population[fitnesses.index(best_fitness)]
        current_distance = calculate_total_distance(best_route)

        if current_distance < best_overall_distance:
            best_overall_distance = current_distance
            best_overall_route = best_route

        # Print progress every 10 generations
        if (generation + 1) % 10 == 0 or generation == 0:
            print(
                f"Gen {generation + 1:03d} | Current Best Distance: {current_distance:.2f} | Overall Best: {best_overall_distance:.2f}"
            )

        # Create new population
        new_population = []
        while len(new_population) < POPULATION_SIZE:
            parent1 = select_parent(population, fitnesses)
            parent2 = select_parent(population, fitnesses)

            child1, child2 = ordered_crossover(parent1, parent2)

            new_population.append(mutate(child1))
            if len(new_population) < POPULATION_SIZE:
                new_population.append(mutate(child2))

        population = new_population

    print("\n--- Final Optimized Route ---")
    formatted_route = " -> ".join(map(str, best_overall_route + [best_overall_route[0]]))
    print(f"Path: {formatted_route}")
    print(f"Minimum Distance: {best_overall_distance:.2f}")


if __name__ == "__main__":
    run_tsp_genetic_algorithm()
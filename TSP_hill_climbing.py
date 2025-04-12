# pylint: disable=all
import random

# City object with travel distances to other cities
class City:
    def __init__(self, name, distances):
        self.name = name  # City name, e.g., 'Mumbai'
        self.distances = distances  # Dictionary of distances to other cities

    # Get the distance to another city
    def distance_to(self, other_city):
        return self.distances[other_city.name]

# TravelPlanner using Hill Climbing to find the shortest route
class TravelPlanner:
    def __init__(self, cities):
        self.cities = cities  # List of City objects

    # Calculate total distance of the trip (route)
    def trip_distance(self, trip):
        total_distance = 0
        for i in range(len(trip) - 1):
            total_distance += trip[i].distance_to(trip[i + 1])
        # Add the return distance back to the starting city
        total_distance += trip[-1].distance_to(trip[0])
        return total_distance

    # Generate a random travel plan
    def random_trip(self):
        trip = self.cities[:]
        random.shuffle(trip)
        return trip

    # Generate a neighboring trip by swapping two cities
    def swap_cities(self, trip):
        i, j = random.sample(range(len(trip)), 2)  # Pick two random cities to swap
        new_trip = trip[:]
        new_trip[i], new_trip[j] = new_trip[j], new_trip[i]
        return new_trip

    # Hill Climbing to find the optimal travel route
    def hill_climbing(self):
        current_trip = self.random_trip()  # Start with a random trip
        current_distance = self.trip_distance(current_trip)

        print(f"Starting trip: {[city.name for city in current_trip]} with distance {current_distance}")

        while True:
            # Generate a neighbor trip by swapping two cities
            new_trip = self.swap_cities(current_trip)
            new_distance = self.trip_distance(new_trip)

            print(f"Trying new trip: {[city.name for city in new_trip]} with distance {new_distance}")

            # If the new trip is better, move to that trip
            if new_distance < current_distance:
                current_trip = new_trip
                current_distance = new_distance
                print(f"New better trip found: {[city.name for city in current_trip]} with distance {current_distance}")
            else:
                # Stop when no better trip is found
                print(f"No better trip found. Final trip: {[city.name for city in current_trip]} with distance {current_distance}")
                break

        return current_trip, current_distance

# Example usage
if __name__ == "__main__":
    # Defining distances between Indian cities
    distances_mumbai = {'Mumbai': 0, 'Delhi': 1400, 'Bangalore': 980, 'Kolkata': 2050, 'Chennai': 1330}
    distances_delhi = {'Mumbai': 1400, 'Delhi': 0, 'Bangalore': 2150, 'Kolkata': 1500, 'Chennai': 2200}
    distances_bangalore = {'Mumbai': 980, 'Delhi': 2150, 'Bangalore': 0, 'Kolkata': 1870, 'Chennai': 350}
    distances_kolkata = {'Mumbai': 2050, 'Delhi': 1500, 'Bangalore': 1870, 'Kolkata': 0, 'Chennai': 1650}
    distances_chennai = {'Mumbai': 1330, 'Delhi': 2200, 'Bangalore': 350, 'Kolkata': 1650, 'Chennai': 0}

    # Create city objects
    cities = [
        City('Mumbai', distances_mumbai),
        City('Delhi', distances_delhi),
        City('Bangalore', distances_bangalore),
        City('Kolkata', distances_kolkata),
        City('Chennai', distances_chennai)
    ]

    # Initialize the TravelPlanner
    planner = TravelPlanner(cities)

    # Solve using Hill Climbing
    best_trip, shortest_distance = planner.hill_climbing()

    # Output the best travel route and its distance
    print("Best travel route:", [city.name for city in best_trip])
    print("Total travel distance:", shortest_distance)
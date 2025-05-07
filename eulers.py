import matplotlib.pyplot as plt
import numpy as np

def eulers(time_step, sim_length, initial_value):
    time = 0
    past_val = initial_value

    solution_points = np.array([initial_value])
    time_points = np.array([0])
    
    while time <= sim_length:
        new_val = past_val + time_step*(past_val - time)
        solution_points = np.append(solution_points, new_val)

        time += time_step
        time_points = np.append(time_points, time)
        past_val = new_val

    return solution_points, time_points


first_solution, time_points1 = eulers(0.1, 1, 1)
second_solution, time_points2 = eulers(0.025, 1, 1)

plt.plot(time_points1, first_solution)
plt.plot(time_points2, second_solution)
plt.title("Euler's")
plt.ylabel("Value")
plt.xlabel("Time")

plt.show()
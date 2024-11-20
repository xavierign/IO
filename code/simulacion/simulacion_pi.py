import random

def estimate_pi(num_points):
    inside_circle = 0
    
    # Simulación Monte Carlo
    for _ in range(num_points):
        x = random.uniform(0, 1)  # Coordenada x entre 0 y 1
        y = random.uniform(0, 1)  # Coordenada y entre 0 y 1
        if x**2 + y**2 <= 1:  # Verificar si el punto está dentro del cuarto de círculo
            inside_circle += 1

    # Estimar pi
    pi_estimate = 4 * (inside_circle / num_points)
    return pi_estimate

# Número de puntos a usar en la simulación
num_points = 100000
pi_value = estimate_pi(num_points)
print(f"Estimación de pi con {num_points} puntos: {pi_value}")
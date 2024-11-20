from scipy.optimize import minimize

# Datos de entrada
D = [1000, 800, 1200, 600, 500, 900, 700, 1100, 1000, 750]  # Demanda anual de cada producto
K = [200, 150, 250, 180, 100, 220, 170, 240, 200, 130]      # Costo fijo por orden
h = [2, 1.5, 2.5, 2, 1, 2.2, 1.8, 2.3, 2, 1.7]             # Costo unitario de almacenamiento
v = [0.5, 0.4, 0.6, 0.3, 0.2, 0.5, 0.35, 0.55, 0.45, 0.25]  # Volumen por unidad de producto
V_max = 50                                                  # Capacidad máxima del almacén

# Función objetivo
def costo_total(Q):
    total_cost = 0
    for i in range(len(Q)):
        if Q[i] <= 0:  # Penalización para soluciones no factibles
            return float('inf')
        total_cost += (D[i] / Q[i]) * K[i] + (Q[i] / 2) * h[i]
    return total_cost

# Restricción de volumen
def restriccion_volumen(Q):
    total_volumen = sum((Q[i] / 2) * v[i] for i in range(len(Q)))
    return V_max - total_volumen

# Restricciones y límites
constraints = [{'type': 'ineq', 'fun': restriccion_volumen}]  # Volumen total <= V_max
bounds = [(1, None)] * len(D)  # Q_i > 0 para todos los productos

# Solución inicial
Q0 = [100] * len(D)  # Suposición inicial para los lotes

# Optimización
resultado = minimize(costo_total, Q0, bounds=bounds, constraints=constraints, method='SLSQP')

# Resultados
if resultado.success:
    Q_optimos = resultado.x
    costo_minimo = resultado.fun
    print("Tamaños óptimos de lote (Q_i):")
    for i, Q in enumerate(Q_optimos):
        print(f"Producto {i + 1}: {Q:.2f}")
    print(f"\nCosto total mínimo: {costo_minimo:.2f}")
else:
    print("No se pudo encontrar una solución óptima.")
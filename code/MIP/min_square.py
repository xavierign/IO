from pulp import LpProblem, LpMinimize, LpVariable, lpSum

# Datos de entrada
x_values = [1, 2, 3, 4, 5]
y_values = [2.2, 2.8, 3.6, 4.5, 5.1]

# Crear el problema
problem = LpProblem("Minimos_Absolutos", LpMinimize)

# Variables de decisión: pendiente (m), ordenada al origen (b), errores absolutos (z_i)
m = LpVariable("m", lowBound=None)
b = LpVariable("b", lowBound=None)
z = [LpVariable(f"z_{i}", lowBound=0) for i in range(len(x_values))]

# Definir la función objetivo: minimizar la suma de los errores absolutos
problem += lpSum(z), "Suma_de_Errores_Absolutos"

# Definir las restricciones para los errores absolutos
for i in range(len(x_values)):
    problem += z[i] >= y_values[i] - (m * x_values[i] + b)
    problem += z[i] >= -(y_values[i] - (m * x_values[i] + b))

# Resolver el problema
problem.solve()

# Resultados
print(f"Pendiente (m): {m.varValue}")
print(f"Ordenada al origen (b): {b.varValue}")
print("Errores absolutos individuales:")
for i, z_var in enumerate(z):
    print(f"z_{i}: {z_var.varValue}")
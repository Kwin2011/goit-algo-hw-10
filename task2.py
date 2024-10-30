import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt

# Функція для обчислення значень інтегрованої функції
def target_function(x):
    return x ** 2

# Межі інтегрування
lower_bound = 0  # Нижня межа
upper_bound = 2  # Верхня межа

# Параметри для методу Монте-Карло
num_points = 100000  # Кількість випадкових точок
x_random = np.random.uniform(lower_bound, upper_bound, num_points)
y_random = np.random.uniform(0, upper_bound ** 2, num_points)

# Визначення точок під кривою
points_under_curve = np.sum(y_random < target_function(x_random))

# Обчислення площі прямокутника
rectangle_area = (upper_bound - lower_bound) * (upper_bound ** 2)

# Результат обчислення площі під кривою методом Монте-Карло
monte_carlo_area = (points_under_curve / num_points) * rectangle_area

# Аналітичне обчислення інтегралу за допомогою функції quad із SciPy
quad_area, quad_error = spi.quad(target_function, lower_bound, upper_bound)

# Виведення результатів
print(f"Метод Монте-Карло: {monte_carlo_area}")
print(f"Аналітичне значення інтегралу (quad): {quad_area} ± {quad_error}")

# Побудова графіка функції
x_values = np.linspace(-0.5, 2.5, 400)
y_values = target_function(x_values)

fig, ax = plt.subplots()

# Графік функції та її заповнена область
ax.plot(x_values, y_values, 'r', linewidth=2)

# Заштрихована область під кривою
interval_x = np.linspace(lower_bound, upper_bound)
interval_y = target_function(interval_x)
ax.fill_between(interval_x, interval_y, color='gray', alpha=0.3)

# Додавання точок Монте-Карло до графіка (візуалізація перших 500 точок)
ax.scatter(x_random[:500], y_random[:500], c=(y_random[:500] < target_function(x_random[:500])), cmap='coolwarm', s=1)

# Налаштування графіка
ax.set_xlim([x_values[0], x_values[-1]])
ax.set_ylim([0, max(y_values) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')








# Межі інтегрування та заголовок графіка
ax.axvline(x=lower_bound, color='gray', linestyle='--')
ax.axvline(x=upper_bound, color='gray', linestyle='--')
ax.set_title(f'Інтегрування f(x) = x^2 від {lower_bound} до {upper_bound}')
plt.grid()
plt.show()

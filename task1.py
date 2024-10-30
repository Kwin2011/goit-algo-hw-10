from pulp import LpMaximize, LpProblem, LpVariable, value 

# Ініціалізація моделі для задачі максимізації обсягу виробництва
production_model = LpProblem(name="optimize_beverage_production", sense=LpMaximize)

# Визначення змінних для продукції
lemonade_units = LpVariable(name="Lemonade_Units", lowBound=0, cat="Integer")
juice_units = LpVariable(name="Fruit_Juice_Units", lowBound=0, cat="Integer")

# Цільова функція: максимізація загального обсягу продуктів
production_model += lemonade_units + juice_units, "Maximize_Total_Production"

# Обмеження по ресурсах
production_model += (2 * lemonade_units + juice_units <= 100), "Water_Limit"
production_model += (lemonade_units <= 50), "Sugar_Limit"
production_model += (lemonade_units <= 30), "Lemon_Juice_Limit"
production_model += (2 * juice_units <= 40), "Fruit_Puree_Limit"

# Розв’язання задачі
production_model.solve()

# Отримання результатів
total_lemonade = value(lemonade_units)
total_juice = value(juice_units)
total_output = value(production_model.objective)

# Вивід результатів
print(f"Максимально можлива кількість Лимонаду: {total_lemonade}")
print(f"Максимально можлива кількість Фруктового соку: {total_juice}")
print(f"Загальний обсяг виробництва: {total_output}")
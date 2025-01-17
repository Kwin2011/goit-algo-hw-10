# Висновки

## Завдання 1: Оптимізація виробництва

У цьому завданні було розроблено модель оптимізації виробництва для двох продуктів — "Лимонад" і "Фруктовий сік" — із використанням обмежених ресурсів: води, цукру, лимонного соку та фруктового пюре. Ми застосували лінійне програмування для максимізації загальної кількості вироблених продуктів, використовуючи бібліотеку PuLP. 

### Результати
- **Оптимальна кількість** виробленого "Лимонаду" та "Фруктового соку" була визначена на основі доступних ресурсів.
- **Обмеження ресурсів** було повністю дотримано, що дозволило уникнути їх перевитрати та забезпечити раціональне використання.

### Висновок
Метод лінійного програмування дозволив ефективно визначити оптимальний розподіл ресурсів між двома продуктами. В умовах реального виробництва цей підхід допомагає підприємствам мінімізувати витрати та максимізувати обсяги виробництва, використовуючи наявні ресурси найбільш ефективно.

## Завдання 2: Обчислення визначеного інтеграла

У другому завданні ми обчислювали значення визначеного інтеграла функції \( f(x) = x^2 \) на інтервалі [0, 2] за допомогою методу Монте-Карло. Також для перевірки результату було застосовано аналітичний метод, використовуючи функцію `quad` з бібліотеки SciPy.

### Результати
- Метод Монте-Карло **надав оцінку площі під кривою**, яка була близькою до результату, отриманого аналітичним методом.
- **Аналітичний результат** надав точне значення інтегралу з вказаною похибкою, яка підтвердила точність обчислень методом Монте-Карло.

### Висновок
Метод Монте-Карло є ефективним чисельним методом для обчислення визначених інтегралів, особливо для складних функцій і великих діапазонів інтегрування, коли аналітичне рішення є складним або неможливим. Однак, в даному випадку, аналітичний метод `quad` є більш точним, і його доцільно використовувати, коли відома точна форма функції.

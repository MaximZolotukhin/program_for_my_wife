from count_price_calc import PropductCostCalc

class InfoFoods():
    """Класс для работы с информацие о продукте"""

    def __init__(self):
        self.foods_list = []  # Список продуктов.
        self.spent_list = []  # Список сколько использованной продукта
        self.weight_list = []  # Список веса
        self.price_list = []  # Список цены за продукт
        self.price_per_gram = []  # Список с ценой за грамм.

    def inform_for_foods(self):
        """Функция сбора данных"""
        dessert = input("Здравствуйте, что вы будите готовить? ")
        while True: # Добавил проверку на правильность ввода данных
            try:
                count_foods = int(input(f"Сколько продуктов входит в {dessert}: "))
                break
            except ValueError:
                print("Введите количество продуктов в цифровом формате: ")

        while int(count_foods):
            # Далее реализовать через вложненный словарь все input преобразовать в float
            weight = 0
            price = 0
            spent_list = 0
            self.foods_list.append(input("Введите название продукта: "))  # Добавляем данные в список продуктов
            try:
                weight = (input("Введите покупной вес продукта в граммах (если это яица то введите '10шт'.): "))  # Добавляем данные в список веса
                self.weight_list.append(weight)
            except ValueError:
                print("Введите количество продуктов в цифровом формате: ")

            self.price_list.append(
                int(input(
                    "Введите цену продукта (если это яица то за 10 шт.): ")))  # Добавляем данные в список веса
            self.spent_list.append(
                int(input(
                    "Введите сколько потрачено продукта: ")))  # Добавляю в списко вес использованного продукта
            count_foods -= 1  # Удаляем одну цифру чтобы прекратить выполнение цикла

        prod_cost_calc = PropductCostCalc(self.weight_list, self.price_list, self.spent_list)
        cost_calc = prod_cost_calc.product_cost_calc()  # Все данные нужно передавать списками.
        inform_foods = {
            'foods_list': self.foods_list,
            'spent_list': self.spent_list,
            'result_for_spent_list': cost_calc['result_for_spent_list'],
            'total_summ': cost_calc['total_summ'],
        }
        return inform_foods

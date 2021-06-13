"""Программа для рассчета затрат на изготовление кондитерских изделией"""
# Версия 0.3
print("---*---*---*---   Десертик v.0.3   ---*---*---*---")

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
        count_foods = int(input(f"Сколько продуктов входит в {dessert}: "))

        while count_foods:
            # Далее реализовать через вложненный словарь все input преобразовать в float
            self.foods_list.append(input("Введите название продукта: "))  # Добавляем данные в список продуктов
            self.weight_list.append(input(
                "Введите покупной вес продукта в граммах (если это яица то введите '10шт'.): "))  # Добавляем данные в список веса
            self.price_list.append(
                int(input("Введите цену продукта (если это яица то за 10 шт.): ")))  # Добавляем данные в список веса
            self.spent_list.append(
                int(input("Введите сколько потрачено продукта: ")))  # Добавляю в списко вес использованного продукта
            count_foods -= 1  # Удаляем одну цифру чтобы прекратить выполнение цикла

        cost_calc = self.product_cost_calc(self.weight_list, self.price_list, self.spent_list)  # Все данные нужно передавать списками.
        inform_foods = {
            'foods_list': self.foods_list,
            'spent_list': self.spent_list,
            'result_for_spent_list': cost_calc['result_for_spent_list'],
            'total_summ': cost_calc['total_summ'],
        }
        return inform_foods

    def product_cost_calc(self, weight, price, spent):
        """Функция производит расчеты по полученным данным"""
        # Получаем ценну за единицу товара
        total_summ = 0  # Общая сумма за все продукты
        result_for_spent_list = []  # Список с рассчетной ценой за потраченное количество продукта.
        count_calc = len(weight)
        index = 0
        while count_calc:
            if weight[index] == '10шт':  # Если это яица тогда рассчитываем за 10
                result = float(price[index]) / 10  # Проверить выполняется ли условие.
            else:  # Иначе цену делим на вес преборазованный в флоат
                result = float(price[index]) / float(weight[index])
            # Разобратся почему не сохраняеся в список
            result_for_spent = result * spent[index]  # Умножаем цену за единицу товара на фактически затраченный товар
            result_for_spent_list.append(result_for_spent)  # Список с ценами за использованный товар
            total_summ += result_for_spent  # Складываем все полученные суммы для формирования общей цены потраченной на все товары

            index += 1
            count_calc -= 1

        result_for_list = {
            'total_summ': total_summ,
            'result_for_spent_list': result_for_spent_list,
        }

        return result_for_list

def displaying_info(): #foods_list, spent_list, result_for_spent_list, total_summ
    inf_f_food = InfoFoods()
    all_info = inf_f_food.inform_for_foods()

    foods_list = all_info['foods_list']
    spent_list = all_info['spent_list']
    result_for_spent_list = all_info['result_for_spent_list']
    total_summ = all_info['total_summ']

    print("Вы использовали следующие продукты: ")
    index = 0
    for food in foods_list:
        print(f"\t{food.upper()}:  вы использовали {spent_list[index]} грамм, цена за использованный товар \
    {round(result_for_spent_list[index], 2)}")
        index += 1
    print(f"Всего потачено денежных средств {round(total_summ, 2)}")


if __name__ == '__main__':
    displaying_info()

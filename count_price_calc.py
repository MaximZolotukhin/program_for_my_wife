class PropductCostCalc():

    def __init__(self, weight, price, spent):
        self.weight = weight
        self.price = price
        self.spent = spent

    def product_cost_calc(self):
        """Функция производит расчеты по полученным данным"""
        # Получаем ценну за единицу товара
        total_summ = 0  # Общая сумма за все продукты
        result_for_spent_list = []  # Список с рассчетной ценой за потраченное количество продукта.
        count_calc = len(self.weight)
        index = 0
        while count_calc:
            if self.weight[index] == '10шт':  # Если это яица тогда рассчитываем за 10
                result = float(self.price[index]) / 10  # Проверить выполняется ли условие.
            else:  # Иначе цену делим на вес преборазованный в флоат
                result = float(self.price[index]) / float(self.weight[index])
            # Разобратся почему не сохраняеся в список
            result_for_spent = result * self.spent[index]  # Умножаем цену за единицу товара на фактически затраченный товар
            result_for_spent_list.append(result_for_spent)  # Список с ценами за использованный товар
            total_summ += result_for_spent  # Складываем все полученные суммы для формирования общей цены потраченной на все товары

            index += 1
            count_calc -= 1

        result_for_list = {
            'total_summ': total_summ,
            'result_for_spent_list': result_for_spent_list,
        }

        return result_for_list
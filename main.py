"""Программа для рассчета затрат на изготовление кондитерских изделией"""
# Версия 0.4
print("---*---*---*---   Десертик v.0.4   ---*---*---*---")
from info_foods import InfoFoods

class DisplayInfo(InfoFoods):

    def __init__(self):
        super().__init__()

    def displaying_info(self): #foods_list, spent_list, result_for_spent_list, total_summ
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
    product_one = DisplayInfo()
    product_one.displaying_info()

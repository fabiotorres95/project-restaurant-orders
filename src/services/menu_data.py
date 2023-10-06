from src.models.dish import Dish
from src.models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path
        file = open(source_path, 'r')
        data = file.readlines()
        file.close()

        all_dishes = []
        for line in data:
            if line.startswith('dish,price'):
                continue
            good_line = line.strip('\n')
            line_list = good_line.split(',')

            line_ingredient = Ingredient(line_list[2])

            if Dish(line_list[0], float(line_list[1])) in all_dishes:
                index = all_dishes.index(Dish(
                    line_list[0],
                    float(line_list[1])
                ))
                all_dishes[index].add_ingredient_dependency(
                    line_ingredient,
                    int(line_list[3])
                )

            else:
                new_dish = Dish(line_list[0], float(line_list[1]))

                new_dish.add_ingredient_dependency(
                    line_ingredient,
                    int(line_list[3])
                )
                all_dishes.append(new_dish)

        self.dishes = set(all_dishes)

import sqlite3


#
# conn = sqlite3.connect("recipe.db")
# cursor = conn.cursor()
# cursor.execute("""CREATE TABLE name_of_the_dish
#                   (dish text)
#                """)
# cursor.execute("""CREATE TABLE ingredients
#                   (dish_name text, ingredient text, grammar real)
#                """)
# cursor.execute("""CREATE TABLE description
#                   (dish_name text, descript text)
#                """)


class Dish:
    def __init__(self):
        self.conn = sqlite3.connect("recipe.db")
        self.cursor = self.conn.cursor()

    def add_dish(self, dish_name: str, ingredients: dict, description: str):
        self.cursor.execute(f"""INSERT INTO name_of_the_dish VALUES ('{dish_name}')""")
        self.cursor.execute(f"""INSERT INTO description VALUES ('{dish_name}', '{description}')""")
        ing = [(dish_name, str(key), int(item)) for key, item in ingredients.items()]
        self.cursor.executemany("INSERT INTO ingredients VALUES (?,?,?)", ing)
        self.conn.commit()
        return "Рецепт успішно додано!"

    def add_ingredient(self, dish_name: str, ingredients: dict):
        ing = [(dish_name, str(key), int(item)) for key, item in ingredients.items()]
        self.cursor.executemany("INSERT INTO ingredients VALUES (?,?,?)", ing)
        self.conn.commit()
        return "Інгредієнт успішно додано!"

    def get_dish(self, dish_name: str):
        self.conn.row_factory = sqlite3.Row

        sql = "SELECT * FROM ingredients WHERE dish_name=?"
        sql2 = "SELECT * FROM description WHERE dish_name=?"
        all_ing = self.cursor.execute(sql, [(dish_name)]).fetchall()
        all_desc = self.cursor.execute(sql2, [(dish_name)]).fetchall()
        ingredients = [(i[1], i[2]) for i in all_ing]
        descriptions = [i[-1] for i in all_desc]
        recipe = {"name": dish_name,
                  "ingredients": ingredients,
                  "descriptions": descriptions}
        return recipe


if __name__ == '__main__':
    print(Dish().add_dish('Салат', {'Капуста': '4', 'Огірок': '2'}, 'Подрібнити та перемішати'))
    print(Dish().get_dish("Салат"))
    print(Dish().add_ingredient("Салат", {"Цибуля": '1'}))

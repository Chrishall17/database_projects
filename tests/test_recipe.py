from lib.recipe import Recipe

"""
Recipe constructs with an id, title and author name
"""
def test_recipe_constructs():
    recipe = Recipe(1, 'Apple Pie', 30, 4)
    assert recipe.id == 1
    assert recipe.name == 'Apple Pie'
    assert recipe.cooking_time == 30
    assert recipe.rating == 4

"""
We can format recipes to strings nicely
"""
def test_recipes_format_nicely():
    recipe = Recipe(1, 'Apple Pie', 30, 4)
    assert str(recipe) == "1 - Apple Pie - 30 - 4"

"""
We can compare two identical recipes
And have them be equal
"""
def test_recipes_are_equal():
    recipe1 = Recipe(1, 'Apple Pie', 30, 4)
    recipe2 = Recipe(1, 'Apple Pie', 30, 4)
    assert recipe1 == recipe2
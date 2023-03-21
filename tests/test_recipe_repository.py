from lib.recipe_repository import RecipeRepository
from lib.recipe import Recipe

"""
When we call RecipeRepository#all
We get a list of Recipes objects reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/recipes.sql") # Seed our database with some test data
    repository = RecipeRepository(db_connection) # Create a new BookRepository

    books = repository.all() # Get all books

    # Assert on the results
    assert books == [
        Recipe(1, 'Apple Pie', 30, 4),
        Recipe(2, 'Cherry Pie', 30, 2),
        Recipe(3, 'Rhubarb Pie', 30, 4),
        Recipe(4, 'Tiramisu', 25, 3),
        Recipe(5, 'Brownie', 20, 5)
    ]

"""
When we call RecipeRepository#find
We get a single Recipe object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/recipes.sql")
    repository = RecipeRepository(db_connection)

    recipe = repository.find(3)
    assert recipe == Recipe(3, 'Rhubarb Pie', 30, 4)
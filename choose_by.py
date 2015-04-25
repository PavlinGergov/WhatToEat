class ChooseBy:

    def __init__(self, recipes, healthy=None, time=None, difficulty=None):

        # the class takes one argument:recipes - a list with the suggested
        # recipes, after we did some search (by default, favourite etc..)
        # the sort type must be choosed (healthy=True)

        self.recipes = recipes
        self.healthy = healthy
        self.time = time
        self.difficulty = difficulty

    def sort_by_time(self):
        # we have a time tag, simple sort is needed
        pass

    def sort_by_difficulty(self):
        # we have a difficulty tag, simple sort needed
        pass

    def sort_by_healthy(self):
        # Необходим е алгоритъм за здравословност, съотношение между
        # въглехидрати, белтъци и мазнини в 100 грама!!!! от ястието
        pass


# Function for listing the available products
# We are gona make a request to the produtcs database and return the products
def check_available_products():
    # sample return:
    # {
    # "name": "apple",
    # "count": 2,
    # "amount": 130  # grams
    # }
    pass


# Cook means that we've cooked the chosen recipe
# Increase the times_cooked tag with 1
# Add date and time to the log(the log contains the recipes we've coked so far)
# Изваждаме продуктите от базата с продукти на хладилника
def cook():
    pass


# Suggest recipes for today
# Take in consideration the last cooked meals
# we should NOT eat the same things every day
def suggested_for_today():
    pass


# We are gona return the favourite (most cooked) recipes
# by the times_cooked tag
def get_favourite_recipes():
    pass


# We are gona return 5 recipes that were most recently cooked
# by the date_cooked tag (in the log we have the last recipes)
def get_recent_recipes():
    pass


# We should be able to add a recipe following the original recipies format
# If we do not have all the fields filled, we should raise an error
def add_recipe():
    pass


# We are gona search the recipe database for an exact recipe
# Show all recipes that have the searched string:
# find: eggs with ham -> Eggs with ham and cheese, Eggs with smoked ham
def find_recipe():
    pass


# Show the ingredients(products) of the recipe
# after each product we should have: available tag -> True/False
# if we need 5 eggs and we have 4 -> avaiable(eggs) -> False
def is_available():
    pass


# Use the upper function to generate the proper return
def list_ingredients():
    # Sample output: Feel free to implement as you wish
    # {
    # "eggs - x4": "available",
    # "milk - 0.4 l": "not available"
    # }
    pass


# We should have an option to buy the missing product/products using a drone!!
# This should display some markets, delivery time, etc (this is about to be discussed)
def buy_product():
    pass

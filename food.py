class food: # main class
    def __init__(self, category, meal_time, cost):  # subclass
        self.category = category
        self.meal_time = meal_time
        self.cost = cost
    def food_type(self):
        print("The meal is a", self.category, "and it is ideal for", self.meal_time, "and it costs", self.cost)
class cakes(food):
    def __init__(self, category, meal_time, cost):  # used to initialize the class when its executed
        super().__init__(category, meal_time, cost)
BlackForest = cakes("snack", "breaktime", "100")  # object eg.black forest
BlackForest.food_type()
class cookies(food):
    def __init__(self, category, meal_time, cost):
        super().__init__(category, meal_time, cost)
weed_cookie = cookies("snack", "anytime", "500")
weed_cookie.food_type()
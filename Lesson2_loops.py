name = "Makarius"
protein_goal = 200
meals = [{"name": "omelet", "protein": 30}, {"name": "salmon", "protein": 25}, {"name": "chicken breast", "protein": 40}]
meals.append({"name": "greek yogurt", "protein": 17})

print(meals)

def protein_left(goal, eaten):
    return goal - eaten

total_eaten = 0
for meal in meals:
    total_eaten = total_eaten + meal["protein"]
    print(meal["name"], "-", meal["protein"], "g")
    if meal["protein"] >= 30:
        print("High protein meal!")

print("total eaten:", total_eaten) 
print("protein left:", protein_left(protein_goal, total_eaten))

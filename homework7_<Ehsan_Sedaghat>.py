#Make a list called pizza_orders and populate it with names of pizzas that have been ordered.
pizza_orders = ["Pepperoni", "Margherita", "Mushroom", "Meat Lover", "Veggie"]

#Make an empty list called finished_pizzas.
finished_pizzas = []

#Loop through the list of pizza orders and print a message for each order, saying “Your pizza pie is finished!”.
while pizza_orders:
    current_pizza = pizza_orders.pop(0)
    print("Your pizza pie is finished!")
    finished_pizzas.append(current_pizza)

#After all of the pizzas have been made, print a message “The pizza {name} was made.” for each finished pizza, replacing {name} with the pizza’s name.

for pizza in finished_pizzas:
    print(f"The pizza {pizza} was made.")


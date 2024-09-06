# Smoothie-Maker

Smoothies are a great way to recover from a workout. We want to create a program that will allow users to create their own smoothie recipes based on ingredients on hand. We will then assess their recipe by giving it a “Drink Score” – based on how drinkable or delicious the smoothie will be – and a “Health Score” – based on how healthy we think the smoothie will be.

Our pantry has only five ingredients on hand:

1. Bananas

2. Strawberries

3. Blueberries

4. Spinach

5. Avocado

The “Drink Score” will be either 0 or 1: 0 if both spinach and avocado are in the smoothie. We consider this recipe “undrinkable”. 1 if only one of spinach and avocado are included (or neither).

The “Health Score” will be 0, 1, or 2: 0 if neither spinach nor avocado is present, 1 if only one of either spinach or avocado is present, and 2 if both ingredients are present.

In this program, we will begin by asking the user about the ingredients on hand. Then, we can ask the user for their recipes – one at a time – and inform them about the scores of their recipes. If the user cannot make the recipe because we are missing an ingredient, we should inform them of that. User’s can enter new recipes until they decide to quit the program.

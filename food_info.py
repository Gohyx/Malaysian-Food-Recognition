import panda as pd

class food_info:
    food_namelist = ["Ayam Goreng",
                    "Bubur Ayam",
                    "Char Kuey Teow",
                    "Curry Puff",
                    "Kaya Toast",
                    "Nasi Goreng",
                    "Nasi Lemak",
                    "Popiah",
                    "Roti Canai",
                    "Satay"]

    malaysian_food = [
        {
            'name':'Ayam Goreng',
            'ingredients':['Chicken','Egg','Flour'],
            'calories':[200,90,54]
        },
        {
            'name':'Bubur Ayam',
            'ingredients':['Rice','Chicken','Onion','Garlic','Ginger','Coriander','Cumin','Coconut Milk','Salt','Pepper'],
            'calories':[220,200,54,4,3,3,3,350,1,1]
        },
        {
            'name':'Char Kuey Teow',
            'ingredients':['Rice Noodles', 'Egg', 'Prawns', 'Bean Sprouts', 'Chili', 'Garlic', 'Onion', 'Coriander', 'Lime Juice', 'Soy Sauce'],
            'calories':[220, 90, 130, 18, 6, 4, 54, 3, 3, 9]
        },
        {
            'name':'Curry Puff',
            'ingredients':['Potatoes', 'Onion', 'Curry Powder', 'Garlic', 'Coriander', 'Cumin', 'Flour', 'Egg', 'Salt'],
            'calories':[120, 54, 9, 4, 3, 3, 120, 90, 1]
        },
        {
            'name':'Kaya Toast',
            'ingredients':['Bread', 'Butter', 'Kaya', 'Egg'],
            'calories':[150, 80, 200, 90]
        },
        {
            'name':'Nasi Goreng',
            'ingredients':['Rice', 'Egg', 'Onion', 'Garlic', 'Chili', 'Shrimp', 'Cumin', 'Coriander', 'Salt', 'Pepper'],
            'calories':[220, 90, 54, 4, 6, 130, 3, 3, 1, 1]
        },
        {
            'name':'Nasi Lemak',
            'ingredients':['Rice', 'Coconut Milk', 'Egg', 'Prawn', 'Fried Anchovies', 'Cucumber', 'Roasted Peanuts'],
            'calories':[220, 350, 90, 130, 200, 18, 120]
        },
        {
            'name':'Popiah',
            'ingredients':['Turnip', 'Carrot', 'Cucumber', 'Onion', 'Garlic', 'Cilantro', 'Shrimp', 'Egg', 'Flour', 'Salt'],
            'calories':[36, 30, 18, 54, 4, 3, 130, 90, 120, 1]
        },
        {
            'name':'Roti Canai',
            'ingredients':['Flour', 'Coconut Milk', 'Egg', 'Salt', 'Butter', 'Yeast'],
            'calories':[120, 350, 90, 1, 80, 9]
        },
        {
            'name':'Satay',
            'ingredients':['Chicken', 'Onion', 'Garlic', 'Cumin', 'Coriander', 'Turmeric', 'Lemongrass'],
            'calories':[200, 54, 4, 3, 3, 3, 3]
        }
    ]

# Create a DataFrame
malaysian_food_df = pd.DataFrame(food_info.malaysian_food)

# Get Nasi Lemak from the dataframe
nasi_lemak_df = malaysian_food_df[food_info.malaysian_food_df['name'] == 'Nasi Lemak']

# Display the content in a table
print(nasi_lemak_df)

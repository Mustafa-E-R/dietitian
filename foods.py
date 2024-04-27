""""
    Food list per meal with by their names, per service sizes and calories

    # Whole list items below was handled using bs4 and pandas, I thought anyone could be able to do it and I
    # did not include these steps
    # I have not been being still sure about the foods are healthy or not, I saw them as just some datas, and I got use
"""

# breakfast
food_list = {
    ######################### breakfast #########################################
    'breakfast': ['Bagel (20z)', 'Cereal, Coco Roos', 'Cereal, Rice Chex', 'Cereal, Toasty-Os', 'Cheese, String',
                  'Cheese, Cottage', 'Egg, Boiled', 'Funnel Cake', 'Granola', 'Juice- Apple', 'Juice- Grape',
                  'Milk, 1%', 'Muffin, Blueberry', 'Muffin, Chocolate', 'Pancakes, Plain', 'Potato Fritter',
                  'Ranchero Taquito', 'Sausage Patty-', 'Syrup, Pancake', 'Waffles, MINI', 'Waffles, WG',
                  'Yogurt- Upstate', 'BBQ Rib Patty', 'Beef, Meatballs', 'Beef/Bean Burrito', 'Chicken, Strips',
                  'Chicken, Kiev', 'Chicken, Pot Pie', 'Chickpea Soup', 'Chili, Vegetarian', 'Cinnamon Roll',
                  'Corn Dog, Chicken', 'Dunker, Bread', 'Gyro, Beef', 'Hashbrown', 'Hot Dog, Beef', 'Hot Dog, Chicken',
                  'Kielbasa', 'Macaroni & Cheese', 'Omelet, Cheese', 'Onion Ring', 'Pizza, WG Pepp',
                  'Pizza, 4x6 Cheese', 'Potato Smile', 'Rainbow Rice', 'Ravioli, beef', 'Ravioli, cheese',
                  'Red Beans & Rice', 'Roast Beef', 'Shrimp Poppers', 'Sloppy Joe w bun', 'Tator Tot Hotdish',
                  'Tempeh, Soy', 'Tofu', 'Vegan Nuggets', 'Veggie Burger', 'Asparagus', 'BBQ Baked Beans',
                  'Bean, Black', 'Bean, Garbanzo', 'Bean, Refried', 'Bean, Kidney', 'Broccoli, Frozen',
                  'Broccoli, Fresh', 'Brussels Sprouts', 'Carrots, Frozen', 'Carrots, Fresh', 'Celery, Fresh',
                  'Corn, Frozen', 'Cucumber', 'Edamame', 'Mashed Potatoes', 'Peas, Frozen', 'Oven Fries',
                  'Peppers, Fresh', 'Potato Smiles(4)', 'Steak Fries', 'Potato Spudster'],

    'service_of_breakfast': ['1', '1 cup', '1 cup', '1 cup', '1', '1/2cup', '1', '1', '2/3 cup', '6.75 oz', '6.75 oz',
                             '8 oz', '1', '1', '2', '1', '1', '2', '2 oz', '1pkg', '2', '4 oz', '1', '5', '1', '3', '1',
                             '1', '1 cup', '4 oz', '1', '1', '1', '5oz', '1', '1', '1', '3oz', '3/4 cup', '1', '5oz',
                             '1 slice', '1 slice', '3oz', '1 cup', '5oz', '5oz', '4oz', '4oz', '1 cup', '1', '1cup',
                             '4oz', '3oz', '4each', '1', '5e', '1/2 cup', '1/2 cup', '1/2 cup', '1/2 cup', '1/2 cup',
                             '1/2 cup', '1/2 cup', '1cup', '1/2 cup', '1/2 cup', '1/2 cup', '1/2 cup', '1/2 cup',
                             '1/2cup', '1/2 cup', '1/2 cup', '1/2 cup', '1/2 cup', '1/2 cup', '1/2cup', '1/2 cup'],

    'calorie_of_breakfast': [280, 100, 100, 100, 80, 210, 60, 280, 120, 90, 100, 110, 190, 190, 210, 230, 180, 140, 60,
                             210, 200, 90, 260, 150, 360, 190, 310, 400, 241, 180, 460, 240, 330, 200, 250, 290, 120,
                             180, 280, 110, 180, 270, 300, 160, 232.21, 290, 200, 207, 110, 238.44, 276.5, 174, 160, 70,
                             180, 170, 20, 80, 143, 19, 109, 15, 15, 20, 38, 25, 13, 72, 8, 80, 100, 62, 180, 15, 90,
                             150, 110, 9],

    ######################## lunch ###############################################
    'lunch': ['Asian Style BBQ Chicken', 'Breakfast Ham & Cheese', 'Breakfast Sausage & Cheese', 'Cheesy Pizza, Extra',
              'Chicken Dunks', 'Chicken Dunks, Uploaded', 'Chicken Pizza', 'Chicken Tacos, Mexican Style',
              'Cinnamon Roll Dippers', 'Cookie Dunks', 'Deep Dish Pizza', 'Dirt Cake Lunch Combinations',
              'Double Cheese Walking Pizza', 'Extra Cheesy Pizza', 'Ham & Cheddar', 'Ham & Cheddar with Crackers',
              'Ham & Cheddar, with Crackers', 'Ham & Swiss Cracker Stackers', 'Ham & Swiss with Crackers',
              'Ham N Cheese', 'Ham, Cheddar & Mini Ritz', 'Hot Dogs, Mini', 'Lunch Combinations'],

    'service_of_lunch': ['1 package ', '1 package ', '1 package ', '1 package ', '1 package ', '1 package ',
                         '1 package ', '1 package ', '1 package ', '1 package ', '1 package ', '1 package ',
                         '1 package ', '1 package ', '1 package ', '1 package ', '1 package ', '1 package ',
                         '1 package ', '83.4 g ', '1 package ', '1 package ', '1 package '],

    'calorie_of_lunch': [230, 210, 260, 320, 250, 400, 220, 340, 300, 250, 420, 230, 250, 270, 260, 260, 260, 260, 260,
                         240, 150, 290, 480],
    ################################ dinner ########################################
    'dinner': ['Fish Chips', 'Pizza', 'Hamburger', 'McDouble', 'Big Mac', 'Cheeseburger', 'Double Cheeseburger',
               'McChicken', 'McSpicy', 'Double McSpicy', 'Filet-O-Fish', 'DoubleFilet-O-Fish', 'Chicken McNuggets',
               'Hotcakes', 'Chicken Porridge', 'Fish Porridge', 'Pork Porridge', 'Century Egg Porride',
               'Char Siew Rice', 'Duck Rice', 'Chicken Rice', 'Fried Rice', 'Nasi Lemak', 'Beef Rendang', 'Rice',
               'Mee Rebus', 'Mee Siam', 'Mee Soto', 'Mee Goreng', 'Hor Fun', 'Laksa', 'Lor Mee', 'Prawn Noodles, Dry',
               'Prawn Noodles, Soup', 'Wanton Noodles, Dry'],

    'service_of_dinner': ['1 serving', '130g', '1 burger', '1 burger', '1 burger', '1 burger', '1 burger', '1 burger',
                          '1 burger', '1 burger', '1 burger', '1 burger', '6 pieces', '3 pieces', '1 bowl', '1 bowl',
                          '1 bowl', '1 bowl', '1 plate', '1 plate', '1 plate', '1 plate', '1 plate', '1 plate',
                          '1 bowl', '1 plate', '1 plate', '1bowl', '1 plate', '1 plate', '1 bowl', '1 bowl', '1 bowl',
                          '1 bowl', '1 bowl'],

    'calorie_of_dinner': [848, 299, 252, 392, 522, 300, 440, 385, 522, 800, 332, 474, 303, 557, 214, 261, 362, 422, 600,
                          706, 702, 508, 600, 228, 260, 558, 519, 432, 660, 708, 589, 383, 459, 293, 409],
    ############################### snack ##########################################
    'snack': ['POWER BAR, chocolate', 'Milk and cereal bar', 'Pretzels, soft', 'Pretzels, soft, unsalted',
              'Rice and Wheat cereal bar', 'Mixed Berry Bar', ' bagel chips, plain', ' banana chips',
              ' beef sticks, smoked', ' brown rice chips', ' CLIF BAR, mixed flavors', 'corn cakes',
              'chips, barbecue-flavor', 'chips, plain', 'chips, unsalted', 'cones, plain', 'onion-flavor',
              'crisped rice bar, almond', ' KRAFT, CORNNUTS, plain', ' oriental mix, rice-based', ' pita chips, salted',
              ' plantain chips, salted', ' popcorn, air-popped', ' popcorn, cakes', ' popcorn, cheese-flavor',
              ' pork skins, plain', ' potato sticks', ' taro chips', ' trail mix, regular', ' trail mix, tropical',
              'Whole milk*', 'Protein-fortified milk*', 'Soy milk*', 'Cheese*', 'Cottage cheese*', 'Yogurt, full-fat*',
              'Greek yogurt, full-fat*', 'Eggnog*', 'Ice cream', 'Slow-Churned Ice Cream',
              'Apple',
              'Chocolate Creme Filled Snack Cake',
              'Chocolate Chip Crisped Rice Bar',
              'Cookie',
              'Doughnut',
              'Hard Granola Bar',
              'Leather Fruit Bar',
              'Licorice',
              'Milk Chocolate Candy Bar',
              'Soft Raisin Granola Bar',
              'Taffy',
              'Air Popped Popcorn',
              'Banana Chips',
              'Beef Jerky',
              'Brown Rice Cakes',
              'Cheese Flavor Popcorn',
              'Cheese Puffs',
              'Corn Chips',
              'Crackers',
              'Hard Pretzels',
              'Mixed Nuts',
              'Peanuts',
              'Salted Potato Chips',
              'Tortilla Chips',
              'Trail Mix'
              ],

    'service_of_snack': ['1 bar', '1 bar', '1 large', '1 large', '1 bar', '1 bar', '1 oz', '1 oz', '1 oz', '1 cake',
                         '1 bar', '1 cake', '1 oz', '1 oz', '1 cup, crushed', '1 oz', '1 oz', '1 bar, (1 oz)', '1 oz',
                         '1 oz', '1 oz', '1 oz', '1 cup', '1 cake', '1 cup', '1 oz', '1 oz', '1 oz', '1 cup', '1 cup',
                         '1 cup', '1 cup', '1 cup', '1 ounce', '½ cup', '6 ounces', '6 ounces', '½ cup', '½ cup',
                         '½ Cup', '1 snack', '1 snack', '1 snack', '1 snack', '1 snack', '1 snack', '1 snack',
                         '1 snack', '1 snack', '1 snack', '1 snack', '1 oz ', '1 oz ', '1 oz ', '1 oz ', '1 oz ',
                         '1 oz ', '1 oz ', '1 oz ', '1 oz ', '1 oz ', '1 oz ', '1 oz ', '1 oz ','1 oz '
                         ],

    'calorie_of_snack': [247, 103, 483, 493, 90, 146, 128, 147, 156, 35, 235, 35, 148, 151, 490, 145, 141, 128, 126,
                         143, 130, 151, 31, 38, 58, 154, 148, 141, 693, 619, 150, 211, 105, 115, 120, 150, 120,
                         180, 130, 100, 72, 188, 113, 49, 190, 118, 81, 41, 235, 193, 44, 110, 147, 116, 110, 149, 158,
                         147, 143, 108, 175, 170, 155, 138, 131]
}

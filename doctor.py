from foods import food_list


class Doctor:
    """
    According to 'https://nationalcareers.service.gov.uk/job-profiles/dietitian'
    what does a dietitian do;
    • assess the nutritional needs of individuals, families or groups.
    • create treatment plans to improve nutrition and overall health.
    • give practical and sensitive dietary advice, tailored to people's needs.
    • monitor people's progress towards healthy eating targets.
    • create and update confidential clinical records.
    """

    def __init__(self):
        """Constructor"""
        self.branch = 'Dietitian'

    @staticmethod
    def calculate_the_bmi(weight: int, height: int):
        """
        Calculate the body mass index

        :param weight: An integer represents the weight in kg.
        :param height: An integer represents the height in cm.
        :return: A float represents the body mass index.
        """

        return round(weight / ((height / 100) ** 2), 1)

    def assess_nutritional_status(self, weight_int_kg: int, height_in_kg: int):
        """
        Assess the nutritional status of the patient.
        :param weight_int_kg: An integer represents the weight in kg.
        :param height_in_kg: An integer represents the height in cm.
        :return: A string represents a nutritional status.
        """

        bmi = self.calculate_the_bmi(weight_int_kg, height_in_kg)
        if bmi < 18.5:
            return 'Underweight'
        elif 15.4 <= bmi < 24.9:
            return 'Normal weight'
        elif 24.9 <= bmi <= 29.9:
            return 'Pre-obesity'
        elif 29.9 < bmi <= 34.9:
            return 'Obesity class I'
        elif 34.9 < bmi < 40:
            return 'Obesity class II'
        else:
            return 'Obesity class III'

    # TODO: assess the nutritional needs of individuals, families or groups
    @staticmethod
    def calculate_calories_needed(lifestyle: str, gender: str, weight: int, height: int, age: int):
        """
        Calculate a calories value, that is a patient need for him/her whole day,
        according to her/him physical activity.

        :param lifestyle: A string represents the physical activity level.
        :param gender: A string represents the gender/sex.
        :param weight: An integer represents the weight in kg.
        :param height: An integer represents the height in cm.
        :param age: An integer represents the age in years.
        :return: A float represents the whole calorie a person will need for whole day.
        """

        # The Basal metabolic rate has calculated by formula of Mifflin-St Jeor Equation.
        bmr = None
        if gender == 'Male':
            bmr = (10 * weight) + (6.25 * height) - (5 * int(age)) - 5
        elif gender == 'Female':
            bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161

        if lifestyle == 'Sedentary':
            return round(bmr * 1.2)
        elif lifestyle == 'Lightly Active':
            return round(bmr * 1.375)
        elif lifestyle == 'Moderately Active':
            return round(bmr * 1.55)
        elif lifestyle == 'Very Active':
            return round(bmr * 1.725)
        elif lifestyle == 'Extra Active':
            return round(bmr * 1.9)

    # TODO: create treatment plans to improve nutrition and overall health
    # TODO: give practical and sensitive dietary advice, tailored to people's needs

    # Create treatment plan and dietary advice to give to the patient
    def create_nutrition_plan(self, lifestyle: str, gender: str, weight: int, height: int, age: int, meal: str):
        """

        :param lifestyle: A string represents the physical activity level.
        :param gender: A string represents the gender/sex.
        :param weight: An integer represents the weight in kg.
        :param height: An integer represents the height in cm.
        :param age: An integer represents the age in years.
        :param meal: A string represents which meal would be evaluated to.
        :return: A dictionary contains lists for seven days of week that are contains foods, their serving sizes, and
        their calories.
        """

        # 21% for breakfast - 33% for lunch - 40% for dinner - 6% for snack: according to
        # 'https://www.ncbi.nlm.nih.gov/books/NBK209815/'

        whole_calorie = self.calculate_calories_needed(lifestyle, gender, weight, height, age)
        per_calorie_sizes = None
        if meal == 'breakfast':
            per_calorie_sizes = 0.21
        elif meal == 'lunch':
            per_calorie_sizes = 0.33
        elif meal == 'dinner':
            per_calorie_sizes = 0.40
        elif meal == 'snack':
            per_calorie_sizes = 0.06

        the_plan = {'day1': {'foods': [], 'services': [], 'calories': []},
                    'day2': {'foods': [], 'services': [], 'calories': []},
                    'day3': {'foods': [], 'services': [], 'calories': []},
                    'day4': {'foods': [], 'services': [], 'calories': []},
                    'day5': {'foods': [], 'services': [], 'calories': []},
                    'day6': {'foods': [], 'services': [], 'calories': []},
                    'day7': {'foods': [], 'services': [], 'calories': []}}
        checking = []
        for i in range(7):
            for food in food_list[meal]:
                i_of_fd = food_list[meal].index(food)
                if sum(the_plan[f'day{i + 1}']['calories']) <= (whole_calorie * per_calorie_sizes):
                    if food_list[f'calorie_of_{meal}'][i_of_fd] <= (whole_calorie * per_calorie_sizes):
                        if food_list[meal][i_of_fd] not in checking:
                            if len(the_plan[f'day{i + 1}']['foods']) < 1:
                                the_plan[f'day{i + 1}']['foods'].append(food_list[meal][i_of_fd])
                                checking.append(food_list[meal][i_of_fd])
                            else:
                                the_plan[f'day{i + 1}']['foods'].append(f'\n{food_list[meal][i_of_fd]}')
                                the_plan[f'day{i + 1}']['services'].append(food_list[f'service_of_{meal}'][i_of_fd])
                                the_plan[f'day{i + 1}']['calories'].append(food_list[f'calorie_of_{meal}'][i_of_fd])
                                checking.append(food_list[meal][i_of_fd])

        # There is no enough data and I created the statement below:
        for day_num in range(7):
            if len(the_plan[f'day{day_num + 1}']['foods']) == 0:
                try:
                    the_plan[f'day{day_num + 1}']['foods'] = the_plan[f'day{day_num - 2}']['foods']
                except KeyError:
                    the_plan[f'day{day_num + 1}']['foods'] = the_plan[f'day1']['foods']
                else:
                    the_plan[f'day{day_num + 1}']['foods'] = the_plan[f'day{day_num - 1}']['foods']

        return the_plan

    # I will handle the steps below, when I have a time
    # TODO: monitor people's progress towards healthy eating targets
    # TODO: create and update confidential clinical records

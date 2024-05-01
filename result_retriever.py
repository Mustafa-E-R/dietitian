from tkinter import *
from tkinter import messagebox
from doctor import Doctor

# Types of Physical Activities
lifestyles = ['Sedentary', 'Lightly Active', 'Moderately Active', 'Very Active', 'Extra Active']
dr = Doctor()


def get_results(old_window, wght, hght, agt, gnd, lstyl):
    """
    Take the form window, that is the first time user face, and weight, height, age, gender, physical activity
    """
    window = old_window
    weight = wght.get()
    height = hght.get()
    age = agt.get()
    gender = gnd.get()
    ls = lstyl.get()
    # TODO: Evaluate the values from the inputs is provided correctly

    # if not then give some warning to the patient
    ballot = []
    if gender not in ['Female', 'Male']:
        messagebox.showwarning('Oops', 'Gender Must be typed as Female or Maleé')
        try:
            ballot.remove('g')
        except ValueError:
            pass

    else:
        ballot.append('g')

    if ls not in lifestyles:
        messagebox.showwarning('Oops', f'The Physical activity must be provided as '
                                       f'\n{lifestyles[0]}(no sport) or '
                                       f'\n{lifestyles[1]}(light sports, 1-3 days a week) or '
                                       f'\n{lifestyles[2]}(moderate sports, 3-5 days a week)'
                                       f'\n{lifestyles[3]}(hard sports, 6-7 days a week )'

                                       f'\n{lifestyles[4]}(very hard sports, physical job or training, twice a day  )')
        try:
            ballot.remove('l')
        except ValueError:
            pass
    else:
        ballot.append('l')

    # if yes then go ahead and handle values
    if ballot == ['g', 'l']:
        # Return the results back to the patient
        breakfast_plan = dr.create_nutrition_plan(ls, gender, weight, height, age, 'breakfast')
        lunch_plan = dr.create_nutrition_plan(ls, gender, weight, height, age, 'lunch')
        dinner_plan = dr.create_nutrition_plan(ls, gender, weight, height, age, 'dinner')
        snack_plan = dr.create_nutrition_plan(ls, gender, weight, height, age, 'snack')

        # Reconfigure the window
        window.destroy()
        new_window = Tk()

        # 1
        body_container = Frame(new_window)
        body_container.grid(row=0, column=0)

        # Create a chart to give information about the bmi and nutritional status
        # 1.1
        top_container = Frame(body_container)
        top_container.grid(row=0, column=0, columnspan=7, pady=10)

        bmi_label = Label(top_container,
                          text=f'BMI: {dr.calculate_the_bmi(weight, height)}', justify='left', font=('BOLD', 13))

        bmi_label.grid(row=0, column=0, padx=20)

        # 1.2
        n_s_label = Label(top_container,
                          text=f'NUTRITIONAL STATUS: {dr.assess_nutritional_status(weight, height)}', justify='left',
                          font=('BOLD', 13))
        n_s_label.grid(row=0, column=1, padx=20)

        # Create a table to give information what should eat the patient
        # 1.3
        time_label = Label(body_container, text='MEAL TIME:', justify='left', relief='raised', font=('BOLD', 12),
                           width=10)
        time_label.grid(row=1, column=0, pady=20)

        breakfast_label = Label(body_container, text='BREAKFAST:', justify='left', relief='raised', font=('BOLD', 11),
                                width=10)
        breakfast_label.grid(row=2, column=0, pady=20)

        lunch_label = Label(body_container, text='LUNCH:', justify='left', relief='raised', font=('BOLD', 11), width=10)
        lunch_label.grid(row=3, column=0, pady=20)

        dinner_label = Label(body_container, text='DINNER:', justify='left', relief='raised', font=('BOLD', 11),
                             width=10)
        dinner_label.grid(row=4, column=0, pady=20)

        snack_label = Label(body_container, text='SNACK:', justify='left', relief='raised', font=('BOLD', 11), width=10)
        snack_label.grid(row=5, column=0, pady=20)

        def i_err_cancel(lst: list, i: int):
            """
            :param lst: A List that would be its length smaller than the parameter i
            :param i: An integer to handle if the list len is smaller than the i
            """
            try:
                lst[i]
            except IndexError:
                pass
            return "".join(lst)

        for r in range(7):
            day_labels = Label(body_container, text=f'DAY {r + 1}', justify='left', relief='raised',
                               font=('BOLD', 10), )
            day_labels.grid(row=1, column=r + 1, padx=3, pady=20)

            meal_bf = Label(body_container, text=f"{i_err_cancel(breakfast_plan[f'day{r + 1}']['foods'], r)}",
                            justify='left', font=('Helvetica', 9))
            meal_bf.grid(row=2, column=r + 1, padx=3, pady=20)

            meal_l = Label(body_container,
                           text=i_err_cancel(lunch_plan[f'day{r + 1}']['foods'], r), justify='left', font=('Helvetica', 9))
            meal_l.grid(row=3, column=r + 1, padx=3, pady=20)

            meal_d = Label(body_container,
                           text=i_err_cancel(dinner_plan[f'day{r + 1}']['foods'], r), justify='left', font=('Helvetica', 9))
            meal_d.grid(row=4, column=r + 1, padx=3, pady=20)

            meal_s = Label(body_container, text=i_err_cancel(snack_plan[f'day{r + 1}']['foods'], r), justify='left', font=('Helvetica', 9))
            meal_s.grid(row=5, column=r + 1, padx=3, pady=20)

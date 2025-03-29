import customtkinter as ctk

def main():

    def runCalculations():
        pass

    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("green")
    ctk.set_widget_scaling(1.0)

    app = ctk.CTk()
    app.geometry('800x700')
    app.minsize(700, 400)
    app.title('Diet Planner')

    app.columnconfigure((0,2), weight=1)
    app.columnconfigure((1,3), weight=3)

    app.rowconfigure((0,2), weight=1)
    app.rowconfigure(1, weight=0)

    app.configure(fg_color="#bbffcc")

    form_frame = ctk.CTkFrame(app, width=800, height=700)
    form_frame.grid(row=1, column=0, columnspan=4, padx=20, pady=20)
    form_frame.configure(fg_color="#99ddaa")

    PADDING_X = (20, 20)
    buttonColor = "#337755"
    buttonHoverColor = "#004400"

    title = ctk.CTkLabel(form_frame, text='Diet Planner', font=('Arial', 24), text_color="#004400")
    title.grid(row=0, column=0, columnspan=4, pady=20)

    gender_label = ctk.CTkLabel(form_frame, text="Gender: ", font=('Arial', 16))
    gender_label.grid(row=1, column=0, padx=PADDING_X, pady=10, sticky='e')
    gender_entry = ctk.CTkOptionMenu(form_frame, width=150, values=["Male","Female"], fg_color="white", text_color="black",  button_color=buttonColor, button_hover_color=buttonHoverColor, dropdown_fg_color="white", dropdown_text_color="black")
    gender_entry.grid(row=1, column=1, padx=PADDING_X, pady=10, sticky='we')

    age_label = ctk.CTkLabel(form_frame, text="Age (years): ", font=('Arial', 16))
    age_label.grid(row=1, column=2, padx=PADDING_X, pady=10, sticky='e')
    age_entry = ctk.CTkEntry(form_frame, width=150)
    age_entry.grid(row=1, column=3, padx=PADDING_X, pady=10, sticky='we')

    weight_label = ctk.CTkLabel(form_frame, text="Weight (lbs): ", font=('Arial', 16))
    weight_label.grid(row=2, column=0, padx=PADDING_X, pady=10, sticky='e')
    weight_entry = ctk.CTkEntry(form_frame, width=150)
    weight_entry.grid(row=2, column=1, padx=PADDING_X, pady=10, sticky='we')

    height_label = ctk.CTkLabel(form_frame, text="Height (inches): ", font=('Arial', 16))
    height_label.grid(row=2, column=2, padx=PADDING_X, pady=10, sticky='e')
    height_entry = ctk.CTkEntry(form_frame, width=150)
    height_entry.grid(row=2, column=3, padx=PADDING_X, pady=10, sticky='we')

    activity_label = ctk.CTkLabel(form_frame, text="Activity Level: ", font=('Arial', 16))
    activity_label.grid(row=3, column=0, padx=PADDING_X, pady=10, sticky='e')
    activity_entry = ctk.CTkOptionMenu(form_frame, width=400, values=["Sedentary", "Lightly active", "Moderately active", "Very active", "Extra active"], fg_color="white", text_color="black", button_color=buttonColor, button_hover_color=buttonHoverColor)
    activity_entry.grid(row=3, column=1, columnspan=3, padx=PADDING_X, pady=10, sticky='we')

    goal_label = ctk.CTkLabel(form_frame, text="Weight Goal: ", font=('Arial', 16))
    goal_label.grid(row=4, column=0, padx=PADDING_X, pady=10, sticky='e')
    goal_entry = ctk.CTkOptionMenu(form_frame, width=400, values=["Lose", "Maintain", "Gain"], fg_color="white", text_color="black", button_color=buttonColor, button_hover_color=buttonHoverColor)
    goal_entry.grid(row=4, column=1, columnspan=3, padx=PADDING_X, pady=10, sticky='we')

    submit_button = ctk.CTkButton(form_frame, text="Find Diet Plan", command=runCalculations, fg_color=buttonColor, hover_color=buttonHoverColor, text_color="white")
    submit_button.grid(row=5, column=0, columnspan=4, padx=PADDING_X, pady=20, sticky="n")

    app.mainloop()


    # gender = input('Please input your gender (Male/Female): ').strip().lower()
    # age = int(input('Please input your age (in years): ').strip())
    # weight = float(input('Please input your weight (in lbs): ').strip())
    # height = float(input('Please input your height (in inches): ').strip())
    # activity_level = input('Please input your activity level (Sedentary, Lightly active, Moderately active, Very active, Extra active): ').strip().lower()
    # goal = input('Please input your goal (Lose, Maintain, Gain): ').strip().lower()
    # rmr = calculate_metabolic_rate(gender, age, weight, height)
    # print(f'Your metabolic rate is {rmr:.0f}')
    # print(f'Your caloric needs are {calculate_calories(rmr, activity_level):.0f}')


    

def calculate_metabolic_rate(gender, age, weight, height):
    weight = weight * 0.453592  # Convert weight from lbs to kg
    height = height * 2.54  # Convert height from inches to centimeters

    if gender == 'female':
        rmr = (10*weight) + (6.25*height) - (5*age) - 161
    else:
        rmr = (10*weight) + (6.25*height) - (5*age) + 5
    return round(rmr,0)

def calculate_calories(rmr, activity_level):
    activity_multiplier = {
        'sedentary': 1.2,
        'lightly active': 1.375,
        'moderately active': 1.55,
        'very active': 1.725,
        'extra active': 1.9
    }
    return round(rmr * activity_multiplier.get(activity_level, 1.2),0)
    

def calculate_protein(weight, goal):
    goal_multiplier = {
        'lose': 1,
        'maintain': .9,
        'gain': .8
    }
    return round(weight * goal_multiplier.get(goal, 1), 0)
    

def calculate_macros(caloric_needs, protein):
    protein_calories = protein * 4
    fat_calories = caloric_needs * .25
    carb_calories = caloric_needs - (protein_calories + fat_calories)
    fat = round(fat_calories / 9, 0)
    carbs = round(carb_calories / 4, 0)
    return protein, fat, carbs    

def get_diet_plan():
    pass

if __name__ == "__main__":
    main()
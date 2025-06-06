import customtkinter as ctk
import requests 

PADDING_X = (20, 20)
buttonColor = "#337755"
buttonHoverColor = "#004400"

def main(): 

    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("green")
    ctk.set_widget_scaling(1.0)

    app = App()

    app.mainloop()

class App(ctk.CTk):
    bmr = 0
    caloric_needs = 0
    protein = 0
    macros = (0, 0, 0)

    def __init__(self):
        super().__init__()

        self.geometry('800x700')
        self.minsize(700, 400)
        self.title('Diet Planner')

        self.columnconfigure((0,2), weight=1)
        self.columnconfigure((1,3), weight=3)

        self.rowconfigure((0,2), weight=1)
        self.rowconfigure(1, weight=0)

        self.configure(fg_color="#bbffcc")
    
        self.form_frame = ctk.CTkFrame(self, width=800, height=700)
        self.result_frame = ctk.CTkFrame(self, width=800, height=700)
        self.diet_frame = ctk.CTkFrame(self, width=800, height=700)

        self.showForm()

    def getDietPlan(self):
        APP_ID = '755a5a1a'
        APP_KEY = '77220d33d8f6d51b6d9a43fda315acae'
        URL = f'https://api.edamam.com/api/meal-planner/v1/{APP_ID}/select'
        HEADERS = {'Content-Type': 'application/json'}
        PARAMS = {'type': ['public'],'app_key': APP_KEY}
        PAYLOAD = {
            "size": 7,
            "plan": {
                "fit": {
                    "ENERC_KCAL": { "min": self.caloric_needs-20, "max": self.caloric_needs+20 },
                    "PROCNT":     { "min": self.macros[0]-10,  "max": self.macros[0]+10  },
                    "CHOCDF":     { "min": self.macros[1]-10,  "max": self.macros[1]+10  },
                    "FAT":        { "min": self.macros[2]-10,   "max": self.macros[2]+10  },
                },
                "sections": {
                    "breakfast": {},
                    "lunch": {},
                    "dinner": {}
                }
            }
        }
        response = requests.post(URL, headers=HEADERS, params=PARAMS, json=PAYLOAD)
        if response.status_code == 200:
            data = response.json()
            meals = data.get('selection', [])
            meal_plan = []
            for meal in meals:
                for section_name, section in day.get('sections', {}).items():
                    if 'assigned' in section:
                        meal_info = {
                            'label': section_name.capitalize(),
                            'recipe_uri': section['assigned'],
                            'recipe_link': section['_links']['self']['href']
                        }
                        meal_plan.append(meal_info)
            self.showDietPlan(meal_plan)
        else:
            print("Error:", response.status_code, response.text)

    def runCalculations(self):
        try:
            self.bmr = calculate_metabolic_rate(self.form_frame.children['!ctkoptionmenu'].get(), int(self.form_frame.children['!ctkentry'].get()), int(self.form_frame.children['!ctkentry2'].get()), int(self.form_frame.children['!ctkentry3'].get()))
            print(self.form_frame.children['!ctkoptionmenu'].get(), int(self.form_frame.children['!ctkentry'].get()), int(self.form_frame.children['!ctkentry2'].get()), int(self.form_frame.children['!ctkentry3'].get()))
            self.caloric_needs = calculate_calories(self.bmr, self.form_frame.children['!ctkoptionmenu2'].get().lower())
            self.protein = calculate_protein(int(self.form_frame.children['!ctkentry2'].get()), self.form_frame.children['!ctkoptionmenu3'].get().lower())
            self.macros = calculate_macros(self.caloric_needs, self.protein)
            self.showResult()
        except ValueError:
            error_label = ctk.CTkLabel(self.form_frame, text="Please enter valid inputs.", font=('Arial', 16), text_color="red")
            error_label.grid(row=6, column=0, columnspan=4, padx=PADDING_X, pady=(0,10), sticky='n')
            return

    def showForm(self):
        self.result_frame.grid_forget()

        self.form_frame.grid(row=1, column=0, columnspan=4, padx=20, pady=20)
        self.form_frame.configure(fg_color="#99ddaa")

        title = ctk.CTkLabel(self.form_frame, text='Diet Planner', font=('Arial', 24), text_color="#004400")
        title.grid(row=0, column=0, columnspan=4, pady=20)

        gender_label = ctk.CTkLabel(self.form_frame, text="Gender: ", font=('Arial', 16))
        gender_label.grid(row=1, column=0, padx=PADDING_X, pady=10, sticky='e')
        gender_entry = ctk.CTkOptionMenu(self.form_frame, width=150, values=["Male","Female"], fg_color="white", text_color="black",  button_color=buttonColor, button_hover_color=buttonHoverColor, dropdown_fg_color="white", dropdown_text_color="black")
        gender_entry.grid(row=1, column=1, padx=PADDING_X, pady=10, sticky='we')

        age_label = ctk.CTkLabel(self.form_frame, text="Age (years): ", font=('Arial', 16))
        age_label.grid(row=1, column=2, padx=PADDING_X, pady=10, sticky='e')
        age_entry = ctk.CTkEntry(self.form_frame, width=150)
        age_entry.grid(row=1, column=3, padx=PADDING_X, pady=10, sticky='we')

        weight_label = ctk.CTkLabel(self.form_frame, text="Weight (lbs): ", font=('Arial', 16))
        weight_label.grid(row=2, column=0, padx=PADDING_X, pady=10, sticky='e')
        weight_entry = ctk.CTkEntry(self.form_frame, width=150)
        weight_entry.grid(row=2, column=1, padx=PADDING_X, pady=10, sticky='we')

        height_label = ctk.CTkLabel(self.form_frame, text="Height (inches): ", font=('Arial', 16))
        height_label.grid(row=2, column=2, padx=PADDING_X, pady=10, sticky='e')
        height_entry = ctk.CTkEntry(self.form_frame, width=150)
        height_entry.grid(row=2, column=3, padx=PADDING_X, pady=10, sticky='we')

        activity_label = ctk.CTkLabel(self.form_frame, text="Activity Level: ", font=('Arial', 16))
        activity_label.grid(row=3, column=0, padx=PADDING_X, pady=10, sticky='e')
        activity_entry = ctk.CTkOptionMenu(self.form_frame, width=400, values=["Sedentary", "Lightly active", "Moderately active", "Very active", "Extra active"], fg_color="white", text_color="black", button_color=buttonColor, button_hover_color=buttonHoverColor)
        activity_entry.grid(row=3, column=1, columnspan=3, padx=PADDING_X, pady=10, sticky='we')

        goal_label = ctk.CTkLabel(self.form_frame, text="Weight Goal: ", font=('Arial', 16))
        goal_label.grid(row=4, column=0, padx=PADDING_X, pady=10, sticky='e')
        goal_entry = ctk.CTkOptionMenu(self.form_frame, width=400, values=["Lose", "Maintain", "Gain"], fg_color="white", text_color="black", button_color=buttonColor, button_hover_color=buttonHoverColor)
        goal_entry.grid(row=4, column=1, columnspan=3, padx=PADDING_X, pady=10, sticky='we')

        submit_button = ctk.CTkButton(self.form_frame, text="View Macros", command=self.runCalculations, fg_color=buttonColor, hover_color=buttonHoverColor, text_color="white")
        submit_button.grid(row=5, column=0, columnspan=4, padx=PADDING_X, pady=20, sticky="n")

    def showResult(self):



        self.form_frame.grid_forget()

        self.result_frame.grid(row=1, column=0, columnspan=4, padx=20, pady=20)
        self.result_frame.configure(fg_color="#99ddaa", )

        back_button = ctk.CTkButton(self.result_frame, text="Back", command=self.showForm, fg_color=buttonColor, hover_color=buttonHoverColor, text_color="white")
        back_button.grid(row=0, column=0, padx=PADDING_X, pady=(20,0), sticky='n')

        title = ctk.CTkLabel(self.result_frame, text='Your calculated diet plan:', font=('Arial', 24), text_color="#004400")
        title.grid(row=1, column=0, padx=20, pady=20)

        metabolic_rate_label = ctk.CTkLabel(self.result_frame, text="Base Metabolic Rate: ", font=('Arial', 18))
        metabolic_rate_label.grid(row=2, column=0, padx=5, pady=(5,0), sticky='we')
        metabolic_rate = ctk.CTkLabel(self.result_frame, text=self.bmr, font=('Arial', 16))
        metabolic_rate.grid(row=3, column=0, padx=PADDING_X, pady=(0,5), sticky='we')

        caloric_needs_label = ctk.CTkLabel(self.result_frame, text="Daily Calories: ", font=('Arial', 18))
        caloric_needs_label.grid(row=4, column=0, padx=5, pady=(5,0), sticky='we')
        caloric_needs = ctk.CTkLabel(self.result_frame, text=self.caloric_needs, font=('Arial', 16))
        caloric_needs.grid(row=5, column=0, padx=PADDING_X, pady=(0,5), sticky='we')

        protein_label = ctk.CTkLabel(self.result_frame, text="Protein (g): ", font=('Arial', 18))
        protein_label.grid(row=6, column=0, padx=5, pady=(5,0), sticky='we')
        protein = ctk.CTkLabel(self.result_frame, text=self.macros[0], font=('Arial', 16))
        protein.grid(row=7, column=0, padx=PADDING_X, pady=(0,5), sticky='we')

        fat_label = ctk.CTkLabel(self.result_frame, text="Fat (g): ", font=('Arial', 18))
        fat_label.grid(row=8, column=0, padx=5, pady=(5,0), sticky='we')
        fat = ctk.CTkLabel(self.result_frame, text=self.macros[1], font=('Arial', 16))
        fat.grid(row=9, column=0, padx=PADDING_X, pady=(0,5), sticky='we')

        carbs_label = ctk.CTkLabel(self.result_frame, text="Carbohydrates (g): ", font=('Arial', 18))
        carbs_label.grid(row=10, column=0, padx=5, pady=(5,0), sticky='we')
        carbs = ctk.CTkLabel(self.result_frame, text=self.macros[2], font=('Arial', 16))
        carbs.grid(row=11, column=0, padx=PADDING_X, pady=(0,10), sticky='we')

        diet_button = ctk.CTkButton(self.result_frame, text="Get Diet Plan", command=self.getDietPlan, fg_color=buttonColor, hover_color=buttonHoverColor, text_color="white")
        diet_button.grid(row=12, column=0, padx=PADDING_X, pady=(0,20), sticky='n')

    def showDietPlan(self, meal_plan):
        print(meal_plan)
        self.result_frame.grid_forget()

        self.diet_frame.grid(row=1, column=0, columnspan=4, padx=20, pady=20)
        self.diet_frame.configure(fg_color="#99ddaa", )

        title = ctk.CTkLabel(self.diet_frame, text='Your Diet Plan:', font=('Arial', 24), text_color="#004400")
        title.grid(row=0, column=0, padx=20, pady=20)


def calculate_metabolic_rate(gender, age, weight, height):
    weight = weight * 0.453592  # Convert weight from lbs to kg
    height = height * 2.54  # Convert height from inches to centimeters
    gender = gender.lower()
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
    protein = round(float(protein), 0)
    return protein, fat, carbs

if __name__ == "__main__":
    main()
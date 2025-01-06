label parameter_1_1:
    $ name1 = renpy.input("Name it: ")
    $ name1 = name1.strip()
    "Name: [name1]"
    menu:
        "Choose a Dominant Personality Trait"

        "Cunning":
            $ person_type1 += 1
            jump parameter_2_1
        "Deceitful":
            $ person_type2 += 1
            jump parameter_2_1
        "Aggressive":
            $ person_type1 += 1
            jump parameter_2_1
        "Naieve":
            $ person_type2 += 1
            jump parameter_2_1

label parameter_2_1:
    menu:
        "How sociable is this person?"

        "Eventually Divorced":
            $ person_type2 += 1
            jump parameter_3_1

        "Married with Children that Hate Them":
            $ person_type2 += 1
            jump parameter_3_1

        "Sociopathic and Charming":
            $ person_type2 += 1
            jump parameter_3_1

label parameter_3_1:
    menu:
        "Is this person physically active?"

        "Somewhat":
            $ person_type1 += 1

        "No":
            $ person_type2 += 1

    "Calculating data..."
    "Person generated."
    menu:   
        "View Adult Facial Data":
            if person_type1 > person_type2:
                show p101
            else:
                show p102
    $ person_type1 = 0
    $ person_type2 = 0
    "I should check the report."

    menu:
        "View Report":
            jump report


label report:
    "Report for [name1]:"
    "Life Expectancy: 45 years"
    "Happiness: 12"
    "Sadness: 88"
    "Likelihood to Kill: NaN"

    menu:
        "Initiate Time Control Lifetime Highlight Reel":
            jump lifetime1

label lifetime1:
    hide p101
    hide p102
    show bg lifespan1
    pause 17.98
    hide bg lifespan1
    show bg desk
    $ kills += 3
    $ happy -= 1
    $ sad += 1
    $ people += 1

    "Data tab updated."
    menu:
        "Generate Another Person":
            jump parameter_1_2
        "Watch again":
            jump lifetime1
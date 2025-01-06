label parameter_1_2:
    $ name1 = renpy.input("Name it: ")
    $ name1 = name1.strip()
    "Name: [name1]"
    menu:
        "Choose a Dominant Personality Trait"

        "Silly":
            $ person_type1 += 1
            jump parameter_2_2
        "Genius":
            $ person_type2 += 1
            jump parameter_2_2
        "Jovial":
            $ person_type1 += 1
            jump parameter_2_2
        "Serious":
            $ person_type2 += 1
            jump parameter_2_2

label parameter_2_2:
    menu:
        "How sociable is this person?"

        "Friendly and Promiscuous":
            $ person_type2 += 1
            jump parameter_3_2

        "Easily Manipulated":
            $ person_type2 += 1
            jump parameter_3_2

        "Socially Awkward":
            $ person_type2 += 1
            jump parameter_3_2

label parameter_3_2:
    menu:
        "Is this person physically active?"

        "Constantly":
            $ person_type1 += 1

        "Most of the time":
            $ person_type2 += 1

    "Calculating data..."
    "Person generated."
    menu:   
        "View Adult Facial Data":
            if person_type1 > person_type2:
                show p201
            else:
                show p202
    $ person_type1 = 0
    $ person_type2 = 0
    "I should check the report."

    menu:
        "View Report":
            jump report2


label report2:
    "Report for [name1]:"
    "Life Expectancy: 75 years"
    "Happiness: 67"
    "Sadness: 33"
    "Likelihood to Kill: Half"

    menu:
        "Initiate Time Control Lifetime Highlight Reel":
            jump lifetime2

label lifetime2:
    hide p201
    hide p202
    show bg lifespan2
    pause 25.64
    hide bg lifespan2
    show bg desk
    $ kills += 26000000
    $ happy += 1
    $ sad -= 1
    $ people += 1

    "Data tab updated."
    menu:
        "Generate Another Person":
            jump parameter_1_2
        "Watch again":
            jump lifetime1
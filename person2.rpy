label parameter_1_2:
    $ name1 = renpy.input("Name it: ")
    $ name1 = name1.strip()
    "Name: [name1]"
    menu:
        "Choose a Dominant Personality Trait"

        "Silly, with a penchant for wearing socks with sandals. Neutral otherwise.":
            $ person_type1 += 1
            jump parameter_2_2
        "Freaky and weird.":
            $ person_type2 += 1
            jump parameter_2_2
        "Jovial and happy-go-lucky book worm.":
            $ person_type1 += 1
            jump parameter_2_2
        "Serious on the outside, but playful on the inside.":
            $ person_type2 += 1
            jump parameter_2_2

label parameter_2_2:
    menu:
        "How sociable is this person?"

        "Friendly to people who commit fashio faux pas. Completely neutral towards people with dress sense.":
            $ person_type2 += 1
            jump parameter_3_2

        "Potentially popular when they remember to eat one serving of legumes per week. Otherwise, only slightly popular.":
            $ person_type2 += 1
            jump parameter_3_2

        "Anxious if they are at a train station due to trauma brought on by a public access cartoon about anthropomorphic trains":
            $ person_type2 += 1
            jump parameter_3_2

label parameter_3_2:
    menu:
        "Is this person physically active?"

        "Constantly lifting weights incorrectly, resulting in physical injury.":
            $ person_type1 += 1

        "Most of the time they are running away from their problems. To do this, they literally run. Extemely sweaty.":
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
            jump parameter_1_3
        "Watch again":
            jump lifetime2

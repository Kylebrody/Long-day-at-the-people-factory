label parameter_1_3:
    $ name1 = renpy.input("Name it: ")
    $ name1 = name1.strip()
    "Name: [name1]"
    menu:
        "Choose a Dominant Personality Trait"

        "Funny and sarcastic in the presence of clowns. Not funny or sarcastic in the presence of mimes. Neutral otherwise.":
            $ person_type1 += 1
            jump parameter_2_3
        "Determined to answer the question of the meaning of life. Extremely serious. Too stupid to ever figure it out.":
            $ person_type2 += 1
            jump parameter_2_3
        "Whimsical and unpredictable on their birthday. Otherwise, very serious.":
            $ person_type1 += 1
            jump parameter_2_3
        "Very interested in anthropods, particularly the Giant wētā. Extemely knowledgeable. This exteme interest makes them a bit of a bore.":
            $ person_type2 += 1
            jump parameter_2_3

label parameter_2_3:
    menu:
        "How sociable is this person?"

        "Easily makes friends with people who have the same favorite color. Otherwise, very shy.":
            $ person_type2 += 1
            jump parameter_3_3

        "The life of the party if the party provides both cake and ice cream. Extremely aggressive and anti social at parties that provide N/A beer.":
            $ person_type2 += 1
            jump parameter_3_3

        "Socially awkward and only speaks in riddles. Very charming.":
            $ person_type2 += 1
            jump parameter_3_3

label parameter_3_3:
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
                show p301
            else:
                show p302
    $ person_type1 = 0
    $ person_type2 = 0
    "I should check the report."

    menu:
        "View Report":
            jump report3


label report3:
    "Report for [name1]:"
    "Life Expectancy: 85 years"
    "Happiness: 100"
    "Sadness: 0"
    "Likelihood to Kill: Half and one quarter"

    menu:
        "Initiate Time Control Lifetime Highlight Reel":
            jump lifetime3

label lifetime3:
    hide p301
    hide p302
    show bg lifespan3
    pause 25.64
    hide bg lifespan3
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
            jump lifetime3
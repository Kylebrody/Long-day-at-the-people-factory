label start:
    "You are an employee at The People Factory, a company that generates humans under the direction of The LORD, and his supervisor The People Person."
    "In the dead of night you are summoned to a telepathic transmission."
    "The LORD speaks..."
    show bg heaven

    # Add your text or actions
    g "Employees from Earth..."
    g "I have summoned you to this all hands meeting to discuss the future of The People Factory."
    g "We have updated our system to version 2.0, which allows for more dynamic human generation."
    g "You will report in to The People Person when you arrive in the morning for your assignments."
    g "Oh and one more thing..."
    g "Your data will be tracked and analyzed for efficiency. It's a new year. Your data tab is clean. Use this oppotunity for a fresh start, and lets see some good numbers."
    g "Wake up, and get to work."

label morningone:
    hide bg heaven
    show screen button
    show bg bedroom
    "You wake up in your bedroom, and get ready for work."
    "You need to greet your wife. She is probably awake by now."

    hide bg bedroom
    show bg livingroom
    $ wifename = renpy.input("Your wifes name is... ")
    $ wifename = wifename.strip()
    w "Good morning sweetheart. I heard you up talking to The LORD last night!"
    mc "Yes, I was summoned to a telepathic transmission. The LORD has updated the system to version 2.0."
    w "That's great news! I hope you have a good day at work."
    mc "I hope I do too. I'll see you when I get home."

    hide bg livingroom
    show bg hallway
    menu:
        "God is calling. Answer the call, or see him at work?"
        "Answer the call":
            jump call
        "See him at work":
            jump walk_to_work

label call:
    mc "Hello?"
    pp "Hey slugger. I see you're up and at 'em."
    mc "Oh hey People Person. I'm on my way to work."
    pp "Great. See me in my office when you get here. We have a lot to discuss."
    mc "I'll see you soon."
    jump walk_to_work

label walk_to_work:
    hide bg hallway
    show bg sidewalk
    menu: 
        "Walk to work":
            jump office

label office:
    hide bg sidewalk
    show bg out_office
    "You arrive at The People Factory. It's time to get to work."
    hide bg out_office
    show bg office_lobby

    menu:
        "Head to The People Person's office":
            jump people_person_intro
        "Go to your desk":
            jump people_person_intro

label people_person_intro:
    show bg office_lobby
    hide bg office_lobby
    show bg office_lobby_pp
    pp "Good morning. I hope you had a good night's rest."
    mc "I did. I'm ready to get to work."
    pp "I'll bet you are."
    mc "... Did you want to meet now?"
    pp "Yes. Follow me."
    hide bg office_lobby_pp
    show bg pp office
    pp "Welcome to my office. Let's talk turkey, shooter."
    mc "Okay."
    pp "With 2.0 officially in place, we are tracking all people data."
    pp "We are looking for efficiency. We are looking for quality."
    pp "The LORD wanted you excommunicated last year. You were on the chopping block."
    pp "But I fought for you. I believe in you."
    pp "So we have some special features for you and only you to use."
    pp "The People Factory is a business. We need to innovate to stay ahead."
    pp "We are giving you the power to make people from a set of dynamic conditions."
    pp "You will use time control to see out their lives. You will be able to see their data. Make successful people, and report the conditions to me as soon as you do."
    pp "This is your chance to prove yourself. Do not fail."
    pp "Now get to work."
    mc "Yes sir."

    menu:
        "Go to your desk":
            jump desk

label desk:
    hide bg pp office
    show bg desk
    "You sit at your desk. It's time to generate some people."
    "The software takes a moment to load. Finally you are greeted with a screen."

    menu:
        "Welcome to Personhood 2.0. Begin":
            jump parameter_1_1


            
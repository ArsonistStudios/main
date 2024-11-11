
define switch = True

label story:
    play music t4
    "debug"
    window hide
    scene bg m_house with dissolve_scene_full:
        truecenter
        linear 4.5 zoom 1.2
    pause 1.5
    scene bg m_room
    window auto

    show monika 1a at t21
    m "..."
    m "it's already morning..."
    m "i think i'll sleep a little more..."
    m "..."
    m "shit the bus!"
    hide monika with moveoutleft
    show bg school_f with fade
    pause(1.0)
    show bg school_int_1
    show monika 1a at t41
    show kylar 1a at rightin
    "yo, catch!"
    hide kylar with moveoutleft
    show monika 1a at t11
    m "jesus christ, how are they so active at 8 in the morning here."
    show crispin 1a at t33
    "yo, girl, you uh- you look kinda new here,  huh?"
    show monika 1a at t21
    m "hey... i'm new yeah... bye now."
    "w-wait! would you huh, like, i could help you get around the school if you want, like, yeah."
    m  "no thanks, i can handle it."
    "are you sure? this is a huh, pretty big school, it's not a problem for me i swear i just wanna help you."
    menu:
        "Fuck no i'd rather go to class":
            jump choice1A
        "Destroy him mentally and skip class":
            jump choice1B
        "fine, what's the worst that could happen?":
            jump choice1C

label choice1A: # sayori beginnig replaces Jecka
    m "shut up, just leave me alone."
    pause

label choice1B: # natsuki beginning replaces Emily
    m "Dude, no matter what you do, you will not get me to fuck you."
    "..."
    "what? you thought that was my intention? nahh you're like, totally off."

label choice1C: # yuri beginning replaces Karen
    m "fine, i guess"
    "oh thats great! you'll have a lot of fun-"
    pause
    


    
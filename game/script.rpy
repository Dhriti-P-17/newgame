# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
image sacrifice_full = Movie(play="sacrifice.webm", loop=False)
image dog_dead = Movie(play="dogdead.webm", loop=False)
image cat_dead = Movie(play="catdead.webm", loop=False)

# The game starts here.
define config.default_text_cps = 30
define p = Character("Parents")
define m = Character("Mom")
define n = Character("Narrator")
define y = Character("You")

transform fit_screen:
    zoom (config.screen_width / 1920)
transform fit_1560:
    zoom (config.screen_width / 1560)
transform character_fit:
    zoom (config.screen_width / 1700)
transform sacrifice_fit:
    zoom (config.screen_width / 1536)

screen choose_pet:
    frame:
        align (0.5, 0.5)
        has vbox

        textbutton "Puppy":
            action [Hide("choose_pet"), Jump("puppy_scenario")]

        textbutton "Kitty":
            action [Hide("choose_pet"), Jump("kitty_scenario")]

screen kill_dog:
    frame:
        align (0.5, 0.5)
        has vbox

        textbutton "I'm fine with that...":
            action [Hide("kill_dog"), Jump("puppy_death")]

        textbutton "OF COURSE NOT!!!":
            action [Hide("kill_dog"), Jump("you_death")]

screen kill_cat:
    frame:
        align (0.5, 0.5)
        has vbox

        textbutton "I'm fine with that...":
            action [Hide("kill_cat"), Jump("kitty_death")]

        textbutton "OF COURSE NOT!!!":
            action [Hide("kill_cat"), Jump("you_death")]




image sacrifice_small = Movie(play="sacrifice.webm", size=(800, 600))
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.


    scene orphanage rm

    show parents happy at character_fit

    p "Hi, Lucy. We are going to be your new parents. We know how much you've been through. "
    p "We are here to support you, so make yourself comfortable."
    y "Oh, uh..."
    y "Thank you."
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    scene girl bedroom at fit_screen

    show parents happy at character_fit

    p "So this is your new room. It is your personal space, so we won't come in here without your permission."
    p "Remember Lucy, we want you to be happy in your new home!"
    y "Okay, thanks. Mom and Dad, is it okay if I go play outside?"
    p "Sure, sweetie! Go ahead!"

    scene cat dog road at sacrifice_fit

    y "Oh...what's this?"
    y "Hi kitty...hi puppy...you guys are so cute!"
    y "Why are you all alone? Where is your mommy?"
    y "...maybe I should take you home."
    y "Let me ask Mommy and Daddy... I'll be right back!"

    scene living room at sacrifice_fit

    show parents happy at character_fit

    y "Mommy, Daddy!"
    p "Yes, sweetie?"
    y "I found a cute little kitty and a puppy on the street. They're all alone. Can we keep them both? Please?"
    p "*sigh*"
    p "Okay, you can have a pet. But on two conditions: you can only have one of them, and you have to take good care of her."
    y "Yay! You are the best parents ever!"

    scene cat dog road at sacrifice_fit
    y "Hmmm...which one should I take?"
    call screen choose_pet

     




label puppy_scenario:
    y "Come on puppy, let's take you home!"

    scene living room at sacrifice_fit  

    show parents happy at character_fit

    show dog small at character_fit

    y "See, here she is!"

    p "She is adorable! What's her name?"
    y "Hmm... I like 'Bella, Lucy's daughter'. What do you think?"
    m "*laughs*"
    m "It's a great name! And we can also call her Bella for short."
    y "Yay!"

    scene clock at sacrifice_fit
    n "A day passes by..."

    scene dog injured at sacrifice_fit

    y "Oh my gosh, Bella! What happened? Why do you have a bruise?"
    y "...maybe you probably just bumped into something. Let me wash your bruise."
    scene clock at sacrifice_fit
    n "Another day passes by..."

    scene dog injured2 at sacrifice_fit

    y "..Bella? Why do you keep getting injured?! I should tell my parents..."
    
    scene living room at sacrifice_fit

    show parents happy at character_fit

    y "Mom, Dad! Why    does Bella keep getting hurt?"
    m "Sweetie, she's probably just bumping into things. She's just a clumsy little puppy."
    y "Yeah, but she seems really hurt."
    p "Lucy, don't worry about it. We'll make sure to take care of that dog."
    m "Are you sure? ...you know what, I'll just go play with Bella."

    scene clock at sacrifice_fit
    n "Another day goes by..."

    scene dog injured3 at sacrifice_fit
    m "AAAAAHHH! What happened?! Something is truly wrong!"

    scene living room at sacrifice_fit  

    show parents happy at character_fit

    y "Mom, Dad, something is seriously wrong. It looks like Bella got beat up by rowdy gangsters or something."

    scene living room at sacrifice_fit

    show parents angry at character_fit

    m "We're sorry, Lucy. We didn't want you to find out about us like this. But we've been hurting the dog."
    y "What?! Why???"
    m "Because we couldn't stand the thought of losing you, Lucy..."
    y "Are you crazy?! You literally just adopted me a few days ago!"
    p "We know, but we still can't bear the thought of you not loving us."
    p "So now we will have to kill this dog."

    call screen kill_dog
    hide screen kill_dog
    scene black
    n "From this point onwards, Bella would never be able to feel the soft soil underneath her paws. The warm sunlight on her fur. All because of the choices that YOU made."
    n "THE END"
    # This ends the game.


label kitty_scenario:
    y "Come on kitty, let's take you home!"

    scene living room at sacrifice_fit  

    show parents happy at character_fit

    show cat small at character_fit

    y "See, here he is!"

    p "He is adorable! What's his name?"
    y "Hmm... I like 'Oliver'. What do you think?"
    m "*laughs*"
    m "I love it! So fun!"
    y "Yay! Welcome home, Oliver."

    scene clock at sacrifice_fit
    n "A day passes by..."

    scene cat injured1 at sacrifice_fit

    y "Oliver! What happened? Why do you have a bruise?"
    y "...did you get into a fight with another cat? Well, don't do that again, or you're going to get hurt even more. Let me wash your bruise."
    scene clock at sacrifice_fit
    n "Another day passes by..."

    scene cat injured2 at sacrifice_fit

    y "..Oliver? Why do you keep getting injured?! I should tell my parents..."
    
    scene living room at sacrifice_fit

    show parents happy at character_fit

    y "Mom, Dad! Why does Oliver keep getting hurt?"
    m "Sweetie, he's probably just bumping into things. he's just a clumsy little kitten."
    y "Yeah, but he seems really hurt."
    p "Lucy, don't worry about it. We'll make sure to take care of that cat."
    m "Are you sure? ...you know what, it's okay. I'll just go play with Oliver."

    scene clock at sacrifice_fit
    n "Another day goes by..."

    scene cat injured3 at sacrifice_fit
    m "AAAAAHHH! What happened?! Something is truly wrong!"

    scene living room at sacrifice_fit  

    show parents happy at character_fit

    y "Mom, Dad, something is seriously wrong. It looks like Oliver got run over by a speeding truck or something."

    scene living room at sacrifice_fit

    show parents angry at character_fit

    m "We're sorry, Lucy. We didn't want you to find out about us like this. But we've been hurting the cat."
    y "What?! Why???"
    m "Because we couldn't stand the thought of losing you, Lucy..."
    y "Are you crazy?! You literally just adopted me a few days ago!"
    p "We know, but we still can't bear the thought of you not loving us."
    p "So now we will have to kill this cat."

    call screen kill_cat
    hide screen kill_dog
    scene black
    n "From this point onwards, Oliver would never be able to feel the soft soil underneath his paws. The warm sunlight on his fur. All because of the choices that YOU made."
    n "THE END"
    # This ends the game.
 

label you_death:
    scene sacrifice_full 
    y "Wait! NO!"
    window hide
    pause 10.0
    window show
    hide screen sacrifice_full
    scene black
    n "She never opened her eyes again..."
    n "THE END"
    $ renpy.quit()

label kitty_death:
    scene cat_dead
    y "NOOOO! WHYYYYY?!?!?!??!"
    $ renpy.quit()

label puppy_death:
    scene dog_dead
    y "NOOOO! WHYYYYY?!?!?!??!"
    $ renpy.quit()


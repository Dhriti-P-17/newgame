# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

define p = Character("Parents")
define m = Character("Mom")
define n = Character("Narrator")
define y = Character("You")

label start:


    transform fit_screen:
        zoom (config.screen_width / 1920)
    transform fit_1560:
        zoom (config.screen_width / 1560)
    transform character_fit:
        zoom (config.screen_width / 1700)

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

    scene dog road at fit_1560

    y "Oh, hi there, puppy!"
    y "Why are you all alone? Where is your mommy?"
    y "...Maybe I should take you home."
    y "Let me ask Mommy and Daddy... I'll be right back!"

    scene living room at fit_1560

    show parents happy at character_fit

    y "Mommy, Daddy!"
    p "Yes, sweetie?"
    y "I found a cute little puppy on the street. She's all alone. Can we keep her? Please?"
    p "*sigh*"
    p "Okay, you can keep her. But on one condition: you have to take good care of her."
    y "Yay! You are the best parents ever!"

    scene dog road at fit_1560

    y "Come on puppy, let's take you home!"

    scene living room at fit_1560

    show parents happy at character_fit

    show dog small 

    y "See, here she is!"

    p "She is adorable! What's her name?"
    y "Hmm... I like 'Bella, Lucy's daughter'. What do you think?"
    m "*laughs*"
    m "It's a great name! And we can also call her Bella for short."
    y "Yay!"

    scene clock at fit_1560
    n "A day passes by..."

    scene dog injured at fit_1560

    y "Oh my gosh, Bella! What happened? Why do you have a bruise?"
    y "...maybe you probably just bumped into something. Let me wash your bruise."

    scene dog injured2 at fit_1560

    y "Bella! Why do you keep getting injured? I should tell my parents"
    
    scene living room at fit_1560

    show parents happy at character_fit

    y "Mom, Dad! Why does Bella keep getting hurt?"
    m "Sweetie, she's probably just bumping into things. She is only just a clumsy little puppy."
    y "Yeah, but she seems really hurt."
    p "Lucy, don't worry about it. We'll make sure to take care of that dog."
    m "If you're sure? I'll just go play with Bella."

    scene clock at fit_1560
    n "Another day goes by..."

    scene dog injured3 at fit_1560
    m "AAAAAHHH! What happened. Something is truly wrong!"

    scene living room at fit_1560

    show parents happy at character_fit

    y "Guys, something is seriously wrong. It looks like Bella got beat up or something."

    scene living room at fit_1560

    show parents angry at character_fit

    m "I'm sorry Lucy. We didn't want you to find out about us like this. "
    # This ends the game.

    

     


    return

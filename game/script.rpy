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
    y "Oh, uh."
    y "Thank you."
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    scene girl bedroom at fit_screen

    show parents happy at character_fit

    p "So, this is your new room. It is your personal space, so we won't come in here without your permission"
    p "Remember that we want you to be happy in your new home Lucy!"
    y "Okay, thanks. Mom and Dad, is it okay if I go play outside?"
    p "Sure, sweetie"

    scene dog road at fit_1560

    y "Oh hi there, puppy"
    y "Why are you all alone? Where is your mommy."
    y "I should take you home."
    y "Let me ask Mommy and Daddy... I'll be right back!"

    scene living room at fit_1560

    show parents happy at character_fit

    y "Mommy, Daddy!"
    p "Yes, sweetie!"
    y "I found a cute little puppy on the street. She's all alone. Can we keep her? Please"
    p "*sigh"
    p "Okay fine, but you have to take good care of her."
    y "Yay! You are the best parents ever!"

    scene dog road at fit_1560

    y "Come on puppy, lets take you home!"

    scene living room at fit_1560

    show parents happy at character_fit

    show dog small 

    y "See, here she is!"

    p "She is addorable! What's her name"
    y "Bella, Lucy's daughter"
    m "*laughs"
    m "We can call her Bella for short"
    y "Yay!"

    scene clock at fit_1560
    n "A day passes by..."






    # This ends the game.

    

     


    return

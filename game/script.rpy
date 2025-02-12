init python:
    import random


define m = Character("Monica")


# The game starts here.

label start:
    $ hp = 50
    $ stamina = 50
    $ strenght = 50

 
    scene bg world
    
    "Welcome to Animated Game!"
    show monica normal2 with dissolve
    "I am Monica and I am your character"
    m "We are in the Animated World"
    m "Thats where our story begins!"

    m "Now I am no one that means I have low character statistics"
    m "These are my statistics"
    "HP: [hp]\nStamina: [stamina]\nStrenght: [strenght]"

    
    
    m "It's time to check your luck in character lottery"
    m "If you're not ready, abandon game"
    hide monica normal2 with dissolve
    scene bg cards with dissolve

    
 
    $ char = random.randint(0, 5)

label choice:
    menu:
        "Check":
            #if char == char[i]:
            #    jump char[i]:
            if char == 0:
                jump Normal
            elif char == 1:
                jump Warrior
            elif char == 2:
                jump Mage
            elif char == 3:
                jump Rogue
            elif char == 4:
                jump Paladin
            else:
                jump end
        "Abandon":
            jump end
    


label Normal:
    scene bg world with dissolve
    show monica normal2 with dissolve
    m "I am still no one. You shouldn't do lotterys any more..."
    jump end

label Warrior:
    $ hp += 50
    $ stamina += 30
    $ strenght += 40
    scene bg world with dissolve
    show monica warrior with dissolve
    m "Now I am Warrior"
    m "These are my statistics"
    "HP: [hp]\nStamina: [stamina]\nStrenght: [strenght]"
    jump end

label Mage:
    $ hp += 30
    $ stamina += 30
    $ strenght += 20
    scene bg world with dissolve
    show monica mage2 with dissolve
    m "Now I am Mage"
    m "These are my statistics"
    "HP: [hp]\nStamina: [stamina]\nStrenght: [strenght]"
    jump end

label Rogue:
    $ hp += 20
    $ stamina += 30
    $ strenght += 30
    scene bg world with dissolve
    show monica rogue with dissolve
    m "Now I am Rogue"
    m "These are my statistics"
    "HP: [hp]\nStamina: [stamina]\nStrenght: [strenght]"
    jump end

label Paladin:
    $ hp += 70
    $ stamina += 30
    $ strenght += 30
    scene bg world with dissolve
    show monica paladin with dissolve
    m "Now I am Paladin"
    m "These are my statistics"
    "HP: [hp]\nStamina: [stamina]\nStrenght: [strenght]"
    jump end



label end:
    "See you later!"

    return

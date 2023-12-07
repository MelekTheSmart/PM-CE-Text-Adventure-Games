def render_introduction():
    '''
    Create the message to be displayed at the start of your game.
    Returns:
        str: The introductory text of your game to be displayed.
    '''
    return "Welcome, brave hero, to the kingdom of Thaloria. \n\nYou are a soldier in the king's army, but not just any soldier - you are an Eldritch Knight, a master of both the sword and the arts of magic. \n\nRecently, the king has lost contact with the city of Azuth, which is home to many great wizards and the great Wizard's Tower, a repository of great knowledge and ancient artifacts.\n\nThe blackness of a thunderstorm accents the walls of the city, and a flash of lightning outlines the great Tower before you."
def create_world():
    '''
    Creates a new version of the world in its initial state.
    Returns:
        World: The initial state of the world
    '''
    def create_map():
        return {
            'gate':{
                'neighbors':['center'],
                'about':"A grand wooden gate stands before you.",
                'stuff': []
            },
            'city center':{
                'neighbors':['gate','shop','cottage','armor'],
                'about':"The city's center lies eerily silent, empty save the shadows, a few dark and cold buildings... \nAnd an armored figure? It took you a second to notice them. They seem to be guarding the Tower.\n\nYour gut tells you to search for clues first...",
                'stuff':[]
            },
            'armored figure':{
                'neighbors':['center','armor_sneak','armor_fight'],
                'about':"It appears like it will attack anyone who gets close - but you have a plan.",
                'stuff':[]
            },
            'sneak':{
                'neighbors':['armor_sneak_box','armor_sneak_tree'],
                'about':"You decide stealth is the way to go - there appear to be two decent hiding spots that you can get to the Tower's doors from - a large tree, and a modest-sized box.",
                'stuff':[]
            },
            'the box':{
                'neighbors':["tower f1"],
                'about':"The box looks like a better hiding spot than the tree, and you're right! The armor begins to move away from your area, giving you just enough time to get to the door!",
                'stuff':[]
            },
            'the tree':{
                'neighbors':["fight the armor"],
                'about':"The tree looks like a good place, but when you start to move towards it, the animated armor takes notice and an ear-piercing shriek emits from it as it surges towards you.\nOnly one thing to do now!",
                'stuff':[]
            },
            'fight the armor':{
                'neighbors':["sword, fireball"],
                'about':"As the armor begins to advance, you must choose the weapon that will work best.",
                'stuff':[]
            },
            'armor_sword':{
                'neighbors':["tower f1"],
                'about':"It seems to hit only air, until the arm plates fall to the ground. You take another swing at where the neck should be, and down falls the helmet.\nThe armor stand for a second before crumpling into a pile of mundane steel, the animating sprit having left.",
                'stuff':[]
            },
            'armor_lost':{
                'neighbors':[],
                'about':"A fireball should do quite nicely, you decide - but foolishly. As soon as you begin reciting the incantation to summon the inferno, the armor is upon you.",
                'stuff':[]
            },
            'cottage':{
                'neighbors':['city center'],
                'about':"This small cottage appears to be abandoned. Something isn't right...",
                'stuff':["shadow"]
            },
            'old store':{
                'neighbors':['city center'],
                'about':"This small store appears to be abandoned, but maybe there's something here...",
                'stuff':["history book"]
            },
            'tower f1':{
                'neighbors':['center','tower f2'],
                'about':"A grand spiral staircase is before you, with each stair labeled with three different letters - it seems random. Beside the stairs is a stone pedestal, with some writing engraved on it.",
                'stuff':["staircase","pedestal"]
            },
            'staircase':{
                'neighbors':['tower f1', 'tower f2'],
                'about':"It's impossible to walk on the steps without standing on a letter.",
                'stuff':[]
            },
            'tower f2':{
                'neighbors':['staircase','library','tower f3'],
                'about':'Two hallways are built to your left and right - one appears to be an old library, and the other an empty room.',
                'stuff':[]
            },
            'empty room':{
                'neighbors':['"empty" room'],
                'about':'This room is made completely of solid stone, and is completely empty. Seems like a good place to have some fun.',
                'stuff':[]
            },
            '"empty" room':{
              'neighbors':['tower f2'],
              'about':'Light shines down on you from the hole you blew in the ceiling.',
              'stuff':[]
            },
            'library':{
                'neighbors':["tower f2"],
                'about':"This dusty old library hasn't been touched for a while - nothing but old books.",
                'stuff':["old book"]
            },
            'tower f3':{
                'neighbors':['dark figure'],
                'about':"You spot a dark silouhette in flowing red robes standing in front of a large, floating, black gem. The figure is holding their hands out towards the gem, but he isn't moving.",
                'stuff':[]
                },
            'maldrak':{
                'neighbors':['maldrak_sword_1'],
                'about':'You begin to approach the dark, imposing figure in the room.\n\nAs you get closer to them, you gasp as you feel your body freeze up, unable to move - you have been temporarily petrified!\n"So, you passed my armored guardian - but you are still a fool...", the figure begins to speak, with an unnaturally deep voice.\n"My power is more immense than any other mage in history. And you think you can fight me, let alone win."'+
                '\nThe figure begins to turn. \n"Nothing will end my eternity of glory. NOTHING!"\nThe figure begins to move into the light. Finally, you can get a good look at it. It is an abomination - a walking corpse, with its robes adorned with arcane sigils.'+
                '\n"I am called Maldrak - and I will be the greatest king of this world, the Great Lich-King! I will rule with the sword and the spell. You cannot stop it! It begins here, in Azuth - my home.\nThey imprisoned me, for desiring the knowledge to gain life eternal. And they have paid the price - all of them, now only shadows of their former foolishness."'+
                '\n"Now come. I will show you the power I have learned."\n\nYou regain motion while Maldrak begins reciting an incantation. You must end this threat!\n',
                'stuff':[]
                },
            'maldrak_sword_1':{
                'neighbors':['maldrak'],
                'about':"Maldrak is reciting an incantation for a spell. The tactician in you thinks a counterattack is best, but you aren't sure - you've never fought a lich before.",
                'stuff':[]
                },
            'maldrak_defend':{
                'neighbors':['maldrak_sword_1','maldrak_flying','maldrak_fireball'],
                'about':'"AAAAUUUGGGH!!", screams Maldrak. He rears up in his fury, his hands glowing with a sickly green light. He is going to strike you with them.',
                'stuff':[]
                },
            'maldrak_flying':{
                'neighbors':['maldrak_defend','maldrak_fireball'],
                'about':"You dodge maldrak's undead touch by quickly flying away. He reacts by extending his right hand in your direction, preparing another spell.",
                'stuff':[]
                },
            'maldrak_fireball':{
                'neighbors':['maldrak_defend','maldrak_sword_2'],
                'about': "You hit the wall behind you, and fall down to the floor. As you get up, the cold sting of dread fills your body when you see Maldrak.\nHe's moving across the floor at an unnatural pace, his red robes flowing a few feet off the floor, his undead claws extended. It's a big room though, you've got time to prepare your next action - relatively.",
                'stuff':[]
                },
            'maldrak_sword_2':{
                'neighbors':['maldrak_fireball','tower f3 win'],
                'about':'You release the fireball spell with a powerful CRRRACK and BOOOOM, and Maldrak falls on his back, stunned.',
                'stuff':[]
                },
            'tower f3 win':{
                'neighbors':['maldrak_sword_2','city center win'],
                'about':'The floating black gem fractures and disintegrates, and the blackened sky clears. You hear... cheering from the city center below?',
                'stuff':[]
                },
            'city center win':{
                'neighbors':['tower f3 win'],
                'about':'As you exit the tower doors, your ears are assualted with the sounds of cheering - people, and hundreds of them!\nThey explain to you where they came from - they had been transformed into shadows, assumably by Maldrak, and killing him has freed them all.',
                'stuff':[]
                }
            }
    def create_player():
        return{
            'location': 'gate',
            'inventory': ['sword','spell: fireball','spell: levitate'],
        }
    return{
        'map': create_map(),
        'player': create_player(),
        'status': ["playing"]
    }
def render(world):
    '''
    Consumes a world and produces a string that will describe the current state
    of the world. Does not print.
    Args:
        world (World): The current world to describe.
    Returns:
        str: A textual description of the world.
    '''
    player_location = world['player']['location']
    map_location = world['map'][player_location]
    about = map_location['about']
    print("----------------------------------------------------------------------------------------------------------------")
    if player_location == 'gate':
        return ("You are at the "+player_location+'.'+'\n'+about+'\n')
    elif player_location == "sneak":
        return ("You find yourself sneaking around an armored figure.")
    elif player_location == "armored figure":
        return ("\nAs you approach the armored figure, you discover it isn't someone in armor at all - it's just armor, walking by itself!"+'\n'+about+'\n')
    elif player_location == "fight the armor":
        return ("You charge towards the suit of armor while it shrieks at you!"+'\n'+about+'\n')
    elif player_location == 'city center':
        return ("You find yourself in the "+player_location.title()+'.'+"\n"+about+"\n")
    elif player_location == "cottage":
        return ("You find yourself in the "+player_location.title()+'.'+"\n"+about+"\n")
    elif player_location == 'old store':
        return ("You find yourself in the "+player_location.title()+'.'+"\n"+about+"\n")
    elif player_location == "the box":
        return ("\n"+about+"\n")
    elif player_location == "the tree":
        return ("You attempt to hide behind a particularly large tree. "+'\n'+about+'\n')
    elif player_location == "armor_sword":
        return ("You brandish your trusty longsword, and take a powerful swing at a gap in the armor near the shoulder. "+'\n'+about+'\n')
    elif player_location == "tower f1":
        return ("As you move into the Wizard's Tower, the doors slam behind you, locked. You immediately notice two things:"+'\n'+about+'\n')
    elif player_location == "staircase":
        return ("You begin to walk up the spiral staircase.\n\n"+about)
    elif player_location == "tower f2":
        return ('As you step on the last stair, "H", the central room of the next floor comes within view.\n\n'+about+'\n')
    elif player_location == "library":
        return(about)
    elif player_location == "empty room":
        return ('\n\n'+about+'\n')
    elif player_location == '"empty" room':
        return('You find yourself in an "empty" room.\n'+about+'\n')
    elif player_location == "tower f3":
        return("You land on the final floor of the tower, ready for whatever comes next.\n"+about+'\n')
    elif player_location == "maldrak":
        return(about)
    elif player_location == "maldrak_sword_1":
        return(about)
    elif player_location == "maldrak_defend":
        return(about)
    elif player_location == "maldrak_flying":
        return("You quickly fly to your left as a bolt of acid flies past your head."+about)
    elif player_location == "maldrak_fireball":
        return(about)
    elif player_location == "maldrak_sword_2":
        return(about)
    elif player_location == 'tower f3 win':
        return(about)
    elif player_location == "city center win":
        return("You make your way down the Tower, and out to the city center.\n"+about)
def get_options(world):
    '''
    Consumes a world and produces a list of strings representing the options
    that are available to be chosen given this state.
    Args:
        world (World): The current world to get options for.
    Returns:
        list[str]: The list of commands that the user can choose from.
    '''
    commands = ["quit",'inspect inventory']
    player_location = world['player']['location']
    map_location = world['map'][player_location]
    stuff = map_location['stuff']
    if player_location == 'gate':
        commands.append("open gate")
    if player_location == 'city center':
        commands.append("move to armored figure")
        commands.append("move to cottage")
        commands.append("move to old store")
    if player_location == 'cottage':
        commands.append("inspect shadow")
        commands.append("move to city center")
    if player_location == 'old store':
        if 'old history book - reads:\n"Our fair city was named after the god of magic, Azuth - and it is fitting, too!\nSoon after our founding, many wizards flocked here to study."' not in world['player']['inventory']:
            commands.append("look around")
        commands.append("move to city center")
    if player_location == 'armored figure':
        commands.append("sneak")
        commands.append("fight")
    if player_location == "sneak":
        commands.append("move to the box")
        commands.append("move to the tree")
    if player_location == "fight the armor":
        commands.append("draw your sword")
        commands.append("cast a fireball")
    if player_location == "armor_sword":
        commands.append('move to tower f1')
    if player_location == "the box":
        commands.append("move to tower f1")
    if player_location == "the tree":
        commands.append("fight")
    if player_location == "tower f1":
        commands.append("inspect pedestal")
        commands.append("ascend stairs")
    if player_location == "staircase":
        commands.append("dash up the stairs")
        commands.append("step on specific letters")
    if player_location == "tower f2":
        if not made_hole:
            commands.append("move to empty room")
        if made_hole:
            commands.append('move to "empty" room')
        commands.append("move to library")
    if player_location == "empty room":
        commands.append("violently swing your sword")
        commands.append("shoot random fireballs")
        commands.append("cast levitate and fly")
        if "spell: shield" in world['player']['inventory']:
            commands.append("cast shields")
        commands.append("move to tower f2")
    if player_location == '"empty" room':
        commands.append("violently swing your sword")
        commands.append("shoot random fireballs")
        commands.append("cast levitate and fly")
        if "spell: shield" in world['player']['inventory']:
            commands.append("cast shields")
        commands.append("move to tower f2")
    if player_location == "library":
        commands.append("look around")
        commands.append("move to tower f2")
    if player_location == "tower f3":
        commands.append("move towards figure")
    if player_location == "maldrak":
        commands.append("fight")
    if player_location == "maldrak_sword_1":
        commands.append("draw your sword")
        commands.append("cast a fireball")
        commands.append("begin flying")
        if "spell: shield" in world['player']['inventory']:
            commands.append("summon a shield")
    if player_location == "maldrak_defend":
        commands.append("draw your sword")
        commands.append("cast a fireball")
        commands.append("begin flying")
        if "spell: shield" in world['player']['inventory']:
            commands.append("summon a shield")
    if player_location == "maldrak_flying":
        commands.append("fly left")
        commands.append('fly right')
    if player_location == "maldrak_fireball":
        commands.append("draw your sword")
        commands.append("cast a fireball")
        commands.append("begin flying")
        if "spell: shield" in world['player']['inventory']:
            commands.append("summon a shield")
    if player_location == "maldrak_sword_2":
        commands.append("draw your sword")
        commands.append("cast a fireball")
        commands.append("begin flying")
        if "spell: shield" in world['player']['inventory']:
            commands.append("summon a shield")
    if player_location == "tower f3 win":
        commands.append('move to city center')
    if player_location == "city center win":
        commands.append('return to the king')
    return commands
made_hole = False
def update(world, command):
    '''
    Consumes a world and a command and updates the world according to the
    command, also producing a message about the update that occurred. This
    function should modify the world given, not produce a new one.
    Args:
        world (World): The current world to modify.
    Returns:
        str: A message describing the change that occurred in the world.
    '''
    stairsequence = ""
    player_location = world['player']['location']
    if command == "quit":
        world['status'] = "quit"
        return "You pull a stone of teleportation out of your bags, and raise it in the air, whisking you back to the king's palace as the stone disintegrates."
    if command == "open gate":
        world['player']['location'] = "city center"
        return "The gate swings open with a loud creak."
    if player_location == "tower f3 win":
        if command == "move to city center":
            world['player']['location'] = "city center win"
            return ''
    if command == "return to the king":
        world['status'] = "won"
        return ""
    if player_location != "tower f3":
        if command.startswith("move to"):
            goto(world, command)
            return ""
    if command.startswith("inspect"):
        if command == "inspect shadow":
            return "This shadow on the floor caught your eye. It first appeared to be just a trick of the light, but as you get closer you realize this is no coincidence - the shadow is shaped like a little girl holding a toy doll.\n Something tragic happened here.\n"
        if command == "inspect inventory":
            print("You have a few items at your disposal, however some might be useless in your current situation:")
            for i in world['player']['inventory']:
                print("- "+i.title())
    if player_location == 'old store':
        if command == "look around" and 'old history book - reads "Our fair city was named after the god of magic, Azuth - and it is fitting, too!\nSoon after our founding, many wizards flocked here to study."' not in world['player']['inventory']:
            world['player']['inventory'].append('old history book - reads "Our fair city was named after the god of magic, Azuth - and it is fitting, too!\nSoon after our founding, many wizards flocked here to study."')
            return 'After a bit of searching, you find a dusty old history book about the city. Sadly, most of the pages of this book are torn or faded, but you do find one interesting piece of trivia:\n\n"Our fair city was named after the god of magic, Azuth - and it is fitting, too!\nSoon after our founding, many wizards flocked here to study." \n\nYou might as well take it, right?\n\nOld History Book has been added to your inventory.'
        elif command == "look around":
            return 'You continue to search the old shop, but find nothing except dust bunnies.'
    if player_location == "armored figure":
        if command == "sneak":
            world['player']['location'] = 'sneak'
            return ''
    if command == "fight" and player_location == "the tree" or player_location == "armored figure":
        world['player']['location'] = 'fight the armor'
        return ''
    if player_location == "fight the armor":
        if command == "draw your sword":
            world['player']['location'] = 'armor_sword'
            return ''
        if command == "cast a fireball":
            world['player']['location'] = 'armor_lost'
            world['status'] = ["lost"]
            world['status'].append("armor")
            return ''
    if player_location == "tower f1":
        if command == "inspect pedestal":
            return("The markings on the pedestal read as follows:"+'\n\n'+"Within a city's embrace,"+'\n'+"named after the arcane,"+'\n'+"Wizards' haven, where knowledge is gained."+'\n'+"Staff and robe, a god's abode,"
                +'\n'+"Whose name in the city's roots is sown."+'\n\n'+"Yet heed this, seeker, as you climb with care,"+'\n'+"For in the ascent, beware the false step's snare.")
        if command == "ascend stairs":
            world['player']['location'] = 'staircase'
    if player_location == "staircase":
        if command == "dash up the stairs":
            world['status'] = ["lost"]
            world['status'].append("stairs")
        if command == "step on specific letters":
            stairsequence = input("What stairs are you stepping on? (only letters, no '-'s, spaces, or anything)").lower()
            if stairsequence != "azuth":
                world['status'] = ["lost"]
                world['status'].append("stairs")
                return ''
            else:
                world['player']['location'] = "tower f2"
                return "You make it all the way up the stairs with no trouble. Congrats!"
    if player_location == "empty room":
        if command == "violently swing your sword":
            return("You swing your longsword with power and fury - at least, that's what you think it would look like. An observer might think it looked silly, swinging a sword at nothing in an empty room.")
        if command == "shoot random fireballs":
            made_hole = True
            world['player']['location'] = '"empty" room'
            return("You begin blasting fireballs at random places in the room, when you accidentally blow a hole in the ceiling!\nIt doesn't seem like just any hole, though - there's light coming from it!")
        if command == "cast levitate and fly":
            return("You start flying. WHEEEEEEE! You safely land.")
        if command == "cast shields" and "spell: shield" in world['player']['inventory']:
            return("You try out your fancy new shield spell. It creates a barely visible magical barrier around you for a very brief time.\nThe shield from the spell warps the light into flashing your eyes, which is strange, seeing as there's not a light source in this particular room.")
    if player_location == '"empty" room':
        if command == "violently swing your sword":
            return("You swing your longsword with power and fury - at least, that's what you think it would look like. An observer might think it looked silly, swinging a sword at nothing in an empty room.")
        if command == "cast levitate and fly":
            world['player']['location'] = "tower f3"
            return("You start to rise off the floor, your body feeling weightless. You soar over to the hole you 'excavated' and find the light is coming from the next floor!")
        if command == "shoot random fireballs":
            return("After the idea to shoot more fireballs pops into your head, you decide against it - if you broke an important part of the room, it might fall on you!")
        if command == "cast shields" and "spell: shield" in world['player']['inventory']:
            return("You try out your fancy new shield spell. It creates a barely visible magical barrier around you for a very brief time.\nThe spell warps the light from the hole in the ceiling, flashing it into your eyes.")
    if player_location == "library":
        if command == "look around":
            if "spell: shield" not in world['player']['inventory']:
                world['player']['inventory'].append("spell: shield")
                return ("After a little bit of rustling around in dusty old bookshelves, you find an arcane tome with directions for a new spell!\n\n Spell: Shield has been added to your inventory.")
            if command == "look around" and "spell: shield" in world['player']['inventory']:
                return("You fiddle with some of the old books, but can't seem to find anything.")
    if player_location == "tower f3":
        if command == "move towards figure":
            world['player']['location'] = "maldrak"
            return ''
    if player_location == "maldrak":
        if command == "fight":
            world['player']['location'] = "maldrak_sword_1"
            return("You ready yourself for a fight!")
    if player_location == "maldrak_sword_1":
        if command == "draw your sword":
            world['player']['location'] = "maldrak_defend"
            return("You exploit how long it take to cast a spell, and get a good hit on Maldrak with your longsword!")
        if command == "cast a fireball":
            world['status'] = ["lost"]
            world['status'].append("maldrak")
            world['status'].append("sword_1")
            world['status'].append("fireball")
            return ''
        if command == "begin flying":
            world['status'] = ["lost"]
            world['status'].append("maldrak")
            world['status'].append("sword_1")
            world['status'].append("flying")
            return ''
        if command == "summon a shield":
            world['status'] = ["lost"]
            world['status'].append("maldrak")
            world['status'].append("sword_1")
            world['status'].append("shield")
            return ''
    if player_location == "maldrak_defend":
        if command == "draw your sword":
            world['status'] = ["lost"]
            world['status'].append("maldrak")
            world['status'].append("defend")
            world['status'].append("sword")
            return ''
        if command == "cast a fireball":
            world['status'] = ["lost"]
            world['status'].append("maldrak")
            world['status'].append("defend")
            world['status'].append("fireball")
            return ''
        if command == "begin flying":
            world['player']['location'] = 'maldrak_flying'
            return ''
        if command == "summon a shield":
            world['player']['location'] = "maldrak_fireball"
            return "You raise a shield just as Maldrak's hands come down on it, breaking the shield and sending you flying across the room."
    if player_location == "maldrak_flying":
        if command == "fly left":
            world['player']['location'] = "maldrak_fireball"
            return ''
        if command == "fly right":
            world['status'] = ["lost"]
            world['status'].append("maldrak")
            world['status'].append("flying")
            world['status'].append("right")
            return ''
    if player_location == "maldrak_fireball":
        if command == "draw your sword":
            world['status'] = ["lost"]
            world['status'].append("maldrak")
            world['status'].append("fireball")
            world['status'].append("sword")
            return ''
        if command == "cast a fireball":
            world['player']['location'] = "maldrak_sword_2"
        if command == "begin flying":
            world['status'] = ["lost"]
            world['status'].append("maldrak")
            world['status'].append("fireball")
            world['status'].append("flying")
            return ''
        if command == "summon a shield":
            world['status'] = ["lost"]
            world['status'].append("maldrak")
            world['status'].append("fireball")
            world['status'].append("shield")
            return ''
    if player_location == "maldrak_sword_2":
        if command == "draw your sword":
            world['player']['location'] = "tower f3 win"
            return "You dash with your sword in hand, and take a mighty leap, bringing your sword behind your head and back down on Maldrak's accursed skull with a great CRACK as you land."
        if command == "cast a fireball":
            return "You ready another fireball as Maldrak begins to stand back up."
        if command == "begin flying":
            world['status'] = ["lost"]
            world['status'].append("maldrak")
            world['status'].append("sword_2")
            world['status'].append("flying")
            return ''
        if command == "summon a shield":
            world['status'] = ["lost"]
            world['status'].append("maldrak")
            world['status'].append("sword_2")
            world['status'].append("shield")
            return ''
    else:
        return ''
def goto(world, command):
    new_location = command[len("move to "):]
    world['player']['location'] = new_location
    return new_location
def render_ending(world):
    '''
    Create the message to be displayed at the end of your game.
    Args:
        world (World): The final world state to use in describing the ending.
    Returns:
        str: The ending text of your game to be displayed.
    '''
    if world['status'] == "won":
        return("You pull a stone of teleportation out of your bags, and raise it in the air, whisking you back to the king's palace as the stone disintegrates.\nCongradulations! You have freed Azuth and you have won!")
    elif world['status'][0] == "lost":
        if world['status'][1] == "armor":
            return "The animated armor takes you down before you can cast your spell. You lose. (Don't worry, just run the program again to restart! :)"
        if world['status'][1] == "stairs":
            return "You take a careless step on the stair, and you panic as the stair breaks beneath you and you plummet hundreds of feet to your doom.\nYou lose. (Don't worry, just run the program again to restart! :)"
        elif world['status'][1] == "maldrak":
            if world['status'][2] == "sword_1":
                if world['status'][3] == "fireball":
                    return "You begin casting a mighty fireball - but you didn't account for the time it takes to cast a spell, and are cut off as Maldrak releases a bolt of lightning and fries you.\nYou lose. (Don't worry, just run the program again to restart! :)"
                elif world['status'][3] == "flying":
                    return "You begin to fly away, but Maldrak releases a lightning bolt and fries you mid-air.\nYou lose. (Don't worry, just run the program again to restart! :)"
                elif world['status'][3] == "shield":
                    return "You predict when Maldrak releases his spell, and cast a shield when he releases it - or, should have. You realize he held his spell for a moment longer while a lightning bolt courses through your body.\n You lose. (Don't worry, just run the program again to restart! :)"
            elif world['status'][2] == "defend":
                if world['status'][3] == "sword":
                    return "You cleave off one of Maldrak's arms, but the other clasps your face and you feel your soul slip away.\nYou lose. (Don't worry, just run the program again to restart! :)"
                elif world['status'][3] == "fireball":
                    return "You throw a mighty fireball at Maldrak - but you're standing right next to him, so you are also consumed in the flames.\nYou lose. (Don't worry, just run the program again to restart! :)"
            elif world['status'][2] == "flying":
                if world['status'][3] == "right":
                    return "You dodge to the right, but feel a ball of acid splash across your face.\n You lose. (Don't worry, just run the program again to restart! :)"
            elif world['status'][2] == "fireball":
                if world['status'][3] == "sword":
                    return "You ready your sword, but when you look to Maldrak again, he's gone - that is, until you feel cold undead hands grasp your head, and your soul slip away.\nYou lose. (Don't worry, just run the program again to restart! :)"
                elif world['status'][3] == "flying":
                    return "You take off, but watch in horror as Maldrak flies up to meet you, and cold undead hands grasp you and you feel your soul slip away.\nYou lose. (Don't worry, just run the program again to restart! :)"
                elif world['status'][3] == "shield":
                    return "You cleave off one of Maldrak's arms, but the other clasps your face and you feel your soul slip away.\nYou lose. (Don't worry, just run the program again to restart! :)"
            elif world['status'][2] == "sword_2":
                if world['status'][3] == "flying":
                    return "You begin to fly away as Maldrak gets up - and blasts you with a volley of magic missiles.\nYou lose. (Don't worry, just run the program again to restart! :)"
                elif world['status'][3] == "shield":
                    return "You put up a shield as Maldrak gets up. The shield fades, and a volley of magic missiles flies into your face.\nYou lose. (Don't worry, just run the program again to restart! :)"
    elif world['status'] == "quit":
        return "You quit. (Don't worry, just run the program again to restart! :)"
def choose(options):
    '''
    Consumes a list of commands, prints them for the user, takes in user input
    for the command that the user wants (prompting repeatedly until a valid
    command is chosen), and then returns the command that was chosen.
    Note:
        Use your answer to Programming Problem #42.3
    Args:
        options (list[str]): The potential commands to select from.
    Returns:
        str: The command that was selected by the user.
    '''
    responded = False
    while not responded:
        print("You can:")
        for i in options:
            print("- "+i.title())
        response = input("What is your command?:\n").lower()
        for i in options:
            if response == i:
                responded = True
                return response
############# Main Function ##############
# Do not modify anything below this line #
##########################################
def main():
    '''
    Run your game using the Text Adventure console engine.
    Consumes and produces nothing, but prints and indirectly takes user input.
    '''
    print(render_introduction())
    world = create_world()
    while world['status'][0] == 'playing':
        print(render(world))
        options = get_options(world)
        command = choose(options)
        print(update(world,command))
    print(render_ending(world))
if __name__ == '__main__':
    main()
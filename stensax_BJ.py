import random
"""Detta program slumpar i en lista mellan sten, sax, påse och 
man spelar tills man vinner över slumpgeneratorn, eller max 3 ggr"""
possible_actions = ['sten', 'sax', 'påse']
spelomgang = 0
while True:
    # För att slumpgenerator ej skall börja på samma hämtar jag choice direkt
    from random import choice
    dator_val = random.choice(possible_actions)
    anv_input = input('Välj ett av (sten, sax eller påse): ')
    print('Du valde ' + anv_input + ', Python valde ' + str(dator_val)+ '.\n')
    if anv_input == dator_val:
        print('Oavgjort!!')
    elif anv_input == 'sten':
        if dator_val == 'sax':
            print('Sten vinner över sax! Du vann!!, du behöver ej spela mer')
            break
        else:
            print('Påse vinner över sten! Du förlorade!')
    elif anv_input == 'påse':
        if dator_val == 'sten':
            print('Påse vinner över sten! Du vann!, du behöver ej spela mer')
            break
        else:
            print('Sax vinner över påse! Du förlorade!')
    elif anv_input == 'sax':
        if dator_val == 'påse':
            print('Sax vinner över påse! Du vann!, du behöver ej spela mer')
            break
        else:
            print('Sten vinner över sax! Du förlorade!')
    play_again = input('Vill du spela igen (y/n): ')
    #Räknar antal spel:
    spelomgang += 1
    # rensar random variabeln:
    dator_val ="tomvariabel"
    if spelomgang >=3:
        print('Det får du inte eftersom du har spelat 3ggr och kan bli spelberoende, dessutom har ni ni inte vunnit än.')
        break
    # Om inte y \(gjort till gemener) är inmatat avslutas spelet:
    if play_again.lower() != "y":
        print("Tack för denna gången, välkommen åter")
        break

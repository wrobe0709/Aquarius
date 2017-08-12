"""Handles puzzles withing Aquarius"""

def sword_case_puzzle(character):
    """Handles sword case puzzle"""
    print'''
    *****************************************************
    Move swift as the ___ and closely-formed as the ___.
    Attack like ___ and be still as the ___.
    ****************************************************
    '''
    # Get input and make sure it is in order
    user_command = raw_input('> ')
    command_list = user_command.split(" ")
    for word in range(len(command_list)):
        if command_list[word] == 'wind':
            if command_list[word+1] == 'wood':
                if command_list[word+2] == 'fire':
                    if command_list[word+3] == 'mountain':
                        print " Your knowledge of The Art of War has proven True."
                        print " The sword case opens slowly...revealing a mighty sword."
                        character.get_current_room().get_items()['Sword'].set_hidden(False)
        elif command_list[0] != 'wind':
            print " Hmm that doesn't seem to be right, perhaps Sun Tzu would know..."

def key_puzzle(character):
    """Handles puzzle to unlock end room key"""
    print "Vanity of vanities, all is vanity."
    print '''
                                ...----....
                         ..-:"''         ''"-..
                      .-'                      '-.
                    .'              .     .       '.
                  .'   .          .    .      .    .''.
                .'  .    .       .   .   .     .   . ..:.
              .' .   . .  .       .   .   ..  .   . ....::.
             ..   .   .      .  .    .     .  ..  . ....:IA.
            .:  .   .    .    .  .  .    .. .  .. .. ....:IA.
           .: .   .   ..   .    .     . . .. . ... ....:.:VHA.
           '..  .  .. .   .       .  . .. . .. . .....:.::IHHB.
          .:. .  . .  . .   .  .  . . . ...:.:... .......:HIHMM.
         .:.... .   . ."::"'.. .   .  . .:.:.:II;,. .. ..:IHIMMA
         ':.:..  ..::IHHHHHI::. . .  ...:.::::.,,,. . ....VIMMHM
        .:::I. .AHHHHHHHHHHAI::. .:...,:IIHHHHHHMMMHHL:. . VMMMM
       .:.:V.:IVHHHHHHHMHMHHH::..:" .:HIHHHHHHHHHHHHHMHHA. .VMMM.
       :..V.:IVHHHHHMMHHHHHHHB... . .:VPHHMHHHMMHHHHHHHHHAI.:VMMI
       ::V..:VIHHHHHHMMMHHHHHH. .   .I":IIMHHMMHHHHHHHHHHHAPI:WMM
       ::". .:.HHHHHHHHMMHHHHHI.  . .:..I:MHMMHHHHHHHHHMHV:':H:WM
       :: . :.::IIHHHHHHMMHHHHV  .ABA.:.:IMHMHMMMHMHHHHV:'. .IHWW
       '.  ..:..:.:IHHHHHMMHV" .AVMHMA.:.'VHMMMMHHHHHV:' .  :IHWV
        :.  .:...:".:.:TPP"   .AVMMHMMA.:. "VMMHHHP.:... .. :IVAI
       .:.   '... .:"'   .   ..HMMMHMMMA::. ."VHHI:::....  .:IHW'
       ...  .  . ..:IIPPIH: ..HMMMI.MMMV:I:.  .:ILLH:.. ...:I:IM
     : .   .'"' .:.V". .. .  :HMMM:IMMMI::I. ..:HHIIPPHI::'.P:HM.
     :.  .  .  .. ..:.. .    :AMMM IMMMM..:...:IV":T::I::.".:IHIMA
     'V:.. .. . .. .  .  .   'VMMV..VMMV :....:V:.:..:....::IHHHMH
       "IHH:.II:.. .:. .  . . . " :HB"" . . ..PI:.::.:::..:IHHMMV"
        :IP""HHII:.  .  .    . . .'V:. . . ..:IH:.:.::IHIHHMMMMM"
        :V:. VIMA:I..  .     .  . .. . .  .:.I:I:..:IHHHHMMHHMMM
        :"VI:.VWMA::. .:      .   .. .:. ..:.I::.:IVHHHMMMHMMMMI
        :."VIIHHMMA:.  .   .   .:  .:.. . .:.II:I:AMMMMMMHMMMMMI
        :..VIHIHMMMI...::.,:.,:!"I:!"I!"I!"V:AI:VAMMMMMMHMMMMMM'
        ':.:HIHIMHHA:"!!"I.:AXXXVVXXXXXXXA:."HPHIMMMMHHMHMMMMMV
          V:H:I:MA:W'I :AXXXIXII:IIIISSSSSSXXA.I.VMMMHMHMMMMMM
            'I::IVA ASSSSXSSSSBBSBMBSSSSSSBBMMMBS.VVMMHIMM'"'
             I:: VPAIMSSSSSSSSSBSSSMMBSSSBBMMMMXXI:MMHIMMI
            .I::. "H:XIIXBBMMMMMMMMMMMMMMMMMBXIXXMMPHIIMM'
            :::I.  ':XSSXXIIIIXSSBMBSSXXXIIIXXSMMAMI:.IMM
            :::I:.  .VSSSSSISISISSSBII:ISSSSBMMB:MI:..:MM
            ::.I:.  ':"SSSSSSSISISSXIIXSSSSBMMB:AHI:..MMM.
            ::.I:. . ..:"BBSSSSSSSSSSSSBBBMMMB:AHHI::.HMMI
            :..::.  . ..::":BBBBBSSBBBMMMB:MMMMHHII::IHHMI
            ':.I:... ....:IHHHHHMMMMMMMMMMMMMMMHHIIIIHMMV"
              "V:. ..:...:.IHHHMMMMMMMMMMMMMMMMHHHMHHMHP'
               ':. .:::.:.::III::IHHHHMMMMMHMHMMHHHHM"
                 "::....::.:::..:..::IIIIIHHHHMMMHHMV"
                   "::.::.. .. .  ...:::IIHHMMMMHMV"
                     "V::... . .I::IHHMMV"'
                       '"VHVHHHAHHHHMMV:"'
    '''
    print " For ___ thou art, and unto ___ shalt thou return."
    # Check for correct puzzle solution
    user_command = raw_input('> ')
    if user_command == 'dust':
        print " But you are not dust, you still draw breath, and thus, have a chance..."
        print " The chest opens and reveals a key."
        character.get_current_room().get_items()['End Room Key'].set_hidden(False)
    else:
        print " Your actions are futile...give up..."

def gear_room_puzzle(character):
    """Handles gear room puzzle"""
    print'''
    You enter the gear room and notice this on the wall.
    _         _
    /\_| |_/\    | |
    \       / /\/   \/\
_/       \_\       /
|_    _    _|   _   |_
_|  (_)  |_   (_)   _|
|_         _|       |
    \       / /       \
    / _   _ \ \/\   /\/
    \/ |_| \/    |_|
    Should you interact with it?
    '''
    # Check if user wants to take on puzzle
    user_command = raw_input('  (yes or no) > ')
    if user_command == 'yes':
        print '''
        You move the gears and it reveals...
        ,---------------------------------------.---------.
        |                                       |         |
        |    ,-----------------------------.    |    .    |
        |    |                             |    |    |    |
        |    |    ,-------------------.    |    |    |    |
        |    |    |                   |    |    |    |    |
        |    |    `----     ,----     |    |    |    |    |
        |    |              | X       |    |    |    |    |
        |    |    ,---------"---------:    |    `----'    |
        |    |    |                   |    |              |
        |    `----:    ,---------.    |    `---------.    |
        |         |    |         |    |              |    |
        |    .    |    |    .    |    |     ---------'    |
        |    |    |    |    |    |    |                   |
        :----'    |    |    |    |    |    ,--------------:
        |         |    |    |    |    |    |              |
        |    .    |    `----'    |    |    |     ----.    |
        |    |    |              |    |    |         |    |
        |    `----"---------     |    |    `---------'    |
        |                        |    |                   |
        `------------------------'    `-------------------'
        How can you get to the x...?
        Use keywords up, down, left, or right. Do not include commas.
        Keep it lower case, it must be exactly correct.
        '''
        # Take and check user input
        user_command = raw_input('> ')
        if user_command == 'up left down right down left up right up left up right down right down left up left down right up right down left':
            print " The gears in the room move and reveal the bow room!"
            character.get_game_map()['Bow Room'].set_locked("false")
        else:
            print " The gears grind to a halt in the room. Nothing more happens."
    else:
        print " You decide not to bother with the gear."

def gaseous_room_entry(character):
    """Handles entering the gaseous room"""
    # Enter gaseous room and unlock it if user has bow
    if 'Bow' in character.get_inventory():
        print """ 
 You take out your bow and draw an arrow. You approach the lit blue torch and
 light your arrow. Drawing the string back you face the entrance to the gaseous room
 and loose your arrow! It's blue flame flys into the gaseous room and a brilliant flash
 of light englufs the room and corridor! As your eyes adjust you notice that the gas is gone
 and it's safe to enter in.\n"""
        character.get_game_map()['Gaseous Room'].set_locked("false")
    else:
        print """   This flame's proximity to the gaseous room would probably be useful if there was a way to light it and shoot it in there..."""


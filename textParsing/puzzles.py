#This file will contain the various puzzles found in the game world that
#the user will be able to interact with
import sys
import csv

#A function that will require the user to guess and properly input the
#missing words (wind, wood, fire, mountain), in order, to gain access
#to the sword within the case
def swordCasePuzzle():
    print'''
    *****************************************************
    Move swift as the ___ and closely-formed as the ___.
    Attack like ___ and be still as the ___.
    ****************************************************
    '''
    user_command = raw_input('> ')
    command_list = user_command.split(" ")
    #iterate through and make sure the user selected the
    #proper words and in order
    for word in range(len(command_list)):
        if command_list[word] == 'wind':
            if command_list[word+1] == 'wood':
                if command_list[word+2] == 'fire':
                    if command_list[word+3] == 'mountain':
                        print "Your knowledge of The Art of War has proven True."
                        print "The sword case opens slowly...revealing a mighty sword."
                        #add something that interacts with the room feature (case)
        elif command_list[0] != 'wind':
            print "Hmm that doesn't seem to be right, perhaps Sun Tzu would know..."

#This puzzle will have a prompt and a picture, if the player correctly guesses what
#it is the case will open revealing the key
def keyPuzzle():
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
    print "For ___ thou art, and unto ___ shalt thou return."
    user_command = raw_input('> ')
    if user_command == 'dust':
        print "But you are not dust, you still draw breath, and thus, have a chance..."
        print "The chest opens and reveals a key."
        #something here to interact with the chest's feature and unlock's it
    else:
        print "Your actions are futile...give up..."

#This puzzle
def gearRoomPuzzle():
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
    user_command = raw_input('> ')
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
        user_command = raw_input('> ')
        if user_command == 'up left down right down left up right up left up right down right down left up left down right up right down left':
            print "The gears in the room move and reveal the bow room!"
        else:
            print "The gears grind to a halt in the room. Nothing more happens."
    else:
        print "You decide not to bother with the gear."

def gaseous_room_entry(character):
    if 'Bow' in character.get_inventory():
        print """You take out your bow and draw an arrow. You approach the lit blue torch and
        light your arrow. Drawing the string back you face the entrance to the gaseous room
        and loose your arrow! It's blue flame flys into the gaseous room and a brilliant flash
        of light englufs the room and corridor! As your eyes adjust you notice that the gas is gone
        and it's safe to enter in."""
        #need a way to make it so that the gaseous room is able to be entered.
    else:
        print """This flame's proximity to the gaseous room would probably be useful if there was a way
        to light it and shoot it in there..."""




#testing purposes
#swordCasePuzzle()
#keyPuzzle()
#gearRoomPuzzle()

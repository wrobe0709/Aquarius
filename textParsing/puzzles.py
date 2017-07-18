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
    userCommand = raw_input('> ')
    commandList = userCommand.split(" ")
    #iterate through and make sure the user selected the
    #proper words and in order
    for word in range(len(commandList)):
        if commandList[word] == 'wind':
            if commandList[word+1] == 'wood':
                if commandList[word+2] == 'fire':
                    if commandList[word+3] == 'mountain':
                        print "Your knowledge of The Art of War has proven True."
                        print "The sword case opens slowly...revealing a mighty sword."
                        #add something that interacts with the room feature (case)
        elif commandList[0] != 'wind':
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
    userCommand = raw_input('> ')
    if userCommand == 'dust':
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
    userCommand = raw_input('> ')
    if userCommand == 'yes':
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
        userCommand = raw_input('> ')
        if userCommand == 'up left down right down left up right up left up right down right down left up left down right up right down left':
            print "The gears in the room move and reveal the bow room!"
        else:
            print "The gears grind to a halt in the room. Nothing more happens."
    else:
        print "You decide not to bother with the gear."


#testing purposes
#swordCasePuzzle()
#keyPuzzle()
#gearRoomPuzzle()

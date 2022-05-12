'''                                       ``..`.-----....```                                        
                                      `.-://::/++ossssssso+/::-----.```                             
                                   `.-://:::+o+:oysyhddhssoooysssssoo/:-.``                         
                             ``..-::::+oo+oyhhyyhhyddmmmdhddmmmddddddhhyso+:`                       
                           -:::://::oyhhhhhhdmmdhdmddmmmmdmmmmmddddmmddhhyyso-`                     
                         `::::////:oddmmmmdmmmmmmmmmmmmmmmmmmdddddhdmmdhyyyyys:`                    
                         .::::/+ossyhhdmmmmmmmmmmmmmmmdmmmmmmmddddhhdmmddhhhyys`                    
                      `.-://+ooo+osyhhdmmmmmmmmmmmmmmmmmmmdmmmmmmdddmmmmmmdddhy.                    
                     `+oo+///oshhdddddmmmmmmmmmmmmmmmmmmmddddddddmmmmmmmmmdddhy-                    
                    `/+/:/oyhdmmmmmmmmdddmmmmmmmmmmmmmmmmmddmmmmmmmmmmmmmdddhho`                    
                   .:--/yddddmmmmmmmmmmmdmmmmmmmmmmmmmmmmddddddddddmmmmdddhhho-                     
                  .--:/ydmmmmmmmmmmmmmmddddmddddddddmddddddddddddddddddddhhs:`                      
                 .:/ohddmmmmmmmmmmmmmmmmmddddhhhhhhhhhhhhhhhhhhyhhhhhdddhhs.                        
                .+shddmmmmmmmmmmmmmmmdmmmdddddhhyyyyssoo++++++///////osss++.                        
                .+o+ddmmmmmmmmmmmmmmdddddddddhyyssoo+////////::::::---::/:/:`                       
                 -ohddmmmmmmmmmmmmmmmdddddddhysooo++//////////::::::::::::::-                       
                 -yhdmmmmmmmmmmmmmmddddddddhysoooo+++/////////:::::::::::::::`                      
                `ohddmmmmmmmmmmmmmddddddddhyysooooo++++////////::::::::::::::.                      
                :ydddmmmmmmmmmmmmmdddddddhhyysooooooo+++///////::::::::::::::.                      
               `/yhddmmmmmmmmmmmmmddddddddhhyssoooooo+++////////////:::::::::.                      
               ./hhdmmmmmmmmmmmmmmmdddddddhhyssooooooo+++///////:::::::::::::.                      
              `oyhddmmmmmmmmmmmmmmmmmddddhhyssooooooooo+++ooooosssssoo+/:://+/`                     
              .ohdddmmmmmmmmmmmmmmmmmdddhyyssooooooossssssooo++++oosso+///+oso`                     
              `+hddmmmmmmmmmmmmmmmmmmdddhyyssooooossssooo++++++oo+/+oo+/:/+o+`                      
               :hddmmmmmdhssosydddddddddhhyssoooooo+++++++oososso////++///ss.                       
               `sdddmmmhooosssoosyhhhdhhhyyssoooo++++////////:::::////++///-`                       
                :ydddmd+oys++syooossyyhhyyssoooooo++++/////:::::::////++++/:.`                      
                `oyhddh+syo//ohsoooossssssssoooooooo++++//////:::::///+++++/:-`                     
                `/sydddyoso/ososss+osssssssssooooooooo++++/////:::::/+ooo++//:-                     
                 `/yhdddyso++++osyooosssssssssssooooooooo+++/////::/+so++++++/-                     
                  `+yhdddysooo+++osoossssssssssssssoooooo+++//////:/ssoosyyso-                      
                   .+ydddhysooo+//+oosssssssssssssooooooo+++///////://+//++:`                       
                    .+hdhyyyyyssooosssssssssssssssooooooo+++/////////:::::/-                        
                     .ohysssssyyyyssssssssssssssssoooooo++++////////////://`                        
                     `-+ossssssssssssssssssssssssssoooooo+++///+osooo+++++/`                        
                      .-/osssssssssssssssssssssssssooooooo++/////+ooooooo+-                         
                      .-/ossssssssosssssssssssssssssoooooo++//////++++///:                          
                      `-/osssssssssssssssssssssssssssooooo+++////////////`                          
                 `:-...-/oossssssssssssssssssssssssssssooooo+////////::::`                          
                .o-`--.-ooossssssssssssssssssssssssssssssoooo++//////://.                           
              `-+o`-+/:+sssssssssssssssssssssssssssyyyyssssssooo++/////-`                           
            `-/ohs..ossssssssssssssssssssssssssssssssyyyyyssssssssoo+/-`                            
           ./syhdd+.:sssssssssssssssssssssssosooosssssyyyo--...----..`                              
       ``-/shddmmmh:-/syssssssssssssooooooooooooooossssso/-.                                        
    `.:/oydmmmmNNNm+--/yyssssssssssoo++++oooooooo+++++////:..`                                      
..-/oyhdmmNNNNNNNNNy/-./sssssssssssoo++++++oooo+++///////++-.::.`                                   
shdmmmmmNNNNNNNNNNNm+:-.:osssssssssoo+++++++oooooo+++++//++-.-hdyo/:-```````                        
mmNNNNNNNNNNNNNNNNNNy/-...+ssssssssoo++++++++++oo+++++//+s:-../mmmyy++ooooooo+:/:                   
NNNNNNNNNNNNNNNNNNNNmo:-.../ssssssssoo++++++++++++++++/+s+--...dmmhyyyysyyyyyyoso```                
NNNNNNNNNNNNNNNNNNNNNdo:-...:ossssssoo+++++++++++++++++yy::-...ommyyyyysssssssoso+/-..`             
NNNNNNNNNNNNNNNNNNNNNNh+:-...-+sssssoo++++++++oo+++++oyh+:-..../mdsyyyyyyysyssso/+mddyo/-...`       
NNNNNNNNNNNNNNNNNNNNNNdo/:-....:osssso++++++++++++++shds/:-....-mdoyyyyyyyyyssso//mmmmmmdhs+:..``   
NNNNNNNNNNNNNNNNNNNNNNh+/:--....-+ssso++++++++++++oyhhy+:-......hhoyyyyyyyysssoo+ommmmmmmmmmdhs/-'''
music = lambda ns: [ ["Never gonna ", "NEVER GONNA "][i%2] + ["give you up", "let you down", "run around \
and desert you", "make you cry", "say goodbye", "tell a lie and hurt you"][n] for i, n in enumerate(ns) ]

#OR

def music(n):
    lyrics = {0:"give you up",
              1:"let you down",
              2:"run around and desert you",
              3:"make you cry",
              4:"say goodbye",
              5:"tell a lie and hurt you"
              }
    res = []
    counter = 0
    for x in n:
        if counter%2 != 0:
            res.append("NEVER GONNA " + lyrics[x])
        else:
            res.append("Never gonna " + lyrics[x])
        counter += 1
    return res
        

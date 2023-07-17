import Room

## Init Rooms
def init_Rooms(initialRoom):


    ## Setup Rooms
    print("Initializing Rooms")
##    thecrash = Room.Room()
##    thecrash.name = 'The Crash'
##    thecrash.narrative = ' James’s helicopter lost control in the sandstorm and blew up as he crashed into the desert.'
##    thecrash.image = ('images\\mummy.png')

    question1 = Room.Room()
    question1.name = 'Question 1'
    question1.narrative = 'Which war was the Sultan Muhamad of Riau Johor was murdered?'
    question1.image = 'Images//First Question go brrr.png'


    answer1 = Room.Room()
    answer1.name = 'Answer Question 2'
    answer1.narrative = '1963'
    answer1.image = 'images//First Awnser go brrr.png'
    
    

    question2 = Room.Room()
    question2.name = 'Question 2'
    question2.narrative = 'What war did Alfonso de Albuquerque fight in malaysia?'
    question2.image = 'Images//Second Second Awnser go brrr.png'

    answer3 = Room.Room()
    answer3.name = 'Answer Question 3'
    answer3.narrative = 'Capture of Malaka'
    answer3.image = 'Images//whack.png'


    question3 = Room.Room()
    question3.name = 'Question 3'
    question3.narrative = 'What War Lasted From 1857 to 1863 in Malaysia?'
    question3.image = 'Images//die.png'

    answer4 = Room.Room()
    answer4.name = 'Answer 4'
    answer4.narrative = 'Pahang Civil War'
    answer4.image = 'Images//Iamgoinginsane.png'


    question4 = Room.Room()
    question4.name = 'Question 4'
    question4.narrative = 'why did japanese attack malaya?'
    question4.image = 'Images//slapme.png'

    answer5 = Room.Room()
    answer5.name = 'Answer 4'
    answer5.narrative = 'For Resrourses'
    answer5.image = 'Images//oof.png'


    question5 = Room.Room()
    question5.name = 'Question 5'
    question5.narrative = 'In World War 2 Who Were The Main Parties?'
    question5.image = 'Images//sendhelpplease.png'

    answer6 = Room.Room()
    answer6.name = 'Answer 6'
    answer6.narrative = 'ally and axis'
    answer6.image = 'Images//mesad.png'


    question6 = Room.Room()
    question6.name = 'Question 6'
    question6.narrative = 'One Of The Guys Died'
    question6.image = 'Images//stabby.png'

    answer7 = Room.Room()
    answer7.name = 'Answer 7'
    answer7.narrative = 'Slappy'
    answer7.image = 'Images//kinda cringe.png'


    question7 = Room.Room()
    question7.name = 'Question 7'
    question7.narrative = 'Whack'
    question7.image = 'Images//question7b.png'

    answer8 = Room.Room()
    answer8.name = 'Answer 8'
    answer8.narrative = 'Long Time Ago'
    answer8.image = 'Images//question7a.png'


    question8 = Room.Room()
    question8.name = 'Question 8'
    question8.narrative = 'Jump Away'
    question8.image = 'Images//question8a.png'

    answer9 = Room.Room()
    answer9.name = 'Answer 9'
    answer9.narrative = 'wheeeeeeee'
    answer9.image = 'Images//question8b.png'
    

    question10 = Room.Room()
    question10.name = 'Question 10'
    question10.narrative = 'Question Yes Answer Now'
    question10.image = 'Images//takemehome.png'

    answer100 = Room.Room()
    answer100.name = 'Answer 100'
    answer100.narrative = 'Answer Yes Question Now'
    answer100.image = 'Images//game over yes..png'

    
    # Linking the Roosm
    print("Linking Rooms")
    initialRoom.forward = question1

    question1.left = answer1
    answer1.forward = question2
    question2.forward = answer3
    answer3.forward = question3
    question3.left = answer4
    answer4.forward = question4
    question4.forward = answer5
    answer5.forward = question5
    question5.left = answer6
    answer6.forward = question6
    question6.forward = answer7
    answer7.forward = question7
    question7.forward = answer8
    answer8.forward = question8
    question8.right = answer9
    answer9.forward = question10
    question10.forward = answer100
    answer100.forward = question1

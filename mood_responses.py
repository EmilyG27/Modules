def mood_response(mood):
    if mood == "happy":
        return("I'm glad you'er having a good day!")
    elif mood == "sad":
        return("I hope your day gets better.")
    elif mood == "excited":
        return("That's great!")
    else:
        return("Please choose 'happy', 'sad', or 'excited'.")
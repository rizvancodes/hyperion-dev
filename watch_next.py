import spacy

nlp = spacy.load('en_core_web_md')


comp = 'After the death of Superman, several new people present themselves as possible successors.'

def suggest_movie(current_movie):
    #initialize movies and scores dict
    movies = {}
    scores = {}
    #read movies from file, strip of new line and split into a list at colon
    #store movie as key and description as value in movies dict
    with open('movies.txt', 'r') as file:
        for line in file:
            film = line.strip('\n').split(' :')
            movies[film[0]] = film[1]

    #create nlp object from input movie description
    model_movie = nlp(current_movie)
    #loop over movies dict
    for name, description in movies.items():
        #if the movie description is already in the list then skip comparison
        if current_movie == description:
            print('match')
            continue
        #calculate similarity score between input and movie in database
        similarity = nlp(description).similarity(model_movie)
        #store movie name and score in a scores dict
        scores[name] = similarity
    #sort the scores dict in reverse by value using sorted and key function
    sorted_scores = dict(sorted(scores.items(), key=lambda x:x[1], reverse=True))

    #return the first key in the sorted scores dict using next and iter 
    return next(iter(sorted_scores))




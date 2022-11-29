import spacy

#Example 1
nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
word4 = nlp("apples")
word5 = nlp("pears")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
print(word4.similarity(word5))

#The similarity score between monkey and banana is moderately high as they are both animals
#The similarity between monkey and banana is twice the similarity between cat and banana
#This demonstrates that the similarity method calculates some link between cat and banana
#There is an extremely high level of similairty between apples and pears
#This may be due to the fact they are both fruits which are associated with each other in language

#Example 2
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
      print(token1.text, token2.text, token1.similarity(token2))

#Example 3
sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
      similarity = nlp(sentence).similarity(model_sentence)
      print(sentence + " - ",  similarity)

#Run the example file with the simpler language model ‘en_core_web_sm’ 
#and write a note on what you notice is different from the model 'en_core_web_md'

#The similarity scores are lower when using the simpler language model.
#A word vector is a numerical representation of words in the form of multidimensional matrices
#Word vectors are built on the analysis of words in context

#A warning stated that this language pack does not have word vectors loaded
#The sm pack was also not trained with word vectors but allows loading of own vectors
#As the md model was trained on vectors and comes with vectors 
#loaded it provides a more accurate judgement of similarity
      
#References
      #http://spacy.pythonhumanities.com/01_03_word_vectors.html  


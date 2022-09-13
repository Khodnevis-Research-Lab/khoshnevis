# from hazm import sent_tokenize, word_tokenize, POSTagger


# class Ending:

#     def __init__(self):
#         pass

#     def endings(self, text, pos_dir="Hazm/postagger.model"):
#         """
#         This function fills last uncompleted sentence of generated text.
#         Args:
#             text: the text you want to fill its last sentence
#             pos_dir: directory of pos tagger model
#         Returns:
#             cleaned text with complete last sentence based on verb
#         """
#         tagger = POSTagger(model=pos_dir)
#         # sentence tokenizing on the generated text
#         sentences = sent_tokenize(text)
#         # getting the last sentence which is candidate for broken sentence and word_tokenize
#         # it for feeding to POS tagger
#         last_sent_tokens = word_tokenize(sentences[-1])
#         # getting pos tags of last sentence
#         last_sent_tags = tagger.tag(last_sent_tokens)
#         # making the pos tag list reverse to iterate through it backward
#         last_sent_tags = last_sent_tags[::-1]
#         # going through pos tag list backward and getting the verb, when find it breaks the loop
#         for extracted_tuple in last_sent_tags:
#             if extracted_tuple[1] == "V":
#                 verb = extracted_tuple[0]
#                 break
#             else:
#                 verb = ""
#         if not verb:
#             return " ".join(sentences[:-1]) + "."
#         if '_' in verb:
#             verb = verb.replace('_', ' ')
#         new_last_sent = sentences[-1][:sentences[-1].index(verb) + len(verb)]
#         sentences[-1] = new_last_sent
#         return " ".join(sentences) + "."

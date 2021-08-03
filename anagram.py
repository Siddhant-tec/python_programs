import string


def isanagram(sentence, alphabet=string.ascii_lowercase):
    return set(sentence.lower()) == set(alphabet)


print(isanagram(input('sentence: ')))

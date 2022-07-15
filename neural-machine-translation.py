import pandas as pd

# import corpus
eng = pd.read_csv("data/europarl-v7.nl-en.en", sep="\t", names=["eng"])
nl = pd.read_csv("data/europarl-v7.nl-en.nl", sep="\t", names=["nl"]) #to do: solve error: Expected 1 fields in line 952982, saw 2
corpus = pd.DataFrame(eng, nl)

# task 1: analysis of corpus

## mandatory to do: compare length of same sentence in english and in dutch

## mandatory to do: number of sentences in english and dutch corpus respectively

## list and count words that are same in english and dutch

# task 2: pre-process corpus
# lowercase the text
# strip empty lines and their correspondences
# remove lines with XML-Tags (starting with "<")

# task 3: comparing machine translation models
# English to Dutch neural machine translation (RNN based sequence to sequence model and word based model)
 
# Dutch to English neural machine translation (RNN based sequence to sequence model and word based model)

# character based model

# task 4: neural machine translation with attention
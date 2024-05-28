from pprint import pprint
import random

def create_markov_model(s):
    s=s.lower()
    s = s.replace('\n','')
    s = s.split(' ')
    keys_list = []
    n = 0
    for e in s[:len(s)-2]:
        n+=1
        keys_list.append(e+' '+s[n])
    count_dict = {}
    for e in keys_list:
        if e in count_dict:
            count_dict[e]+=1
        else:
            count_dict[e]=1
    markov_dict = {}
    for e in count_dict:
        percent_dict = {}
        l = 0
        while l < len(s) - 2:
            if s[l] + ' ' + s[l+1] == e:
                next_word = s[l+2]
                if next_word in percent_dict:
                    percent_dict[next_word] += 1 / count_dict[e]
                else:
                    percent_dict[next_word] = 1 / count_dict[e]
            l += 1
        markov_dict[e] = percent_dict
    return markov_dict

s = 'to be or not to be that is the question'
m = create_markov_model(s)
pprint(m)

def get_next_word(model, word):
    rand_chance = random.random()
    word_chance = model[word]
    probability = 0
    for e in word_chance:
        probability+=word_chance[e]
        if rand_chance<=probability:
            return e

print(get_next_word(m,'to be' ))
s = open('data/alice.txt')
s = s.read()

def generate_text(model, num_words):
    n = 0
    word_current = random.choice(list(model.items()))
    newStr = ''
    while n < num_words:
        word_current = get_next_word(model, word_current)
        newStr+=(word_current+' ')
        n+=1
    return newStr
m = create_markov_model(s)
print(m)
'''print(generate_text(m, 100))'''

#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def remove_punc(str1):
    punctuation_marks = [".", ",", "?", "!", '"', ":", ";", "—", "-", "(", ")", "'", "...", "[", "]", "/", "&"]
    str2=str1
    for i in punctuation_marks:
        str1= str1.replace(i, "")
    return str1
def word_split(str2):
    L1=str2.split()
    return L1
def word_dict(L1):
    d1={}
    for i in L1:
        if i in d1:
            d1[i]+=1
        else:
            d1[i]=1
    return d1

import pandas as pd
def word_freq_table(d1):
    df = pd.DataFrame({'word': L1, 'No of occurrences': [d1[word] for word in L1]})

    return df
str1="Politics and law may be inseparable, but the first may sometimes overshadow the second, especially when it comes to prosecution of political leaders. An ongoing example is the spike in the activity of the Enforcement Directorate (ED) in Tamil Nadu. Close on the heels of the arrest of V. Senthilbalaji, now a Minister without portfolio in the DMK regime, and the legal wrangling over the legality of his arrest and remand, another high-profile Minister, K. Ponmudy, is under the ED’s investigation. While the agency may have good reason to investigate and prosecute them, it does appear that they have been chosen for such action from among many political functionaries in the State who have pending probes against them. Both Mr. Senthilbalaji, who has now been shifted from a private hospital to a prison in Chennai, and Mr. Ponmudy, the Minister for Higher Education, face serious charges."
str2=remove_punc(str1)
print(str2)
L1=word_split(str2)
print("L1",L1)
d1=word_dict(L1)
print(d1)
df=word_freq_table(d1)
print("df",df)


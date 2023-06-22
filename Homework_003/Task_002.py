# В большой текстовой строке подсчитать количество встречаемых 
# слов и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов. 
# За основу возьмите любую статью из википедии или из документации к языку.

import re
from collections import Counter

def count_words(text):
    # Удаление знаков препинания и приведение к нижнему регистру
    cleaned_text = re.sub(r'[^\w\s]', '', text.lower())
    
    # Разделение текста на отдельные слова
    words = cleaned_text.split()
    
    # Подсчет количества встречаемых слов
    word_counts = Counter(words)
    
    # Возврат 10 самых частых слов
    most_common_words = word_counts.most_common(10)
    
    return most_common_words

text = '''
Evil is Evil. Lesser, greater, middling… Makes no difference. 
The degree is arbitary. The definition's blurred. 
If I'm to choose between one evil and another… 
I'd rather not choose at all.
'''

most_common = count_words(text)
print(most_common)

import pandas as pd
import numpy as np
import scipy.stats as st

def from_csv_to_list():
    """Метод для перевода дата-фрейма в 3 последовательности"""
    data_frame = pd.read_csv('table.csv')
    operator_table = data_frame[data_frame['Action'] == 'operator']
    reask_table = data_frame[data_frame['Action'] == 'reask']
    correct_table = data_frame[data_frame['Action'] == 'correct']
    operator_list = operator_table['Score'].tolist()
    reask_list = reask_table['Score'].tolist()
    correct_list = correct_table['Score'].tolist()

    return operator_list, reask_list, correct_list

def confidence_interval(data, confidence=0.95):
    """Метод определения доверительного интервала"""
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), st.sem(a)
    h = se * st.t.ppf((1 + confidence) / 2., n-1)
    return round(m-h, 2), round(m+h, 2)

def BotDecision(score):
    operator_list, reask_list, correct_list = from_csv_to_list()
    operator_interval = confidence_interval(operator_list)
    reask_interval = confidence_interval(reask_list)
    correct_interval = confidence_interval(correct_list)
    if score < reask_interval[0]:
        # print("Бот совсем не уверен в ответе (score низкий)")
        return "Перевести на оператора (уверенность низкая)"
    elif score < correct_interval[0]:
        # print("Бот совсем не уверен в ответе (score низкий)")
        return "Переспросить пользователя (уверенность средняя)"
    else:
        return "Вывести ответ пользователю (уверенность высокая)"

print(BotDecision(88))

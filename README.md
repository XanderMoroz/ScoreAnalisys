# ScoreAnalisys
Второе тестовое задание компании EORA. `Алгоритм принятия решения для бота`. Первое задание доступно по [ссылке](https://github.com/XanderMoroz/EORA_APIBot).

## **Описание проблемы**

Хотим сделать бота, который отвечает на часто задаваемые вопросы. Для этого у нас
есть какой-то чёрный ящик, который для данной реплики возвращает наиболее
подходящий ответ и score, насколько по мнению этого чёрного ящика этот ответ
подходит (от 0 до 100). При этом мы понимаем, что бот не сможет отвечать на все
вопросы, и поэтому делаем так:

- Если бот сильно уверен в ответе (score высокий), то даём пользователю ответ
- Если бот совсем не уверен в ответе (score низкий), то переводим пользователя
на оператора
- Если score средний, то просим пользователя переформулировать вопрос.

Чтобы выяснить, какой score считать низким, какой средним, а какой высоким мы
провели эксперимент: попросили живых людей задать вопрос боту, а потом указать,
что было бы правильно после такого вопроса сделать: ответить, переспросить или
перевести на оператора. Мы записали в таблицу score от чёрного ящика,
предложенное тестером действие и сложили в таблицу `table.csv`.  ([Вот она.](https://github.com/XanderMoroz/ScoreAnalisys/blob/master/table.csv))

## *Задачи*
 
- 1) Нужно выяснить, какой score считать низким, какой средним, а какой высоким.
- 2) Реализовать алгоритм, который будет принимать на вход score и возвращать
следующее действие: вывести ответ пользователю, переспросить пользователя или
перевести на оператора. 
- 3) Обосновать, почему был выбран именно такой алгоритм и
именно такие параметры для него.
- 4) Предложить метрику для определения точности своего алгоритма и посчитайте её
значение для данных из table.csv.

## **Ответы**

Более обстоятельный разбор решения предложен в GoogleColab и доступен по [ссылке](https://colab.research.google.com/drive/1L80yR6mViPKH5sRVPm9HaRkVJZ_D5r2I?usp=share_link).

### Ответ №1 Ранжирование значения `"Score"`
Опираясь на данные можно утверждать что:

Score следует считать `низким`, когда его значение в диапазоне от 26.28 и до 32.5
Score следует считать `средним`, когда его значение в диапазоне от 34.18 и до 41.01
Score следует считать `высоким`, когда его значение в диапазоне от 81.68 и до 91.48
 
### Ответ №2 Реализация алгоритма

Алгоритм принятия решения построен основан на [доверительном интервале](https://ru.wikipedia.org/wiki/Доверительный_интервал) с погрешностью 5%. Реализован на проверке вхождения переданного значения "Score" в один из трех интервалов:

0 <= score < 34.18 - (уверенность низкая) - перевести на оператора
34.18 < score < 81.68 - (уверенность средняя) - переспросить пользователя
81.68 < score <= 100 - (уверенность высокая) - вывести ответ пользователю

### Ответ №3 Обоснование алгоритма

Прежде всего хочу сообщить что выборка была очень маленькая (всего 366 строк), что в определенной степени ограничивает точность модели.Тем не менее, исходя из предложенных данных, мой выбор интервалов основывается на следующих соображениях:

Хотя области доверителных интервалов ограничены значениями 26.28 и 91.48, я их отбросил потому что в реальности значения находятся в интервале от 0 и до 100.
Правый конец первого интервала я осознанно сместил на начало доверительного интервала значений средней уверенности (34.18 вместо 32.5). Обосновываю свое решение соображениями экономии сил оператора. Его и так часто зовут. Считаю целесообразным давать боту больше шансов на попытку понять собеседника.
Правый конец второго интервала я также сместил на начало доверительного интервала значений средней уверенности (81.68 вместо 41.01). Обосновываю свое решение соображениями клиентоориентированности. На мой взгляд лучше уж бот переспросит чем будет отвечать некорректно.Считаю что нервы клиента следует поберечь.

## Ответ №3 Метрика определения точности.

Метрикой оценки точности выступает доверительный интервал. Соответственно для данных из таблицы `"table.csv."` - точность алгоритма составляет `95%`. Соответственно `погрешность 5%`.






## Лицензия

MaffinWare

## Авторы

* [XanderMoroz](https://https://github.com/XanderMoroz/) - *Все работы*


import re,vk_api,os,sys,random, requests, time, threading
from vkauth import *
slova = ['подпишись', 'настроение', 'конкурс', 'да', 'сила', 'хорошо', 'любимая', 'любимый', 'девушка', 'парень', 'доброе утро', 'ты', 'вечер', 'море', 'отдых', 'праздник', 'деньги', 'дорого', 'встреча', 'дружба', 'гуляем', 'солнце', 'чилл', 'коронавирус', 'корона', 'история', 'дом', 'изи', 'жиза', 'лето', 'новость', 'новости', 'россия', 'конституция', 'помимо', 'фактор', 'слепой', 'целовать', 'отказ', 'волшебник', 'нажать', 'заказать', 'соответствовать', 'решаться', 'болтать', 'указание', 'прочь', 'страдание', 'окончание', 'строка', 'конфликт', 'справка', 'мебель', 'вежливо', 'ноготь', 'химический', 'сосуд', 'корея', 'трудовой', 'явный', 'владеть', 'достижение', 'дополнительный', 'константин', 'асфальт', 'заменить', 'челюсть', 'наряд', 'кончать', 'скрытый', 'рисунок', 'прятаться', 'плюс', 'попадаться', 'частность', 'транспорт', 'наказание', 'изображать', 'выражать', 'образоваться', 'способствовать', 'съезд', 'заложить', 'исходить', 'окончить', 'рамка', 'акт', 'посетитель', 'невероятный', 'влажный', 'божий', 'обсуждать', 'рисковать', 'выступление', 'гордиться', 'загадочный', 'издание', 'выразить', 'окружающий', 'чашка', 'жир', 'намерение', 'жаркий', 'спасать', 'ванный', 'ложь', 'отходить', 'кузнец', 'балкон', 'полевой', 'жарко', 'подходящий', 'спектакль', 'предупреждать', 'длительный', 'почва', 'легенда', 'срочно', 'малейший', 'жидкость', 'приемный', 'благодарить', 'блок', 'усталость', 'рисовать', 'надеть', 'заключить', 'надежный', 'нужда', 'окошко', 'сюжет', 'приличный', 'генеральный', 'угадать', 'хитрый', 'сок', 'будущий', 'испытать', 'усталый', 'мышка', 'эффект', 'зад', 'хранить', 'небесный', 'сменить', 'браться', 'задумываться', 'великолепный', 'металл', 'отсутствовать', 'фонд', 'догнать', 'майка', 'полгода', 'ночевать', 'выехать', 'рай', 'один', 'схема', 'четверть', 'ерунда', 'несчастье', 'радостный', 'окружение', 'учительница', 'давний', 'предок', 'кислота', 'пропадать', 'просыпаться', 'подпись', 'гнев', 'физика', 'резать', 'тронуть', 'чудесный', 'стоя', 'совместный', 'змея', 'некуда', 'монах', 'осенний', 'картинка', 'общение', 'советовать', 'соседка', 'проявить', 'сметь', 'переулок', 'неправильный', 'поделать', 'аж', 'лечить', 'подъем', 'ругаться', 'сопротивление', 'раздражение', 'уложить', 'завидовать', 'уголь', 'масштаб', 'заслужить', 'стойка', 'довести', 'плита', 'пляж', 'подросток', 'присутствовать', 'спальня', 'скучно', 'тупой', 'поцелуй', 'уважаемый', 'туфля', 'шампанский', 'благодарность', 'перспектива', 'последующий', 'стесняться', 'дружок', 'превратить', 'обижаться', 'накрыть', 'вставить', 'гад', 'примета', 'залить', 'разумный', 'недовольный', 'внезапный', 'игрушка', 'стоимость', 'учреждение', 'сжечь', 'спинка', 'проверка', 'уход', 'удержаться', 'эксперимент', 'пообещать', 'англия', 'падение', 'девятый', 'петух', 'записывать', 'любитель', 'чеченец', 'ценный', 'глупо', 'тесный', 'исполнение', 'хронический', 'стремление', 'наполнить', 'четко', 'проехать', 'отобрать', 'вина', 'ведьма', 'апрель', 'бюджет', 'разрушить', 'алый', 'архив', 'выслушать', 'цветной', 'прыгнуть', 'доверять', 'юность', 'сбор', 'базар', 'нарушить', 'готовность', 'искренне', 'ай', 'прибыль', 'почта', 'сдавать', 'практика', 'тратить', 'совершать', 'нарисовать', 'сниться', 'академия', 'грустный', 'головной', 'переставать', 'гнома', 'процедура', 'понести', 'нуждаться', 'лужа', 'необычный', 'юбка', 'соединить', 'ошибаться', 'недавний', 'аэропорт', 'задать', 'промолчать', 'богатство', 'мудрый', 'налог', 'минимум', 'ад', 'полотенце', 'воспаление', 'наслаждение', 'продажа', 'выиграть', 'полость', 'удивить', 'уверенно', 'маска', 'включать', 'удивленно', 'атака', 'согласие', 'клясться', 'раскрытый', 'пожелать', 'красный', 'приложить', 'кинуть', 'оперативный', 'жрать', 'техник', 'дошлый', 'надолго', 'оторваться', 'охранник', 'пугать', 'установка', 'расход', 'неприятно', 'забытый', 'поесть', 'зависть', 'талантливый', 'отправляться', 'несомненно', 'изобразить', 'бред', 'прихожая', 'высказать', 'кисть', 'цирк', 'квартал', 'пешком', 'жуткий', 'жилье', 'приступ', 'предыдущий', 'спалить', 'спасение', 'моральный', 'определение', 'образец', 'фантазия', 'спорт', 'вначале', 'гладкий', 'июль', 'телеграмма', 'напиток', 'торговля', 'юмор', 'испортить', 'следовательно', 'отъезд', 'чтение', 'мучить', 'надевать', 'вылететь', 'недолго', 'видеться', 'свободно', 'охранять', 'скрываться', 'весенний', 'влезть', 'приблизиться', 'дыра', 'настаивать', 'визит', 'напряженный', 'машинка', 'термин', 'интервью', 'выжить', 'гордый', 'покидать', 'приезд', 'табак', 'переговоры', 'гараж', 'книжный', 'сельский', 'классический', 'осторожный', 'исполнить', 'таковой', 'слышный', 'кризис', 'ответственный', 'подобно', 'риск', 'живой', 'мыло', 'забросить', 'повышенный', 'ремонт', 'авторитет', 'провод', 'использоваться', 'извиняться', 'уверять', 'объем', 'отнять', 'рев', 'щит', 'стадо', 'некого', 'прогулка', 'натура', 'рассмотреть', 'учитывать', 'признание', 'гениальный', 'маг', 'сгореть', 'плотно', 'обращение', 'ген', 'торговый', 'злость', 'пузырь', 'испытание', 'нанести', 'прохожий', 'прыжок', 'вена', 'включая', 'осознать', 'обидно', 'палочка', 'ленинградский', 'мысленно', 'заполнить', 'раздражать', 'коллектив', 'новенький', 'хор', 'отказать', 'отложить', 'свести', 'зарабатывать', 'заказ', 'максимальный', 'свидетельство', 'отмечать', 'фактически', 'привязать', 'положительный', 'трагедия', 'наружу', 'прогресс', 'реклама', 'бокал', 'проспект', 'увеличение', 'братец', 'маршрут', 'энергичный', 'возить', 'продолжение', 'размышлять', 'капитал', 'космос', 'разбить', 'абсолютный', 'непосредственно', 'обидеть', 'коснуться', 'италия', 'заключенный', 'описание', 'выделить', 'помереть', 'ругать', 'сынок', 'беспокоить', 'восстановить', 'выставка', 'ноль', 'достигать', 'цепочка', 'монета', 'волновать', 'отчаянный', 'идеал', 'перчатка', 'село', 'задержаться', 'сердечный', 'ранее', 'рожа', 'дата', 'зелень', 'подчеркнуть', 'набирать', 'разделить', 'февраль', 'исполнять', 'категория', 'придавать', 'трамвай', 'любопытный', 'светло', 'набережная', 'продукция', 'выгнать', 'приступить', 'фабрика', 'делиться', 'показание', 'выносить', 'безусловно', 'пустяк', 'растение', 'гул', 'вступать', 'стройный', 'одеваться', 'ценить', 'стыд', 'воспринимать', 'дока', 'избавиться', 'унести', 'зажечь', 'жажда', 'популярный', 'преимущество', 'лет', 'имущество', 'премия', 'влюбленный', 'привлечь', 'внешность', 'приход', 'ставка', 'уголовный', 'прощаться', 'располагаться', 'рис', 'манера', 'пасть', 'медаль', 'крутиться', 'украина', 'тетрадь', 'стремительно', 'нарушать', 'велосипед', 'противный', 'кончик', 'ванна', 'густо', 'жалоба', 'традиционный', 'благодарный', 'убедить', 'холодильник', 'бешеный', 'исход', 'ласковый', 'воспитание', 'награда', 'печень', 'типичный', 'часовой', 'стихотворение', 'характеристика', 'торжественно', 'огненный', 'повязка', 'праздничный', 'учет', 'крепость', 'проявлять', 'качать', 'трудность', 'просторный', 'соответственно', 'умение', 'завалить', 'внести', 'перерыв', 'губернатор', 'опускаться', 'доверие', 'подряд', 'фантастический', 'яд', 'гостиный', 'доход', 'оказать', 'роскошный', 'мак', 'инструкция', 'ир', 'спокойствие', 'психологический', 'лысый', 'килограмм', 'печально', 'меньший', 'двойной', 'вселенная', 'тварь', 'чайник', 'опубликовать', 'отпускать', 'намек', 'пробить', 'воровать', 'плач', 'природный', 'отдельно', 'допускать', 'рассчитать', 'модный', 'расстаться', 'гитара', 'совершенный', 'проводиться', 'раб', 'заведение', 'бедро', 'вспышка', 'фрукт', 'скрыть', 'мотоцикл', 'мероприятие', 'чин', 'действующий', 'администрация', 'опоздать', 'ненужный', 'простыня', 'аппетит', 'потихоньку', 'успокаивать', 'обеспечивать', 'уточнить', 'опасно', 'ресница', 'обрести', 'критика', 'чертовый', 'дуб', 'лениво', 'технология', 'болезненный', 'крутить', 'убежать', 'культурный', 'воскресенье', 'собачий', 'сохраниться', 'помешать', 'проводник', 'свеча', 'красиво', 'светиться', 'белок', 'защитить', 'применяться', 'симпатичный', 'младенец', 'желающий', 'преподаватель', 'пошло', 'мусор', 'выключить', 'рекомендовать', 'оказывать', 'подход', 'прижимать', 'снижение', 'заодно', 'як', 'тоня', 'том', 'диск', 'реветь', 'нежно', 'управлять', 'загадка', 'дуть', 'пациент', 'хата', 'суета', 'оттенок', 'пребывание', 'любоваться', 'гусь', 'улететь', 'бессмертный', 'бензин', 'инвалид', 'убежденный', 'роса', 'крючок', 'косой', 'нервно', 'сочинять', 'вероника', 'резиновый', 'вложить', 'плевать', 'купаться', 'проникнуть', 'заговор', 'сдаваться', 'елка', 'гром', 'медленный', 'порыв', 'переводить', 'обман', 'подробно', 'медицина', 'полно', 'видный', 'откровенно', 'нуль', 'соответствие', 'разнообразный', 'практический', 'капуста', 'неплохой', 'вкусный', 'бесплатно', 'выбить', 'окружать', 'сук', 'травма', 'законный', 'предоставить', 'отражение', 'самостоятельный', 'длина', 'похороны', 'ресурс', 'сценарий', 'смертельный', 'вытаскивать', 'школьник', 'беречь', 'молиться', 'рюкзак', 'проявляться', 'покупка', 'описывать', 'безумный', 'япония', 'специальность', 'походка', 'приветствовать', 'оборот', 'бульвар', 'итальянский', 'бумажный', 'серия', 'наказать', 'развитый', 'копия', 'научно', 'рама', 'расположение', 'приглашение', 'башка', 'горько', 'буря', 'сухо', 'философия', 'шерсть', 'двадцатый', 'ягода', 'низко', 'выделяться', 'фокус', 'тонна', 'материя', 'мышь', 'кушать', 'невозможный', 'общаться', 'побег', 'лунный', 'учение', 'почитать', 'размышление', 'одинаково', 'ступень', 'расставить', 'мадам', 'мирно', 'трасса', 'учебный', 'существующий', 'идеальный', 'жидкий', 'столкнуться', 'учебник', 'уговаривать', 'комсомольский', 'прикрывать', 'смесь', 'электронный', 'упор', 'обходить', 'котенок', 'эффективный', 'ежедневно', 'очевидный', 'наивный', 'порошок', 'кол', 'оранжевый', 'интеллектуальный', 'удержать', 'промышленный', 'формула', 'эмоция', 'тройка', 'длиться', 'эмоциональный', 'непосредственный', 'сонный', 'мяч', 'философ', 'отрицательный', 'расстройство', 'деться', 'закат', 'добиваться', 'грубо', 'напиться', 'дерьмо', 'свойственный', 'упустить', 'объявление', 'каблук', 'бурный', 'слушаться', 'пропускать', 'равнодушно', 'выполнение', 'забирать', 'пейзаж', 'реагировать', 'гладить', 'терпение', 'порода', 'корзина', 'огурец', 'корейский', 'пацан', 'обманывать', 'кузов', 'уронить', 'партнер', 'вой', 'шлем', 'выраженный', 'конференция', 'продавец', 'казак', 'доза', 'вылезать', 'одиночка', 'пленка', 'пруд', 'давить', 'рождаться', 'повсюду', 'сохранять', 'простор', 'блокнот', 'неудача', 'веко', 'сезон', 'основать', 'милость', 'снимок', 'подсказать', 'заботиться', 'расходиться', 'обязательный', 'задумать', 'набор', 'таблетка', 'молочный', 'уволить', 'поискать', 'быт', 'фигурка', 'чистота', 'храниться', 'образованный', 'танцор', 'утверждение', 'денежный', 'конкурс', 'увести', 'сводить', 'приобретать', 'удалиться', 'змей', 'доступный', 'салон', 'наливать', 'бак', 'сантиметр', 'прошедший', 'печаль', 'подтверждать', 'грамм', 'привлекать', 'семя', 'трезвый', 'полоска', 'рабочий', 'залезть', 'пусто', 'умолять', 'покупатель', 'пожить', 'неважно', 'выкинуть', 'выводить', 'чистить', 'телега', 'градус', 'справедливый', 'откликнуться', 'четкий', 'дорого', 'комар', 'пошутить', 'военно', 'проживать', 'устало', 'выложить', 'кастрюля', 'скучный', 'терпеливо', 'узнавать', 'постоять', 'миллиард', 'взлететь', 'барьер', 'дырка', 'проиграть', 'бытие', 'коза', 'офис', 'босой', 'предстоящий', 'повар', 'переносить', 'касса', 'независимый', 'тяжкий', 'опускать', 'изящный', 'переехать', 'убегать', 'кампания', 'прислушаться', 'освободиться', 'уличный', 'крыса', 'толкать', 'освобождение', 'бетонный', 'прогноз', 'съемка', 'икона', 'местность', 'драгоценный', 'изнутри', 'аккуратный', 'добавлять', 'шумный', 'гонять', 'негр', 'вонючий', 'поспешить', 'стоп', 'упорно', 'пробежать', 'удовлетворение', 'засунуть', 'ритм', 'сдерживать', 'прелесть', 'спрятаться', 'открыто', 'введение', 'мороженый', 'бессмысленный', 'округ', 'па', 'складываться', 'дружно', 'разводить', 'уютный', 'повторяться', 'мелодия', 'вал', 'трудиться', 'формирование', 'одеться', 'преодолеть', 'определяться', 'грань', 'назначать', 'курица', 'качаться', 'темп', 'информационный', 'тесно', 'посадка', 'потерпеть', 'нитка', 'внимательный', 'плакат', 'банда', 'скучать', 'избежать', 'инфекция', 'убеждение', 'кидать', 'успешно', 'жадно', 'худо', 'даваться', 'сбегать', 'пробка', 'связывать', 'рф', 'изучить', 'проведение', 'подать', 'строчок', 'уступать', 'прощение', 'порция', 'потребоваться', 'сорт', 'питаться', 'командующий', 'угрожать', 'официально', 'понедельник', 'польша', 'удобно', 'самостоятельно', 'висок', 'уговорить', 'глина', 'почка', 'профессионал', 'недостаточно', 'шарик', 'конфета', 'виски', 'делить', 'сетка', 'бассейн', 'заря', 'студенческий', 'метод', 'человечек', 'призывать', 'протяжение', 'королевский', 'поздороваться', 'красавец', 'минутка', 'равнодушный', 'обнимать', 'пополам', 'пяток', 'изучение', 'кататься', 'районный', 'лишить', 'виновато', 'удерживать', 'заряд', 'ребро', 'сустав', 'привыкать', 'шумно', 'пластинка', 'потрясать', 'мотив', 'дневной', 'воспитывать', 'съездить', 'свалить', 'биологический', 'малый', 'указанный', 'застрять', 'диплом', 'обходиться', 'пена', 'кипеть', 'убеждать', 'восстановление', 'злиться', 'молитва', 'коммерческий', 'уступить', 'избегать', 'склонный', 'религия', 'пригодиться', 'существенный', 'кличка', 'отвратительный', 'запустить', 'местечко', 'поделиться', 'обещание', 'вестись', 'веранда', 'скука', 'отмечаться', 'торжество', 'проникать', 'паренек', 'семейство', 'употреблять', 'устав', 'погон', 'мудрость', 'смело', 'фонтан', 'битва', 'паника', 'возникновение', 'мыть', 'удачный', 'печатать', 'сексуальный', 'публикация', 'оправдать', 'оборудование', 'вредный', 'рок', 'распространить', 'ишь', 'разбирать', 'груша', 'гроза', 'кислород', 'прохладный', 'выпуск', 'ля', 'хирург', 'объединить', 'символ', 'магия', 'убирать', 'расставаться', 'развод', 'звонкий', 'звездный', 'творить', 'инициатива', 'индивидуальный', 'единица', 'излишний', 'загнать', 'подчеркивать', 'регион', 'защитник', 'немой', 'сектор', 'ссылка', 'механический', 'предназначить', 'дружить', 'уникальный', 'восприятие', 'тропа', 'судебный', 'сало', 'живо', 'увеличиваться', 'питер', 'светило', 'подробный', 'мед', 'восхищение', 'мисс', 'сочетание', 'отправлять', 'независимо', 'прочный', 'ворваться', 'магический', 'выпивать', 'нагрузка', 'перец', 'обсуждение', 'ручной', 'достаточный', 'постановление', 'заметка', 'принцесса', 'посещать', 'нежность', 'миф', 'объявлять', 'противно', 'выдающийся', 'валюта', 'разработать', 'блин', 'выезд', 'предатель', 'удаляться', 'психика', 'трещина', 'поражать', 'настать', 'поляна', 'снаружи', 'интернет', 'посетить', 'будить', 'алкоголь', 'актриса', 'внешне', 'призрак', 'увеличить', 'бесплатный', 'математика', 'сыр', 'навестить', 'соединение', 'окончательный', 'невероятно', 'матерый', 'учеба', 'кукла', 'терапия', 'позор', 'конструкция', 'концепция', 'весть', 'строиться', 'бабочка', 'тыкать', 'изделие', 'студия', 'ленинский', 'видение', 'попрощаться', 'круто', 'отменить', 'сложность', 'строение', 'украсить', 'ложный', 'бас', 'песенка', 'сани', 'федерация', 'диагноз', 'премьера', 'букет', 'доставлять', 'придать', 'хорошенький', 'боковой', 'кредит', 'поздравлять', 'староста', 'нетерпение', 'копье', 'матч', 'бесконечно', 'поддаваться', 'зажигалка', 'акцент', 'вероятность', 'плавно', 'призыв', 'уничтожать', 'крупнейший', 'щенок', 'тигр', 'распространение', 'обувь', 'влюбиться', 'аргумент', 'полотно', 'недовольно', 'содержаться', 'овощ', 'отрываться', 'микрофон', 'стадия', 'легкость', 'скромно', 'око', 'активно', 'платформа', 'подружка', 'практик', 'ограниченный', 'объятие', 'оригинальный', 'рыбка', 'игрок', 'вить', 'ура', 'новичок', 'парнишка', 'премьер', 'заканчиваться', 'женатый', 'эфир', 'присутствующий', 'связаться', 'строитель', 'разложить', 'знакомый', 'слушатель', 'остро']
start = 0
end = 300


try:
    f = open('slova.txt')
    lines = f.readlines()
    num_lines = sum(1 for line in open('slova.txt'))
    for i in range(num_lines):
        slova.append(lines[i].replace('\n', ''))
except Exception as err:
    print(err)
    print(u"Ошибка, возможно вы не создали файл slova.txt")


def auth_handler():
    """ При двухфакторной аутентификации вызывается эта функция.
    """

    # Код двухфакторной аутентификации
    key = input("Enter authentication code: ")
    # Если: True - сохранить, False - не сохранять.
    remember_device = True

    return key, remember_device

def watch_story(author, story, read_token):
    data = {
        'act': 'read_stories',
        'al': 1,
        'all': 0,
        'connection_type': 'wi-fi',
        'hash': read_token,  # токен, который мы получали при парсинге страницы
        'loading_stats': '{author_id},{story_id},{random_tickrate}'.format(author_id=author, story_id=story,
                                                                           random_tickrate=random.randint(50, 1000)),
        'navigation_stats:': '{author_id},{story_id},list,view_story'.format(author_id=author, story_id=story),
        'progress': 0,
        'source': 'list',
        'story_id': '{author_id}_{story_id}'.format(author_id=author, story_id=story),
        'track_code': ''
    }
    vk_session.http.post("https://vk.com/al_stories.php", data=data)

def get_active_stories(user_id):
    data = vk.stories.get(owner_id=user_id)
    return data
def pars_users(zapros, megatoken):
    stories = []
    authors = []

    for j in zapros:
        try:
            time.sleep(0.3)
            print(f'Собрано {len(stories)} историй.')
            params = {'q':j,
                      'access_token':megatoken,
                      'v':'5.101',
                      'count':1000
                      }
            r = requests.get('https://api.vk.com/method/stories.search?', params=params)
            count = r.json()['response']['items']
           # if len(count)>=25:
           #     results = open('good_words.txt', 'a')
           #     results.write(f'{j}\n')
           #     results.close()
            for i in count:
                if i[0]['id'] not in stories:
                    stories.append(i[0]['id'])
                    authors.append(i[0]['owner_id'])
        except Exception as err:
            print(err)
            continue
    return stories, authors


def worker(authors ,start, end):
    for i in range(start,end):
        print(f'Смотрю историю {authors[i]} | # {users_list[i]}')
        watch_story(authors[i],users_list[i],read_token)
    else:
        pass
        #print("нет историй для просмотра")

#login, password = '+919536190157', 'qazzaq3221'
login = os.environ.get('login')
password = os.environ.get('password')

vk_session = vk_api.VkApi(
    login, password,
    # функция для обработки двухфакторной аутентификации
    auth_handler=auth_handler
)

try:
    vk_session.auth()
except vk_api.AuthError as error_msg:
    print(error_msg)
    sys.exit(1)

vk = vk_session.get_api()
url_src = vk_session.http.get('http://vk.com/feed')
tmp =  re.search('"read_hash":"\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w"',url_src.text)
read_token = url_src.text[tmp.start():tmp.end()].split(":")[-1].replace('"','')

if __name__=='__main__':
    auth_token = VKAuth(['stories'],'7512092','5.101',login,password)
    auth_token.auth()
    token = auth_token.get_token()
    print(len(slova))
    while True:
        users = pars_users(slova, token)
        users_list = users[0]
        authors_list = users[1]
        print(f'Собрано {len(users_list)} историй и {len(authors_list)} авторов.')
        THREADS = len(users_list) // 300
        for index in range(THREADS):
            threading.Thread(target=worker, args=(authors_list ,start, end)).start()
            start += 300
            end += 300

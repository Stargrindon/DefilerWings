﻿# имена девушек генерируются из списков имен (тип девушки_first) и фамилий (тип девушки_last). Если списка фамилий нет - генерируется только из списка имен. 
girls_names = {
    'peasant_first': [u'Жанна', u'Герда', u'Баббета', u'Cюзи', u'Альба', u'Амели', u'Аннета', u'Жоржетта', u'Бетти',
                      u'Бетси', u'Бланка', u'Бьянка', u'Дейзи', u'Джинни', u'Джуди', u'Дороти', u'Зои', u'Ирен',
                      u'Ивет',
                      u'Колет', u'Криси', u'Кэтти', u'Кэт', u'Лили', u'Лиди', u'Лулу'],
    'citizen_first': [u'Аделия', u'Аврора', u'Альбертина', u'Анджелла', u'Аврелия', u'Беатрис', u'Бернадетт',
                      u'Бриджит', u'Вероник', u'Виолет', u'Вирджиния', u'Габриэлла', u'Джаннет', u'Джулиана',
                      u'Доминика',
                      u'Жаклина', u'Жозефина', u'Джульетта', u'Камилла', u'Каролина', u'Кэйтлин', u'Ирен', u'Мелисса',
                      u'Марджори',
                      u'Натали', u'Пенелопа', u'Розали', u'Розета', u'Селеста', u'Симона', u'Стефани', u'Сюзанна',
                      u'Тереза', u'Флора', u'Эммануэль', u'Адалинда', u'Альбертина', u'Амелинда', u'Гризельда',
                      u'Виктория', u'Ирма', u'Каролина', u'Кристиана', u'Кэтрин', u'Лиона', u'Лорели', u'Маргарита',
                      u'Франциска',
                      u'Хенелора', u'Хильда', u'Элеонора', u'Абигайль', u'Антония', u'Долорес', u'Доротея',
                      u'Женевьева', u'Жозефина', u'Инесс', u'Кармелита', u'Консуэлла', u'Летиция', u'Марселла',
                      u'Присцилла',
                      u'Рамона', u'София', u'Ефимия', u'Ефания', u'Лидия', u'Беатриче', ],
    'princess_first': [u'Аннабель', u'Аделия', u'Авелин', u'Айседора', u'Альбертина', u'Анастасия', u'Антуанетта',
                       u'Беатрис', u'Валентина', u'Виктория', u'Габриэлла', u'Джиневра', u'Доминика', u'Джулианна',
                       u'Джульетта', u'Жюстина', u'Жозефина', u'Ивонна', u'Изабелла', u'Камилла', u'Клариса',
                       u'Клементина', u'Кристина', u'Лукреция', u'Марго', u'Матильда', u'Мелисента', u'Марианна',
                       u'Олимпия',
                       u'Пенелопа', u'Розалинда', u'Розамунда', u'Селестина', u'Серафина', u'Сюзанна', u'Стефания',
                       u'Тереза',
                       u'Флафия', u'Фелиция', u'Генриэтта', u'Гертруда', u'Шарлотта', u'Эмммануэль', u'Альбертина',
                       u'Амелинда',
                       u'Брунгильда', u'Вильгельмина', u'Изольда', u'Рафаэлла', u'Амаранта', u'Дельфиния', u'Доротея',
                       u'Мерседес', u'Офелия', ],
    'princess_last': [u'дэ Мюзи', u'фон Баургафф', u'дэ Альбре', u'дэ Блуа', u'дэ Виржи', u'ди Гиз', u'дэ Бриенн',
                      u'дэ Колиньи', u'дэ Ла Тур', u'дэ Лузиньян', u'дэ Фуа', u'дэ Брисак', u'дэ Круа', u'дэ Лин',
                      u'дэ Кюлот', u'дэ Сен-При', u'фон Баттенберг', u'фон Беннгис', u'фон Вальбиц', u'фон Вительсбах',
                      u'фон Гогеншауфен', u'фон Зальф', u'фон Люденштафф', u'фон Мирбах', u'фон Розен', u'фон Церинген',
                      u'фон Грюнберг', u'фон Штюрберг', u'фон Шелленбург', u'Строцци', u'Сфорца', u'Альбици',
                      u'Барбариго', u'Пацци', u'Бранкаччо', u'да Верана', u'Висконти', u'Гримальди', u'да Полента',
                      u'делла Тори',
                      u'да Камино', u'Монтрефельто', u'Манфреди', u'Фарнезе', u'Фрегозо', u'де Мендоза', u'ла Серда', ],
    'elf_first': [u'Берунвен', u'Фанавен', u'Арвен', u'Лучиэнь', u'Феалиндэ', u'Эстелендиль', u'Астера', u'Теолинвен',
                  u'Куивэн', u'Мрвэн', u'Интиальвен', u'Анарвен', u'Аманиэль', u'Анариэль', u'Лариэль', u'Лотанариэ',
                  u'Исильиндиль', u'Селфарианис', u'Йорингель', u'Оросинвиль', u'Гилэстель', u'Валакирэ'],
    'ogre_first': [u'Хунн', u'Йорва', u'Дирга', u'Велга', u'Сига', u'Йалгуль', u'Дорба', u'Гирга', u'Давири', u'Шалга',
                   u'Орва', u'Дезра', u'Арга', u'Бигра', u'Варга', u'Енза', u'Зарта', u'Икла', u'Корда', u'Логаза',
                   u'Мирбу',
                   u'Нира', ],
    'mermaid_first': [u'Ариэль', u'Блажена', u'Будимила', u'Ведана', u'Велина', u'Венцеслава', u'Верея', u'Велезара',
                      u'Веселина', u'Витана', u'Влада', u'Весемлиа', u'Годица', u'Горлина', u'Далина', u'Ждана',
                      u'Деяна', u'Дивина', u'Доляна', u'Есена',
                      u'Жилена', u'Завида', u'Зоряна', u'Златина', u'Ивица', u'Калёна', u'Красоя', u'Купава', u'Лада',
                      u'Леля', u'Малиша',
                      u'Млава', u'Милана', u'Младлена', u'Мирана', u'Невена', u'Обрица', u'Пава', u'Пригода', u'Рада',
                      u'Ракита', u'Ружана',
                      u'Силимина', u'Серебрина', u'Славена', u'Станимира', u'Стояна', u'Томила', u'Умила', u'Ундина',
                      u'Цветана', u'Чаруна',
                      u'Янина', u'Яромила', u'Ясмания'],
    'siren_first': [u'Ариэль', u'Блажена', u'Будимила', u'Ведана', u'Велина', u'Венцеслава', u'Верея', u'Велезара',
                    u'Веселина', u'Витана', u'Влада', u'Весемлиа', u'Годица', u'Горлина', u'Далина', u'Ждана', u'Деяна',
                    u'Дивина', u'Доляна', u'Есена',
                    u'Жилена', u'Завида', u'Зоряна', u'Златина', u'Ивица', u'Калёна', u'Красоя', u'Купава', u'Лада',
                    u'Леля', u'Малиша',
                    u'Млава', u'Милана', u'Младлена', u'Мирана', u'Невена', u'Обрица', u'Пава', u'Пригода', u'Рада',
                    u'Ракита', u'Ружана',
                    u'Силимина', u'Серебрина',
                    u'Славена', u'Станимира', u'Стояна', u'Томила', u'Умила', u'Ундина', u'Цветана', u'Чаруна',
                    u'Янина', u'Яромила', u'Ясмания'],
    'ice_first': [u'Астрид', u'Бригита', u'Боргильда', u'Вигдис', u'Вилла', u'Гурдун', u'Гунхильд', u'Дорта', u'Ингрид',
                  u'Ингеборга', u'Йорнун',
                  u'Матильда', u'Рангильда', u'Руна', u'Сигурд', u'Сванхильда', u'Сигюнд', u'Ульрика', u'Фрида',
                  u'Хлодвен', u'Хильда', u'Эрика'],
    'fire_first': [u'Азиль', u'Азиза', u'Базайна', u'Багира', u'Будур', u'Бушра', u'Гюльчатай', u'Гуля', u'Гульнара',
                   u'Гулистан', u'Фируза', u'Фатима', u'Ясмин', u'Айгюль', u'Зульфия', u'Ламия', u'Лейла', u'Марьям',
                   u'Самира', u'Хурма',
                   u'Чинара', u'Эльмира'],
    'titan_first': [u'Агата', u'Адонисия', u'Алексино', u'Амброзия', u'Антигона', u'Ариадна', u'Артемисия', u'Афродита',
                    u'Гликерия', u'Дельфиния', u'Деметра', u'Зиновия', u'Калисто', u'Калипсо', u'Кора', u'Ксения',
                    u'Медея', u'Мельпомена', u'Мнемозина',
                    u'Немезида', u'Олимпия', u'Пандора', u'Персефона', u'Таисия', u'Персея', u'Персея', u'Психея',
                    u'Сапфо', u'Талия', u'Терпсихора',
                    u'Фаломена', u'Гаромония', u'Хрисеида',
                    u'Эфимия', u'Юнона']}

girls_info = {  # Информация о всех типах девушек
                'peasant': {
                    'magic_rating': 0,  # магический рейтинг
                    'regular_spawn': 'poisonous_asp',  # идентификатор обычного отродья
                    'advanced_spawn': 'basilisk',  #идентификатор продвинутого отродья
                    'giantess': False,  #является ли великаншей
                    'avatar': 'peasant',  #аватарка
                    't_count_min': 0,  #количество сокровищ минимальное
                    't_count_max': 2,  #количество сокровищ максимальное
                    't_price_min': 1,  #минимальная цена предмета
                    't_price_max': 50,  #максимальная цена предмета
                    't_alignment': 'human',  #тип украшений
                    't_list': ['casket', 'statue', 'mirror', 'comb', 'phallos', 'band', 'earring', 'necklace',
                               'pendant', 'ring', 'broch', 'armbrace', 'legbrace', 'fibula', 'farting'],
                    #список возможных предметов в сокровищах

                },
                'citizen': {
                    'magic_rating': 0,
                    'regular_spawn': 'winged_asp',
                    'advanced_spawn': 'kobold',
                    'giantess': False,
                    'avatar': 'citizen',
                    't_count_min': 2,
                    't_count_max': 5,
                    't_price_min': 25,
                    't_price_max': 250,
                    't_alignment': 'human',
                    't_list': ['casket', 'statue', 'mirror', 'comb', 'phallos', 'band', 'diadem', 'tiara', 'earring',
                               'necklace', 'pendant', 'ring', 'broch', 'gemring', 'armbrace', 'legbrace', 'chain',
                               'fibula', 'taller'],
                },
                'thief': {
                    'magic_rating': 0,
                    'regular_spawn': 'winged_asp',
                    'advanced_spawn': 'kobold',
                    'giantess': False,
                    'avatar': 'thief',
                    't_count_min': 2,
                    't_count_max': 5,
                    't_price_min': 25,
                    't_price_max': 250,
                    't_alignment': 'human',
                    't_list': ['casket', 'statue', 'mirror', 'comb', 'phallos', 'band', 'diadem', 'tiara', 'earring',
                               'necklace', 'pendant', 'ring', 'broch', 'gemring', 'armbrace', 'legbrace', 'chain',
                               'fibula', 'taller', 'dublon'],
                },
                'knight': {
                    'magic_rating': 1,
                    'regular_spawn': 'krokk',
                    'advanced_spawn': 'lizardman',
                    'giantess': False,
                    'avatar': 'knight',
                    't_count_min': 2,
                    't_count_max': 5,
                    't_price_min': 25,
                    't_price_max': 250,
                    't_alignment': 'knight',
                    't_list': ['casket', 'statue', 'mirror', 'comb', 'phallos', 'band', 'diadem', 'tiara', 'earring',
                               'necklace', 'pendant', 'ring', 'broch', 'gemring', 'armbrace', 'legbrace', 'chain',
                               'fibula', 'taller', 'dublon'],
                },
                'princess': {
                    'magic_rating': 1,
                    'regular_spawn': 'krokk',
                    'advanced_spawn': 'lizardman',
                    'giantess': False,
                    'avatar': 'princess',
                    't_count_min': 4,
                    't_count_max': 10,
                    't_price_min': 250,
                    't_price_max': 100000,
                    't_alignment': 'knight',
                    't_list': ['casket', 'statue', 'mirror', 'comb', 'phallos', 'band', 'diadem', 'tiara', 'earring',
                               'necklace', 'pendant', 'ring', 'broch', 'gemring', 'armbrace', 'legbrace', 'chain',
                               'fibula'],
                },
                'elf': {
                    'magic_rating': 2,
                    'regular_spawn': 'gargoyle',
                    'advanced_spawn': 'dragonborn',
                    'giantess': False,
                    'avatar': 'elf',
                    't_count_min': 3,
                    't_count_max': 7,
                    't_price_min': 250,
                    't_price_max': 100000,
                    't_alignment': 'elf',
                    't_list': ['casket', 'statue', 'mirror', 'comb', 'phallos', 'band', 'diadem', 'tiara', 'earring',
                               'necklace', 'pendant', 'ring', 'broch', 'gemring', 'armbrace', 'legbrace', 'chain'],
                },
                'mermaid': {
                    'magic_rating': 2,
                    'regular_spawn': 'octopus',
                    'advanced_spawn': 'sea_bastard',
                    'giantess': False,
                    'avatar': 'mermaid',
                    't_count_min': 2,
                    't_count_max': 5,
                    't_price_min': 10,
                    't_price_max': 500,
                    't_alignment': 'merman',
                    't_list': ['casket', 'statue', 'mirror', 'comb', 'phallos', 'band', 'diadem', 'tiara', 'earring',
                               'necklace', 'pendant', 'ring', 'broch', 'gemring', 'armbrace', 'legbrace', 'chain'],
                },
                'ogre': {
                    'magic_rating': 2,
                    'regular_spawn': 'strigg',
                    'advanced_spawn': 'minotaur',
                    'giantess': True,
                    'avatar': 'ogre',
                    't_count_min': 2,
                    't_count_max': 5,
                    't_price_min': 25,
                    't_price_max': 250,
                    't_alignment': 'knight',
                    't_list': ['casket', 'statue', 'mirror', 'comb', 'phallos', 'band', 'diadem', 'tiara', 'earring',
                               'necklace', 'pendant', 'ring', 'broch', 'gemring', 'armbrace', 'legbrace', 'chain',
                               'fibula', 'farting', 'taller', 'dublon'],
                },
                'siren': {
                    'magic_rating': 3,
                    'regular_spawn': 'murloc',
                    'advanced_spawn': 'naga',
                    'giantess': True,
                    'avatar': 'mermaid',
                    't_count_min': 2,
                    't_count_max': 5,
                    't_price_min': 100,
                    't_price_max': 5000,
                    't_alignment': 'merman',
                    't_list': ['casket', 'statue', 'mirror', 'comb', 'phallos', 'band', 'diadem', 'tiara', 'earring',
                               'necklace', 'pendant', 'ring', 'broch', 'gemring', 'armbrace', 'legbrace', 'chain',
                               'taller', 'dublon'],
                },
                'ice': {
                    'magic_rating': 3,
                    'regular_spawn': 'ice_worm',
                    'advanced_spawn': 'yetti',
                    'giantess': True,
                    'avatar': 'ice',
                    't_count_min': 3,
                    't_count_max': 7,
                    't_price_min': 100,
                    't_price_max': 1000,
                    't_alignment': 'human',
                    't_list': ['casket', 'statue', 'mirror', 'comb', 'phallos', 'band', 'diadem', 'tiara', 'earring',
                               'necklace', 'pendant', 'ring', 'broch', 'gemring', 'armbrace', 'legbrace', 'chain',
                               'taller', 'dublon'],
                },
                'fire': {
                    'magic_rating': 3,
                    'regular_spawn': 'hell_hound',
                    'advanced_spawn': 'barlog',
                    'giantess': True,
                    'avatar': 'fire',
                    't_count_min': 3,
                    't_count_max': 7,
                    't_price_min': 100,
                    't_price_max': 1000,
                    't_alignment': 'dwarf',
                    't_list': ['casket', 'statue', 'mirror', 'comb', 'phallos', 'band', 'diadem', 'tiara', 'earring',
                               'necklace', 'pendant', 'ring', 'broch', 'gemring', 'armbrace', 'legbrace', 'chain',
                               'taller', 'dublon'],
                },
                'titan': {
                    'magic_rating': 4,
                    'regular_spawn': 'chimera',
                    'advanced_spawn': 'troll',
                    'giantess': True,
                    'avatar': 'titan',
                    't_count_min': 3,
                    't_count_max': 7,
                    't_price_min': 100,
                    't_price_max': 1000,
                    't_alignment': 'elf',
                    't_list': ['casket', 'statue', 'mirror', 'comb', 'phallos', 'band', 'diadem', 'tiara', 'earring',
                               'necklace', 'pendant', 'ring', 'broch', 'gemring', 'armbrace', 'legbrace', 'chain',
                               'taller', 'dublon'],
                },
}

spawn_info = {  # Информация о всех типах отродий
                'goblin': {
                    'power': 1,  # сила
                    'modifier': [],  # возможные роли
                    'name': u'Гоблин',  #название
                },
                'poisonous_asp': {
                    'power': 1,  # сила
                    'modifier': ['poisonous'],  # возможные роли
                    'name': u'Ядовитый аспид',  #название
                },
                'winged_asp': {
                    'power': 2,
                    'modifier': ['poisonous'],
                    'name': u'Крылатый аспид',
                },
                'krokk': {
                    'power': 1,
                    'modifier': ['servant'],
                    'name': u'Крокк',
                },
                'basilisk': {
                    'power': 3,
                    'modifier': ['poisonous'],
                    'name': u'Василиск',
                },
                'kobold': {
                    'power': 2,
                    'modifier': ['servant'],
                    'name': u'Кобольд',
                },
                'lizardman': {
                    'power': 3,
                    'modifier': ['warrior'],
                    'name': u'Ящерик',
                },
                'dragonborn': {
                    'power': 3,
                    'modifier': ['elite'],
                    'name': u'Драконорождённый',
                },
                'gargoyle': {
                    'power': 4,
                    'modifier': ['warrior'],
                    'name': u'Гаргуйль',
                },
                'sea_bastard': {
                    'power': 3,
                    'modifier': ['poisonous', 'marine'],
                    'name': u'Рыбоглаз',
                },
                'octopus': {
                    'power': 5,
                    'modifier': ['poisonous', 'marine'],
                    'name': u'Ядовитый спрут',
                },
                'hell_hound': {
                    'power': 4,
                    'modifier': ['poisonous'],
                    'name': u'Адская гончая',
                },
                'minotaur': {
                    'power': 5,
                    'modifier': ['elite'],
                    'name': u'Минотавр',
                },
                'murloc': {
                    'power': 3,
                    'modifier': ['warrior', 'marine'],
                    'name': u'Мурлок',
                },
                'naga': {
                    'power': 5,
                    'modifier': ['elite', 'marine'],
                    'name': u'Нага',
                },
                'yettie': {
                    'power': 5,
                    'modifier': ['warrior'],
                    'name': u'Йетти',
                },
                'troll': {
                    'power': 6,
                    'modifier': ['elite'],
                    'name': u'Тролль',
                },
                'strigg': {
                    'power': 6,
                    'modifier': ['poisonous'],
                    'name': u'Стригой',
                },
                'barlog': {
                    'power': 7,
                    'modifier': ['elite'],
                    'name': u'Дэв',
                },
                'chimera': {
                    'power': 10,
                    'modifier': ['poisonous'],
                    'name': u'Химера',
                },
}

girls_texts = {
    # Подстановки: {0} - имя девушки, {1} - имя дракона, {2} - ситуативные описания - что украли, кого родила и прочее
    'girl': {  # используется, если нет подходящего текста или отсутствует нужный тип девушки
               'sex': (  # Описание секса с девушкой
                         u"Случайная сцена секса вариант 1",
                         u"Случайная сцена секса вариант 2",
                         u"Случайная сцена секса вариант 3",
               ),
               'new': (  # Описание новой девушки
                         u"{0}",
               ),
               'free': (  # Описание процесса выпускания на свободу
                          u"Описание процесса выпускания на свободу",
               ),
               'free_prison': (  # Описание процесса выпускания на свободу из тюрьмы
                                 u"Описание процесса выпускания на свободу из тюрьмы",
               ),
               'steal': (  # Описание процесса воровства девушки
                           u"{1} относит пленницу в своё логово...",
               ),
               'jail': (  # Описание процесса заточения в темницу
                          u"...и сажает её под замок",
               ),
               'jailed': (  # Описание процесса возврата в темницу
                            u"{1} возвращает девушку в темницу",
               ),
               'eat': (  # Описание процесса поедания девушки. Как же ему не стыдно, червяку подколодному.
                         u"{1} кушает девушку",
               ),
               'rob': (  # Описание процесса ограбления девушки.
                         u"{1} грабит девушку и получает: \n {2}",
               ),
               'traps': (  # Описание процесса побега и гибели в ловушке.
                           u"{0} убегает из темницы и гибнет в ловушках",
               ),
               'escape': (  # Описание успешного побега
                            u"{0} спасается бегством",
               ),
               'birth': (  # Описание родов
                           u"{0} рожает кучу тварей, известных людям под именем {2}",
               ),
               'anguish': (  # Описание смерти от тоски
                             u"{0} умирает в тоске",
               ),
               'hunger': (  # Описание смерти от голода
                            u"{0} умирает от голода",
               ),
               'kill': (  # Описание смерти от селян
                          u"Люди узнают, что {0} беременна от дракона и убивают её",
               ),
               'free_birth': (  # Описание родов на свободе
                                u"{0} рожает что-то на воле",
               ),
               'prison': (  # Проведываем девушку в тюрьме
                            u"{0} в тюрьме",
               ),
    },
    'peasant': {  # используется для крестьянок
                  'sex': (  # Возможные описания секса с крестьянкой
                            u"Подходящая сцена секса c крестьянкой",
                  )
    },
}
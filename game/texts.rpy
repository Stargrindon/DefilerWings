#здесь хранятся тексты для игры

python early:
    #Описания дракона
    hunger_texts = {}
    hunger_texts[0] = '{font=fonts/AnticvarShadow.ttf}{color=#ff0000}Обожрался{/color}{/font}'
    hunger_texts[1] = '{font=fonts/AnticvarShadow.ttf}{color=#ff00ff}Сытый{/color}{/font}'
    hunger_texts[2] = '{font=fonts/AnticvarShadow.ttf}{color=#0000ff}Заморил червячка{/color}{/font}'
    hunger_texts[3] = '{font=fonts/AnticvarShadow.ttf}{color=#00ff00}Голодный{/color}{/font}'

    lust_texts = {}
    lust_texts[0] = '{font=fonts/AnticvarShadow.ttf}{color=#ff0000}Вялый{/color}{/font}'
    lust_texts[1] = '{font=fonts/AnticvarShadow.ttf}{color=#ff00ff}Возбужден{/color}{/font}'
    lust_texts[2] = '{font=fonts/AnticvarShadow.ttf}{color=#0000ff}Осеменитель{/color}{/font}'
    lust_texts[3] = '{font=fonts/AnticvarShadow.ttf}{color=#00ff00}Сосуд похоти{/color}{/font}'

    bloodlust_texts = {}
    bloodlust_texts[5] = '{font=fonts/AnticvarShadow.ttf}{color=#ff0000}Взбешен{/color}{/font}'
    bloodlust_texts[4] = '{font=fonts/AnticvarShadow.ttf}{color=#ff00ff}Разъярен{/color}{/font}'
    bloodlust_texts[3] = '{font=fonts/AnticvarShadow.ttf}{color=#ff00ff}Раздражен{/color}{/font}'
    bloodlust_texts[2] = '{font=fonts/AnticvarShadow.ttf}{color=#0000ff}Напряжен{/color}{/font}'
    bloodlust_texts[1] = '{font=fonts/AnticvarShadow.ttf}{color=#ссссff}Спокоен{/color}{/font}'    
    bloodlust_texts[0] = '{font=fonts/AnticvarShadow.ttf}{color=#00ff00}Умиротворен{/color}{/font}'

    health_texts = {}
    health_texts[0] = '{font=fonts/AnticvarShadow.ttf}{color=#ff0000}Полудохлый{/color}{/font}'
    health_texts[1] = '{font=fonts/AnticvarShadow.ttf}{color=#ff00ff}Раненый{/color}{/font}'
    health_texts[2] = '{font=fonts/AnticvarShadow.ttf}{color=#00ff00}Цел и невредим{/color}{/font}'
    
    size_texts = {}
    size_texts[1] = 'Мелкий'
    size_texts[2] = 'Обычный'
    size_texts[3] = 'Крупный'
    size_texts[4] = 'Внушительный'
    size_texts[5] = 'Огромный'
    size_texts[6] = 'Исполинский'
    
    womennum = ['первая', 'вторая', 'третья', 'четвёртая', 'пятая', 'шестая', 'седьмая']

    head_texts = {}
    head_texts['red'] = 'изрыгает дымное плямя'
    head_texts['white'] = 'обладает леденящим дыханием'
    head_texts['blue'] = 'оснащена жабрами и плавниками'
    head_texts['black'] = 'испускает нозрдями ядовитые испарения'
    head_texts['iron'] = 'щетинится стальными пластинами'
    head_texts['bronze'] = 'способна рыть землю как бронзовый ковш'
    head_texts['silver'] = 'украшена гребнем по которому струятся молнии'
    head_texts['gold'] = 'изрыгает имеет способность видеть невидимое'
    head_texts['shadow'] = 'повелевает жуткой некромантией'
                
    wingstxt = ['Он ползает извиваясь по земле подобно исполинскому змею.', 'Он оснащен могучими крыльями, способными нести его по воздуху.', 'У него на спине две пары перепончатых крыл', 'Он оснащён тремя парами разноразмерных крыльев, обеспечиваюих невероятную маневренность.']
    pawstxt = ['Он ползает извиваясь по земле подобно исполинскому змею.', 'Он опирается на пару мощных когтистых лап', 'У него четыре когтистые лапы.', 'Три пары мощных когтистых лап дают ему невероятную подвижность и устойчивость.']
    
    #Прыдстория игры
    intro_text = '{font=fonts/AnticvarShadow.ttf}{size=+10}    Давным-давно, в незапамятные времена, наш мир был юн и чист. Все пять народов, жили в мире и гармонии, процветали и развивались. Люди, народ равнин, засеяли бескрайние поля золотой пшеницей и разбили на холмах цветущие сады полные сладких плодов. Дети богини Дану, мудрые и прекрасные альвы сплетали магические узоры из песен и лунного света в глубине своих обширных лесов. Искусные цверги ковали металлы и гранили сияющие словно звезды самоцветы под сенью своих резных чертогов. Беспечные русалки играли с серебристыми рыбками и танцевали хороводы под синей гладью океана. И даже старые словно сам мир великаны не трогали малых народов, но наставляли их в древнем знании.     {vspace=30}Те дни минули без следа, когда в наш мир вошло зло. Никто доподлинно не знает, откуда явилась Она. Нагая, крылатая, прекрасная как полуденная греза и ужасная как полуночный кошмар. В преданиях сказано, что она вышла из белого как молоко утреннего тумана что сгустился в глубине непролазного бурелома. Но многие верят что ее породила сама преисподняя.    {vspace=30}Способная принять любой облик, соблазнительный или внушающий леденящий страх, она несла за собой гиль и раздор. В своей противоестественной, неуемной похоти она сходилась со всеми до кого могла добраться. Жаждала всякого мужского семени от гордых королей и от грязных крестьян, от людей и от зверей. В сих противоестественных союзах она породила сонмы тварей, искаженных и злобных, жестоких, жадных и полных греха.    {vspace=30}Страхом и ненавистью Владычица Тьмы выковала себе армию и двинула ее на вольные народы, чтобы навеки поработить весь свет и заставить каждого служить себе. Могучая и безжалостная армия Тьмы оставляла за собой лишь трупы, пепелища и бесплодную землю.     {vspace=30}Но пять свободных народов дали ей отпор. Собравшись вместе армии людей, альвов, цвергов, русалок и великанов одолели темную силу и загнали исчадий Владычицы в бесплодные вулканические земли далеко на востоке. Чтобы защититься, люди построили неприступные крепости и возвели города с высокими стенами и башнями, цверги создали боевые машины и автоматы, альвы оградили свои рощи чарами сокрытия и выставили на границах бдительных стражей. Даже беспечные русалки взяли в руки трезубцы и сети, готовые отразить нападение.     {vspace=30}Глядя на эту неодолимую силу Владычица поклялась создать чудовище, перед мощью которого не устоит никто на свете. В дышащих ядовитыми испарениям южных болотах она сошлась с самым откормленным змеем которого только смогла сыскать и отложила три больших яйца из которых вылупились чудовища, подобных которым еще не знала земля - драконы.    {vspace=30}   Все смертные грехи слились в этих тварях. Яростные и кровожадные, драконы не знают пощады и милосердия. Их гордыня и зависть заставляет драконов стяжать себе дурную славу, разрушая все прекрасное и неся страдание всему живому. В неуемной похоти своей они оскверняют невинных девушек и те рожают им чудовищ подобных выродкам самой Владычицы. Ненасытные, пожирают драконы равно добрых людей и лесных зверей, и морских рыб, и птиц небесных. Алчные до серебра и злата, сгребают в своих зловонных пещерах груды сокровищ и спят на них годами, предаваясь праздности и самодовольству.     {vspace=30}Первые из драконов были не так уж и могучи, не многим больше чем огромные болотные змеи. Но Владычица раз за разом отбирает лучших, чтобы в кровосмесительно-мерзостном соитии породить новое, беспрестанно мутирующее потомство. Все крупнее, сильнее, все злобнее и коварнее становятся драконы. Если не пресечь их род, то наступит день когда перед их мощью не устоят ни самые высокие стены, ни самые большие армии. Даже богоподобные титаны в своих облачных цитаделях не смогут спать спокойно. Но покамест надежда еще жива...{/size}{/font}'
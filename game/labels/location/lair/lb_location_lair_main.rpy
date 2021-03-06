# coding=utf-8

init python:
    import random
    
    from pythoncode import utils
    
label lb_location_lair_main:
    python:
        if not renpy.music.is_playing():
            renpy.music.play(get_random_files('mus/ambient'))    
    $ place = game.lair.type_name
    hide bg
    show place as bg
    nvl clear
    
    menu:
        'Осмотреть дракона':
            # чтобы вывести сообщение от имени дракона можно использовать "game.dragon"
            game.dragon.third "{font=fonts/AnticvarShadow.ttf}{size=+5} [game.dragon.fullname] {/size}{/font} \n\n[game.dragon.description]"
        'Проинспектировать логово':
            python hide:
                lair_description = u"Логово: %s.\n" % game.lair.type.name
                if len(game.lair.upgrades) > 0: 
                    lair_description += u"Улучшения:\n"
                    for upgrade in game.lair.upgrades.values():   
                        lair_description += u" %s\n" % upgrade.name
                else:
                    lair_description += u"Улучшений нет"
                narrator(lair_description)
            call lb_location_lair_main from _call_lb_location_lair_main
        'Сотворить заклинание' if game.dragon.bloodiness < 5 and game.dragon.mana > 0:
            if game.choose_spell(u"Вернуться в логово"):
                python:
                    game.dragon.drain_mana()
                    game.dragon.gain_rage()
            call lb_location_lair_main from _call_lb_location_lair_main_1
        'Чахнуть над златом' if game.lair.treasury.wealth > 0:
            python:
                files = [f for f in renpy.list_files() if f.startswith("img/bg/hoard/%s" % game.dragon.color_eng)]    
                if len(files) > 0:
                    treasurybg = random.choice(files)
                else:
                    treasurybg = "img/bg/hoard/base.jpg"
                renpy.treasurybg = ui.image(treasurybg)
                    
            show image renpy.treasurybg as bg
            nvl clear
            menu:
                '[game.lair.treasury.wealth_description]'
                '[game.lair.treasury.gems_mass_description]' if game.lair.treasury.gem_mass > 0:
                    "[game.lair.treasury.gems_list]"
                    nvl clear
                '[game.lair.treasury.materials_mass_description]' if game.lair.treasury.metal_mass + game.lair.treasury.material_mass > 0:
                    "[game.lair.treasury.materials_list]"
                    nvl clear
                '[game.lair.treasury.coin_mass_description]' if game.lair.treasury.coin_mass > 0:
                    $ description = u"В сокровищнице:\n"
                    $ description += u"%s\n" % treasures.number_conjugation_rus(game.lair.treasury.farting, u"фартинг")
                    $ description += u"%s\n" % treasures.number_conjugation_rus(game.lair.treasury.taller, u"талер")
                    $ description += u"%s" % treasures.number_conjugation_rus(game.lair.treasury.dublon, u"дублон")
                    "[description]"
                    nvl clear
                '[game.lair.treasury.jewelry_mass_description]' if len(game.lair.treasury.jewelry) > 0:
                    menu:
                        'Самая дорогая в сокровищнице':
                            "[game.lair.treasury.most_expensive_jewelry]"
                            nvl clear
                        'Самая дешёвая в сокровищнице':
                            "[game.lair.treasury.cheapest_jewelry]"
                            nvl clear
                        'Случайная':
                            "[game.lair.treasury.random_jewelry]"
                            nvl clear
                        'Вернуться в логово':
                            jump lb_location_lair_main   
                'Вернуться в логово':
                    jump lb_location_lair_main        
            call lb_location_lair_main from _call_lb_location_lair_main_2
        'Проведать пленниц' if game.girls_list.prisoners_count > 0:
            call screen girls_menu
            call lb_location_lair_main from _call_lb_location_lair_main_3            
        'Смастерить вещь' if ('servant' in game.lair.upgrades) or ('gremlin_servant' in game.lair.upgrades):
            $ new_item = game.lair.treasury.craft(**data.craft_options['servant'])
            if new_item:
                $ game.lair.treasury.receive_treasures([new_item])
                $ test_description = new_item.description()
                "Изготовлено: [test_description]."
            call lb_location_lair_main from _call_lb_location_lair_main_4                
        'Уволить слуг-гремлинов' if 'gremlin_servant' in game.lair.upgrades:
            $ del game.lair.upgrades['gremlin_servant']
            "Гремлины уходят"
            call lb_location_lair_main from _call_lb_location_lair_main_5            
        'Уволить охрану' if 'smuggler_guards' in game.lair.upgrades:
            $ del game.lair.upgrades['smuggler_guards']
            "Охрана покидает посты"
            call lb_location_lair_main from _call_lb_location_lair_main_6
        'Лечь спать':
            nvl clear
            python:
                # Делаем хитрую штуку.
                # Используем переменную game_loaded чтобы определить была ли игра загружена.
                # Но ставим ее перед самым сохранинием, используя renpy.retain_after_load() для того
                # чтобы она попала в сохранение.
                if 'game_loaded' in locals() and game_loaded:
                    del game_loaded
                    game.narrator("game loaded")
                    renpy.restart_interaction()
                else:
                    game_loaded = True
                    renpy.retain_after_load()
                    if not freeplay:
                        utils.call ("lb_achievement_acquired")
                        game.save()
                    else:
                        game.save_freegame()
                    save_blocked = True
                    
                    game.sleep()
                    save_blocked = False
                    del game_loaded
            $this_turn_achievements = []
        'Покинуть логово':
            $ pass
            
    return
    
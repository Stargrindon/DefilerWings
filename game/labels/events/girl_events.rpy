# coding=utf-8
label lb_event_girl_escape:
    $ place = game.lair.type_name
    hide bg
    show place as bg
    nvl clear
    $ game.girls_list.description('escape', True)  # описание чудесного спасения
    return

label lb_event_girl_spawn(spawn_type):
    $ spawn_image = "img/scene/spawn/%s.png" % spawn_type
    hide bg
    show expression spawn_image as bg
    nvl clear
    python:
        spawn_description = game.girls_list.description(spawn_type)  # описание родов конкретного типа
        if not spawn_description:
            from pythoncode import girls_data
            if 'elite' in girls_data.spawn_info[spawn_type]['modifier']:
                spawn_description = game.girls_list.description('spawn_elite')
            else:
                spawn_description = game.girls_list.description('spawn_common')
    "[spawn_description]"
    return

label lb_event_girl_free_spawn(spawn_type):
    $ spawn_image = 'img/scene/spawn/%s.png' % spawn_type
    hide bg
    show expression spawn_image as bg
    nvl clear
    $ free_spawn_description = game.girls_list.description('free_spawn')  # описание родов на воле
    "[free_spawn_description]"
    return

label lb_event_girl_hunger_death:
    $ place = game.lair.type_name
    hide bg
    show place as bg
    nvl clear
    $ game.girls_list.description('hunger_death', True)  # описание смерти девушки от голода
    return

label lb_event_girl_kill:
    hide bg
    show expression 'img/scene/girl_death.png' as bg
    nvl clear
    $ game.girls_list.description('kill', True)  # убивают из-за беременности
    return
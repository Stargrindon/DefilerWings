label lb_location_sky_main:
    $ place = 'sky'
    show expression get_place_bg(place) as bg
    nvl clear
    
    if not game.dragon.can_fly: 
        '[game.dragon.name] с тоской смотрит в небо. Если бы только он умел летать...'
        return
        
    return
    
from folium import Map, Marker, Icon

show_map = Map(location=[54.6877410077157, 25.283378174997512], zoom_start=6)

locations = [
    [54.899572230498976, 23.90833610389087],
    [54.6877410077157, 25.283378174997512],
    [55.70781449602359, 21.170957775607707],
    [55.92050275116782, 23.339913888681366],
    [55.745983221205684, 24.31741416887826],
]

for location in locations:
    Marker(location, popup='<i>Healthy Food Store</i>', icon=Icon(icon='info-sign')).add_to(show_map)

show_map.save("templates/contact_info_app/map.html")

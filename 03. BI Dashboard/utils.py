def format_number(num):
    if num > 1000000:
        if not num % 1000000:
            return f'{num // 1000000} M'
        return f'{round(num / 1000000, 1)} M'
    return f'{num // 1000} K'


color_palettes = [
    "tableau10",
    "tableau20",
    "viridis",
    "spectral",
    "category10",
    "inferno",
    "magma",
    "cividis",
    "dark2",
    "paired",
    "blues",
    "greens",
    "reds",
    "plasma",
    "rainbow",
    "turbo",
    "accent",
    "category20",
    "category20b",
    "category20c",
    "pastel1",
    "pastel2",
    "set1",
    "set2",
    "set3",
    "tealblues",
    "teals",
    "browns",
    "greys",
    "purples",
    "warmgreys",
    "oranges",
    "bluegreen",
    "bluepurple",
    "goldgreen",
    "goldorange",
    "goldred",
    "greenblue",
    "orangered",
    "purplebluegreen",
    "purpleblue",
    "purplered",
    "redpurple",
    "yellowgreenblue",
    "yellowgreen",
    "yelloworangebrown",
    "yelloworangered",
    "darkblue",
    "darkgold",
    "darkgreen",
    "darkmulti",
    "darkred",
    "lightgreyred",
    "lightgreyteal",
    "lightmulti",
    "lightorange",
    "lighttealblue",
    "blueorange",
    "brownbluegreen",
    "purplegreen",
    "pinkyellowgreen",
    "purpleorange",
    "redblue",
    "redgrey",
    "redyellowblue",
    "redyellowgreen",
    "sinebow"
]

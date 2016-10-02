#central_server_address = 'http://localhost:8000/'
central_server_address = 'http://192.168.0.200/'

intersection_label = 'inter2'

# light pin definitions
light_pins = {
    'as1r': (12,),
    'as1y': (5,),
    'as1g': (13,),
    'as2r': (0,),
    'as2y': (6,),
    'as2g': (26,),
    'alg': (19,),
    'bsr': (1,),
    'bsy': (7,),
    'bsg': (8,),
    'cs1r': (25,),
    'cs1y': (10,),
    'cs1g': (22,),
    'cs2r': (11,),
    'cs2y': (9,),
    'cs2g': (27,),
    'clg': (17,),
    'dsr': (21,),
    'dsy': (20,),
    'dsg': (16,),
}

# map lights keys to directions
mapping_labels = {
    'roadA': {
        'L': (
            ('',),
            ('',),
            ('alg',),
        ),
        'S': (
            ('as1r', 'as2r',),
            ('as1y', 'as2y',),
            ('as1g', 'as2g',),
        ),
    },
    'roadB': {
        'S': (
            ('bsr',),
            ('bsy',),
            ('bsg',),
        ),
    },
    'roadC': {
        'L': (
            ('',),
            ('',),
            ('clg',),
        ),
        'S': (
            ('cs1r', 'cs2r',),
            ('cs1y', 'cs2y',),
            ('cs1g', 'cs2g',),
        ),
    },
    'roadD': {
        'S': (
            ('dsr',),
            ('dsy',),
            ('dsg',),
        ),
    },
}

# fallback pattern
disabled_pattern = {
    'signals': [
        {
            'roadA': {},
            'roadB': {'L':0, 'S':0, 'R':0},
            'roadC': {},
            'roadD': {'L':0, 'S':0, 'R':0},
        },
        {
            'roadA': {'L':0, 'S':0, 'R':0},
            'roadB': {},
            'roadC': {'L':0, 'S':0, 'R':0},
            'roadD': {},
        },
    ]
}

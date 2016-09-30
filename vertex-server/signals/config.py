central_server_address = 'http://localhost:8000/'
# central_server_address = 'http://10.0.0.21/'

intersection_label = 'inter4'

# light pin definitions
light_pins = {
    'alr': (24, 1),
    'aly': (24, 20),
    'alg': (24, 21),
    'asr': (24, 4),
    'asy': (24, 5),
    'asg': (24, 6),
    'ary': (24, 8),
    'arg': (24, 9),
    'bly': (23, 20),
    'blg': (23, 22),
    'bs1r': (27, 1),
    'bs1y': (27, 20),
    'bs1g': (27, 21),
    'bs2r': (23, 4),
    'bs2y': (23, 5),
    'bs2g': (23, 6),
    'bry': (23, 8),
    'brg': (23, 9),
    'clr': (26, 1),
    'cly': (26, 20),
    'clg': (26, 21),
    'csr': (26, 4),
    'csy': (26, 5),
    'csg': (26, 6),
    'cry': (26, 8),
    'crg': (26, 9),
    'dly': (26, 8),
    'dlg': (26, 9),
    'ds1r': (25, 1),
    'ds1y': (25, 20),
    'ds1g': (25, 21),
    'ds2r': (27, 4),
    'ds2y': (27, 5),
    'ds2g': (27, 6),
    'dry': (25, 5),
    'drg': (25, 6),
}

# map lights keys to directions
mapping_labels = {
    'roadA': {
        'L': (
            ('alr',),
            ('aly',),
            ('alg',),
        ),
        'S': (
            ('asr',),
            ('asy',),
            ('asg',),
        ),
        'R': (
            (),
            ('ary',),
            ('arg',),
        ),
    },
    'roadB': {
        'L': (
            (),
            ('bly',),
            ('blg',),
        ),
        'S': (
            ('bs1r', 'bs2r',),
            ('bs1y', 'bs2r',),
            ('bs1g', 'bs2g',),
        ),
        'R': (
            (),
            ('bry',),
            ('brg',),
        ),
    },
    'roadC': {
        'L': (
            ('clr',),
            ('cly',),
            ('clg',),
        ),
        'S': (
            ('csr',),
            ('csy',),
            ('csg',),
        ),
        'R': (
            (),
            ('cry',),
            ('crg',),
        ),
    },
    'roadD': {
        'L': (
            (),
            ('dly',),
            ('dlg',),
        ),
        'S': (
            ('ds1r', 'ds2r',),
            ('ds1y', 'ds2y',),
            ('ds1g', 'ds2g',),
        ),
        'R': (
            (),
            ('dry',),
            ('drg',),
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

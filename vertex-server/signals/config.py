#central_server_address = 'http://localhost:8000/'
central_server_address = 'http://10.0.0.21/'

intersection_label = 'inter3'

# light pin definitions
light_pins = {
  'alr': (26, 1),
  'aly': (26, 20),
  'alg': (26, 21),
  'asr': (26, 4),
  'asy': (26, 5),
  'asg': (26, 6),
  'ary': (26, 8),
  'arg': (26, 9),
  'bly': (25, 20),
  'blg': (25, 21),
  'bs1r': (25, 4),
  'bs1y': (25, 5),
  'bs1g': (25, 6),
  'bs2r': (27, 1),
  'bs2y': (27, 20),
  'bs2g': (27, 21),
  'bry': (25, 8),
  'brg': (25, 9),
  'clr': (23, 1),
  'cly': (23, 20),
  'clg': (23, 21),
  'csr': (23, 4),
  'csy': (23, 5),
  'csg': (23, 6),
  'cry': (23, 8),
  'crg': (23, 9),
  'dly': (24, 20),
  'dlg': (24, 21),
  'ds1r': (24, 4),
  'ds1y': (24, 5),
  'ds1g': (24, 6),
  'ds2r': (27, 4),
  'ds2y': (27, 5),
  'ds2g': (27, 6),
  'dry': (24, 8),
  'drg': (24, 9),
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
            ('',),
            ('ary',),
            ('arg',),
        ),
    },
    'roadB': {
        'L': (
            ('',),
            ('bly',),
            ('blg',),
        ),
        'S': (
            ('bs1r', 'bs2r'),
            ('bs1y', 'bs2y'),
            ('bs1g', 'bs2g'),
        ),
        'R': (
            ('',),
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
            ('',),
            ('cry',),
            ('crg',),
        ),
    },
    'roadD': {
        'L': (
            ('',),
            ('dly',),
            ('dlg',),
        ),
        'S': (
            ('ds1r', 'ds2r'),
            ('ds1y', 'ds2y'),
            ('ds1g', 'ds2g'),
        ),
        'R': (
            ('',),
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

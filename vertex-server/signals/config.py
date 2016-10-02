#central_server_address = 'http://localhost:8000/'
central_server_address = 'http://10.0.0.21/'

intersection_label = 'node2'

# light pin definitions
light_pins = {
  'alr': (19,),
  'aly': (13,),
  'alg': (5,),
  'asr': (26,),
  'asy': (6,),
  'asg': (0,),
  'bsr': (25,),
  'bsy': (8,),
  'bsg': (7,),
  'csr': (16,),
  'csy': (20,),
  'csg': (21,),
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
    },
    'roadB': {
        'S': (
            ('bsr',),
            ('bsy',),
            ('bsg',),
        ),
    },
    'roadC': {
        'S': (
            ('csr',),
            ('csy',),
            ('csg',),
        ),
    },
}

# fallback pattern
disabled_pattern = {
    'signals': [
        {
            'roadA': {'L':0, 'S':0, 'R':0},
            'roadB': {},
            'roadC': {'L':0, 'S':0, 'R':0},
        },
        {
            'roadA': {},
            'roadB': {'L':0, 'S':0, 'R':0},
            'roadC': {},
        },
    ]
}

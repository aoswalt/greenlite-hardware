#central_server_address = 'http://localhost:8000/'
central_server_address = 'http://10.0.0.21/'

intersection_label = 'inter5'

# light pin definitions
light_pins = {
  'aly': (20,),
  'alg': (18,),
  'asr': (21,),
  'asy': (16,),
  'asg': (12,),
  'bly': (13,),
  'blg': (5,),
  'bsr': (26,),
  'bsy': (19,),
  'bsg': (6,),
  'cly': (8,),
  'clg': (24,),
  'csr': (1,),
  'csy': (7,),
  'csg': (23,),
  'dly': (27,),
  'dlg': (22,),
  'dsr': (4,),
  'dsy': (17,),
  'dsg': (10,),
}

# map lights keys to directions
mapping_labels = {
    'roadA': {
        'L': (
            ('',),
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
        'L': (
            ('',),
            ('bly',),
            ('blg',),
        ),
        'S': (
            ('bsr',),
            ('bsy',),
            ('bsg',),
        ),
    },
    'roadC': {
        'L': (
            ('',),
            ('cly',),
            ('clg',),
        ),
        'S': (
            ('csr',),
            ('csy',),
            ('csg',),
        ),
    },
    'roadD': {
        'L': (
            ('',),
            ('dly',),
            ('dlg',),
        ),
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
            'roadA': {'L':0, 'S':0, 'R':0},
            'roadB': {},
            'roadC': {'L':0, 'S':0, 'R':0},
            'roadD': {},
        },
        {
            'roadA': {},
            'roadB': {'L':0, 'S':0, 'R':0},
            'roadC': {},
            'roadD': {'L':0, 'S':0, 'R':0},
        },
    ]
}

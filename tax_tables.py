# List of 50 states
STATES = [
    "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS",
    "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY",
    "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV",
    "WI", "WY"
]

# Federal standard deductions by filing status
FEDERAL_STANDARD_DEDUCTIONS = {
    "single": 14600,
    "married": 29200,
    "head_of_household": 21900
}

# Maximum wage base for Social Security tax
SOCIAL_SECURITY_WAGE_BASE = 168600

# Additional Medicare tax rate and thresholds
ADDITIONAL_MEDICARE_TAX_RATE = 0.009
ADDITIONAL_MEDICARE_TAX_THRESHOLDS = {
    "single": 200000,
    "married": 250000,
    "head_of_household": 200000,
}

# Federal tax brackets by income and filing status
FEDERAL_TAX_BRACKETS = {
    "single": [
        (0, 11600, 0.10),
        (11601, 47150, 0.12),
        (47151, 100525, 0.22),
        (100526, 191950, 0.24),
        (191951, 243725, 0.32),
        (243726, 609350, 0.35),
        (609351, float('inf'), 0.37)
    ],
    "married": [
        (0, 23200, 0.10),
        (23201, 94300, 0.12),
        (94301, 201050, 0.22),
        (201051, 383900, 0.24),
        (383901, 487450, 0.32),
        (487451, 731200, 0.35),
        (731201, float('inf'), 0.37)
    ],
    "head_of_household": [
        (0, 16550, 0.10),
        (16551, 63100, 0.12),
        (63101, 100500, 0.22),
        (100501, 191950, 0.24),
        (191951, 243700, 0.32),
        (243701, 609350, 0.35),
        (609351, float('inf'), 0.37)
    ]
}

# Social Security, Medicare, FUTA, and SUTA rates
SOCIAL_SECURITY_RATE = 0.062  # 6.2%
MEDICARE_RATE = 0.0145  # 1.45%
FUTA_RATE = 0.06  # 6.0%
FUTA_WAGE_BASE = 7000
STD_STATE_CREDIT = 0.054 

# Standard deductions and tax brackets for all states
STATE_TAX_INFO = {
    "AL": {
        "standard_deduction": {
            "single": 2500,
            "married": 7500,
            "head_of_household": 7500
        },
        "single": [
            (0, 500, 0.02),
            (501, 3000, 0.04),
            (3001, float('inf'), 0.05)
        ],
        "married": [
            (0, 1000, 0.02),
            (1001, 6000, 0.04),
            (6001, float('inf'), 0.05)
        ],
        "head_of_household": [
            (0, 1000, 0.02),
            (1001, 6000, 0.04),
            (6001, float('inf'), 0.05)
        ]
    },
    "AK": {
        "standard_deduction": {
            "single": 0,
            "married": 0,
            "head_of_household": 0
        },
        "single": [(0, float('inf'), 0.0)],
        "married": [(0, float('inf'), 0.0)],
        "head_of_household": [(0, float('inf'), 0.0)]
    },
    "AZ": {
        "standard_deduction": {
            "single": 12200,
            "married": 24400,
            "head_of_household": 18300
        },
        "single": [
            (0, 27808, 0.0259),
            (27809, 55615, 0.0334),
            (55616, 166843, 0.0417),
            (166844, 250000, 0.045),
            (250001, float('inf'), 0.048)
        ],
        "married": [
            (0, 55615, 0.0259),
            (55616, 111229, 0.0334),
            (111230, 333686, 0.0417),
            (333687, 500000, 0.045),
            (500001, float('inf'), 0.048)
        ],
        "head_of_household": [
            (0, 27808, 0.0259),
            (27809, 55615, 0.0334),
            (55616, 166843, 0.0417),
            (166844, 250000, 0.045),
            (250001, float('inf'), 0.048)
        ]
    },
    "AR": {
        "standard_deduction": {
            "single": 2200,
            "married": 4400,
            "head_of_household": 4400
        },
        "single": [
            (0, 4500, 0.02),
            (4501, 8900, 0.04),
            (8901, 13300, 0.059),
            (13301, 22200, 0.065),
            (22201, float('inf'), 0.069)
        ],
        "married": [
            (0, 4500, 0.02),
            (4501, 8900, 0.04),
            (8901, 13300, 0.059),
            (13301, 22200, 0.065),
            (22201, float('inf'), 0.069)
        ],
        "head_of_household": [
            (0, 4500, 0.02),
            (4501, 8900, 0.04),
            (8901, 13300, 0.059),
            (13301, 22200, 0.065),
            (22201, float('inf'), 0.069)
        ]
    },
    "CA": {
        "standard_deduction": {
            "single": 4600,
            "married": 9200,
            "head_of_household": 9200
        },
        "single": [
            (0, 8932, 0.01),
            (8933, 21175, 0.02),
            (21176, 33421, 0.04),
            (33422, 46394, 0.06),
            (46395, 58634, 0.08),
            (58635, 299508, 0.093),
            (299509, 359407, 0.103),
            (359408, 599012, 0.113),
            (599013, float('inf'), 0.123)
        ],
        "married": [
            (0, 17864, 0.01),
            (17865, 42350, 0.02),
            (42351, 66842, 0.04),
            (66843, 92788, 0.06),
            (92789, 117268, 0.08),
            (117269, 599016, 0.093),
            (599017, 718814, 0.103),
            (718815, 1198024, 0.113),
            (1198025, float('inf'), 0.123)
        ],
        "head_of_household": [
            (0, 17864, 0.01),
            (17865, 42350, 0.02),
            (42351, 66842, 0.04),
            (66843, 92788, 0.06),
            (92789, 117268, 0.08),
            (117269, 599016, 0.093),
            (599017, 718814, 0.103),
            (718815, 1198024, 0.113),
            (1198025, float('inf'), 0.123)
        ]
    },
    "CO": {
        "standard_deduction": {
            "single": 12400,
            "married": 24800,
            "head_of_household": 18650
        },
        "single": [
            (0, float('inf'), 0.0463)
        ],
        "married": [
            (0, float('inf'), 0.0463)
        ],
        "head_of_household": [
            (0, float('inf'), 0.0463)
        ]
    },
    "CT": {
        "standard_deduction": {
            "single": 15000,
            "married": 24000,
            "head_of_household": 19000
        },
        "single": [
            (0, 10000, 0.03),
            (10001, 50000, 0.05),
            (50001, 100000, 0.055),
            (100001, 200000, 0.06),
            (200001, 500000, 0.065),
            (500001, float('inf'), 0.0699)
        ],
        "married": [
            (0, 20000, 0.03),
            (20001, 100000, 0.05),
            (100001, 200000, 0.055),
            (200001, 400000, 0.06),
            (400001, 1000000, 0.065),
            (1000001, float('inf'), 0.0699)
        ],
        "head_of_household": [
            (0, 16000, 0.03),
            (16001, 80000, 0.05),
            (80001, 160000, 0.055),
            (160001, 320000, 0.06),
            (320001, 800000, 0.065),
            (800001, float('inf'), 0.0699)
        ]
    },
    "DE": {
        "standard_deduction": {
            "single": 3250,
            "married": 6500,
            "head_of_household": 6500
        },
        "single": [
            (0, 2000, 0.022),
            (2001, 5000, 0.039),
            (5001, 10000, 0.048),
            (10001, 20000, 0.052),
            (20001, 25000, 0.0555),
            (25001, float('inf'), 0.066)
        ],
        "married": [
            (0, 2000, 0.022),
            (2001, 5000, 0.039),
            (5001, 10000, 0.048),
            (10001, 20000, 0.052),
            (20001, 25000, 0.0555),
            (25001, float('inf'), 0.066)
        ],
        "head_of_household": [
            (0, 2000, 0.022),
            (2001, 5000, 0.039),
            (5001, 10000, 0.048),
            (10001, 20000, 0.052),
            (20001, 25000, 0.0555),
            (25001, float('inf'), 0.066)
        ]
    },
    "FL": {
        "standard_deduction": {
            "single": 0,
            "married": 0,
            "head_of_household": 0
        },
        "single": [(0, float('inf'), 0.0)],
        "married": [(0, float('inf'), 0.0)],
        "head_of_household": [(0, float('inf'), 0.0)]
    },
    "GA": {
        "standard_deduction": {
            "single": 4600,
            "married": 6000,
            "head_of_household": 4600
        },
        "single": [
            (0, 750, 0.01),
            (751, 2250, 0.02),
            (2251, 3750, 0.03),
            (3751, 5250, 0.04),
            (5251, 7000, 0.05),
            (7001, float('inf'), 0.0575)
        ],
        "married": [
            (0, 1000, 0.01),
            (1001, 3000, 0.02),
            (3001, 5000, 0.03),
            (5001, 7000, 0.04),
            (7001, 10000, 0.05),
            (10001, float('inf'), 0.0575)
        ],
        "head_of_household": [
            (0, 750, 0.01),
            (751, 2250, 0.02),
            (2251, 3750, 0.03),
            (3751, 5250, 0.04),
            (5251, 7000, 0.05),
            (7001, float('inf'), 0.0575)
        ]
    },
    "HI": {
        "standard_deduction": {
            "single": 2200,
            "married": 4400,
            "head_of_household": 3200
        },
        "single": [
            (0, 2400, 0.014),
            (2401, 4800, 0.032),
            (4801, 9600, 0.055),
            (9601, 14400, 0.064),
            (14401, 19200, 0.068),
            (19201, 24000, 0.072),
            (24001, 36000, 0.076),
            (36001, 48000, 0.079),
            (48001, 150000, 0.0825),
            (150001, 175000, 0.09),
            (175001, 200000, 0.10),
            (200001, float('inf'), 0.11)
        ],
        "married": [
            (0, 4800, 0.014),
            (4801, 9600, 0.032),
            (9601, 19200, 0.055),
            (19201, 28800, 0.064),
            (28801, 38400, 0.068),
            (38401, 48000, 0.072),
            (48001, 72000, 0.076),
            (72001, 96000, 0.079),
            (96001, 300000, 0.0825),
            (300001, 350000, 0.09),
            (350001, 400000, 0.10),
            (400001, float('inf'), 0.11)
        ],
        "head_of_household": [
            (0, 3600, 0.014),
            (3601, 7200, 0.032),
            (7201, 14400, 0.055),
            (14401, 21600, 0.064),
            (21601, 28800, 0.068),
            (28801, 36000, 0.072),
            (36001, 54000, 0.076),
            (54001, 72000, 0.079),
            (72001, 225000, 0.0825),
            (225001, 262500, 0.09),
            (262501, 300000, 0.10),
            (300001, float('inf'), 0.11)
        ]
    },
    "ID": {
        "standard_deduction": {
            "single": 12950,
            "married": 25900,
            "head_of_household": 19400
        },
        "single": [
            (0, 1658, 0.01),
            (1659, 3316, 0.03),
            (3317, 4974, 0.045),
            (4975, 6632, 0.055),
            (6633, 8290, 0.065),
            (8291, float('inf'), 0.0675)
        ],
        "married": [
            (0, 3316, 0.01),
            (3317, 6632, 0.03),
            (6633, 9948, 0.045),
            (9949, 13264, 0.055),
            (13265, 16580, 0.065),
            (16581, float('inf'), 0.0675)
        ],
        "head_of_household": [
            (0, 1658, 0.01),
            (1659, 3316, 0.03),
            (3317, 4974, 0.045),
            (4975, 6632, 0.055),
            (6633, 8290, 0.065),
            (8291, float('inf'), 0.0675)
        ]
    },
    "IL": {
        "standard_deduction": {
            "single": 2250,
            "married": 4750,
            "head_of_household": 2250
        },
        "single": [
            (0, float('inf'), 0.0495)
        ],
        "married": [
            (0, float('inf'), 0.0495)
        ],
        "head_of_household": [
            (0, float('inf'), 0.0495)
        ]
    },
    "IN": {
        "standard_deduction": {
            "single": 1000,
            "married": 2000,
            "head_of_household": 1000
        },
        "single": [
            (0, float('inf'), 0.0323)
        ],
        "married": [
            (0, float('inf'), 0.0323)
        ],
        "head_of_household": [
            (0, float('inf'), 0.0323)
        ]
    },
    "IA": {
        "standard_deduction": {
            "single": 2030,
            "married": 5020,
            "head_of_household": 5020
        },
        "single": [
            (0, 1743, 0.0033),
            (1744, 3486, 0.0067),
            (3487, 6972, 0.0225),
            (6973, 15678, 0.0414),
            (15679, 26130, 0.0563),
            (26131, 34840, 0.0596),
            (34841, 52260, 0.0625),
            (52261, 78400, 0.0744),
            (78401, float('inf'), 0.0853)
        ],
        "married": [
            (0, 1743, 0.0033),
            (1744, 3486, 0.0067),
            (3487, 6972, 0.0225),
            (6973, 15678, 0.0414),
            (15679, 26130, 0.0563),
            (26131, 34840, 0.0596),
            (34841, 52260, 0.0625),
            (52261, 78400, 0.0744),
            (78401, float('inf'), 0.0853)
        ],
        "head_of_household": [
            (0, 1743, 0.0033),
            (1744, 3486, 0.0067),
            (3487, 6972, 0.0225),
            (6973, 15678, 0.0414),
            (15679, 26130, 0.0563),
            (26131, 34840, 0.0596),
            (34841, 52260, 0.0625),
            (52261, 78400, 0.0744),
            (78401, float('inf'), 0.0853)
        ]
    },
    "KS": {
        "standard_deduction": {
            "single": 3000,
            "married": 7500,
            "head_of_household": 5500
        },
        "single": [
            (0, 15000, 0.031),
            (15001, 30000, 0.0525),
            (30001, float('inf'), 0.057)
        ],
        "married": [
            (0, 30000, 0.031),
            (30001, 60000, 0.0525),
            (60001, float('inf'), 0.057)
        ],
        "head_of_household": [
            (0, 22500, 0.031),
            (22501, 45000, 0.0525),
            (45001, float('inf'), 0.057)
        ]
    },
    "KY": {
        "standard_deduction": {
            "single": 2770,
            "married": 5540,
            "head_of_household": 2770
        },
        "single": [
            (0, float('inf'), 0.05)
        ],
        "married": [
            (0, float('inf'), 0.05)
        ],
        "head_of_household": [
            (0, float('inf'), 0.05)
        ]
    },
    "LA": {
        "standard_deduction": {
            "single": 4500,
            "married": 9000,
            "head_of_household": 9000
        },
        "single": [
            (0, 12500, 0.02),
            (12501, 50000, 0.04),
            (50001, float('inf'), 0.06)
        ],
        "married": [
            (0, 25000, 0.02),
            (25001, 100000, 0.04),
            (100001, float('inf'), 0.06)
        ],
        "head_of_household": [
            (0, 12500, 0.02),
            (12501, 50000, 0.04),
            (50001, float('inf'), 0.06)
        ]
    },
    "ME": {
        "standard_deduction": {
            "single": 12400,
            "married": 24800,
            "head_of_household": 18650
        },
        "single": [
            (0, 22600, 0.058),
            (22601, 53150, 0.0675),
            (53151, float('inf'), 0.0715)
        ],
        "married": [
            (0, 45200, 0.058),
            (45201, 106300, 0.0675),
            (106301, float('inf'), 0.0715)
        ],
        "head_of_household": [
            (0, 33900, 0.058),
            (33901, 79725, 0.0675),
            (79726, float('inf'), 0.0715)
        ]
    },
    "MD": {
        "standard_deduction": {
            "single": 2350,
            "married": 4700,
            "head_of_household": 2350
        },
        "single": [
            (0, 1000, 0.02),
            (1001, 2000, 0.03),
            (2001, 3000, 0.04),
            (3001, 100000, 0.0475),
            (100001, 125000, 0.05),
            (125001, 150000, 0.0525),
            (150001, 250000, 0.055),
            (250001, float('inf'), 0.0575)
        ],
        "married": [
            (0, 1000, 0.02),
            (1001, 2000, 0.03),
            (2001, 3000, 0.04),
            (3001, 150000, 0.0475),
            (150001, 175000, 0.05),
            (175001, 225000, 0.0525),
            (225001, 300000, 0.055),
            (300001, float('inf'), 0.0575)
        ],
        "head_of_household": [
            (0, 1000, 0.02),
            (1001, 2000, 0.03),
            (2001, 3000, 0.04),
            (3001, 100000, 0.0475),
            (100001, 125000, 0.05),
            (125001, 150000, 0.0525),
            (150001, 250000, 0.055),
            (250001, float('inf'), 0.0575)
        ]
    },
    "MA": {
        "standard_deduction": {
            "single": 4400,
            "married": 8800,
            "head_of_household": 6600
        },
        "single": [
            (0, float('inf'), 0.05)
        ],
        "married": [
            (0, float('inf'), 0.05)
        ],
        "head_of_household": [
            (0, float('inf'), 0.05)
        ]
    },
    "MI": {
        "standard_deduction": {
            "single": 4900,
            "married": 9800,
            "head_of_household": 4900
        },
        "single": [
            (0, float('inf'), 0.0425)
        ],
        "married": [
            (0, float('inf'), 0.0425)
        ],
        "head_of_household": [
            (0, float('inf'), 0.0425)
        ]
    },
    "MN": {
        "standard_deduction": {
            "single": 12950,
            "married": 25900,
            "head_of_household": 19400
        },
        "single": [
            (0, 27930, 0.0535),
            (27931, 92030, 0.068),
            (92031, 171220, 0.0785),
            (171221, float('inf'), 0.0985)
        ],
        "married": [
            (0, 41280, 0.0535),
            (41281, 163060, 0.068),
            (163061, 284870, 0.0785),
            (284871, float('inf'), 0.0985)
        ],
        "head_of_household": [
            (0, 34980, 0.0535),
            (34981, 139210, 0.068),
            (139211, 232760, 0.0785),
            (232761, float('inf'), 0.0985)
        ]
    },
    "MS": {
        "standard_deduction": {
            "single": 2300,
            "married": 4600,
            "head_of_household": 2300
        },
        "single": [
            (0, 5000, 0.03),
            (5001, 10000, 0.04),
            (10001, float('inf'), 0.05)
        ],
        "married": [
            (0, 5000, 0.03),
            (5001, 10000, 0.04),
            (10001, float('inf'), 0.05)
        ],
        "head_of_household": [
            (0, 5000, 0.03),
            (5001, 10000, 0.04),
            (10001, float('inf'), 0.05)
        ]
    },
    "MO": {
        "standard_deduction": {
            "single": 12950,
            "married": 25900,
            "head_of_household": 19400
        },
        "single": [
            (0, 1058, 0.015),
            (1059, 2116, 0.02),
            (2117, 3174, 0.025),
            (3175, 4232, 0.03),
            (4233, 5290, 0.035),
            (5291, 6348, 0.04),
            (6349, 7406, 0.045),
            (7407, 8464, 0.05),
            (8465, 9522, 0.055),
            (9523, float('inf'), 0.059)
        ],
        "married": [
            (0, 1058, 0.015),
            (1059, 2116, 0.02),
            (2117, 3174, 0.025),
            (3175, 4232, 0.03),
            (4233, 5290, 0.035),
            (5291, 6348, 0.04),
            (6349, 7406, 0.045),
            (7407, 8464, 0.05),
            (8465, 9522, 0.055),
            (9523, float('inf'), 0.059)
        ],
        "head_of_household": [
            (0, 1058, 0.015),
            (1059, 2116, 0.02),
            (2117, 3174, 0.025),
            (3175, 4232, 0.03),
            (4233, 5290, 0.035),
            (5291, 6348, 0.04),
            (6349, 7406, 0.045),
            (7407, 8464, 0.05),
            (8465, 9522, 0.055),
            (9523, float('inf'), 0.059)
        ]
    },
    "MT": {
        "standard_deduction": {
            "single": 4850,
            "married": 9700,
            "head_of_household": 4850
        },
        "single": [
            (0, 3200, 0.01),
            (3201, 6400, 0.02),
            (6401, 9600, 0.03),
            (9601, 12800, 0.04),
            (12801, 16000, 0.05),
            (16001, 19200, 0.06),
            (19201, float('inf'), 0.069)
        ],
        "married": [
            (0, 3200, 0.01),
            (3201, 6400, 0.02),
            (6401, 9600, 0.03),
            (9601, 12800, 0.04),
            (12801, 16000, 0.05),
            (16001, 19200, 0.06),
            (19201, float('inf'), 0.069)
        ],
        "head_of_household": [
            (0, 3200, 0.01),
            (3201, 6400, 0.02),
            (6401, 9600, 0.03),
            (9601, 12800, 0.04),
            (12801, 16000, 0.05),
            (16001, 19200, 0.06),
            (19201, float('inf'), 0.069)
        ]
    },
    "NE": {
        "standard_deduction": {
            "single": 7300,
            "married": 14600,
            "head_of_household": 10950
        },
        "single": [
            (0, 3360, 0.0246),
            (3361, 20190, 0.0351),
            (20191, 32610, 0.0501),
            (32611, float('inf'), 0.0684)
        ],
        "married": [
            (0, 6720, 0.0246),
            (6721, 40380, 0.0351),
            (40381, 65220, 0.0501),
            (65221, float('inf'), 0.0684)
        ],
        "head_of_household": [
            (0, 5040, 0.0246),
            (5041, 30285, 0.0351),
            (30286, 48915, 0.0501),
            (48916, float('inf'), 0.0684)
        ]
    },
    "NV": {
        "standard_deduction": {
            "single": 0,
            "married": 0,
            "head_of_household": 0
        },
        "single": [(0, float('inf'), 0.0)],
        "married": [(0, float('inf'), 0.0)],
        "head_of_household": [(0, float('inf'), 0.0)]
    },
    "NH": {
        "standard_deduction": {
            "single": 0,
            "married": 0,
            "head_of_household": 0
        },
        "single": [(0, float('inf'), 0.05)],
        "married": [(0, float('inf'), 0.05)],
        "head_of_household": [(0, float('inf'), 0.05)]
    },
    "NJ": {
        "standard_deduction": {
            "single": 1000,
            "married": 2000,
            "head_of_household": 1500
        },
        "single": [
            (0, 20000, 0.014),
            (20001, 35000, 0.0175),
            (35001, 40000, 0.035),
            (40001, 75000, 0.05525),
            (75001, 500000, 0.0637),
            (500001, 5000000, 0.0897),
            (5000001, float('inf'), 0.1075)
        ],
        "married": [
            (0, 20000, 0.014),
            (20001, 50000, 0.0175),
            (50001, 70000, 0.0245),
            (70001, 80000, 0.035),
            (80001, 150000, 0.05525),
            (150001, 500000, 0.0637),
            (500001, 5000000, 0.0897),
            (5000001, float('inf'), 0.1075)
        ],
        "head_of_household": [
            (0, 20000, 0.014),
            (20001, 35000, 0.0175),
            (35001, 40000, 0.035),
            (40001, 75000, 0.05525),
            (75001, 500000, 0.0637),
            (500001, 5000000, 0.0897),
            (5000001, float('inf'), 0.1075)
        ]
    },
    "NM": {
        "standard_deduction": {
            "single": 6350,
            "married": 12700,
            "head_of_household": 9350
        },
        "single": [
            (0, 5500, 0.017),
            (5501, 11000, 0.032),
            (11001, 16000, 0.047),
            (16001, 21000, 0.049),
            (21001, float('inf'), 0.059)
        ],
        "married": [
            (0, 8000, 0.017),
            (8001, 16000, 0.032),
            (16001, 24000, 0.047),
            (24001, 31500, 0.049),
            (31501, float('inf'), 0.059)
        ],
        "head_of_household": [
            (0, 8000, 0.017),
            (8001, 16000, 0.032),
            (16001, 24000, 0.047),
            (24001, 31500, 0.049),
            (31501, float('inf'), 0.059)
        ]
    },
    "NY": {
        "standard_deduction": {
            "single": 8000,
            "married": 16050,
            "head_of_household": 11200
        },
        "single": [
            (0, 8500, 0.04),
            (8501, 11700, 0.045),
            (11701, 13900, 0.0525),
            (13901, 21400, 0.059),
            (21401, 80650, 0.0633),
            (80651, 215400, 0.0657),
            (215401, 1077550, 0.0685),
            (1077551, float('inf'), 0.0882)
        ],
        "married": [
            (0, 17150, 0.04),
            (17151, 23600, 0.045),
            (23601, 27900, 0.0525),
            (27901, 43000, 0.059),
            (43001, 161550, 0.0621),
            (161551, 323200, 0.0685),
            (323201, 2155350, 0.0965),
            (2155351, float('inf'), 0.103)
        ],
        "head_of_household": [
            (0, 12800, 0.04),
            (12801, 17650, 0.045),
            (17651, 20600, 0.0525),
            (20601, 32200, 0.059),
            (32201, 107650, 0.0621),
            (107651, 269300, 0.0685),
            (269301, 1616450, 0.0965),
            (1616451, float('inf'), 0.103)
        ]
    },
    "NC": {
        "standard_deduction": {
            "single": 10500,
            "married": 21000,
            "head_of_household": 15750
        },
        "single": [
            (0, float('inf'), 0.0525)
        ],
        "married": [
            (0, float('inf'), 0.0525)
        ],
        "head_of_household": [
            (0, float('inf'), 0.0525)
        ]
    },
    "ND": {
        "standard_deduction": {
            "single": 12950,
            "married": 25900,
            "head_of_household": 19400
        },
        "single": [
            (0, 40975, 0.011),
            (40976, 98925, 0.02),
            (98926, 201200, 0.0227),
            (201201, 445000, 0.0264),
            (445001, float('inf'), 0.029)
        ],
        "married": [
            (0, 68350, 0.011),
            (68351, 162150, 0.02),
            (162151, 242950, 0.0227),
            (242951, 445000, 0.0264),
            (445001, float('inf'), 0.029)
        ],
        "head_of_household": [
            (0, 55100, 0.011),
            (55101, 129950, 0.02),
            (129951, 209500, 0.0227),
            (209501, 445000, 0.0264),
            (445001, float('inf'), 0.029)
        ]
    },
     "OH": {
        "standard_deduction": {
            "single": 12950,
            "married": 25900,
            "head_of_household": 19400
        },
        "single": [
            (0, 25000, 0.02865),
            (25001, 44250, 0.03326),
            (44251, 88450, 0.03802),
            (88451, 110650, 0.04213),
            (110651, float('inf'), 0.04897)
        ],
        "married": [
            (0, 25000, 0.02865),
            (25001, 44250, 0.03326),
            (44251, 88450, 0.03802),
            (88451, 110650, 0.04213),
            (110651, float('inf'), 0.04897)
        ],
        "head_of_household": [
            (0, 25000, 0.02865),
            (25001, 44250, 0.03326),
            (44251, 88450, 0.03802),
            (88451, 110650, 0.04213),
            (110651, float('inf'), 0.04897)
        ]
    },
    "OK": {
        "standard_deduction": {
            "single": 6350,
            "married": 12700,
            "head_of_household": 9350
        },
        "single": [
            (0, 1000, 0.005),
            (1001, 2500, 0.01),
            (2501, 3750, 0.02),
            (3751, 4900, 0.03),
            (4901, float('inf'), 0.05)
        ],
        "married": [
            (0, 2000, 0.005),
            (2001, 5000, 0.01),
            (5001, 7500, 0.02),
            (7501, 9800, 0.03),
            (9801, float('inf'), 0.05)
        ],
        "head_of_household": [
            (0, 2000, 0.005),
            (2001, 5000, 0.01),
            (5001, 7500, 0.02),
            (7501, 9800, 0.03),
            (9801, float('inf'), 0.05)
        ]
    },
    "OR": {
        "standard_deduction": {
            "single": 2360,
            "married": 4720,
            "head_of_household": 4720
        },
        "single": [
            (0, 3650, 0.0475),
            (3651, 9200, 0.0675),
            (9201, 125000, 0.0875),
            (125001, 250000, 0.099),
            (250001, float('inf'), 0.099)
        ],
        "married": [
            (0, 7300, 0.0475),
            (7301, 18400, 0.0675),
            (18401, 250000, 0.0875),
            (250001, 500000, 0.099),
            (500001, float('inf'), 0.099)
        ],
        "head_of_household": [
            (0, 7300, 0.0475),
            (7301, 18400, 0.0675),
            (18401, 250000, 0.0875),
            (250001, 500000, 0.099),
            (500001, float('inf'), 0.099)
        ]
    },
    "PA": {
        "standard_deduction": {
            "single": 0,
            "married": 0,
            "head_of_household": 0
        },
        "single": [
            (0, float('inf'), 0.0307)
        ],
        "married": [
            (0, float('inf'), 0.0307)
        ],
        "head_of_household": [
            (0, float('inf'), 0.0307)
        ]
    },
    "RI": {
        "standard_deduction": {
            "single": 8650,
            "married": 17300,
            "head_of_household": 12975
        },
        "single": [
            (0, 66600, 0.0375),
            (66601, 151200, 0.0475),
            (151201, float('inf'), 0.0599)
        ],
        "married": [
            (0, 66600, 0.0375),
            (66601, 151200, 0.0475),
            (151201, float('inf'), 0.0599)
        ],
        "head_of_household": [
            (0, 66600, 0.0375),
            (66601, 151200, 0.0475),
            (151201, float('inf'), 0.0599)
        ]
    },
    "SC": {
        "standard_deduction": {
            "single": 12950,
            "married": 25900,
            "head_of_household": 19400
        },
        "single": [
            (0, 3220, 0.0),
            (3221, 6440, 0.03),
            (6441, 9660, 0.04),
            (9661, 12880, 0.05),
            (12881, 16100, 0.06),
            (16101, float('inf'), 0.07)
        ],
        "married": [
            (0, 6440, 0.0),
            (6441, 12880, 0.03),
            (12881, 19320, 0.04),
            (19321, 25760, 0.05),
            (25761, 32200, 0.06),
            (32201, float('inf'), 0.07)
        ],
        "head_of_household": [
            (0, 6440, 0.0),
            (6441, 12880, 0.03),
            (12881, 19320, 0.04),
            (19321, 25760, 0.05),
            (25761, 32200, 0.06),
            (32201, float('inf'), 0.07)
        ]
    },
    "SD": {
        "standard_deduction": {
            "single": 0,
            "married": 0,
            "head_of_household": 0
        },
        "single": [(0, float('inf'), 0.0)],
        "married": [(0, float('inf'), 0.0)],
        "head_of_household": [(0, float('inf'), 0.0)]
    },
    "TN": {
        "standard_deduction": {
            "single": 0,
            "married": 0,
            "head_of_household": 0
        },
        "single": [(0, float('inf'), 0.0)],
        "married": [(0, float('inf'), 0.0)],
        "head_of_household": [(0, float('inf'), 0.0)]
    },
    "TX": {
        "standard_deduction": {
            "single": 0,
            "married": 0,
            "head_of_household": 0
        },
        "single": [(0, float('inf'), 0.0)],
        "married": [(0, float('inf'), 0.0)],
        "head_of_household": [(0, float('inf'), 0.0)]
    },
    "UT": {
        "standard_deduction": {
            "single": 12950,
            "married": 25900,
            "head_of_household": 19400
        },
        "single": [
            (0, float('inf'), 0.0495)
        ],
        "married": [
            (0, float('inf'), 0.0495)
        ],
        "head_of_household": [
            (0, float('inf'), 0.0495)
        ]
    },
    "VT": {
        "standard_deduction": {
            "single": 6350,
            "married": 12700,
            "head_of_household": 9350
        },
        "single": [
            (0, 40750, 0.0335),
            (40751, 98200, 0.066),
            (98201, 204000, 0.0765),
            (204001, float('inf'), 0.0875)
        ],
        "married": [
            (0, 68200, 0.0335),
            (68201, 164350, 0.066),
            (164351, 248350, 0.0765),
            (248351, float('inf'), 0.0875)
        ],
        "head_of_household": [
            (0, 54400, 0.0335),
            (54401, 136600, 0.066),
            (136601, 222700, 0.0765),
            (222701, float('inf'), 0.0875)
        ]
    },
    "VA": {
        "standard_deduction": {
            "single": 4500,
            "married": 9000,
            "head_of_household": 9000
        },
        "single": [
            (0, 3000, 0.02),
            (3001, 5000, 0.03),
            (5001, 17000, 0.05),
            (17001, float('inf'), 0.0575)
        ],
        "married": [
            (0, 3000, 0.02),
            (3001, 5000, 0.03),
            (5001, 17000, 0.05),
            (17001, float('inf'), 0.0575)
        ],
        "head_of_household": [
            (0, 3000, 0.02),
            (3001, 5000, 0.03),
            (5001, 17000, 0.05),
            (17001, float('inf'), 0.0575)
        ]
    },
    "WA": {
        "standard_deduction": {
            "single": 0,
            "married": 0,
            "head_of_household": 0
        },
        "single": [(0, float('inf'), 0.0)],
        "married": [(0, float('inf'), 0.0)],
        "head_of_household": [(0, float('inf'), 0.0)]
    },
    "WV": {
        "standard_deduction": {
            "single": 2000,
            "married": 4000,
            "head_of_household": 2000
        },
        "single": [
            (0, 10000, 0.03),
            (10001, 25000, 0.04),
            (25001, 40000, 0.045),
            (40001, 60000, 0.06),
            (60001, float('inf'), 0.065)
        ],
        "married": [
            (0, 10000, 0.03),
            (10001, 25000, 0.04),
            (25001, 40000, 0.045),
            (40001, 60000, 0.06),
            (60001, float('inf'), 0.065)
        ],
        "head_of_household": [
            (0, 10000, 0.03),
            (10001, 25000, 0.04),
            (25001, 40000, 0.045),
            (40001, 60000, 0.06),
            (60001, float('inf'), 0.065)
        ]
    },
    "WI": {
        "standard_deduction": {
            "single": 11000,
            "married": 22000,
            "head_of_household": 16500
        },
        "single": [
            (0, 12760, 0.0354),
            (12761, 25520, 0.0465),
            (25521, 280950, 0.0627),
            (280951, float('inf'), 0.0765)
        ],
        "married": [
            (0, 25520, 0.0354),
            (25521, 51040, 0.0465),
            (51041, 374600, 0.0627),
            (374601, float('inf'), 0.0765)
        ],
        "head_of_household": [
            (0, 19140, 0.0354),
            (19141, 38280, 0.0465),
            (38281, 327800, 0.0627),
            (327801, float('inf'), 0.0765)
        ]
    },
    "WY": {
        "standard_deduction": {
            "single": 0,
            "married": 0,
            "head_of_household": 0
        },
        "single": [(0, float('inf'), 0.0)],
        "married": [(0, float('inf'), 0.0)],
        "head_of_household": [(0, float('inf'), 0.0)]
    }
}

# Credit reduction by CR state (2024)
CREDIT_REDUCTION = {
    "CA": 0.009,
    "CT": 0.009,
    "NY": 0.009
}

# SUTA rates for all 50 states
SUTA_RATES = {
    "AL": 0.027,
    "AK": 0.022,
    "AZ": 0.020,
    "AR": 0.028,
    "CA": 0.033,
    "CO": 0.018,
    "CT": 0.025,
    "DE": 0.0135,
    "FL": 0.029,
    "GA": 0.027,
    "HI": 0.031,
    "ID": 0.019,
    "IL": 0.0375,
    "IN": 0.0275,
    "IA": 0.009,
    "KS": 0.027,
    "KY": 0.025,
    "LA": 0.024,
    "ME": 0.026,
    "MD": 0.024,
    "MA": 0.015,
    "MI": 0.029,
    "MN": 0.0135,
    "MS": 0.027,
    "MO": 0.025,
    "MT": 0.022,
    "NE": 0.0125,
    "NV": 0.033,
    "NH": 0.015,
    "NJ": 0.029,
    "NM": 0.012,
    "NY": 0.037,
    "NC": 0.019,
    "ND": 0.012,
    "OH": 0.0275,
    "OK": 0.010,
    "OR": 0.024,
    "PA": 0.039,
    "RI": 0.022,
    "SC": 0.016,
    "SD": 0.018,
    "TN": 0.015,
    "TX": 0.026,
    "UT": 0.010,
    "VT": 0.0135,
    "VA": 0.028,
    "WA": 0.015,
    "WV": 0.028,
    "WI": 0.027,
    "WY": 0.014
}


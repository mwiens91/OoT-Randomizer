# Progressive: True  -> Advancement
#              False -> Priority
#              None  -> Normal
#    Item:                            (type, Progessive, GetItemID, special),
item_table = {
    'Bombs (5)':                        ('Item',     None,  0x01, None),
    'Deku Nuts (5)':                    ('Item',     None,  0x02, None),
    'Bombchus (10)':                    ('Item',     True,  0x03, None),
    'Boomerang':                        ('Item',     True,  0x06, None),
    'Deku Stick (1)':                   ('Item',     None,  0x07, None),
    'Lens of Truth':                    ('Item',     True,  0x0A, None),
    'Hammer':                           ('Item',     True,  0x0D, None),
    'Cojiro':                           ('Item',     True,  0x0E, None),
    'Bottle':                           ('Item',     True,  0x0F, {'bottle': float('Inf')}),
    'Bottle with Milk':                 ('Item',     True,  0x14, {'bottle': float('Inf')}),
    'Bottle with Letter':               ('Item',     True,  0x15, None),
    'Deliver Letter':                   ('Item',     True,  None, {'bottle': float('Inf')}),
    'Sell Big Poe':                     ('Item',     True,  None, {'bottle': float('Inf')}),
    'Magic Bean':                       ('Item',     True,  0x16, None),
    'Skull Mask':                       ('Item',     None,  0x17, None),
    'Spooky Mask':                      ('Item',     None,  0x18, None),
    'Keaton Mask':                      ('Item',     None,  0x1A, None),
    'Bunny Hood':                       ('Item',     None,  0x1B, None),
    'Mask of Truth':                    ('Item',     None,  0x1C, None),
    'Pocket Egg':                       ('Item',     True,  0x1D, None),
    'Pocket Cucco':                     ('Item',     True,  0x1E, None),
    'Odd Mushroom':                     ('Item',     True,  0x1F, None),
    'Odd Potion':                       ('Item',     True,  0x20, None),
    'Poachers Saw':                     ('Item',     True,  0x21, None),
    'Broken Sword':                     ('Item',     True,  0x22, None),
    'Prescription':                     ('Item',     True,  0x23, None),
    'Eyeball Frog':                     ('Item',     True,  0x24, None),
    'Eyedrops':                         ('Item',     True,  0x25, None),
    'Claim Check':                      ('Item',     True,  0x26, None),
    'Kokiri Sword':                     ('Item',     True,  0x27, None),
    'Deku Shield':                      ('Item',     None,  0x29, None),
    'Hylian Shield':                    ('Item',     None,  0x2A, None),
    'Mirror Shield':                    ('Item',     True,  0x2B, None),
    'Goron Tunic':                      ('Item',     True,  0x2C, None),
    'Zora Tunic':                       ('Item',     True,  0x2D, None),
    'Iron Boots':                       ('Item',     True,  0x2E, None),
    'Hover Boots':                      ('Item',     True,  0x2F, None),
    'Stone of Agony':                   ('Item',     True,  0x39, None),
    'Gerudo Membership Card':           ('Item',     True,  0x3A, None),
    'Heart Container':                  ('Item',     None,  0x3D, None),
    'Piece of Heart':                   ('Item',     None,  0x3E, None),
    'Boss Key':                         ('BossKey',  True,  0x3F, None),
    'Compass':                          ('Compass',  None,  0x40, None),
    'Map':                              ('Map',      None,  0x41, None),
    'Small Key':                        ('SmallKey', True,  0x42, {'progressive': float('Inf')}),
    'Weird Egg':                        ('Item',     True,  0x47, None),
    'Recovery Heart':                   ('Item',     None,  0x48, None),
    'Arrows (5)':                       ('Item',     None,  0x49, None),
    'Arrows (10)':                      ('Item',     None,  0x4A, None),
    'Arrows (30)':                      ('Item',     None,  0x4B, None),
    'Rupee (1)':                        ('Item',     None,  0x4C, None),
    'Rupees (5)':                       ('Item',     None,  0x4D, None),
    'Rupees (20)':                      ('Item',     None,  0x4E, None),
    'Heart Container (Boss)':           ('Item',     None,  0x4F, None),
    'Milk':                             ('Item',     None,  0x50, None),
    'Goron Mask':                       ('Item',     None,  0x51, None),
    'Zora Mask':                        ('Item',     None,  0x52, None),
    'Gerudo Mask':                      ('Item',     None,  0x53, None),
    'Rupees (50)':                      ('Item',     None,  0x55, None),
    'Rupees (200)':                     ('Item',     None,  0x56, None),
    'Biggoron Sword':                   ('Item',     True,  0x57, None),
    'Fire Arrows':                      ('Item',     True,  0x58, None),
    'Ice Arrows':                       ('Item',     True,  0x59, None),
    'Light Arrows':                     ('Item',     True,  0x5A, None),
    'Gold Skulltula Token':             ('Token',    True,  0x5B, {'progressive': float('Inf')}),
    'Dins Fire':                        ('Item',     True,  0x5C, None),
    'Nayrus Love':                      ('Item',     True,  0x5E, None),
    'Farores Wind':                     ('Item',     True,  0x5D, None),
    'Deku Nuts (10)':                   ('Item',     None,  0x64, None),
    'Bombs (10)':                       ('Item',     None,  0x66, None),
    'Bombs (20)':                       ('Item',     None,  0x67, None),
    'Deku Seeds (30)':                  ('Item',     None,  0x69, None),
    'Bombchus (5)':                     ('Item',     True,  0x6A, None),
    'Bombchus (20)':                    ('Item',     True,  0x6B, None),
    'Rupee (Treasure Chest Game)':      ('Item',     None,  0x72, None),
    'Piece of Heart (Treasure Chest Game)': ('Item', None,  0x76, None),
    'Ice Trap':                         ('Item',     None,  0x7C, None),
    'Progressive Hookshot':             ('Item',     True,  0x80, {'progressive': 2}),
    'Progressive Strength Upgrade':     ('Item',     True,  0x81, {'progressive': 3}),
    'Bomb Bag':                         ('Item',     True,  0x82, None),
    'Bow':                              ('Item',     True,  0x83, None),
    'Slingshot':                        ('Item',     True,  0x84, None),
    'Progressive Wallet':               ('Item',     True,  0x85, {'progressive': 2}),
    'Progressive Scale':                ('Item',     True,  0x86, {'progressive': 2}),
    'Deku Nut Capacity':                ('Item',     None,  0x87, None),
    'Deku Stick Capacity':              ('Item',     None,  0x88, None),
    'Bombchus':                         ('Item',     True,  0x89, None),
    'Magic Meter':                      ('Item',     True,  0x8A, None),
    'Ocarina':                          ('Item',     True,  0x8B, None),
    'Bottle with Red Potion':           ('Item',     True,  0x8C, {'bottle': True, 'shop_object': 0x0F}),
    'Bottle with Green Potion':         ('Item',     True,  0x8D, {'bottle': True, 'shop_object': 0x0F}),
    'Bottle with Blue Potion':          ('Item',     True,  0x8E, {'bottle': True, 'shop_object': 0x0F}),
    'Bottle with Fairy':                ('Item',     True,  0x8F, {'bottle': True, 'shop_object': 0x0F}),
    'Bottle with Fish':                 ('Item',     True,  0x90, {'bottle': True, 'shop_object': 0x0F}),
    'Bottle with Blue Fire':            ('Item',     True,  0x91, {'bottle': True, 'shop_object': 0x0F}),
    'Bottle with Bugs':                 ('Item',     True,  0x92, {'bottle': True, 'shop_object': 0x0F}),
    'Bottle with Big Poe':              ('Item',     True,  0x93, {'shop_object': 0x0F}),
    'Bottle with Poe':                  ('Item',     True,  0x94, {'bottle': True, 'shop_object': 0x0F}),
    'Boss Key (Forest Temple)':         ('BossKey',  True,  0x95, None),
    'Boss Key (Fire Temple)':           ('BossKey',  True,  0x96, None),
    'Boss Key (Water Temple)':          ('BossKey',  True,  0x97, None),
    'Boss Key (Spirit Temple)':         ('BossKey',  True,  0x98, None),
    'Boss Key (Shadow Temple)':         ('BossKey',  True,  0x99, None),
    'Boss Key (Ganons Castle)':         ('BossKey',  True,  0x9A, None),
    'Compass (Deku Tree)':              ('Compass',  None,  0x9B, None),
    'Compass (Dodongos Cavern)':        ('Compass',  None,  0x9C, None),
    'Compass (Jabu Jabus Belly)':       ('Compass',  None,  0x9D, None),
    'Compass (Forest Temple)':          ('Compass',  None,  0x9E, None),
    'Compass (Fire Temple)':            ('Compass',  None,  0x9F, None),
    'Compass (Water Temple)':           ('Compass',  None,  0xA0, None),
    'Compass (Spirit Temple)':          ('Compass',  None,  0xA1, None),
    'Compass (Shadow Temple)':          ('Compass',  None,  0xA2, None),
    'Compass (Bottom of the Well)':     ('Compass',  None,  0xA3, None),
    'Compass (Ice Cavern)':             ('Compass',  None,  0xA4, None),
    'Map (Deku Tree)':                  ('Map',      None,  0xA5, None),
    'Map (Dodongos Cavern)':            ('Map',      None,  0xA6, None),
    'Map (Jabu Jabus Belly)':           ('Map',      None,  0xA7, None),
    'Map (Forest Temple)':              ('Map',      None,  0xA8, None),
    'Map (Fire Temple)':                ('Map',      None,  0xA9, None),
    'Map (Water Temple)':               ('Map',      None,  0xAA, None),
    'Map (Spirit Temple)':              ('Map',      None,  0xAB, None),
    'Map (Shadow Temple)':              ('Map',      None,  0xAC, None),
    'Map (Bottom of the Well)':         ('Map',      None,  0xAD, None),
    'Map (Ice Cavern)':                 ('Map',      None,  0xAE, None),
    'Small Key (Forest Temple)':        ('SmallKey', True,  0xAF, {'progressive': float('Inf')}),
    'Small Key (Fire Temple)':          ('SmallKey', True,  0xB0, {'progressive': float('Inf')}),
    'Small Key (Water Temple)':         ('SmallKey', True,  0xB1, {'progressive': float('Inf')}),
    'Small Key (Spirit Temple)':        ('SmallKey', True,  0xB2, {'progressive': float('Inf')}),
    'Small Key (Shadow Temple)':        ('SmallKey', True,  0xB3, {'progressive': float('Inf')}),
    'Small Key (Bottom of the Well)':   ('SmallKey', True,  0xB4, {'progressive': float('Inf')}),
    'Small Key (Gerudo Training Grounds)':('SmallKey',True, 0xB5, {'progressive': float('Inf')}),
    'Small Key (Gerudo Fortress)':('FortressSmallKey',True, 0xB6, {'progressive': float('Inf')}),
    'Small Key (Ganons Castle)':        ('SmallKey', True,  0xB7, {'progressive': float('Inf')}),
    'Double Defense':                   ('Item',     True,  0xB8, None),
    'Zeldas Letter':                    ('Item',     True,  None, None),
    'Time Travel':                      ('Event',    True,  None, None),
    'Epona':                            ('Event',    True,  None, None),
    'Carpenter Rescue':                 ('Event',    True,  None, None),
    'Gerudo Fortress Gate Open':        ('Event',    True,  None, None),
    'Goron City Woods Warp Open':       ('Event',    True,  None, None),
    'Drain Well':                       ('Event',    True,  None, None),
    'Links Cow':                        ('Event',    True,  None, None),

    'Kokiri Forest Open':               ('Event',    True,  None, None),
    'Forest Temple Jo and Beth':        ('Event',    True,  None, None),
    'Forest Temple Amy and Meg':        ('Event',    True,  None, None),
    'Child Water Temple':               ('Event',    True,  None, None),
    'Lake Refill':                      ('Event',    True,  None, None),
    'Forest Trial Clear':               ('Event',    True,  None, None),
    'Fire Trial Clear':                 ('Event',    True,  None, None),
    'Water Trial Clear':                ('Event',    True,  None, None),
    'Shadow Trial Clear':               ('Event',    True,  None, None),
    'Spirit Trial Clear':               ('Event',    True,  None, None),
    'Light Trial Clear':                ('Event',    True,  None, None),
    'Triforce':                         ('Event',    True,  None, None),

    'Deku Stick Drop':                  ('Drop',     True,  None, None),
    'Deku Nut Drop':                    ('Drop',     True,  None, None),
    'Blue Fire':                        ('Drop',     True,  None, None),
    'Fairy':                            ('Drop',     True,  None, None),
    'Fish':                             ('Drop',     True,  None, None),
    'Bugs':                             ('Drop',     True,  None, None),
    'Big Poe':                          ('Drop',     True,  None, None),
    'Bombchu Drop':                     ('Drop',     True,  None, None),

    'Scarecrow Song':                   ('Event',    True,  None, None),
    'Minuet of Forest':                 ('Song',     True,  0xBB,
                                            {
                                                'text_id': 0x73,
                                                'song_id': 0x02,
                                                'item_id': 0x5A,
                                            }),
    'Bolero of Fire':                   ('Song',     True,  0xBC,
                                            {
                                                'text_id': 0x74,
                                                'song_id': 0x03,
                                                'item_id': 0x5B,
                                            }),
    'Serenade of Water':                ('Song',     True,  0xBD,
                                            {
                                                'text_id': 0x75,
                                                'song_id': 0x04,
                                                'item_id': 0x5C,
                                            }),
    'Requiem of Spirit':                ('Song',     True,  0xBE,
                                            {
                                                'text_id': 0x76,
                                                'song_id': 0x05,
                                                'item_id': 0x5D,
                                            }),
    'Nocturne of Shadow':               ('Song',     True,  0xBF,
                                            {
                                                'text_id': 0x77,
                                                'song_id': 0x06,
                                                'item_id': 0x5E,
                                            }),
    'Prelude of Light':                 ('Song',     True,  0xC0,
                                            {
                                                'text_id': 0x78,
                                                'song_id': 0x07,
                                                'item_id': 0x5F,
                                            }),
    'Zeldas Lullaby':                   ('Song',     True,  0xC1,
                                            {
                                                'text_id': 0xD4,
                                                'song_id': 0x0A,
                                                'item_id': 0x60,
                                            }),
    'Eponas Song':                      ('Song',     True,  0xC2,
                                            {
                                                'text_id': 0xD2,
                                                'song_id': 0x09,
                                                'item_id': 0x61,
                                            }),
    'Sarias Song':                      ('Song',     True,  0xC3,
                                            {
                                                'text_id': 0xD1,
                                                'song_id': 0x08,
                                                'item_id': 0x62,
                                            }),
    'Suns Song':                        ('Song',     True,  0xC4,
                                            {
                                                'text_id': 0xD3,
                                                'song_id': 0x0B,
                                                'item_id': 0x63,
                                            }),
    'Song of Time':                     ('Song',     True,  0xC5,
                                            {
                                                'text_id': 0xD5,
                                                'song_id': 0x0C,
                                                'item_id': 0x64,
                                            }),
    'Song of Storms':                   ('Song',     True,  0xC6,
                                            {
                                                'text_id': 0xD6,
                                                'song_id': 0x0D,
                                                'item_id': 0x65,
                                            }),

    'Buy Deku Nut (5)':                 ('Shop',     True,  0x00, {'object': 0x00BB, 'price': 15}),
    'Buy Arrows (30)':                  ('Shop',     False, 0x01, {'object': 0x00D8, 'price': 60}),
    'Buy Arrows (50)':                  ('Shop',     False, 0x02, {'object': 0x00D8, 'price': 90}),
    'Buy Bombs (5) [25]':               ('Shop',     False, 0x03, {'object': 0x00CE, 'price': 25}),
    'Buy Deku Nut (10)':                ('Shop',     True,  0x04, {'object': 0x00BB, 'price': 30}),
    'Buy Deku Stick (1)':               ('Shop',     True,  0x05, {'object': 0x00C7, 'price': 10}),
    'Buy Bombs (10)':                   ('Shop',     False, 0x06, {'object': 0x00CE, 'price': 50}),
    'Buy Fish':                         ('Shop',     True,  0x07, {'object': 0x00F4, 'price': 200}),
    'Buy Red Potion [30]':              ('Shop',     False, 0x08, {'object': 0x00EB, 'price': 30}),
    'Buy Green Potion':                 ('Shop',     False, 0x09, {'object': 0x00EB, 'price': 30}),
    'Buy Blue Potion':                  ('Shop',     False, 0x0A, {'object': 0x00EB, 'price': 100}),
    'Buy Hylian Shield':                ('Shop',     True,  0x0C, {'object': 0x00DC, 'price': 80}),
    'Buy Deku Shield':                  ('Shop',     True,  0x0D, {'object': 0x00CB, 'price': 40}),
    'Buy Goron Tunic':                  ('Shop',     True,  0x0E, {'object': 0x00F2, 'price': 200}),
    'Buy Zora Tunic':                   ('Shop',     True,  0x0F, {'object': 0x00F2, 'price': 300}),
    'Buy Heart':                        ('Shop',     False, 0x10, {'object': 0x00B7, 'price': 10}),
    'Buy Bombchu (10)':                 ('Shop',     True,  0x15, {'object': 0x00D9, 'price': 99}),
    'Buy Bombchu (20)':                 ('Shop',     True,  0x16, {'object': 0x00D9, 'price': 180}),
    'Buy Bombchu (5)':                  ('Shop',     True,  0x18, {'object': 0x00D9, 'price': 60}),
    'Buy Deku Seeds (30)':              ('Shop',     False, 0x1D, {'object': 0x0119, 'price': 30}),
    'Sold Out':                         ('Shop',     False, 0x26, {'object': 0x0148}),
    'Buy Blue Fire':                    ('Shop',     True,  0x27, {'object': 0x0173, 'price': 300}),
    'Buy Bottle Bug':                   ('Shop',     True,  0x28, {'object': 0x0174, 'price': 50}),
    'Buy Poe':                          ('Shop',     False, 0x2A, {'object': 0x0176, 'price': 30}),
    'Buy Fairy\'s Spirit':              ('Shop',     True,  0x2B, {'object': 0x0177, 'price': 50}),
    'Buy Arrows (10)':                  ('Shop',     False, 0x2C, {'object': 0x00D8, 'price': 20}),
    'Buy Bombs (20)':                   ('Shop',     False, 0x2D, {'object': 0x00CE, 'price': 80}),
    'Buy Bombs (30)':                   ('Shop',     False, 0x2E, {'object': 0x00CE, 'price': 120}),
    'Buy Bombs (5) [35]':               ('Shop',     False, 0x2F, {'object': 0x00CE, 'price': 35}),
    'Buy Red Potion [40]':              ('Shop',     False, 0x30, {'object': 0x00EB, 'price': 40}),
    'Buy Red Potion [50]':              ('Shop',     False, 0x31, {'object': 0x00EB, 'price': 50}),

    'Kokiri Emerald':                   ('DungeonReward',    True,  None,
                                            {
                                                'addr2_data': 0x80,
                                                'bit_mask':   0x00040000,
                                                'item_id':    0x6C,
                                            }),
    'Goron Ruby':                       ('DungeonReward',    True,  None,
                                            {
                                                'addr2_data': 0x81,
                                                'bit_mask':   0x00080000,
                                                'item_id':    0x6D,
                                            }),
    'Zora Sapphire':                    ('DungeonReward',    True,  None,
                                            {
                                                'addr2_data': 0x82,
                                                'bit_mask':   0x00100000,
                                                'item_id':    0x6E,
                                            }),
    'Forest Medallion':                 ('DungeonReward',    True,  None,
                                            {
                                                'addr2_data': 0x3E,
                                                'bit_mask':   0x00000001,
                                                'item_id':    0x66,
                                            }),
    'Fire Medallion':                   ('DungeonReward',    True,  None,
                                            {
                                                'addr2_data': 0x3C,
                                                'bit_mask':   0x00000002,
                                                'item_id':    0x67,
                                            }),
    'Water Medallion':                  ('DungeonReward',    True,  None,
                                            {
                                                'addr2_data': 0x3D,
                                                'bit_mask':   0x00000004,
                                                'item_id':    0x68,
                                            }),
    'Spirit Medallion':                 ('DungeonReward',    True,  None,
                                            {
                                                'addr2_data': 0x3F,
                                                'bit_mask':   0x00000008,
                                                'item_id':    0x69,
                                            }),
    'Shadow Medallion':                 ('DungeonReward',    True,  None,
                                            {
                                                'addr2_data': 0x41,
                                                'bit_mask':   0x00000010,
                                                'item_id':    0x6A,
                                            }),
    'Light Medallion':                  ('DungeonReward',    True,  None,
                                            {
                                                'addr2_data': 0x40,
                                                'bit_mask':   0x00000020,
                                                'item_id':    0x6B,
                                            }),
}

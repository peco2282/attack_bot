osdict = {
    0: 1.00,
    1: 1.09,
    2: 1.18,
    3: 1.27,
    4: 1.36,
    5: 1.45,
    6: 1.54,
    7: 1.63,
    8: 1.72,
    9: 1.81,
    10: 2.02659,
    11: 2.15072,
    12: 2.22172,
    13: 2.26701,
    14: 2.29829,
    15: 2.32114,
    16: 2.33856,
    17: 2.35227,
    18: 2.36334,
    19: 2.37246,
    20: 2.38011,
    21: 2.38611,
    22: 2.39221,
    23: 2.39707,
    24: 2.40135,
    25: 2.40513,
    26: 2.40849,
    27: 2.41151,
    28: 2.41424,
    29: 2.4167,
    30: 2.41895,
    31: 2.421,
    32: 2.42289,
    33: 2.42462,
    34: 2.42623,
    35: 2.42772,
    36: 2.4291,
    37: 2.43039,
    38: 2.43159,
    39: 2.43272,
    40: 2.43377,
    41: 2.443476,
    42: 2.4357,
    43: 2.43658,
    44: 2.43742,
    45: 2.43821,
    46: 2.43895,
    47: 2.43966,
    48: 2.44034,
    49: 2.44098,
    50: 2.44159,
    51: 2.44217,
    52: 2.44273,
    53: 2.44326,
    54: 2.44377,
    55: 2.44426,
    56: 2.44473,
    57: 2.44518,
    58: 2.44561,
    59: 2.44602,
    60: 2.44642,
    61: 2.4468,
    62: 2.44717,
    63: 2.44753,
    64: 2.44787,
    65: 2.4482,
    66: 2.44852,
    67: 2.44883,
    68: 2.44913,
    69: 2.44942,
    70: 2.4497,
    71: 2.44997,
    72: 2.45024,
    73: 2.45049,
    74: 2.45074
}

castimedict = {
    0: 1.00,
    1: 0.95,
    2: 0.90,
    3: 0.85,
    4: 0.80,
    5: 0.75,
    6: 0.70,
    7: 0.65,
    8: 0.60,
    9: 0.55,
    10: 0.50
}

dict_1 = {'1': 1.10, '2': 1.15, '3': 1.23, '4': 1.35, '4_5': 1.40, '5': 1.55
          }

dict_2 = {'1': 1.10,
          '2': 1.15, '1, 2': 1.10 * 1.15,
          '3': 1.23, '1, 3': 1.10 * 1.23, '2, 3': 1.15 * 1.23,
          '4': 1.35, '1, 4': 1.10 * 1.35, '2, 4': 1.15 * 1.35, '3, 4': 1.23 * 1.35,
          '4_5': 1.40, '1, 4_5': 1.10 * 1.40, '2, 4_5': 1.15 * 1.40, '3, 4_5': 1.23 * 1.40, '4, 4_5': 1.35 * 1.40,
          '5': 1.55, '1, 5': 1.10 * 1.55, '2, 5': 1.15 * 1.55, '3, 5': 1.23 * 1.55, '4, 5': 1.35 * 1.55}

dict_3 = {'1': 1.10,
          '2': 1.15, '1, 2': 1.10 * 1.15,
          '3': 1.23, '1, 3': 1.10 * 1.23, '2, 3': 1.15 * 1.23, '1, 2, 3': 1.10 * 1.15 * 1.23,
          '4': 1.35, '1, 4': 1.10 * 1.35, '2, 4': 1.15 * 1.35, '3, 4': 1.23 * 1.35,
          '1, 2, 4': 1.10 * 1.15 * 1.35, '1, 3, 4': 1.10 * 1.23 * 1.35, '2, 3, 4': 1.15 * 1.23 * 1.35,
          '4_5': 1.40, '1, 4_5': 1.10 * 1.40, '2, 4_5': 1.15 * 1.40, '1, 2, 4_5': 1.10 * 1.15 * 1.40,
          '3, 4_5': 1.23 * 1.40, '1, 3, 4_5': 1.10 * 1.23 * 1.40, '2, 3, 4_5': 1.15 * 1.23 * 1.40,
          '4, 4_5': 1.35 * 1.40, '1, 4, 4_5': 1.10 * 1.35 * 1.40, '2, 4, 4_5': 1.15 * 1.35 * 1.40, '3, 4, 4_5': 1.23 * 1.35 * 1.40,
          '5': 1.55, '1, 5': 1.10 * 1.55, '2, 5': 1.15 * 1.55, '1, 2, 5': 1.10 * 1.15 * 1.55, '3, 5': 1.23 * 1.55,
          '1, 3, 5': 1.10 * 1.23 * 1.55, '2, 3, 5': 1.15 * 1.23 * 1.55, '4, 5': 1.35 * 1.55,
          '1, 4, 5': 1.10 * 1.35 * 1.55, '2, 4, 5': 1.15 * 1.35 * 1.55, '3, 4, 5': 1.23 * 1.35 * 1.55}

dict_4 = {'1': 1.10,
          '2': 1.15, '1, 2': 1.10 * 1.15,
          '3': 1.23, '1, 3': 1.10 * 1.23, '2, 3': 1.15 * 1.23, '1, 2, 3': 1.10 * 1.15 * 1.23,
          '4': 1.35, '1, 4': 1.10 * 1.35, '2, 4': 1.15 * 1.35, '1, 2, 4': 1.10 * 1.15 * 1.35, '3, 4': 1.23 * 1.35,
          '1, 3, 4': 1.10 * 1.23 * 1.35, '2, 3, 4': 1.15 * 1.23 * 1.35, '1, 2, 3, 4': 1.10 * 1.15 * 1.23 * 1.35,
          '4_5': 1.40, '1, 4_5': 1.10 * 1.40, '2, 4_5': 1.15 * 1.40, '1, 2, 4_5': 1.10 * 1.15 * 1.40,
          '3, 4_5': 1.23 * 1.40, '1, 3, 4_5': 1.10 * 1.23 * 1.40, '2, 3, 4_5': 1.15 * 1.23 * 1.40, '1, 2, 3, 4_5': 1.10 * 1.15 * 1.23 * 1.40,
          '4, 4_5': 1.35 * 1.40, '1, 4, 4_5': 1.10 * 1.35 * 1.40, '2, 4, 4_5': 1.15 * 1.35 * 1.40, '1, 2, 4, 4_5': 1.10 * 1.15 * 1.35 * 1.40,
          '3, 4, 4_5': 1.23 * 1.35 * 1.40, '1, 3, 4, 4_5': 1.10 * 1.23 * 1.35 * 1.40, '2, 3, 4, 4_5': 1.15 * 1.23 * 1.35 * 1.40,
          '5': 1.55, '1, 5': 1.10 * 1.55, '2, 5': 1.15 * 1.55, '1, 2, 5': 1.10 * 1.15 * 1.55, '3, 5': 1.23 * 1.55,
          '1, 3, 5': 1.10 * 1.23 * 1.55, '2, 3, 5': 1.15 * 1.23 * 1.55, '1, 2, 3, 5': 1.10 * 1.15 * 1.23 * 1.55,
          '4, 5': 1.35 * 1.55, '1, 4, 5': 1.10 * 1.35 * 1.55, '2, 4, 5': 1.15 * 1.35 * 1.55, '1, 2, 4, 5': 1.10 * 1.15 * 1.35 * 1.55,
          '3, 4, 5': 1.23 * 1.35 * 1.55, '1, 3, 4, 5': 1.10 * 1.23 * 1.35 * 1.55, '2, 3, 4, 5': 1.15 * 1.23 * 1.35}

dict_5 = {'1': 1.10,
          '2': 1.15, '1, 2': 1.10 * 1.15,
          '3': 1.23, '1, 3': 1.10 * 1.23, '2, 3': 1.15 * 1.23, '1, 2, 3': 1.10 * 1.15 * 1.23,
          '4': 1.35, '1, 4': 1.10 * 1.35, '2, 4': 1.15 * 1.35, '1, 2, 4': 1.10 * 1.15 * 1.35, '3, 4': 1.23 * 1.35,
          '1, 3, 4': 1.10 * 1.23 * 1.35, '2, 3, 4': 1.15 * 1.23 * 1.35, '1, 2, 3, 4': 1.10 * 1.15 * 1.23 * 1.35,
          '4_5': 1.40, '1, 4_5': 1.10 * 1.40, '2, 4_5': 1.15 * 1.40, '1, 2, 4_5': 1.10 * 1.15 * 1.40,
          '3, 4_5': 1.23 * 1.40, '1, 3, 4_5': 1.10 * 1.23 * 1.40, '2, 3, 4_5': 1.15 * 1.23 * 1.40, '1, 2, 3, 4_5': 1.10 * 1.15 * 1.23 * 1.40,
          '4, 4_5': 1.35 * 1.40, '1, 4, 4_5': 1.10 * 1.35 * 1.40, '2, 4, 4_5': 1.15 * 1.35 * 1.40, '1, 2, 4, 4_5': 1.10 * 1.15 * 1.35 * 1.40,
          '3, 4, 4_5': 1.23 * 1.35 * 1.40, '1, 3, 4, 4_5': 1.10 * 1.23 * 1.35 * 1.40, '2, 3, 4, 4_5': 1.15 * 1.23 * 1.35 * 1.40, '1, 2, 3, 4, 4_5': 1.10 * 1.15 * 1.23 * 1.35 * 1.40,
          '5': 1.55, '1, 5': 1.10 * 1.55, '2, 5': 1.15 * 1.55, '1, 2, 5': 1.10 * 1.15 * 1.55, '3, 5': 1.23 * 1.55,
          '1, 3, 5': 1.10 * 1.23 * 1.55, '2, 3, 5': 1.15 * 1.23 * 1.55, '1, 2, 3, 5': 1.10 * 1.15 * 1.23 * 1.55,
          '4, 5': 1.35 * 1.55, '1, 4, 5': 1.10 * 1.35 * 1.55, '2, 4, 5': 1.15 * 1.35 * 1.55, '1, 2, 4, 5': 1.10 * 1.15 * 1.35 * 1.55,
          '3, 4, 5': 1.23 * 1.35 * 1.55, '1, 3, 4, 5': 1.10 * 1.23 * 1.35 * 1.55, '2, 3, 4, 5': 1.15 * 1.23 * 1.35, '1, 2, 3, 4, 5': 1.10 * 1.15 * 1.23 * 1.35 * 1.55}


dangeondict = {
    '知識の水路  --(-53, 114, 6)': 0,
    '愛の結晶  --(-3, 106, -9)': 0,
    'パントリー2  --(69, 112, 17)': 2,
    'エルドール地下室  --(12, 116, 2)': 2,
    '精錬所の地下  --(-9, 111, -50)': 2,
    'Forssa  --(799, 74, -218)': 3,
    'Forssa迷いの森  --(Forssa内)': 3,
    'エルドール鉱山  --(118, 112, -27)': 3,
    'スワロー洞窟  --(-404, 136, 121)': 4,
    '始まりの遺跡  --(91, 128, 191)': 4,
    'エルドール牢獄跡  --(-35, 118, -65)': 4,
    'エルドール洞窟  --(93, 125, 25)': 5,
    'Lovers2  --(-91, 112, -113)': 5,
    'グランスメル  --(113, 87, -204)': 5,
    'Celia\'s Big Tree  --(-514, 79, -181)': 6,
    'エルドール墓地  --(-98, 140, -6)': 7,
    'Library  --(Lovers内)': 8,
    '畑の風車小屋  --(54, 119, 64)': 8,
    'Ice Age  --(197, 120, -350)': 9,
    'エルドールの森  --(-10, 122, 47)': 9,
    'ソラリス大木  --(-300, 163, 82)': 10,
    'ルーレイ洞窟  --(-698, 79, 204)': 10,
    'FrederickMount  --(350, 75, -219)': 10,
    'エルドールのレストラン  --(40, 115, -7)': 10,
    'エルドール教会の地下  --(-55, 118, -37)': 10,
    '奈落アスレポルボー  --(トロールガ 内)': 11,
    'Deep Woods  --(516, 101, 376)': 12,
    'エルドールの不思議な森  --(57, 118, -122)': 13,
    'ロンゴノット  --(556, 86, 95)': 14,
    'マイセン洞窟  --(465, 94, 325)': 15,
    'シーク  --(-965, 65, -488)': 15,
    'Remains Corrupt  --(54, 87, -351)': 15,
    'Water Maze  --(-397, 77, 556)': 15,
    'ガルダ  --(154, 120, -1055)': 16,
    'スライム洞窟  --(527, 96, 329)': 18,
    'Oma海底ダンジョン  --(-1321, 72, 894)': 18,
    'sorrow tunnel  --(旧エルドール採掘場 内)': 19,
    'Ali\'s nest  --(210, 111, 431)': 19,
    '名もなき池  --(-150, 88, -238)': 20,
    'Flotrave  --(1336, 68, -1092)': 20,
    'Calanchies  --(-638, 135, -516)': 20,
    '底深き洞窟  --(276, 78, -962)': 20,
    'ポッポの森  --(-104, 101, 480)': 20,
    'マシュー  --(934, 30, -1286)': 21,
    'Curse mansion  --(-595, 20, -1054)': 22,
    'アラマンダー  --(-1049, 110, -803)': 23,
    'Book world  --(-475, 174, -620)': 23,
    'キャラウェイ  --(-950, 72, -1358)': 24,
    'Abandoned Waterway  --(-639, 65, -618)': 24,
    'Icicle Temple  --(1386, 142, -1125)': 25,
    '神父の地下墓地  --(1364, 84, -448)': 25,
    '精霊の巣窟  --(255, 98, -161)': 25,
    'ソドンの滝  --(364, 92, -662)': 27,
    '図書館の地下  --(Library内)': 28,
    'コロセウム  --(-1334, 73, -903)': 29,
    'Qanat  --(-985, 86, -956)': 30,
    'グリムスヴォトン  --(-1280, 98, -1186)': 30,
    'コキュートス  --(1522, 76, 197)': 31,
    'マンティナ洞窟  --(1165, 88, -1222)': 33,
    '訓練所　第1,2訓練室  --(-1014, 69, 822)': 34,
    'ジャデュベ廃坑  --(-838, 108, -1250)': 35,
    'Deja_Boo  --(907, 90, -400)': 36,
    'カシュガル(Qesqer)  --(-1123, 62, -670)': 37,
    'パーゴタリー  --(-196, 125, 389)': 38,
    'FinalFestival  --(-180, 160, -7)': 39,
    'ホートン鉱山  --(-201, 85, -103)': 40,
    'カラ・ルーナ  --(-1366, 70, -547)': 40,
    '深き洞窟  --(-1020, 104, 1225)': 40,
    '憑依船  --(-1297, 73, 705)': 41,
    'Unreasonable Gravity Island  --(194, 49, 1176)': 41,
    'Los cyanyones  --(-879, 71, -1167)': 42,
    'Red Hell Tree  --(-668, 114, -1128)': 43,
    'ザルモザラ  --(-1220, 102, -858)': 44,
    'Collapse Experiment Site  --(1110, 90, -1318)': 45,
    'タオピピ  --(パルジャ(海底村) 内)': 46,
    'マナナスラ  --(-1193, 73, -535)': 47,
    'Amber Break Cave  --(965, 76, 79)': 48,
    'Trollga  --(61, 66, -512)': 50,
    'Lavatree  --(-1096, 75, -1112)': 51,
    'ベルフォート鉱山  --(-1070, 63, 708)': 52,
    'クリベラ洞窟  --(-345, 92, -363)': 53,
    'VenLin回廊  --(1360, 114, 722)': 53,
    '死者の谷  --(-1016, 65, 119)': 54,
    'monte sub terra(モンテサブテラ)  --(-1380, 72, -745)': 55,
    'Mycelium cave  --(870, 22, -1283)': 55,
    'クラバスタ(厄災去りて闇に沈む)  --(1220, 17, -1294)': 55,
    '碧の洞窟  --(-500, 42, 1284)': 55,
    '訓練所　第3,4訓練室  --(-1014, 69, 822)': 56,
    '虚空の地下  --(-902, 69, 1124)': 57,
    '不完全な拷問所  --(-386, 130, 246)': 58,
    '芋虫ダンジョン(高難度アスレ)  --(Trollga 内)': 59,
    'bocyanyu  --(-979, 58, -1158)': 60,
    'cature  --(550, 105, -1158)': 60,
    'マリンディ鉱山  --(109, 118, -801)': 60,
    'Clay Dungeon  --(1189, 88, 410)': 60,
    'Loftgain  --(-989, 65, -1117)': 64,
    'Vambrila Castle  --(クラバスタ(厄災去りて闇に沈む) 内)': 65,
    'Votive  --(ドンケル・エルドール内)': 65,
    'Barco de la Liebre  --(574, 67, 907)': 66,
    'エイドリアン城  --(-1102, 70, 340)': 68,
    '輝煌の残滓(EX)  --(Lux et Tenebrae 内)': 68,
    '力試し  --(-80, 187, 1221)': 70,
    '永久に眠る図書館  --(-619, 29, -658)': 75,
    '厄災降臨  --(クラバスタ(厄災去りて闇に沈む) 内)': 75,
    '追憶と創成の間  --(Lux et Tenebrae-光- 又は 輝煌の残滓 クリア後 TP)': 80,
    '海底谷に沈む研究所(2鯖)  --(海底村(マーラン) 内)': 83
}

highlv_dangeondict = {
    'Underground  --(260, 155, 1)': 'アスレS',
    'Qubasar  --(364, 167, -855)': 'BossRush',
    'カルグラス遺跡  --(nyakonyan\'s secret room1(-1269,79,-927)でNPC(nyakonyan)からクエストを受ける)': 'BossRush',
    '魔界:ココリ山  --(1406, 104, 700)': 'BossRush+++',
    'Estrada Of Cave  --(-1023, 71, -107)': 'Elite',
    'Desert Templum  --(-1197, 121, -1165)': 'Elite',
    'IceCave  --(1437, 153, -1222)': 'Elite',
    'Lux et Tenebrae  --(90,88,-567 (入口: 143,170,-486))': 'Elite',
    'Tower of Judgement  --(-378, 30, 1360)': 'Extream',
    'ムスペルヘイム(バジリスク溶岩洞窟)': 'Expert',
    '魔界:封印の洞窟  --(1470, 70, -790)': 'Expert',
    '魔界:ヘルスラ  --(-906, 78, -704)': 'Expert',
    'AGNI ruins (高難易度アスレ)  --(-474, 150, -622)': 'Extra',
    'Vaaasa  --(1424, 133, -1180)': 'Extra',
    '蒼天に舞う輝煌の創者(1,2鯖)  --(Lux et Tenebrae 最初の部屋)': 'Ulutimate',
    'ドラゴンの谷  --(-1106, 89, 623)': 'Impossible(2鯖)',
    '冥界  --(ドンケル・エル・ドール内)': 'Impossible++',
    'Xen\'s Castle  --(857, 66, -745)': 'XEN',
    '魔界:ソマの谷  --(972, 75, 214)': 'UNKNOWN',
    '浮世の砂海(N)(2鯖)  --(-992,46,-1145)': '未知数',
    '浮世の砂海(T)(2鯖)  --(-992,46,-1145)': '未知数',
    'Last Judgement(2鯖)  --(-948,178,865 (入口: 90 181 -458))': 'Insanity'
}


def get_keys_from_value(dan, val):
    return [k for k, v in dangeondict.items() if v == val]

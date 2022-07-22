category = ['detskiy-mir', 'nedvizhimost', 'transport', 'zapchasti-dlya-transporta', 'zhivotnye', 'dom-i-sad',
            'elektronika', 'uslugi', 'moda-i-stil', 'hobbi-otdyh-i-sport']

category_dict = {'transport': '����', 'nedvizhimost': '������������', 'dom-i-sad': '���-���',
                 'zapchasti-dlya-transporta': "�������� ��� ����������",
                 'elektronika': '�����������', 'moda-i-stil': '������', 'zhivotnye': '��������',
                 'detskiy-mir': '����', 'hobbi-otdyh-i-sport': '�����'}

subcategory = {
    'transport': {'legkovye-avtomobili': '��������', "spetstehnika": "�����������", "selhoztehnika": "��������������",
                  'moto': '���������-�������', "avtomobili-iz-polshi": "���� � ������",
                  "avtobusy": "��������", "vodnyy-transport": "������ ���������",
                  "pritsepy-doma-na-kolesah": "������� , ���� �� �������",
                  "vozdushnyy-transport": "��������� ���������", "drugoy-transport": "������ ���������",
                  'gruzovye-avtomobili': '���������'},

    'nedvizhimost': {'posutochno-pochasovo': '���������� ������', 'nedvizhimost-za-rubezhom': '������������ �� �������',
                     'komnaty': '�������', 'zemlya': '�����',
                     'kommercheskaya-nedvizhimost': '����������� ������������', 'kwatery-pracownicze': '���������',
                     'doma': '����', "kvartiry/novostroyki": "�����������", 'hale-magazyny': '������',
                     'garazhy-parkovki': '������, ��������', 'kvartiry': '��������'},

    'zapchasti-dlya-transporta': {"avtozapchasti-i-aksessuary": "������������ � ���������",
                                  "shiny-diski-i-kolesa": "����, ����� � �����",
                                  "zapchasti-dlya-spets-sh-tehniki": "�������� ��� ����/�� �������",
                                  "motozapchasti-i-aksessuary": "������������",
                                  "prochie-zapchasti": "������ ��������"},

    'zhivotnye': {'sobaki': '������', 'selskohozyaystvennye-zhivotnye': '������� ��������',
                  'akvariumnye-rybki': '����', 'koshki': '����', 'ptitsy': '�����',
                  'drugie-zhivotnye': '������', 'gryzuny': '�������', "reptilii": "��������",
                  'tovary-dlya-zhivotnyh': '����������'},

    'detskiy-mir': {'igrushki': '�������', 'detskaya-odezhda': '������ ', 'detskie-kolyaski': '�������',
                    'detskaya-obuv': '�����',
                    'akcesoria-dla-niemowlat': '����������', 'detskaya-mebel': '������',
                    'detskie-avtokresla': '����-������',
                    'prochie-detskie-tovary': '������', },

    'dom-i-sad ': {'mebel': '������', 'stroitelstvo-remont': '��������', 'sprzet-agd': '�������',
                   "kantstovary-rashodnye-materialy": "����������",
                   "produkty-pitaniya-napitki": "�������� � �������", "sad-ogorod": "���-������",
                   'predmety-interera': '��������', 'instrumenty': '�����������',
                   'prochie-tovary-dlya-doma': '������', },

    'elektronika': {'telefony-i-aksesuary': '��������', 'planshety-el-knigi-i-aksessuary': '��������',
                    'foto-video': '����',
                    'aksessuary-i-komplektuyuschie': '����������',
                    'tehnika-dlya-doma': '������� ��� ����', 'audiotehnika': '������������',
                    'kompyutery-i-komplektuyuschie': '����������',
                    'igry-i-igrovye-pristavki': '������� ���������',
                    'prochaja-electronika': '������', 'tehnika-dlya-kuhni': '������� ��� �����',
                    'noutbuki-i-aksesuary': '��������', "klimaticheskoe-oborudovanie": "������������� ������������",
                    "individualnyy-uhod": "�������������� ����", "tv-videotehnika": "����������/������������"},

    'moda-i-stil': {'odezhda': '������', 'dlya-svadby': '��� �������', 'naruchnye-chasy': '������� ����',
                    'podarki': '�������',
                    'aksessuary': '���������', 'krasota-zdorove': '���������',
                    'moda-raznoe': '���� ������'},

    'hobbi-otdyh-i-sport': {'muzykalnye-instrumenty': '����������� �����������', 'sport-otdyh': '����� �����',
                            'drugoe': '������', 'antikvariat-kollektsii': '��������',
                            'knigi-zhurnaly': '�����', 'cd-dvd-plastinki': '���������/������/�����', "bilety": "������",
                            "poisk-poputchikov": "����� ����������",
                            "poisk-grupp-muzykantov": "����� �����/����������"}}

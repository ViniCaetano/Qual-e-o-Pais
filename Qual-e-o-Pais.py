import unicodedata
import random
import time
from tkinter import *
from tkinter import messagebox

# Dados do jogo
SENHA = ["AFEGANISTAO", "AFRICA DO SUL", "ALBANIA", "ALEMANHA", "ANDORRA", "ANGOLA", "ANTIGUA E BARBUDA", "ARABIA SAUDITA", "ARGELIA", "ARGENTINA", "ARMENIA", "AUSTRALIA", "AUSTRIA", "AZERBAIJAO", "BAHAMAS", "BAHREIN", "BANGLADESH", "BARBADOS", "BELGICA", "BELIZE", "BENIM", "BIELORRUSSIA", "BOLIVIA", "BOSNIA E HERZEGOVINA", "BOTSUANA", "BRASIL", "BRUNEI", "BULGARIA", "BURQUINA FASSO", "BURUNDI", "BUTAO", "CABO VERDE", "CAMAROES", "CAMBOJA", "CANADA", "CATAR", "CAZAQUISTAO", "CHADE", "CHILE", "CHINA", "CHIPRE", "COLOMBIA", "COMORES", "COREIA DO NORTE", "COREIA DO SUL", "COSTA DO MARFIM", "COSTA RICA", "CROACIA", "CUBA", "DINAMARCA", "DJIBUTI", "DOMINICA", "EGITO", "EL SALVADOR", "EMIRADOS ARABES UNIDOS", "EQUADOR", "ERITREIA", "ESCOCIA", "ESLOVAQUIA", "ESLOVENIA", "ESPANHA", "ESSUATINI", "ESTADOS UNIDOS", "ESTONIA", "ETIOPIA", "FIJI", "FILIPINAS", "FINLANDIA", "FRANCA", "GABAO", "GAMBIA", "GANA", "GEORGIA", "GRANADA", "GRECIA", "GUATEMALA", "GUIANA", "GUINE", "GUINE BISSAU", "GUINE EQUATORIAL", "HAITI", "HOLANDA", "HONDURAS", "HUNGRIA", "IEMEN", "ILHAS COOK", "ILHAS MARSHALL", "ILHAS SALOMAO", "INDIA", "INDONESIA", "INGLATERRA", "IRA", "IRAQUE", "IRLANDA", "IRLANDA DO NORTE", "ISLANDIA", "ISRAEL", "ITALIA", "JAMAICA", "JAPAO", "JORDANIA", "KIRIBATI", "KOSOVO", "KUWAIT", "LAOS", "LESOTO", "LETONIA", "LIBANO", "LIBERIA", "LIBIA", "LIECHTENSTEIN", "LITUANIA", "LUXEMBURGO", "MACEDONIA DO NORTE", "MADAGASCAR", "MALASIA", "MALAWI", "MALDIVAS", "MALI", "MALTA", "MARROCOS", "MAURICIA", "MAURITANIA", "MEXICO", "MICRONESIA", "MOCAMBIQUE", "MOLDAVIA", "MONACO", "MONGOLIA", "MONTENEGRO", "MYANMAR", "NAMIBIA", "NAURU", "NEPAL", "NICARAGUA", "NIGER", "NIGERIA", "NIUE", "NORUEGA", "NOVA ZELANDIA", "OMA", "PAIS DE GALES", "PALAU", "PALESTINA", "PANAMA", "PAPUA NOVA GUINE", "PAQUISTAO", "PARAGUAI", "PERU", "POLONIA", "PORTUGAL", "QUENIA", "QUIRGUISTAO", "REPUBLICA CENTRO AFRICANA", "REPUBLICA CHECA", "REPUBLICA DEMOCRATICA DO CONGO", "REPUBLICA DO CONGO", "REPUBLICA DOMINICANA", "ROMENIA", "RUANDA", "RUSSIA", "SAMOA", "SAN MARINO", "SANTA LUCIA", "SAO CRISTOVAO E NEVES", "SAO TOME E PRINCIPE", "SAO VICENTE E GRANADINAS", "SEICHELES", "SENEGAL", "SERRA LEOA", "SERVIA", "SINGAPURA", "SIRIA", "SOMALIA", "SRI LANKA", "SUDAO", "SUDAO DO SUL", "SUECIA", "SUICA", "SURINAME", "TAILANDIA", "TAIWAN", "TAJIQUISTAO", "TANZANIA", "TIMOR LESTE", "TOGO", "TONGA", "TRINIDAD E TOBAGO", "TUNISIA", "TURQUEMENISTAO", "TURQUIA", "TUVALU", "UCRANIA", "UGANDA", "URUGUAI", "UZBEQUISTAO", "VANUATU", "VATICANO", "VENEZUELA", "VIETNA", "ZAMBIA", "ZIMBABWE"]
CONTINENTE = ["ÁSIA", "ÁFRICA", "EUROPA", "EUROPA", "EUROPA", "ÁFRICA", "AMÉRICA", "ÁSIA", "ÁFRICA", "AMÉRICA", "ÁSIA", "OCEANIA", "EUROPA", "ÁSIA", "AMÉRICA", "ÁSIA", "ÁSIA", "AMÉRICA", "EUROPA", "AMÉRICA", "ÁFRICA", "EUROPA", "AMÉRICA", "EUROPA", "ÁFRICA", "AMÉRICA", "ÁSIA", "EUROPA", "ÁFRICA", "ÁFRICA", "ÁSIA", "ÁFRICA", "ÁFRICA", "ÁSIA", "AMÉRICA", "ÁSIA", "ÁSIA", "ÁFRICA", "AMÉRICA", "ÁSIA", "EUROPA", "AMÉRICA", "ÁFRICA", "ÁSIA", "ÁSIA", "ÁFRICA", "AMÉRICA", "EUROPA", "AMÉRICA", "EUROPA", "ÁFRICA", "AMÉRICA", "ÁFRICA", "AMÉRICA", "ÁSIA", "AMÉRICA", "ÁFRICA", "EUROPA", "EUROPA", "EUROPA", "EUROPA", "ÁFRICA", "AMÉRICA", "EUROPA", "ÁFRICA", "OCEANIA", "ÁSIA", "EUROPA", "EUROPA", "ÁFRICA", "ÁFRICA", "ÁFRICA", "ÁSIA", "AMÉRICA", "EUROPA", "AMÉRICA", "AMÉRICA", "ÁFRICA", "ÁFRICA", "ÁFRICA", "AMÉRICA", "EUROPA", "AMÉRICA", "EUROPA", "ÁSIA", "OCEANIA", "OCEANIA", "OCEANIA", "ÁSIA", "ÁSIA", "EUROPA", "ÁSIA", "ÁSIA", "EUROPA", "EUROPA", "EUROPA", "ÁSIA", "EUROPA", "AMÉRICA", "ÁSIA", "ÁSIA", "OCEANIA", "EUROPA", "ÁSIA", "ÁSIA", "ÁFRICA", "EUROPA", "ÁSIA", "ÁFRICA", "ÁFRICA", "EUROPA", "EUROPA", "EUROPA", "EUROPA", "ÁFRICA", "ÁSIA", "ÁFRICA", "ÁSIA", "ÁFRICA", "ÁSIA", "ÁFRICA", "EUROPA", "ÁFRICA", "AMÉRICA", "OCEANIA", "ÁFRICA", "EUROPA", "EUROPA", "ÁSIA", "EUROPA", "ÁSIA", "ÁFRICA", "OCEANIA", "ÁSIA", "AMÉRICA", "ÁFRICA", "ÁFRICA", "OCEANIA", "EUROPA", "OCEANIA", "ÁSIA", "EUROPA", "OCEANIA", "ÁSIA", "AMÉRICA", "OCEANIA", "ÁSIA", "AMÉRICA", "AMÉRICA", "EUROPA", "EUROPA", "ÁFRICA", "ÁSIA", "ÁFRICA", "EUROPA", "ÁFRICA", "ÁFRICA", "AMÉRICA", "EUROPA", "ÁFRICA", "EUROPA", "OCEANIA", "EUROPA", "AMÉRICA", "AMÉRICA", "ÁFRICA", "AMÉRICA", "ÁFRICA", "ÁFRICA", "ÁFRICA", "EUROPA", "ÁSIA", "ÁSIA", "ÁFRICA", "ÁSIA", "ÁSIA", "ÁSIA", "ÁFRICA", "OCEANIA", "ÁFRICA", "OCEANIA", "AMÉRICA", "ÁFRICA", "ÁSIA", "ÁSIA", "OCEANIA", "EUROPA", "ÁFRICA", "AMÉRICA", "ÁSIA", "ÁFRICA", "ÁFRICA"]
AREA = [652090, 1221037, 28748, 356733, 453, 1246700, 440, 2149690, 2381741, 2780400, 29800, 7692024, 83853, 86600, 13878, 678, 143998, 430, 30519, 22965, 112622, 207600, 1098581, 51129, 581730, 8510295, 5765, 110912, 274200, 27834, 47000, 4033, 475442, 181035, 9984670, 11000, 2724900, 1284000, 756945, 9596961, 9251, 1138914, 2235, 120538, 99016, 322463, 51100, 56538, 110861, 43077, 23200, 751, 1001049, 21041, 83600, 283561, 117600, 78772, 49035, 20251, 504782, 17364, 9365412, 45100, 1104300, 18274, 300000, 338145, 551500, 267667, 11295, 238533, 69700, 344, 131990, 108889, 214969, 245857, 36125, 28051, 27750, 41528, 112088, 93032, 527968, 236, 181, 28896, 3287590, 1904569, 130395, 1628750, 438317, 70273, 13843, 103000, 20770, 301338, 10991, 377975, 89342, 726, 10887, 17818, 236800, 30355, 64559, 10452, 111369, 1759540, 160, 65300, 2586, 25713, 587041, 330803, 118484, 298, 1240192, 316, 446550, 2040, 1025520, 1964375, 702, 801590, 33851, 2, 1564116, 13812, 676578, 824116, 260, 385155, 270534, 309500, 20779, 459, 6020, 75517, 462840, 7960951, 406752, 1285216, 312685, 92152, 580367, 199951, 622984, 78867, 2344858, 342000, 48734, 238391, 26338, 17098246, 2831, 61, 539, 261, 1001, 388, 455, 196722, 71740, 88361, 618, 185180, 637657, 65610, 1886068, 644329, 450295, 41285, 163820, 513120, 36179, 143100, 945087, 14874, 56785, 747, 5130, 163610, 488100, 783562, 26, 576604, 241038, 176215, 447400, 12189, 0.44, 912050, 331212, 752612, 390757]
POPULACAO = [38928346, 59308690, 2877797, 83783942, 77265, 32866272, 97929, 34813871, 43851044, 45195774, 2963243, 25499884, 9006398, 10139177, 393244, 1701575, 164689383, 287375, 11589623, 397628, 12123000, 9449323, 11673021, 3280819, 2351627, 213317639, 437479, 6948445, 20903273, 11890784, 771608, 555987, 26545864, 16718965, 37742154, 2881053, 18776707, 16425864, 19116201, 1411780000, 900432, 50882891, 869601, 25778816, 51269185, 26378274, 5094118, 4105267, 11326616, 5792202, 988000, 71986, 102334404, 6486205, 9890402, 17643054, 3546421, 5424800, 5459642, 2078938, 46754778, 1160164, 331449281, 1326335, 114963588, 896445, 109581078, 5540720, 65273511, 2225734, 2416668, 31072940, 3989167, 112523, 10423054, 17915568, 786552, 13132795, 1968001, 1402985, 11402528, 17134872, 9904607, 9660351, 29825968, 17564, 59190, 686884, 1380004385, 273523615, 55619400, 83992949, 40222493, 4937786, 1876695, 341243, 8655535, 60461826, 2961167, 126476461, 10203134, 119449, 1795666, 4270571, 7275560, 2142249, 1886198, 6825445, 5057681, 6871292, 38128, 2722289, 625978, 2083374, 27691018, 32365999, 19129952, 540544, 20250833, 441543, 36910560, 1271768, 4649658, 128932753, 114419, 31255435, 2640438, 39242, 3278290, 649335, 54409800, 2540905, 10824, 29136808, 6624554, 24206644, 206139589, 1626, 5421241, 4822233, 5106626, 3125000, 18094, 5101414, 4314767, 8947024, 220892340, 7132538, 32971854, 37846611, 10344802, 53771296, 6524195, 4829767, 10708981, 89561403, 5518087, 10847910, 19237691, 12952218, 145934462, 198414, 33931, 183627, 53199, 219159, 110940, 98347, 16743927, 7976983, 6926705, 5850342, 17500657, 15893222, 21413249, 43849260, 11193725, 10099265, 8654622, 586632, 69799978, 23816775, 9537645, 59734218, 1318445, 8278724, 105695, 1399488, 11818619, 6031200, 84339067, 11792, 43733762, 45741007, 3473730, 33469203, 307145, 801, 28435940, 97338579, 18383955, 14862924]
CAPITAL = ["CABUL", "PRETÓRIA", "TIRANA", "BERLIM", "ANDORRA-A-VELHA", "LUANDA", "SÃO JOÃO", "RIADE", "ARGEL", "BUENOS AIRES", "EREVÃ", "CAMBERRA", "VIENA", "BACU", "NASSAU", "MANAMA", "DACA", "BRIDGETOWN", "BRUXELAS", "BELMOPÃ", "PORTO NOVO", "MINSQUE", "SUCRE", "SARAIEVO", "GABORONE", "BRASÍLIA", "BANDAR SERI BEGAUÃ", "SÓFIA", "UAGADUGU", "BUJUMBURA", "TIMBU", "PRAIA", "IAUNDÉ", "PNOM PENE", "OTAWA", "DOA", "ASTANA", "JAMENA", "SANTIAGO", "PEQUIM", "NICÓSIA", "BOGOTÁ", "MORONI", "PIONGUIANGUE", "SEUL", "IAMUSSUCRO", "SÃO JOSÉ", "ZAGREBE", "HAVANA", "COPENHAGA", "DJIBUTI", "ROSEAU", "CAIRO", "SAN SALVADOR", "ABU DABI", "QUITO", "ASMARA", "EDIMBURGO", "BRATISLAVA", "LIUBLIANA", "MADRID", "LOBAMBA", "WASHINGTON", "TALIM", "ADIS ABEBA", "SUVA", "MANILA", "HELSÍNQUIA", "PARIS", "LIBREVILLE", "BANJUL", "ACRA", "TEBILÍSSI", "SÃO JORGE", "ATENAS", "CIDADE DA GUATEMALA", "GEORGETOWN", "CONACRI", "BISSAU", "MALABO", "PORTO PRÍNCIPE", "AMESTERDÃ", "TEGUCIGALPA", "BUDAPESTE", "SANÁ", "AVARUA", "MAJURO", "HONIARA", "NOVA DÉLI", "JACARTA", "LONDRES", "TEERÃO", "BAGDADE", "DUBLIN", "BELFAST", "REIQUIAVIQUE", "JERUSALÉM", "ROMA", "KINGSTON", "TÓQUIO", "AMÃ", "TARAUA DO SUL", "PRISTINA", "KUWAIT", "VIENCIANA", "MASERU", "RIGA", "BEIRUTE", "MONRÓVIA", "TRÍPOLI", "VADUZ", "VÍLNIUS", "LUXEMBURGO", "ESCÓPIA", "ANTANANARIVO", "CUALA LUMPUR", "LILÔNGE", "MALÉ", "BAMACO", "VALETA", "REBATE", "PORTO LUÍS", "NUAQUECHOTE", "CIDADE DO MÉXICO", "PALIQUIR", "MAPUTO", "QUIXINAU", "MÓNACO", "ULÃ BATOR", "PODGORITSA", "NEPIEDÓ", "VINDUQUE", "IARÉM", "CATMANDU", "MANÁGUA", "NIAMEI", "ABUJA", "ALOFI", "OSLO", "WELLINGTON", "MASCATE", "CARDIFF", "NGERULMUD", "JERUSALÉM ORIENTAL", "CIDADE DO PANAMÁ", "PORTO MORESBY", "ISLAMABADE", "ASSUNÇÃO", "LIMA", "VARSÓVIA", "LISBOA", "NAIRÓBI", "BISQUEQUE", "BANGUI", "PRAGA", "QUINXASSA", "BRAZAVILE", "SÃO DOMINGOS", "BUCARESTE", "QUIGALI", "MOSCOVO", "APIA", "SAN MARINO", "CASTRIES", "BASSETERRE", "SÃO TOMÉ", "KINGSTOWN", "VITÓRIA", "DACAR", "FREETOWN", "BELGRADO", "SINGAPURA", "DAMASCO", "MOGADÍSCIO", "SRI JAIAVARDENAPURA-COTA", "CARTUM", "JUBA", "ESTOCOLMO", "BERNA", "PARAMARIBO", "BANGUECOQUE", "TAIPÉ", "DUCHAMBÉ", "DODOMA", "DÍLI", "LOMÉ", "NUCUALOFA", "PORTO DE ESPANHA", "TUNES", "ASGABATE", "ANCARA", "FUNAFUTI", "QUIEVE", "CAMPALA", "MONTEVIDEU", "TASQUENTE", "PORTO VILA", "VATICANO", "CARACAS", "HANÓI", "LUSACA", "HARARE"]
IDIOMA = ["DARI, PASTÓ", "AFRICANER, INGLÊS", "ALBANÊS", "ALEMÃO", "CATALÃO", "PORTUGUÊS", "INGLÊS", "ÁRABE", "ÁRABE, BERBERE", "ESPANHOL", "ARMÊNIO", "INGLÊS", "ALEMÃO", "AZERI", "INGLÊS", "ÁRABE", "BENGALI", "INGLÊS", "FRANCÊS, HOLANDÊS, ALEMÃO", "INGLÊS", "FRANCÊS", "BIELORRUSO, RUSSO", "ESPANHOL", "BÓSNIO, CROATA, SÉRVIO", "INGLÊS, TSUANA", "PORTUGUÊS", "BUTANÊS", "BÚLGARO", "FRANCÊS", "KIRUNDI, FRANCÊS, INGLÊS", "BUTÂNES", "PORTUGUÊS", "INGLÊS, FRANCÊS", "KHMER", "INGLÊS, FRANCÊS", "ÁRABE", "CAZAQUE, RUSSO", "ÁRABE, FRANCÊS", "ESPANHOL", "MANDARIM", "GREGO MODERNO, TURCO", "ESPANHOL", "ÁRABE, FRANCÊS, COMORIANO", "COREANO,", "COREANO", "FRANCÊS", "ESPANHOL", "CROATA", "ESPANHOL", "DINAMARQUÊS", "ÁRABE, FRANCÊS", "INGLÊS", "ÁRABE", "ESPANHOL", "ÁRABE", "ESPANHOL", "ÁFRICA, INGLÊS, TIGRINIA", "INGLÊS, GAÉLICO ESCOCÊS", "ESLOVACO", "ESLOVENO", "ESPANHOL", "LÍNGUA SUÁZI, INGLÊS", "INGLÊS,", "ESTONIANO", "AMÁRICO", "INGLÊS, FIJIANO", "FILIPINO, INGLÊS", "FINLANDÊS, SUECO", "FRANCÊS", "FRANCÊS", "ÁRABE, INGLÊS", "INGLÊS", "GEORGIANO", "INGLÊS", "GREGO MODERNO", "ESPANHOL", "INGLÊS", "FRANCÊS", "PORTUGUÊS", "ESPANHOL, FRANCÊS, PORTUGUÊS", "HAITIANO, FRANCÊS", "HOLANDÊS", "ESPANHOL", "HÚNGARO", "ÁRABE", "INGLÊS, MAORI", "MARSHALÊS, INGLÊS", "INGLÊS", "HINDI, INGLÊS", "INDONÉSIO", "INGLÊS", "PERSA", "ÁRABE, CURDO", "INGLÊS, IRLANDÊS", "INGLÊS, IRLANDÊS", "ISLANDÊS,", "HEBREU", "ITALIANO", "INGLÊS, JAMAICANO", "JAPONÊS", "ÁRABE", "KIRIBATI, INGLÊS", "ALBANÊS, SÉRVIO", "KUWAITI, INGLES", "LAO", "SESOTO, INGLÊS", "LETÃO", "ÁRABE", "INGLÊS", "ÁRABE", "ALEMÃO", "LITUANO", "LUXEMBURGUÊS, FRANCÊS, ALEMÃO", "MACEDÔNIO, ALBANÊS", "MALGAXE, FRANCÊS", "MALAIO", "INGLÊS, CHEWA", "DIVEHI", "FRANCÊS", "MALTÊS, INGLÊS", "ÁRABE, BERBERE", "INGLÊS, FRANCÊS", "ÁRABE", "ESPANHOL", "INGLÊS", "PORTUGUÊS", "ROMENO", "FRANCÊS", "MONGOL", "MONTENEGRINO", "LÍNGUA BIRMANESA", "INGLÊS", "INGLÊS, NAURUANO", "NEPALI", "ESPANHOL", "FRANCÊS", "INGLÊS", "INGLÊS", "NORUEGUÊS", "INGLÊS, MAORI", "ÁRABE", "INGLÊS, GALÊS", "INGLÊS, PALAU, JAPONÊS", "ÁRABE", "ESPANHOL", "INGLÊS, TOK PISIN, HIRI MOTU", "URDU, INGLÊS", "ESPANHOL, GUARANI", "ESPANHOL, QUÍCHUA, AIMARÁ", "POLONÊS", "PORTUGUÊS", "SUAÍLI, INGLÊS", "QUIRGUIZ, RUSSO", "FRANCÊS, SANGO", "CHECO", "FRANCÊS", "FRANCÊS", "ESPANHOL", "ROMENO", "RUANDA, FRANCÊS, INGLÊS", "RUSSO", "SAMOANO, INGLÊS", "ITALIANO", "INGLÊS", "INGLÊS, CRIOLO", "PORTUGUÊS", "INGLÊS", "CRIOULO DE SYCHEILLES, FRANCÊS, INGLÊS", "FRANCÊS", "INGLÊS", "SÉRVIO", "INGLÊS, MANDARIM, MALAIO, TÂMIL", "ÁRABE", "SOMALI, ÁRABE", "CINGALÊS, TÂMIL, INGLÊS", "ÁRABE, INGLÊS", "INGLÊS", "SUECO", "ALEMÃO, FRANCÊS, ITALIANO, ROMANCE", "HOLANDÊS", "TAILANDÊS", "MANDARIM", "TADJIQUE", "INGLÊS, SUAÍLI", "TÉTUM, PORTUGUÊS", "FRANCÊS", "TONGANÊS, INGLÊS", "INGLÊS", "ÁRABE", "TURQUEMENO", "TURCO", "TUVALUANO, INGLÊS", "UCRANIANO", "UGANDA", "URUGUAI", "UZBEK", "BISLAMA, INGLÊS, FRANCÊS", "LATIM, ITALIANO", "ESPANHOL", "VIETNAMITA", "INGLÊS", "INGLÊS"]


# Dicionário de dificuldade para cada país
DIFICULDADE_PAISES = {
    "AFEGANISTAO": "Difícil", "AFRICA DO SUL": "Fácil", "ALBANIA": "Médio", "ALEMANHA": "Fácil",
    "ANDORRA": "Médio", "ANGOLA": "Difícil", "ANTIGUA E BARBUDA": "Médio", "ARABIA SAUDITA": "Fácil",
    "ARGELIA": "Difícil", "ARGENTINA": "Fácil", "ARMENIA": "Médio", "AUSTRALIA": "Fácil",
    "AUSTRIA": "Fácil", "AZERBAIJAO": "Difícil", "BAHAMAS": "Fácil", "BAHREIN": "Médio",
    "BANGLADESH": "Difícil", "BARBADOS": "Fácil", "BELGICA": "Fácil", "BELIZE": "Médio",
    "BENIM": "Difícil", "BIELORRUSSIA": "Médio", "BOLIVIA": "Médio", "BOSNIA E HERZEGOVINA": "Médio",
    "BOTSUANA": "Difícil", "BRASIL": "Fácil", "BRUNEI": "Difícil", "BULGARIA": "Médio",
    "BURQUINA FASSO": "Difícil", "BURUNDI": "Difícil", "BUTAO": "Difícil", "CABO VERDE": "Médio",
    "CAMAROES": "Difícil", "CAMBOJA": "Fácil", "CANADA": "Fácil", "CATAR": "Difícil",
    "CAZAQUISTAO": "Difícil", "CHADE": "Difícil", "CHILE": "Médio", "CHINA": "Fácil",
    "CHIPRE": "Fácil", "COLOMBIA": "Fácil", "COMORES": "Difícil", "COREIA DO NORTE": "Difícil",
    "COREIA DO SUL": "Fácil", "COSTA DO MARFIM": "Difícil", "COSTA RICA": "Fácil", "CROACIA": "Fácil",
    "CUBA": "Fácil", "DINAMARCA": "Fácil", "DJIBUTI": "Difícil", "DOMINICA": "Difícil",
    "EGITO": "Fácil", "EL SALVADOR": "Médio", "EMIRADOS ARABES UNIDOS": "Fácil", "EQUADOR": "Médio",
    "ERITREIA": "Difícil", "ESCOCIA": "Fácil", "ESLOVAQUIA": "Médio", "ESLOVENIA": "Médio",
    "ESPANHA": "Fácil", "ESSUATINI": "Difícil", "ESTADOS UNIDOS": "Fácil", "ESTONIA": "Médio",
    "ETIOPIA": "Médio", "FIJI": "Médio", "FILIPINAS": "Fácil", "FINLANDIA": "Fácil",
    "FRANCA": "Fácil", "GABAO": "Difícil", "GAMBIA": "Médio", "GANA": "Médio",
    "GEORGIA": "Médio", "GRANADA": "Médio", "GRECIA": "Fácil", "GUATEMALA": "Médio",
    "GUIANA": "Difícil", "GUINE": "Difícil", "GUINE BISSAU": "Difícil", "GUINE EQUATORIAL": "Difícil",
    "HAITI": "Difícil", "HOLANDA": "Fácil", "HONDURAS": "Médio", "HUNGRIA": "Fácil",
    "IEMEN": "Difícil", "ILHAS COOK": "Difícil", "ILHAS MARSHALL": "Difícil", "ILHAS SALOMAO": "Difícil",
    "INDIA": "Fácil", "INDONESIA": "Fácil", "INGLATERRA": "Fácil", "IRA": "Difícil",
    "IRAQUE": "Difícil", "IRLANDA": "Fácil", "IRLANDA DO NORTE": "Fácil", "ISLANDIA": "Fácil",
    "ISRAEL": "Fácil", "ITALIA": "Fácil", "JAMAICA": "Fácil", "JAPAO": "Fácil",
    "JORDANIA": "Fácil", "KIRIBATI": "Difícil", "KOSOVO": "Médio", "KUWAIT": "Médio",
    "LAOS": "Médio", "LESOTO": "Difícil", "LETONIA": "Médio", "LIBANO": "Médio",
    "LIBERIA": "Difícil", "LIBIA": "Difícil", "LIECHTENSTEIN": "Difícil", "LITUANIA": "Médio",
    "LUXEMBURGO": "Médio", "MACEDONIA DO NORTE": "Médio", "MADAGASCAR": "Médio", "MALASIA": "Fácil",
    "MALAWI": "Difícil", "MALDIVAS": "Fácil", "MALI": "Difícil", "MALTA": "Fácil",
    "MARROCOS": "Fácil", "MAURICIA": "Médio", "MAURITANIA": "Difícil", "MEXICO": "Fácil",
    "MICRONESIA": "Difícil", "MOCAMBIQUE": "Médio", "MOLDAVIA": "Médio", "MONACO": "Fácil",
    "MONGOLIA": "Difícil", "MONTENEGRO": "Médio", "MYANMAR": "Difícil", "NAMIBIA": "Médio",
    "NAURU": "Difícil", "NEPAL": "Fácil", "NICARAGUA": "Médio", "NIGER": "Difícil",
    "NIGERIA": "Fácil", "NIUE": "Difícil", "NORUEGA": "Fácil", "NOVA ZELANDIA": "Fácil",
    "OMA": "Difícil", "PAIS DE GALES": "Fácil", "PALAU": "Difícil", "PALESTINA": "Difícil",
    "PANAMA": "Médio", "PAPUA NOVA GUINE": "Difícil", "PAQUISTAO": "Difícil", "PARAGUAI": "Médio",
    "PERU": "Fácil", "POLONIA": "Fácil", "PORTUGAL": "Fácil", "QUENIA": "Fácil",
    "QUIRGUISTAO": "Difícil", "REPUBLICA CENTRO AFRICANA": "Difícil", "REPUBLICA CHECA": "Fácil",
    "REPUBLICA DEMOCRATICA DO CONGO": "Difícil", "REPUBLICA DO CONGO": "Difícil",
    "REPUBLICA DOMINICANA": "Fácil", "ROMENIA": "Médio", "RUANDA": "Médio", "RUSSIA": "Fácil",
    "SAMOA": "Difícil", "SAN MARINO": "Médio", "SANTA LUCIA": "Médio", "SAO CRISTOVAO E NEVES": "Difícil",
    "SAO TOME E PRINCIPE": "Difícil", "SAO VICENTE E GRANADINAS": "Difícil", "SEICHELES": "Médio",
    "SENEGAL": "Médio", "SERRA LEOA": "Difícil", "SERVIA": "Médio", "SINGAPURA": "Fácil",
    "SIRIA": "Difícil", "SOMALIA": "Difícil", "SRI LANKA": "Médio", "SUDAO": "Difícil",
    "SUDAO DO SUL": "Difícil", "SUECIA": "Fácil", "SUICA": "Fácil", "SURINAME": "Difícil",
    "TAILANDIA": "Fácil", "TAIWAN": "Fácil", "TAJIQUISTAO": "Difícil", "TANZANIA": "Fácil",
    "TIMOR LESTE": "Difícil", "TOGO": "Difícil", "TONGA": "Difícil", "TRINIDAD E TOBAGO": "Médio",
    "TUNISIA": "Fácil", "TURQUEMENISTAO": "Difícil", "TURQUIA": "Fácil", "TUVALU": "Difícil",
    "UCRANIA": "Médio", "UGANDA": "Médio", "URUGUAI": "Médio", "UZBEQUISTAO": "Difícil",
    "VANUATU": "Difícil", "VATICANO": "Fácil", "VENEZUELA": "Médio", "VIETNA": "Fácil",
    "ZAMBIA": "Médio", "ZIMBABWE": "Médio"
}

# Mapeia as dificuldades para as listas de países
PAISES_POR_DIFICULDADE = {
    "Fácil": [pais for pais, dif in DIFICULDADE_PAISES.items() if dif == "Fácil"],
    "Médio": [pais for pais, dif in DIFICULDADE_PAISES.items() if dif == "Médio"],
    "Difícil": [pais for pais, dif in DIFICULDADE_PAISES.items() if dif == "Difícil"],
    "Todos": SENHA
}

class JogoQualEOPais:
    def __init__(self, master):
        self.master = master
        master.title("Qual é o País?")
        master.geometry("650x550")
        master.config(bg="#333333")
        self.master.resizable(False, False)

        self.fonte_titulo = ("Arial", 28, "bold")
        self.fonte_texto = ("Arial", 14)
        self.fonte_dica = ("Arial", 16, "italic")
        self.fonte_feedback = ("Arial", 16, "bold")
        self.fonte_resumo = ("Arial", 14)

        self.dicas_restantes = 5
        self.pontos_rodada = 6
        self.pontuacao_total = 0
        self.pais_secreto = ""
        self.dicas_completas = []
        self.lista_paises_jogo = []
        self.modo_jogo = None
        self.indice_pais_sobrevivencia = 0
        self.sequencia_sobrevivencia = []
        self.historico_paises_rodada = []
        
        # Implementa uma pilha para o histórico de frames
        self.frame_history = []
        self.start_time_message = None

        # Containers para as diferentes telas
        self.menu_frame = Frame(master, bg="#333333")
        self.tutorial_frame = Frame(master, bg="#333333")
        self.modo_frame = Frame(master, bg="#333333")
        self.dificuldade_frame = Frame(master, bg="#333333")
        self.tempo_frame = Frame(master, bg="#333333")
        self.jogo_frame = Frame(master, bg="#333333")
        self.fim_rodada_frame = Frame(master, bg="#333333")
        self.fim_sobrevivencia_frame = Frame(master, bg="#333333")
        self.pause_frame = Frame(master, bg="#333333")


        # Cria os widgets de todas as telas
        self._criar_widgets_menu()
        self._criar_widgets_tutorial()
        self._criar_widgets_modo()
        self._criar_widgets_dificuldade()
        self._criar_widgets_tempo()
        self._criar_widgets_jogo()
        self._criar_widgets_pause()


        self.mostrar_frame(self.menu_frame)

    def _criar_widgets_menu(self):
        Label(self.menu_frame, text="QUAL É O PAÍS?", font=self.fonte_titulo, bg="#333333", fg="white").pack(pady=40)
        Button(self.menu_frame, text="Jogar", command=lambda: self.mostrar_frame(self.modo_frame), font=self.fonte_texto, bg="#4CAF50", fg="white", width=25, height=2).pack(pady=5)
        Button(self.menu_frame, text="Tutorial", command=lambda: self.mostrar_frame(self.tutorial_frame), font=self.fonte_texto, bg="#2196F3", fg="white", width=25, height=2).pack(pady=5)
        Button(self.menu_frame, text="Sair", command=self.master.quit, font=self.fonte_texto, bg="#f44336", fg="white", width=25, height=2).pack(pady=5)

    def _criar_widgets_tutorial(self):
        self._criar_botao_voltar(self.tutorial_frame)
        Label(self.tutorial_frame, text="TUTORIAL", font=self.fonte_titulo, bg="#333333", fg="white").pack(pady=40)
        tutorial_text = """
        O objetivo do jogo é adivinhar o país através de 5 dicas:
        (Continente, Área, População, Capital e Idioma).

        A cada dica, você terá um palpite. Se acertar, sua pontuação
        será baseada nas dicas que restarem. Se errar, uma nova dica
        será revelada.

        Modo Por Tempo: O jogo acaba quando o tempo acabar.
        Modo Sobrevivência: O jogo acaba se você errar o palpite após
        receber todas as dicas. Os países são ordenados por dificuldade.

        Dica: Fique atento à escrita (sem acentos).
        """
        Label(self.tutorial_frame, text=tutorial_text, font=self.fonte_texto, bg="#333333", fg="white", justify=LEFT, wraplength=550).pack(pady=20)
        
    def _criar_widgets_modo(self):
        self._criar_botao_voltar(self.modo_frame)
        Label(self.modo_frame, text="ESCOLHA O MODO DE JOGO", font=self.fonte_titulo, bg="#333333", fg="white").pack(pady=40)
        Button(self.modo_frame, text="Por Tempo", command=lambda: self.definir_modo("tempo"), font=self.fonte_texto, bg="#4CAF50", fg="white", width=25, height=2).pack(pady=5)
        Button(self.modo_frame, text="Sobrevivência", command=lambda: self.definir_modo("sobrevivencia"), font=self.fonte_texto, bg="#f44336", fg="white", width=25, height=2).pack(pady=5)

    def definir_modo(self, modo):
        self.modo_jogo = modo
        if modo == "tempo":
            self.mostrar_frame(self.dificuldade_frame)
        elif modo == "sobrevivencia":
            self.iniciar_modo_sobrevivencia()

    def _criar_widgets_dificuldade(self):
        self._criar_botao_voltar(self.dificuldade_frame)
        Label(self.dificuldade_frame, text="ESCOLHA A DIFICULDADE", font=self.fonte_titulo, bg="#333333", fg="white").pack(pady=40)
        Button(self.dificuldade_frame, text="Fácil", command=lambda: self.definir_dificuldade("Fácil"), font=self.fonte_texto, bg="#4CAF50", fg="white", width=25, height=2).pack(pady=5)
        Button(self.dificuldade_frame, text="Médio", command=lambda: self.definir_dificuldade("Médio"), font=self.fonte_texto, bg="#FFC107", fg="black", width=25, height=2).pack(pady=5)
        Button(self.dificuldade_frame, text="Difícil", command=lambda: self.definir_dificuldade("Difícil"), font=self.fonte_texto, bg="#f44336", fg="white", width=25, height=2).pack(pady=5)
        Button(self.dificuldade_frame, text="Todos os Países", command=lambda: self.definir_dificuldade("Todos"), font=self.fonte_texto, bg="#2196F3", fg="white", width=25, height=2).pack(pady=5)

    def definir_dificuldade(self, dificuldade):
        self.lista_paises_jogo = PAISES_POR_DIFICULDADE[dificuldade]
        if not self.lista_paises_jogo:
            messagebox.showinfo("Oops!", f"Não há países disponíveis para a dificuldade {dificuldade}.")
            return
        self.mostrar_frame(self.tempo_frame)

    def _criar_widgets_tempo(self):
        self._criar_botao_voltar(self.tempo_frame)
        Label(self.tempo_frame, text="ESCOLHA O TEMPO", font=self.fonte_titulo, bg="#333333", fg="white").pack(pady=40)
        Button(self.tempo_frame, text="1 Minuto", command=lambda: self.iniciar_jogo_tempo(1), font=self.fonte_texto, bg="#4CAF50", fg="white", width=25, height=2).pack(pady=5)
        Button(self.tempo_frame, text="3 Minutos", command=lambda: self.iniciar_jogo_tempo(3), font=self.fonte_texto, bg="#4CAF50", fg="white", width=25, height=2).pack(pady=5)
        Button(self.tempo_frame, text="5 Minutos", command=lambda: self.iniciar_jogo_tempo(5), font=self.fonte_texto, bg="#4CAF50", fg="white", width=25, height=2).pack(pady=5)

    def _criar_widgets_jogo(self):
        self._criar_botao_voltar(self.jogo_frame)
        Label(self.jogo_frame, text="Descubra o País!", font=self.fonte_titulo, bg="#333333", fg="white").pack(pady=40)
        
        self.dicas_container = Frame(self.jogo_frame, bg="#333333")
        self.dicas_container.pack(pady=10)

        self.feedback_label = Label(self.jogo_frame, text="", font=self.fonte_feedback, bg="#333333", wraplength=550)
        self.feedback_label.pack(pady=5)

        self.tentativas_label = Label(self.jogo_frame, text="", font=self.fonte_texto, bg="#333333", fg="white")
        self.tentativas_label.pack()
        
        self.input_palpite = Entry(self.jogo_frame, width=30, font=self.fonte_texto)
        self.input_palpite.pack(pady=10)
        self.input_palpite.bind('<Return>', lambda event: self.verificar_palpite())

        self.botao_palpite = Button(self.jogo_frame, text="Palpite", command=self.verificar_palpite, font=self.fonte_texto, bg="#4CAF50", fg="white", width=15)
        self.botao_palpite.pack(pady=5)
        
        self.pontuacao_label = Label(self.jogo_frame, text="", font=self.fonte_texto, bg="#333333", fg="white")
        self.pontuacao_label.pack(pady=10)
        
        self.timer_label = Label(self.jogo_frame, text="", font=self.fonte_texto, bg="#333333", fg="yellow")
        self.timer_label.pack(side=BOTTOM, pady=10)
        
    def _criar_widgets_pause(self):
        Label(self.pause_frame, text="JOGO PAUSADO", font=self.fonte_titulo, bg="#333333", fg="white").pack(pady=40)
        Button(self.pause_frame, text="Continuar Jogo", command=self.continuar_jogo, font=self.fonte_texto, bg="#4CAF50", fg="white", width=25, height=2).pack(pady=10)
        Button(self.pause_frame, text="Voltar para o Menu Principal", command=self.reiniciar_jogo, font=self.fonte_texto, bg="#f44336", fg="white", width=25, height=2).pack(pady=10)


    def _criar_botao_voltar(self, frame):
        voltar_button = Button(frame, text="← Voltar", command=self.voltar, font=("Arial", 12), bg="#555555", fg="white")
        voltar_button.place(x=10, y=10)

    def mostrar_frame(self, frame):
        current_frame = self._get_current_frame()
        if current_frame and current_frame != frame:
            current_frame.pack_forget()
            if not self.frame_history or self.frame_history[-1] != current_frame:
                self.frame_history.append(current_frame)
        
        self.menu_frame.pack_forget()
        self.tutorial_frame.pack_forget()
        self.modo_frame.pack_forget()
        self.dificuldade_frame.pack_forget()
        self.tempo_frame.pack_forget()
        self.jogo_frame.pack_forget()
        self.fim_rodada_frame.pack_forget()
        self.fim_sobrevivencia_frame.pack_forget()
        self.pause_frame.pack_forget()
        
        frame.pack(fill="both", expand=True)
        
    def _get_current_frame(self):
        for frame in [self.menu_frame, self.tutorial_frame, self.modo_frame, self.dificuldade_frame, self.tempo_frame, self.jogo_frame, self.fim_rodada_frame, self.fim_sobrevivencia_frame, self.pause_frame]:
            if frame.winfo_ismapped():
                return frame
        return None

    def voltar(self):
        current_frame = self._get_current_frame()
        if current_frame == self.jogo_frame:
            self.mostrar_frame(self.pause_frame)
        elif self.frame_history:
            if self._get_current_frame() == self.frame_history[-1]:
                self.frame_history.pop()

            if self.frame_history:
                previous_frame = self.frame_history.pop()
                current_frame.pack_forget()
                previous_frame.pack(fill="both", expand=True)
            else:
                self.mostrar_frame(self.menu_frame)
        else:
            pass

    def continuar_jogo(self):
        self.mostrar_frame(self.jogo_frame)
        
    def iniciar_jogo_tempo(self, duracao):
        self.frame_history = []
        self.historico_paises_rodada = []
        self.mostrar_frame(self.jogo_frame)
        self.duracao_jogo = duracao * 60
        self.tempo_inicio = time.time()
        self.atualizar_tempo()
        self.iniciar_nova_rodada()

    def iniciar_modo_sobrevivencia(self):
        self.modo_jogo = "sobrevivencia"
        self.sequencia_sobrevivencia = []
        self.historico_paises_rodada = []
        
        paises_faceis = list(PAISES_POR_DIFICULDADE["Fácil"])
        paises_medios = list(PAISES_POR_DIFICULDADE["Médio"])
        paises_dificeis = list(PAISES_POR_DIFICULDADE["Difícil"])
        
        random.shuffle(paises_faceis)
        random.shuffle(paises_medios)
        random.shuffle(paises_dificeis)

        self.sequencia_sobrevivencia = paises_faceis + paises_medios + paises_dificeis
        self.indice_pais_sobrevivencia = 0
        
        self.pontuacao_total = 0
        self.timer_label.config(text="")
        self.frame_history = []
        self.mostrar_frame(self.jogo_frame)
        self.iniciar_nova_rodada()

    def iniciar_nova_rodada(self):
        self.dicas_restantes = 5
        self.pontos_rodada = 6
        
        if self.modo_jogo == "sobrevivencia":
            if self.indice_pais_sobrevivencia >= len(self.sequencia_sobrevivencia):
                self.finalizar_jogo_sobrevivencia(vitoria=True)
                return
            pais_sorteado = self.sequencia_sobrevivencia[self.indice_pais_sobrevivencia]
            indice = SENHA.index(pais_sorteado)
        else:
            indice = random.randint(0, len(self.lista_paises_jogo) - 1)
            self.pais_secreto = self.lista_paises_jogo[indice]

        self.pais_secreto = SENHA[indice]
        self.historico_paises_rodada.append([self.pais_secreto, False]) # False = Errado
        self.dicas_completas = [
            f"Continente: {CONTINENTE[indice]}",
            f"Área: {'{:,}'.format(AREA[indice]).replace(',', '.')} km²",
            f"População: {'{:,}'.format(POPULACAO[indice]).replace(',', '.')} habitantes",
            f"Capital: {CAPITAL[indice]}",
            f"Idioma: {IDIOMA[indice]}"
        ]

        for widget in self.dicas_container.winfo_children():
            widget.destroy()
        self.feedback_label.config(text="")
        self.input_palpite.delete(0, END)
        self.input_palpite.focus_set()

        self.tentativas_label.config(text=f"Dicas restantes: {self.dicas_restantes}")
        self.pontuacao_label.config(text=f"Pontuação Total: {self.pontuacao_total}")
        self.mostrar_proxima_dica()
        
    def mostrar_proxima_dica(self):
        if self.dicas_restantes > 0:
            dica_a_mostrar = self.dicas_completas[5 - self.dicas_restantes]
            Label(self.dicas_container, text=dica_a_mostrar, font=self.fonte_dica, bg="#333333", fg="white").pack(pady=5)
            self.dicas_restantes -= 1
            self.pontos_rodada -= 1
            self.tentativas_label.config(text=f"Dicas restantes: {self.dicas_restantes}")

    def verificar_palpite(self):
        palpite = self.input_palpite.get().strip().upper()
        palpite_sem_acento = unicodedata.normalize("NFD", palpite).encode("ascii", "ignore").decode("utf-8")
        
        # Verifica se o palpite contém apenas letras e espaços
        if not palpite_sem_acento.replace(" ", "").isalpha():
            self.feedback_label.config(text="Por favor, digite apenas letras. Tente novamente.", fg="red")
            self.input_palpite.delete(0, END)
            return

        if palpite_sem_acento == self.pais_secreto:
            self.historico_paises_rodada[-1][1] = True # True = Acertou
            self.pontuacao_total += (self.pontos_rodada + 1)
            self.feedback_label.config(text=f"Parabéns! Você acertou! O país era {self.pais_secreto}.", fg="green")
            self.pontuacao_label.config(text=f"Pontuação Total: {self.pontuacao_total}")
            
            if self.modo_jogo == "sobrevivencia":
                self.indice_pais_sobrevivencia += 1
                self.master.after(2000, self.iniciar_nova_rodada)
            else:
                self.master.after(2000, self.iniciar_nova_rodada)
        else:
            if self.modo_jogo == "sobrevivencia" and self.dicas_restantes == 0:
                self.feedback_label.config(text=f"Você errou! Fim de jogo. O país era {self.pais_secreto}.", fg="red")
                self.master.after(2000, lambda: self.finalizar_jogo_sobrevivencia(vitoria=False))
            elif palpite_sem_acento not in SENHA:
                self.feedback_label.config(text="Palpite incorreto ou inválido. Tente novamente.", fg="red")
                self.input_palpite.delete(0, END)
            else:
                self.feedback_label.config(text="Você errou! Receba a próxima dica.", fg="orange")
                self.mostrar_proxima_dica()
                self.input_palpite.delete(0, END)

    def atualizar_tempo(self):
        if self.modo_jogo == "tempo":
            tempo_restante = self.duracao_jogo - (time.time() - self.tempo_inicio)
            if tempo_restante > 0:
                minutos = int(tempo_restante // 60)
                segundos = int(tempo_restante % 60)
                self.timer_label.config(text=f"Tempo: {minutos:02}:{segundos:02}")
                self.master.after(1000, self.atualizar_tempo)
            else:
                self.finalizar_jogo_tempo()
    
    def finalizar_jogo_tempo(self):
        mensagem = f"O tempo acabou! Sua pontuação final é: {self.pontuacao_total}"
        self.mostrar_tela_fim_rodada(mensagem, "red")

    def finalizar_jogo_sobrevivencia(self, vitoria):
        if vitoria:
            mensagem = f"Parabéns! Você adivinhou todos os países! Sua pontuação final é: {self.pontuacao_total}"
            cor = "green"
        else:
            mensagem = f"Fim de Jogo! Você errou. Sua pontuação final é: {self.pontuacao_total}"
            cor = "red"
        
        self.mostrar_tela_fim_rodada(mensagem, cor)
        
    def mostrar_tela_fim_rodada(self, mensagem, cor):
        self.mostrar_frame(self.fim_rodada_frame)
        self._criar_botao_voltar(self.fim_rodada_frame)
        
        for widget in self.fim_rodada_frame.winfo_children():
            widget.destroy()
        
        # Cria um Frame para o conteúdo rolável
        main_frame = Frame(self.fim_rodada_frame, bg="#333333")
        main_frame.pack(fill="both", expand=True)
        
        canvas = Canvas(main_frame, bg="#333333", highlightthickness=0)
        scrollbar = Scrollbar(main_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = Frame(canvas, bg="#333333")
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        Label(scrollable_frame, text="Fim do Jogo!", font=self.fonte_titulo, bg="#333333", fg="white").pack(pady=20)
        Label(scrollable_frame, text=mensagem, font=self.fonte_feedback, bg="#333333", fg=cor, wraplength=550).pack(pady=10)
        Label(scrollable_frame, text=f"Pontuação Total: {self.pontuacao_total}", font=self.fonte_texto, bg="#333333", fg="white").pack(pady=10)
        
        Label(scrollable_frame, text="Resumo da Partida", font=("Arial", 18, "bold"), bg="#333333", fg="white").pack(pady=20)
        
        # Exibe a lista de países e resultados
        for pais, acertou in self.historico_paises_rodada:
            frame_pais = Frame(scrollable_frame, bg="#333333")
            frame_pais.pack(pady=2)

            simbolo = "✔" if acertou else "✘"
            cor_simbolo = "green" if acertou else "red"

            Label(frame_pais, text=simbolo, font=("Arial", 16, "bold"), bg="#333333", fg=cor_simbolo).pack(side=LEFT)
            Label(frame_pais, text=pais, font=self.fonte_resumo, bg="#333333", fg="white").pack(side=LEFT, padx=10)

        Button(scrollable_frame, text="Jogar Novamente", command=self.reiniciar_jogo, font=self.fonte_texto, bg="#4CAF50", fg="white", width=25, height=2).pack(pady=10)
        Button(scrollable_frame, text="Menu Principal", command=lambda: self.reiniciar_jogo(), font=self.fonte_texto, bg="#2196F3", fg="white", width=25, height=2).pack(pady=10)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
    def reiniciar_jogo(self):
        self.pontuacao_total = 0
        self.historico_paises_rodada = []
        self.frame_history = [] 
        self.mostrar_frame(self.menu_frame)

root = Tk()
app = JogoQualEOPais(root)
root.mainloop()

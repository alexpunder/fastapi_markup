import os

from dotenv import load_dotenv

load_dotenv()

# API endpoints
FAVORIT_URL = 'https://api.favorit-parts.ru/hs/hsprice/'
MOSKVORECHIE_URL = 'https://portal.moskvorechie.ru/portal.api'
FORUM_URL = 'https://api.forum-auto.ru/v2/listGoods'
ROSSKO_URL = 'http://api.rossko.ru/service/v2.1/GetSearch?wsdl'
AUTOEURO_URL = 'https://api.autoeuro.ru/api/v2/json/search_items/'
PROFITLIGA_URL = 'https://api.pr-lg.ru/search/items'
ARMTEK_URL = 'http://ws.armtek.ru/api/ws_search/search?format=json'
MIKADA_URL = 'https://www.mikado-parts.ru/ws1/service.asmx/CodeBrandStockInfo'
MOTEX_URL = 'https://id18596.public.api.abcp.ru/search/articles/'

# API Keys
FAVORIT_KEY = os.getenv('FAVORIT_KEY')
MOSKVORECHIE_KEY = os.getenv('MOSKVORECHIE_KEY')

FORUM_LOGIN = os.getenv('FORUM_LOGIN')
FORUM_PASSWORD = os.getenv('FORUM_PASSWORD')

ROSSKO_KEY1 = os.getenv('ROSSKO_KEY1')
ROSSKO_KEY2 = os.getenv('ROSSKO_KEY2')
ROSSKO_ADDRESS_ID = os.getenv('ROSSKO_ADDRESS_ID')

AUTO_EURO_KEY = os.getenv('AUTO_EURO_KEY')
AUTOEURO_DELIVERY_KEY = os.getenv('AUTOEURO_DELIVERY_KEY')

PROFITLIGA_KEY = os.getenv('PROFITLIGA_KEY')

ARMTEK_LOGIN = os.getenv('ARMTEK_LOGIN')
ARMTEK_PASSWORD = os.getenv('ARMTEK_PASSWORD')
ARMTEK_USER_ID = os.getenv('ARMTEK_USER_ID')

MIKADA_CLIENT_ID = os.getenv('MIKADA_CLIENT_ID')
MIKADA_PASSWORD = os.getenv('MIKADA_PASSWORD')

MOTEX_USER_LOGIN = os.getenv('MOTEX_USER_LOGIN')
MOTEX_USER_PASSWORD = os.getenv('MOTEX_USER_PASSWORD')

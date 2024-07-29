import aiohttp
from zeep import AsyncClient

from constants import *


async def rossko_get_method(article, brand):
    try:
        async with AsyncClient(ROSSKO_URL) as client:
            params = {
                'KEY1': ROSSKO_KEY1,
                'KEY2': ROSSKO_KEY2,
                'text': article + brand,
                'delivery_id': '000000002',
                'address_id': ROSSKO_ADDRESS_ID
            }
            return await client.service.GetSearch(**params)

    except Exception:
        return None


async def autoeuro_get_method(session, article, brand):
    try:
        autoeuro_payload = {
            'key': AUTO_EURO_KEY,
            'code': article,
            'brand': brand,
            'delivery_key': AUTOEURO_DELIVERY_KEY,
            'with_crosses': '0',
            'with_offers': '0'
        }
        async with session.get(
            AUTOEURO_URL, params=autoeuro_payload
        ) as response:
            return await response.json(
                content_type='application/json'
            )

    except Exception:
        return None


async def profitliga_get_method(session, article):
    try:
        profitliga_payload = {
            'secret': PROFITLIGA_KEY,
            'article': article
        }
        async with session.get(
            PROFITLIGA_URL, params=profitliga_payload
        ) as response:
            return await response.json(
                content_type='application/json'
            )

    except Exception:
        return None


async def armtek_get_method(session, article, brand):
    try:
        login = ARMTEK_LOGIN
        password = ARMTEK_PASSWORD
        basic = aiohttp.BasicAuth(login, password)
        armtek_payload = {
            'VKORG': '4000',
            'KUNNR_RG': ARMTEK_USER_ID,
            'PIN': article,
            'BRAND': brand,
            'QUERY_TYPE': '1',
            'PROGRAM': 'LP'
        }
        async with session.post(
            ARMTEK_URL, data=armtek_payload, auth=basic
        ) as response:
            return await response.json()

    except Exception:
        return None


async def moskvorechie_get_method(session, article, brand):
    try:
        moskvorechie_payload = {
            'l': 'autovlz1',
            'p': MOSKVORECHIE_KEY,
            'act': 'price_by_nr_firm',
            'nr': article,
            'f': brand,
            'extstor': 'extstor',
            'cs': 'utf8'
        }
        async with session.get(
            MOSKVORECHIE_URL, params=moskvorechie_payload
        ) as response:
            return await response.json()
    except Exception:
        return None


async def favorit_get_method(session, article, brand):
    try:
        favorit_payload = {
            'key': FAVORIT_KEY,
            'number': article,
            'brand': brand
        }
        async with session.get(
            FAVORIT_URL, params=favorit_payload
        ) as response:
            favorit_products = await response.json()
            return favorit_products
    except Exception:
        return None


async def forum_get_method(session, article, brand):
    try:
        forum_payload = {
            'login': FORUM_LOGIN,
            'pass': FORUM_PASSWORD,
            'cross': '0',
            'art': article,
            'br': brand
        }
        async with session.get(
            FORUM_URL, params=forum_payload
        ) as response:
            forum_products = response.json()
            return await forum_products
    except Exception:
        return None


async def mikado_get_method(session, article, brand):
    try:
        mikada_payload = {
            'ClientID': MIKADA_CLIENT_ID,
            'Password': MIKADA_PASSWORD,
            'Code': article,
            'Brand': brand,
        }
        async with session.get(
            MIKADA_URL, params=mikada_payload
        ) as response:
            mikada_products = response.text()
            return await mikada_products
    except Exception:
        return None


async def motex_get_method(session, article, brand):
    try:
        motex_payload = {
            'userlogin': MOTEX_USER_LOGIN,
            'userpsw': MOTEX_USER_PASSWORD,
            'number': article,
            'brand': brand,
            'withOutAnalogs': 1
        }
        async with session.get(
            MOTEX_URL, params=motex_payload
        ) as response:
            motex_products = response.json()
            return await motex_products
    except Exception:
        return None

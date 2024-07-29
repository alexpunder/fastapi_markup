from lxml import etree
from zeep.helpers import serialize_object


async def rossko_pars(data):
    data = serialize_object(data)

    if not data or not data.get('success'):
        return []
    result_data = []
    product_info = data['PartsList']['Part']

    if len(product_info) > 1:
        product_info = product_info[1]
    else:
        product_info = product_info[0]

    for result in product_info['stocks']['stock']:
        if not result.get('description') == 'Партнерский склад':
            result_data.append({
                'warehouse': 'static/images/api/rossko.svg',
                'title': product_info['name'],
                'brand': product_info['brand'],
                'article': product_info['partnumber'],
                'price': float(result['price']),
                'stock': result['count'],
                'warehouse_name': result['description']
            })
    return result_data


async def motex_parts(data):

    if data is None:
        return []
    if isinstance(data, dict) and data.get('errorCode'):
        return []

    result_data = []
    for value in data:
        if value.get('distributorId') in (1512524, 1508816):
            result = {
                'warehouse': 'static/images/api/motex.webp',
                'title': value.get('description'),
                'brand': value.get('brand'),
                'article': value.get('number'),
                'price': float(value.get('price')),
                'stock': int(value.get('availability')),
                'warehouse_name': value.get('distributorCode'),
            }
            result_data.append(result)

    return result_data


async def autoeuro_pars(data):
    result_data = []

    if (
        not isinstance(data, dict)
        or data.get('result') in ('ERROR', 'EMPTY')
    ):
        return result_data

    for result in data.get('DATA'):
        result_data.append({
            'warehouse': 'static/images/api/autoeuro.svg',
            'title': result.get('name'),
            'brand': result.get('brand'),
            'article': result.get('code'),
            'price': float(result.get('price')),
            'stock': result.get('amount'),
            'warehouse_name': result.get('warehouse_name')
        })
    result_data.sort(key=lambda x: x['price'])
    return result_data[:3]


async def profitliga_pars(data):
    if not data:
        return []
    try:
        data = data[0].get('products')
        if not data:
            return []
        result_data = []
        for result in data.values():
            result_data.append({
                'warehouse': 'static/images/api/profit_liga.svg',
                'title': result.get('description'),
                'brand': result.get('brand'),
                'article': result.get('article'),
                'price': float(result.get('price')),
                'stock': result.get('quantity'),
                'warehouse_name': result.get('custom_warehouse_name')
            })
        return result_data
    except KeyError as error:
        print(f'Возникла ошибка преобразования данных: {error}')


async def armtek_pars(data):
    result_data = []
    if data.get('STATUS') != 200 or type(data.get('RESP')) is not list:
        return result_data
    data = data.get('RESP')
    for result in data:
        if result.get('PARNR') == '0':
            result_data.append({
                'warehouse': 'static/images/api/armtek.svg',
                'title': result.get('NAME'),
                'brand': result.get('BRAND'),
                'article': result.get('PIN'),
                'price': float(result.get('PRICE')),
                'stock': result.get('RVALUE'),
                'warehouse_name': result.get('KEYZAK')
            })
    return result_data


async def moskvorechie_pars(data):
    if not data or not data.get('result'):
        return []
    result_data = []
    data = data.get('result')
    for result in data:
        if result.get('delivery') in ('на складе', '1 день'):
            result_data.append({
                'warehouse': 'static/images/api/moskvorechie.svg',
                'title': result.get('name'),
                'brand': result.get('brand'),
                'article': result.get('nr'),
                'price': float(result.get('price')),
                'stock': result.get('stock'),
                'warehouse_name': result.get('delivery')
            })
    return result_data


async def favorit_pars(data):
    if not data:
        return []
    data = data.get('goods')
    result_data = []
    for warehouse in data[0].get('warehouses'):
        if warehouse['own'] is True:
            result_data.append({
                'warehouse': 'static/images/api/favorit.svg',
                'title': data[0].get('name'),
                'brand': data[0].get('brand'),
                'article': data[0].get('number'),
                'price': float(warehouse.get('price')),
                'stock': warehouse.get('stock'),
                'warehouse_name': warehouse.get('code')
            })
    return result_data


async def forum_pars(data):
    if not data:
        return []
    if type(data) is not list and data.get('errors'):
        return []
    result_data = []
    for result in data:
        if result.get('whse') in ('VLG', 'RST', 'MSK'):
            result_data.append({
                'warehouse': 'static/images/api/forum.svg',
                'title': result.get('name'),
                'brand': result.get('brand'),
                'article': result.get('art'),
                'price': float(result.get('price')),
                'stock': result.get('num'),
                'warehouse_name': result.get('whse')
            })
    return result_data


async def mikado_parts(data):
    if not data:
        return []
    result_data = []
    xml_data_bytes = data.encode('utf-8')
    root = etree.fromstring(xml_data_bytes)
    namespace = {'ns': 'http://mikado-parts.ru/service'}

    for code_brand_line in root.xpath(
        '//ns:CodeBrandLine', namespaces=namespace
    ):
        result = {
            'warehouse': 'static/images/api/mikado.svg',
            'title': code_brand_line.find(
                'ns:Name', namespaces=namespace
            ).text,
            'brand': code_brand_line.find(
                'ns:Brand', namespaces=namespace
            ).text,
            'article': code_brand_line.find(
                'ns:OrderCode', namespaces=namespace
            ).text,
            'price': float(code_brand_line.find(
                'ns:PriceRUR', namespaces=namespace
            ).text),
            'stock': int(code_brand_line.find(
                'ns:StockQTY', namespaces=namespace
            ).text),
            'warehouse_name': code_brand_line.find(
                'ns:StokName', namespaces=namespace
            ).text
        }
        result_data.append(result)

    result_data.sort(key=lambda x: x['price'])
    return result_data[:3]

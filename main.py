import requests
import json

cookies = {
    'manual_input_tooltip': '0',
    '_slid_server': '660846010685572e310495d5',
    '_slsession': '79B1F766-5B49-444A-A085-6311B9C4AA2A',
    'name_highlight': '0',
    '_ga': 'GA1.1.265314047.1711818245',
    '_gcl_au': '1.1.1037102695.1711818245',
    'metro_api_session': '9YhGP5GTZBEZNetlHCxgYhFZljnsDtDF9LsQQIaK',
    'metro_user_id': 'a1ad6f06a5ea7851262538d95b0b4a10',
    'tmr_lvid': '71f451f7ca63b2c62401f73b628cd4d6',
    'tmr_lvidTS': '1711818245081',
    '_ym_uid': '1711818245340626922',
    '_ym_d': '1711818245',
    '_ym_isad': '1',
    'mindboxDeviceUUID': 'd52731eb-2733-4fff-9357-f82134986787',
    'directCrm-session': '%7B%22deviceGuid%22%3A%22d52731eb-2733-4fff-9357-f82134986787%22%7D',
    '_ym_visorc': 'b',
    '_slid': '660846010685572e310495d5',
    'uxs_uid': '84141ac0-eeb7-11ee-965d-7dd6ecdd4a60',
    '_slfreq': '633ff97b9a3f3b9e90027740%3A633ffa4c90db8d5cf00d7810%3A1711825445%3B64a81e68255733f276099da5%3A64abaf645c1afe216b0a0d38%3A1711825445%3B649ea9cb5bdadc85d50474f9%3A65def0999e2a0f68530a11c7%3A1711825507',
    'sl_exit_intent_viewed': 'true',
    '_slfs': '1711818431094',
    'mp_5e1c29b29aeb315968bbfeb763b8f699_mixpanel': '%7B%22distinct_id%22%3A%20%22%24device%3A18e905184271b08-03b33f825524ae-26001a51-384000-18e905184271b08%22%2C%22%24device_id%22%3A%20%2218e905184271b08-03b33f825524ae-26001a51-384000-18e905184271b08%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fdocs.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22docs.google.com%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fdocs.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22docs.google.com%22%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%7D',
    'mp_88875cfb7a649ab6e6e310368f37a563_mixpanel': '%7B%22distinct_id%22%3A%20%22%24device%3A18e905184291b09-0c1bd665c46bd3-26001a51-384000-18e905184291b09%22%2C%22%24device_id%22%3A%20%2218e905184291b09-0c1bd665c46bd3-26001a51-384000-18e905184291b09%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fdocs.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22docs.google.com%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fdocs.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22docs.google.com%22%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%7D',
    '_ga_VHKD93V3FV': 'GS1.1.1711818244.1.1.1711820074.0.0.0',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    'origin': 'https://online.metro-cc.ru',
    'referer': 'https://online.metro-cc.ru/',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}

# Москва
data = '{"query":"\\n query Query($storeId: Int!, $slug: String!, $attributes:[AttributeFilter], $filters: [FieldFilter], $from: Int!, $size: Int!, $sort: InCategorySort, $in_stock: Boolean, $eshop_order: Boolean, $is_action: Boolean, $price_levels: Boolean) {\\n category (storeId: $storeId, slug: $slug, inStock: $in_stock, eshopAvailability: $eshop_order, isPromo: $is_action, priceLevels: $price_levels) {\\n id\\n name\\n slug\\n id\\n parent_id\\n meta {\\n description\\n h1\\n title\\n keywords\\n }\\n disclaimer\\n description {\\n top\\n main\\n bottom\\n }\\n# treeBranch {\\n# id\\n# name\\n# slug\\n# children {\\n# category_type\\n# id\\n# name\\n# slug\\n# children {\\n# category_type\\n# id\\n# name\\n# slug\\n# children {\\n# category_type\\n# id\\n# name\\n# slug\\n# children {\\n# category_type\\n# id\\n# name\\n# slug\\n# }\\n# }\\n# }\\n# }\\n# }\\n breadcrumbs {\\n category_type\\n id\\n name\\n parent_id\\n parent_slug\\n slug\\n }\\n promo_banners {\\n id\\n image\\n name\\n category_ids\\n virtual_ids\\n type\\n sort_order\\n url\\n is_target_blank\\n analytics {\\n name\\n category\\n brand\\n type\\n start_date\\n end_date\\n }\\n }\\n\\n\\n dynamic_categories(from: 0, size: 9999) {\\n slug\\n name\\n id\\n category_type\\n }\\n filters {\\n facets {\\n key\\n total\\n filter {\\n id\\n name\\n display_title\\n is_list\\n is_main\\n text_filter\\n is_range\\n category_id\\n category_name\\n values {\\n slug\\n text\\n total\\n }\\n }\\n }\\n }\\n total\\n prices {\\n max\\n min\\n }\\n pricesFiltered {\\n max\\n min\\n }\\n products(attributeFilters: $attributes, from: $from, size: $size, sort: $sort, fieldFilters: $filters) {\\n health_warning\\n limited_sale_qty\\n id\\n slug\\n name\\n name_highlight\\n article\\n main_article\\n main_article_slug\\n is_target\\n category_id\\n url\\n images\\n pick_up\\n rating\\n icons {\\n id\\n badge_bg_colors\\n rkn_icon\\n caption\\n image\\n type\\n is_only_for_sales\\n stores\\n caption_settings {\\n colors\\n text\\n }\\n stores\\n sort\\n image_png\\n image_svg\\n description\\n end_date\\n start_date\\n status\\n }\\n manufacturer {\\n id\\n image\\n name\\n }\\n packing {\\n size\\n type\\n pack_factors {\\n instamart\\n }\\n }\\n stocks {\\n value\\n text\\n eshop_availability\\n scale\\n prices_per_unit {\\n old_price\\n offline {\\n price\\n old_price\\n type\\n offline_discount\\n offline_promo\\n }\\n price\\n is_promo\\n levels {\\n count\\n price\\n }\\n online_levels {\\n count\\n price\\n discount\\n }\\n discount\\n }\\n prices {\\n price\\n is_promo\\n old_price\\n offline {\\n old_price\\n price\\n type\\n offline_discount\\n offline_promo\\n }\\n levels {\\n count\\n price\\n }\\n online_levels {\\n count\\n price\\n discount\\n }\\n discount\\n }\\n }\\n }\\n }\\n }\\n","variables":{"storeId":12,"sort":"default","size":2000,"from":0,"filters":[{"field":"main_article","value":"0"}],"attributes":[],"in_stock":true,"eshop_order":false,"allStocks":false,"slug":"vino"}}'
response = requests.post('https://api.metro-cc.ru/products-api/graph', cookies=cookies, headers=headers, data=data)
with open('moscow_metro.json', 'w', encoding='UTF-8') as file:
    json.dump(response.json()['data']['category']['products'], file, indent=4, ensure_ascii=False)

# Санкт-Петербург
data = '{"query":"\\n query Query($storeId: Int!, $slug: String!, $attributes:[AttributeFilter], $filters: [FieldFilter], $from: Int!, $size: Int!, $sort: InCategorySort, $in_stock: Boolean, $eshop_order: Boolean, $is_action: Boolean, $price_levels: Boolean) {\\n category (storeId: $storeId, slug: $slug, inStock: $in_stock, eshopAvailability: $eshop_order, isPromo: $is_action, priceLevels: $price_levels) {\\n id\\n name\\n slug\\n id\\n parent_id\\n meta {\\n description\\n h1\\n title\\n keywords\\n }\\n disclaimer\\n description {\\n top\\n main\\n bottom\\n }\\n# treeBranch {\\n# id\\n# name\\n# slug\\n# children {\\n# category_type\\n# id\\n# name\\n# slug\\n# children {\\n# category_type\\n# id\\n# name\\n# slug\\n# children {\\n# category_type\\n# id\\n# name\\n# slug\\n# children {\\n# category_type\\n# id\\n# name\\n# slug\\n# }\\n# }\\n# }\\n# }\\n# }\\n breadcrumbs {\\n category_type\\n id\\n name\\n parent_id\\n parent_slug\\n slug\\n }\\n promo_banners {\\n id\\n image\\n name\\n category_ids\\n virtual_ids\\n type\\n sort_order\\n url\\n is_target_blank\\n analytics {\\n name\\n category\\n brand\\n type\\n start_date\\n end_date\\n }\\n }\\n\\n\\n dynamic_categories(from: 0, size: 9999) {\\n slug\\n name\\n id\\n category_type\\n }\\n filters {\\n facets {\\n key\\n total\\n filter {\\n id\\n name\\n display_title\\n is_list\\n is_main\\n text_filter\\n is_range\\n category_id\\n category_name\\n values {\\n slug\\n text\\n total\\n }\\n }\\n }\\n }\\n total\\n prices {\\n max\\n min\\n }\\n pricesFiltered {\\n max\\n min\\n }\\n products(attributeFilters: $attributes, from: $from, size: $size, sort: $sort, fieldFilters: $filters) {\\n health_warning\\n limited_sale_qty\\n id\\n slug\\n name\\n name_highlight\\n article\\n main_article\\n main_article_slug\\n is_target\\n category_id\\n url\\n images\\n pick_up\\n rating\\n icons {\\n id\\n badge_bg_colors\\n rkn_icon\\n caption\\n image\\n type\\n is_only_for_sales\\n stores\\n caption_settings {\\n colors\\n text\\n }\\n stores\\n sort\\n image_png\\n image_svg\\n description\\n end_date\\n start_date\\n status\\n }\\n manufacturer {\\n id\\n image\\n name\\n }\\n packing {\\n size\\n type\\n pack_factors {\\n instamart\\n }\\n }\\n stocks {\\n value\\n text\\n eshop_availability\\n scale\\n prices_per_unit {\\n old_price\\n offline {\\n price\\n old_price\\n type\\n offline_discount\\n offline_promo\\n }\\n price\\n is_promo\\n levels {\\n count\\n price\\n }\\n online_levels {\\n count\\n price\\n discount\\n }\\n discount\\n }\\n prices {\\n price\\n is_promo\\n old_price\\n offline {\\n old_price\\n price\\n type\\n offline_discount\\n offline_promo\\n }\\n levels {\\n count\\n price\\n }\\n online_levels {\\n count\\n price\\n discount\\n }\\n discount\\n }\\n }\\n }\\n }\\n }\\n","variables":{"storeId":16,"sort":"default","size":2000,"from":0,"filters":[{"field":"main_article","value":"0"}],"attributes":[],"in_stock":true,"eshop_order":false,"allStocks":false,"slug":"vino"}}'
response = requests.post('https://api.metro-cc.ru/products-api/graph', cookies=cookies, headers=headers, data=data)
with open('spb_metro.json', 'w', encoding='UTF-8') as file:
    json.dump(response.json()['data']['category']['products'], file, indent=4, ensure_ascii=False)
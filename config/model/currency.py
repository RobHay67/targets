
from config.model.countries import country_dict


def currency_name(country_name):
	currency_name = '???'

	for key in country_dict.keys():
		if country_dict[key]['country_name'] == country_name:
			currency_name = country_dict[key]['currency_name']

	return currency_name


def currency_symbol(country_name):  
	currency_symbol = '?'

	for key in country_dict.keys():
		if country_dict[key]['country_name'] == country_name:
			currency_symbol = country_dict[key]['currency_symbol']

	return currency_symbol
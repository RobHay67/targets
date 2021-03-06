country_dict =   {
                    'all':{ 'country_name':'Movember (Total)', 'dashboard_group': None  		, 'reporting_group': None      	 , 'default_member_id':None, 'currency_name':'AUD', 'currency_symbol': '$' , 'time_zone':'Australia/Melbourne', 'gmt_diff':11, 'email':'general.at@produs.movember.com'  },
                    'au' :{ 'country_name':'Australia'     , 'dashboard_group': 'Australia'  , 'reporting_group': 'Big4'      , 'default_member_id': 99, 'currency_name':'AUD', 'currency_symbol': '$' , 'time_zone':'Australia/Melbourne', 'gmt_diff':11, 'email':'general.at@produs.movember.com'  },
                    'at' :{ 'country_name':'Austria'       , 'dashboard_group': 'Europe'     , 'reporting_group': 'Europe'    , 'default_member_id': 88, 'currency_name':'EUR', 'currency_symbol': '€' , 'time_zone':'Europe/Vienna'      , 'gmt_diff': 2, 'email':'au@produs.movember.com'  },
                    'be' :{ 'country_name':'Belgium'       , 'dashboard_group': 'Europe'     , 'reporting_group': 'Europe'    , 'default_member_id': 78, 'currency_name':'EUR', 'currency_symbol': '€' , 'time_zone':'Europe/Brussels'    , 'gmt_diff': 2, 'email':'general.be@produs.movember.com'  },
                    'ca' :{ 'country_name':'Canada'        , 'dashboard_group': 'Canada'     , 'reporting_group': 'Big4'      , 'default_member_id': 94, 'currency_name':'CAD', 'currency_symbol': '$' , 'time_zone':'Canada/Central'     , 'gmt_diff':-4, 'email':'ca@produs.movember.com'  },
                    'cz' :{ 'country_name':'Czech Republic', 'dashboard_group': 'Europe'     , 'reporting_group': 'Europe-Big', 'default_member_id': 90, 'currency_name':'CZK', 'currency_symbol': 'Kč', 'time_zone':'Europe/Prague'      , 'gmt_diff': 2, 'email':'general.cz@produs.movember.com'  },
                    'dk' :{ 'country_name':'Denmark'       , 'dashboard_group': 'Europe'     , 'reporting_group': 'Europe'    , 'default_member_id': 84, 'currency_name':'DKK', 'currency_symbol': 'kr', 'time_zone':'Europe/Copenhagen'  , 'gmt_diff': 2, 'email':'general.dk@produs.movember.com'  }, 
                    'fi' :{ 'country_name':'Finland'       , 'dashboard_group': 'Europe'     , 'reporting_group': 'Europe'    , 'default_member_id': 91, 'currency_name':'EUR', 'currency_symbol': '€' , 'time_zone':'Europe/Helsinki'    , 'gmt_diff': 3, 'email':'general.fi@produs.movember.com'  },
                    'fr' :{ 'country_name':'France'        , 'dashboard_group': 'Europe'     , 'reporting_group': 'Europe-Big', 'default_member_id': 86, 'currency_name':'EUR', 'currency_symbol': '€' , 'time_zone':'Europe/Paris'       , 'gmt_diff': 2, 'email':'general.fr@produs.movember.com'  },
                    'de' :{ 'country_name':'Germany'       , 'dashboard_group': 'Europe'     , 'reporting_group': 'Europe-Big', 'default_member_id': 87, 'currency_name':'EUR', 'currency_symbol': '€' , 'time_zone':'Europe/Berlin'      , 'gmt_diff': 2, 'email':'general.de@produs.movember.com'  },
                    'hk' :{ 'country_name':'Hong Kong'     , 'dashboard_group': 'ROW'        , 'reporting_group': 'ROW'       , 'default_member_id': 81, 'currency_name':'HKD', 'currency_symbol': '$' , 'time_zone':'Asia/Hong_Kong'     , 'gmt_diff': 8, 'email':'general.hk@produs.movember.com'  },
                    'ie' :{ 'country_name':'Ireland'       , 'dashboard_group': 'Ireland'    , 'reporting_group': 'Tier2'     , 'default_member_id': 93, 'currency_name':'EUR', 'currency_symbol': '€' , 'time_zone':'Europe/Dublin'      , 'gmt_diff': 1, 'email':'ie@produs.movember.com'  },
                    'it' :{ 'country_name':'Italy'         , 'dashboard_group': 'Europe'     , 'reporting_group': 'Europe'    , 'default_member_id': 0 , 'currency_name':'EUR', 'currency_symbol': '€' , 'time_zone':'Europe/Rome'        , 'gmt_diff': 2, 'email':'general.it@produs.movember.com'  },
                    'nl' :{ 'country_name':'Netherlands'   , 'dashboard_group': 'Europe'     , 'reporting_group': 'Europe-Big', 'default_member_id': 82, 'currency_name':'EUR', 'currency_symbol': '€' , 'time_zone':'Europe/Amsterdam'   , 'gmt_diff': 2, 'email':'general.nl@produs.movember.com'  },
                    'nz' :{ 'country_name':'New Zealand'   , 'dashboard_group': 'New Zealand', 'reporting_group': 'Tier2'     , 'default_member_id': 98, 'currency_name':'NZD', 'currency_symbol': '$' , 'time_zone':'NZ'                 , 'gmt_diff':13, 'email':'nz@produs.movember.com'  },
                    'no' :{ 'country_name':'Norway'        , 'dashboard_group': 'Europe'     , 'reporting_group': 'Europe'    , 'default_member_id': 83, 'currency_name':'NOK', 'currency_symbol': 'kr', 'time_zone':'Europe/Oslo'        , 'gmt_diff': 2, 'email':'general.no@produs.movember.com'  }, 
                    'ex' :{ 'country_name':'Rest Of World' , 'dashboard_group': 'ROW'        , 'reporting_group': 'ROW'       , 'default_member_id': 77, 'currency_name':'USD', 'currency_symbol': '$' , 'time_zone':'America/Los_Angeles', 'gmt_diff':-7, 'email':'general.ex@produs.movember.com'  },
                    'sg' :{ 'country_name':'Singapore'     , 'dashboard_group': 'ROW'        , 'reporting_group': 'ROW'       , 'default_member_id': 80, 'currency_name':'SGD', 'currency_symbol': '$' , 'time_zone':'Asia/Singapore'     , 'gmt_diff': 8, 'email':'general.sg@produs.movember.com'  },
                    'za' :{ 'country_name':'South Africa'  , 'dashboard_group': 'ROW'        , 'reporting_group': 'ROW'       , 'default_member_id': 92, 'currency_name':'ZAR', 'currency_symbol': '$' , 'time_zone':'Africa/Johannesburg', 'gmt_diff': 2, 'email':'za@produs.movember.com'  },
                    'es' :{ 'country_name':'Spain'         , 'dashboard_group': 'Europe'     , 'reporting_group': 'Europe-Big', 'default_member_id': 85, 'currency_name':'EUR', 'currency_symbol': '€' , 'time_zone':'Europe/Madrid'      , 'gmt_diff': 2, 'email':'general.es@produs.movember.com'  },
                    'se' :{ 'country_name':'Sweden'        , 'dashboard_group': 'Europe'     , 'reporting_group': 'Europe-Big', 'default_member_id': 79, 'currency_name':'SEK', 'currency_symbol': 'kr', 'time_zone':'Europe/Stockholm'   , 'gmt_diff': 2, 'email':'general.se@produs.movember.com'  },
                    'ch' :{ 'country_name':'Switzerland'   , 'dashboard_group': 'Europe'     , 'reporting_group': 'Europe'    , 'default_member_id': 89, 'currency_name':'CHF', 'currency_symbol': '₣' , 'time_zone':'Europe/Zurich'      , 'gmt_diff': 2, 'email':'general.ch@produs.movember.com'  },
                    'gb' :{ 'country_name':'UK'            , 'dashboard_group': 'UK'         , 'reporting_group': 'Big4'      , 'default_member_id': 96, 'currency_name':'GBP', 'currency_symbol': '£' , 'time_zone':'Europe/London'      , 'gmt_diff': 1, 'email':'uk@produs.movember.com'  },
                    'us' :{ 'country_name':'USA'           , 'dashboard_group': 'USA'        , 'reporting_group': 'Big4'      , 'default_member_id': 97, 'currency_name':'USD', 'currency_symbol': '$' , 'time_zone':'America/Los_Angeles', 'gmt_diff':-7, 'email':'us@produs.movember.com'  },
                    # 'zz':{ 'country_name':'zz_missing'    , 'dashboard_group': 'ROW'        , 'reporting_group': 'ROW'       , 'default_member_id': 0 , 'currency_name':'USD', 'currency_symbol': '$' , 'time_zone':'America/Los_Angeles', 'gmt_diff':-7, 'email':'zz@zzzzzz.zzzzzzzz.com'  },
                    }



def country_key_from_name(country_name):

	country_key = ''

	for key, value in country_dict.items():
		if country_name == value['country_name']:
			country_key = key
			break
	
	return country_key


def scope_countries(scope):
	# This function depends on the user being assigned a country or list of countries

	country_code_list = []

	for country_code in country_dict.keys():
		if country_code != 'all':
			country_code_list.append(country_code)

	scope.country_code_list = country_code_list

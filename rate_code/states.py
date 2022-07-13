



us_state_codes = {
# 	'AL':'Alabama',
# 	'AK':'Alaska',
# 	'AZ':'Arizona',
# 	'AR':'Arkansas',
	'CA':'California',
	'CO':'Colorado',
	'CT':'Connecticut',
# 	'DE':'Delaware',
	'DC':'District of Columbia',
	'FL':'Florida',
	'GA':'Georgia',
# 	'HI':'Hawaii',
# 	'ID':'Idaho',
	'IL':'Illinois',
# 	'IN':'Indiana',
# 	'IA':'Iowa',
# 	'KS':'Kansas',
# 	'KY':'Kentucky',
# 	'LA':'Louisiana',
# 	'ME':'Maine',
# 	'MD':'Maryland',
	'MA':'Massachusetts',
# 	'MI':'Michigan',
	'MN':'Minnesota',
# 	'MS':'Mississippi',
# 	'MO':'Missouri',
# 	'MT':'Montana',
# 	'NE':'Nebraska',
# 	'NV':'Nevada',
# 	'NH':'New Hampshire',
	'NJ':'New Jersey',
# 	'NM':'New Mexico',
	'NY':'New York',
# 	'NC':'North Carolina',
# 	'ND':'North DakotA',
	'OH':'Ohio',
# 	'OK':'Oklahoma',
# 	'OR':'Oregon',
	'PA':'Pennsylvania',
# 	'RI':'Rhode Island',
# 	'SC':'South Carolina',
# 	'SD':'South Dakota',
# 	'TN':'Tennessee',
	'TX':'Texas',
# 	'UT':'Utah',
# 	'VT':'Vermont',
# 	'VA':'Virginia',
	'WA':'Washington',
# 	'WV':'West Virginia',
# 	'WI':'Wisconsin',
# 	'WY':'Wyoming',
}


ca_state_codes = {
	'AB':'Alberta',
	'BC':'British Columbia',
	'MB':'Manitoba',
	'NB':'New Brunswick',
	'NL':'Newfoundland and Labrador',
	'NT':'Northwest Territories',
	'NS':'Nova Scotia',
	'NT':'Nunavut',
	'ON':'Ontario',
	'PE':'Prince Edward Island',
	'QC':'Quebec',
	'SK':'Saskatchewan',
	'YT':'Yukon',
}

au_state_list = [ 'NSW', 'VIC', 'QLD', 'WA', 'SA', 'ACT', 'TAS', 'NT']
# au_state_list = [ 'NSW', 'VIC'] # For testing


gb_state_list = ['Greater London', 'South East', 'South West', 'East of England', 'North West', 'North East', 'West Midlands', 'Yorkshire and the Humber', 'Scotland', 'Wales', 'East Midlands', 'Northern Ireland', 'East England', 'Channel Islands', 'Isle of Man']

nz_state_list = ['Auckland', 'Wellington', 'Canterbury', 'Waikato', 'Bay of Plenty', 'Otago', 'Manawatu-Wanganui', "Hawke's Bay", 'Taranaki', 'Northland', 'Southland', 'Tasman', 'Marlborough', 'Nelson', 'Gisborne', 'West Coast' ]

ie_state_list = ['Carlow', 'Cavan', 'Clare', 'Cork', 'Donegal', 'Dublin', 'Galway', "Kerry", 'Kildare', 'Kilkenny', 'Laois', 'Leitrim', 'Limerick', 'Longford', 'Louth', 'Mayo', 'Meath', 'Monaghan',  'Offaly',  'Roscommon',  'Sligo',  'Tipperary',  'Waterford',  'Westmeath',  'Wexford', 'Wicklow'  ]

region_field = 'region_field'
regions = 'regions'
no_regions = {region_field:None, regions:['Other'] }

country_region_config = {
#                 'all':no_regions,
                'au':{ region_field:'state'                    , regions: au_state_list},
                'us':{ region_field:'state'                    , regions: list(us_state_codes.keys())},
                'ca':{ region_field:'state'                    , regions: list(ca_state_codes.keys())},
                'gb':{ region_field:'geo_state_region_province', regions: gb_state_list},
                'nz':{ region_field:'geo_city_or_town'         , regions: nz_state_list},
                'ie':{ region_field:'state'                    , regions: ie_state_list},
                'at':no_regions, 
				'be':no_regions, 
				'cz':no_regions, 
				'dk':no_regions, 
				'fi':no_regions, 
				'fr':no_regions, 
				'de':no_regions, 
				'it':no_regions, 
				'nl':no_regions, 
				'no':no_regions, 
				'es':no_regions, 
				'se':no_regions, 
				'ch':no_regions, 
				'hk':no_regions, 
				'ex':no_regions, 
				'sg':no_regions, 
				'za':no_regions
    
}
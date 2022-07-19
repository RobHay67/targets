

from rate_code.report import print_section_title, add_measure



def store_movember_rates(scope):
	rates_df = foundation_donations	(scope)
	rates_df = new_fundraisers     	(scope)
	rates_df = retained_fundraisers	(scope)
	rates_df = returned_fundraisers	(scope)
	rates_df = total_fundraisers   	(scope)
	rates_df = team_direct			(scope)
	rates_df = total_peer_2_peer   	(scope)


def foundation_donations( scope):

	scope.tenure = 'Foundation'

	print_section_title( scope, 'FOUNDATION & RG DONATIONS - ')
	
	foundation_donation_df  = scope.country_dnt_current[scope.country_dnt_current['donation_type'].isin (['donate_to_charity', 'donate_to_recurring'])]	
	foundation_no_dnts	= len( foundation_donation_df )
	foundation_funds    = round(foundation_donation_df['lcl_fundr_total'].sum(),2)
	foundation_ada      = round( ( foundation_funds / foundation_no_dnts ), 2) if foundation_no_dnts > 0 else 0.0
		
	add_measure( scope, 'donations', foundation_no_dnts, 'FOUNDATION & RG - No of Donations' )
	add_measure( scope, 'ada'      , foundation_ada    , 'FOUNDATION & RG - ADA', None, str( round(foundation_funds,2)) +  ' / ' + str(foundation_no_dnts) + ' = ')
	add_measure( scope, 'funds'    , foundation_funds  , 'FOUNDATION & RG - Total Funds' )
	add_measure( scope, 'comment'  , ''                , 'FOUNDATION & RG - Comment' )

def new_fundraisers( scope):

	scope.tenure = 'New'

	print_section_title( scope, 'NEW Fundraisers')
	
	new_df           = scope.country_frs_current[(scope.country_frs_current['tenure_new'] == 1) & (scope.country_frs_current['customer_type'] == 'fundraiser')]
	new_regos        = len( new_df )
	new_active       = new_df.feat_active.sum()
	new_active_ratio = round( ( new_active / new_regos ), 4) if new_regos > 0 else 0.0
	new_funds        = round( new_df['lcl_fundr_total'].sum(),2)
	new_apam         = round( ( new_funds / new_active ), 2) if new_active > 0 else 0.0
	
	new_regos_targets_desc = 'NEW - No of New Fundraisers (' +  str(scope.campaign_previous) + ')'
	new_regos_finance_desc = 'NEW - No of New Fundraisers (previous campaign)'
	new_funds_targets_desc = 'NEW - Total Funds (' +  str(scope.campaign_previous) + ')'
	new_funds_finance_desc = 'NEW - Total Funds' 
		
	add_measure( scope, 'regos'  , new_regos            , new_regos_targets_desc, new_regos_finance_desc )
	add_measure( scope, 'active' , new_active           , 'NEW - No of Active Fundraisers' )
	add_measure( scope, 'apam'   , new_apam             , 'NEW - APAM (Active)', None, (str(new_active)+' / '+str(new_funds) + ' = ' ) )
	add_measure( scope, 'funds'  , new_funds            , new_funds_targets_desc,  new_funds_finance_desc)   
	add_measure( scope, 'ignore' , new_active_ratio     , 'NEW - Active Ratio', None, (str(new_active)+' / '+str(new_regos) + ' = ' ) )
	add_measure( scope, 'comment', ''                   , 'NEW - Comment' )

def retained_fundraisers( scope):

	scope.tenure = 'Retained'

	print_section_title( scope, 'RETAINED Fundraisers (from previous campaign)')

	total_regos_current  = len( scope.country_frs_current)
	total_regos_previous = len( scope.country_frs_previous)
	
	retained_df           = scope.country_frs_current[(scope.country_frs_current['tenure_retained'] == 1) & (scope.country_frs_current['customer_type'] == 'fundraiser')]
	retained_regos        = len( retained_df )
	retained_ratio        = round( ( retained_regos / total_regos_previous ), 4) if total_regos_previous > 0 else 0.0
	
	retained_active       = retained_df.feat_active.sum()
	retained_active_ratio = round( ( retained_active / retained_regos ), 4) if retained_regos > 0 else 0.0
	retained_funds        = round(retained_df['lcl_fundr_total'].sum(),2)
	retained_apam         = round( ( retained_funds / retained_active ), 2) if retained_active > 0 else 0.0

	total_regos_previous_targets_desc = 'RETAINED - No of Fundraisers (' + str(scope.campaign_retained) + ')'
	total_regos_previous_finance_desc = 'RETAINED - No of Fundraisers (previous campaign)'
	retained_regos_targets_desc = 'RETAINED - Total Retained from (' +  str(scope.campaign_retained) + ') into (' +  str(scope.campaign_previous) + ')'
	retained_regos_finance_desc = 'RETAINED - Total Retained from Previous into Current'
	retained_funds_targets_desc = 'RETAINED - Total Funds (' +  str(scope.campaign_previous) + ')'
	retained_funds_finance_desc = 'RETAINED - Total Funds' 
	total_regos_current_targets_desc = 'RETAINED - No of Fundraisers (' +  str(scope.campaign_previous) + ')'
	total_regos_current_finance_desc = 'RETAINED - Total No of Fundraisers (current campaign)' 
		
	add_measure( scope, 'regos_total_prior', total_regos_previous ,  total_regos_previous_targets_desc, total_regos_previous_finance_desc)
	add_measure( scope, 'regos'            , retained_regos       ,  retained_regos_targets_desc,  retained_regos_finance_desc)
	add_measure( scope, 'active'           , retained_active      , 'RETAINED - No of Active Fundraisers')
	add_measure( scope, 'apam'             , retained_apam        , 'RETAINED - APAM (Active)', None, str( retained_funds) +  ' / ' + str(retained_active) + ' = ')
	add_measure( scope, 'funds'            , retained_funds       ,  retained_funds_targets_desc, retained_funds_finance_desc )   
	add_measure( scope, 'ignore'           , retained_ratio       , 'RETAINED - Retained Ratio', None, str( retained_regos) +  ' / ' + str(total_regos_previous) + ' = ')
	add_measure( scope, 'ignore'           , retained_active_ratio, 'RETAINED - Active Ratio', None, str( retained_active) +  ' / ' + str(retained_regos) + ' = ') 
	add_measure( scope, 'comment'          , ''                   , 'RETAINED - Comment' )
	add_measure( scope, 'regos_total_curnt', total_regos_current  , total_regos_current_targets_desc, total_regos_current_finance_desc )

def returned_fundraisers( scope):

	scope.tenure = 'Returned'

	print_section_title( scope, 'RETURNING Fundraisers (from campaigns before last campaign)')
	
	returned_df           = scope.country_frs_current[(scope.country_frs_current['tenure_returning'] == 1) & (scope.country_frs_current['customer_type'] == 'fundraiser')]
	returned_regos        = len( returned_df )
	returned_active       = returned_df.feat_active.sum()
	returned_active_ratio = round( ( returned_active / returned_regos ), 4) if returned_regos > 0 else 0.0
	returned_funds        = round(returned_df['lcl_fundr_total'].sum(),2)
	returned_apam         = round( ( returned_funds / returned_active ), 2) if returned_active > 0 else 0.0
	

	returned_regos_targets_desc = 'RETURNING - No of Returning Fundraisers from before (' + str(scope.campaign_retained) + ') campaign'
	returned_regos_finance_desc = 'RETURNING - No of Returning Frs before previous campaign'
	returned_funds_targets_desc = 'RETURNING - Total Funds     (' + str(scope.campaign_previous) + ')' 
	returned_funds_finance_desc = 'RETURNING - Total Funds'

	add_measure( scope, 'regos'  , returned_regos        , returned_regos_targets_desc, returned_regos_finance_desc )
	add_measure( scope, 'active' , returned_active       , 'RETURNING - No of Active Fundraisers' )
	add_measure( scope, 'apam'   , returned_apam         , 'RETURNING - APAM (Active)', None, str( returned_funds) +  ' / ' + str(returned_active) + ' = ')
	add_measure( scope, 'funds'  , returned_funds        , returned_funds_targets_desc, returned_funds_finance_desc)
	add_measure( scope, 'ignore' , returned_active_ratio , 'RETURNING - Active Ratio', None, str( returned_active) +  ' / ' + str(returned_regos)  + ' = ')
	add_measure( scope, 'comment', ''                    , 'RETURNING - Comment' )

def total_fundraisers( scope):
	
	scope.tenure = 'total'

	print_section_title( scope, 'Total INDIVIDUALS Fundraising')

	fundraiser_df = scope.country_frs_current[scope.country_frs_current['customer_type'] == 'fundraiser']
	
	total_regos_current  = len( fundraiser_df)
	total_active       = fundraiser_df.feat_active.sum()
	total_funds_current  = round((fundraiser_df['lcl_fundr_total'].sum()),2)
	
	add_measure( scope, 'ignore', total_regos_current, 'TOTAL INDIVIDUALS - Total Number of Fundraisers' )
	add_measure( scope, 'ignore', total_active   	 , 'TOTAL INDIVIDUALS - Total Active Fundraisers' )
	add_measure( scope, 'ignore', total_funds_current, 'TOTAL INDIVIDUALS - Total Funds Raised' )


def team_direct( scope):

	scope.tenure = 'Team'

	print_section_title( scope, 'TEAM DIRECT DONATIONS')
	
	team_direct_df = scope.country_frs_current[scope.country_frs_current['customer_type'] == 'team']
	# Remove teams that did not raise any funds
	team_direct_df = team_direct_df[team_direct_df['aud_fundr_total'] != 0]
	
	team_count  = len( team_direct_df )
	team_funds  = round(team_direct_df['lcl_donor_team'].sum(),2)
	team_atdd   = round( ( team_funds / team_count ), 2) if team_count > 0 else 0.0
	# ATDD - Average Team Direct Donations?
	
	add_measure( scope, 'donations', team_count, 'TEAM - No of Teams' )
	add_measure( scope, 'atdd'     , team_atdd , 'TEAM - ATDD', None, str( round(team_funds,2)) +  ' / ' + str(team_count) + ' = ')
	add_measure( scope, 'funds'    , team_funds, 'TEAM - Total Funds' )
	add_measure( scope, 'comment'  , ''        , 'TEAM - Comment' )


def total_peer_2_peer( scope):

	scope.tenure = 'total'

	print_section_title( scope, 'Total PEER 2 PEER Fundraising')

	fundraisers_df = scope.country_frs_current[scope.country_frs_current['customer_type'] == 'fundraiser']
	teams_active_df = scope.country_frs_current[scope.country_frs_current['customer_type'] == 'team']
	teams_active_df = teams_active_df[teams_active_df['aud_fundr_total'] != 0]

	total_regos_current  = len( fundraisers_df) + len( teams_active_df)
	total_funds_current  = round((scope.country_frs_current['lcl_fundr_total'].sum()),2)

	add_measure( scope, 'ignore', total_regos_current   , 'TOTAL PEER 2 PEER - Total Number of Fundraisers' )
	add_measure( scope, 'ignore', total_funds_current   , 'TOTAL PEER 2 PEER - Total Funds Raised' )

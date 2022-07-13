

from rate_code.report import print_section_title, print_measure




def movember_rates(params, rates_df, country, region, frs_current, dnt_current, total_regos_current, total_regos_previous, total_funds_current):
    rates_df = new_fundraisers     	( params, rates_df, country, region, frs_current )
    rates_df = retained_fundraisers	( params, rates_df, country, region, frs_current, total_regos_current, total_regos_previous )
    rates_df = returned_fundraisers	( params, rates_df, country, region, frs_current)
    rates_df = total_peer_2_peer   	( params, rates_df, country, region,              total_regos_current, total_funds_current)
    rates_df = team_direct			( params, rates_df, country, region, dnt_current)
    rates_df = foundation_donations	( params, rates_df, country, region, dnt_current)

    return rates_df


def new_fundraisers( params, rates_df, country, region, frs_current ):
    print_section_title( 'NEW Fundraisers - '+country+' - region = '+region )
    
#     new_df           = frs_current[frs_current['tenure_new'] == 1]
    new_df           = frs_current[(frs_current['tenure_new'] == 1)        & (frs_current['customer_type'] == 'fundraiser')]
    new_regos        = len( new_df )
    new_active       = new_df.feat_active.sum()
    new_active_ratio = round( ( new_active / new_regos ), 4) if new_regos > 0 else 0.0
    new_funds        = round( new_df['lcl_fundr_total'].sum(),2)
    new_apam         = round( ( new_funds / new_active ), 2) if new_active > 0 else 0.0
        
    desc_new_regos = 'NEW - No of New Fundraisers (previous campaign)' if params.finance_description else 'NEW - No of New Fundraisers (' + params.previous_campaign + ')'
    desc_new_funds = 'NEW - Total Funds'                               if params.finance_description else 'NEW - Total Funds (' + params.previous_campaign + ')'
        
    rates_df = print_measure( rates_df, country, region, 'New', 'regos'       , new_regos            ,  desc_new_regos)
    rates_df = print_measure( rates_df, country, region, 'New', 'active'      , new_active           , 'NEW - No of Active Fundraisers' )
    rates_df = print_measure( rates_df, country, region, 'New', 'apam'        , new_apam             , 'NEW - APAM (Active)', (str(new_active)+' / '+str(new_funds) + ' = ' ) )
    rates_df = print_measure( rates_df, country, region, 'New', 'funds'       , new_funds            , desc_new_funds )   
    rates_df = print_measure( rates_df, country, region, 'New', 'ignore'      , new_active_ratio     , 'NEW - Active Ratio', (str(new_active)+' / '+str(new_regos) + ' = ' ) )
    rates_df = print_measure( rates_df, country, region, 'New', 'comment'     , ''                   , 'NEW - Comment' )
    
    return rates_df



def retained_fundraisers( params, rates_df, country, region, frs_current, total_regos_current, total_regos_previous):
    
    print_section_title( 'RETAINED Fundraisers (from previous campaign) - '+country+' - region = '+region )
    
#     retained_df           = frs_current[frs_current['tenure_retained'] == 1]
    retained_df           = frs_current[(frs_current['tenure_retained'] == 1)        & (frs_current['customer_type'] == 'fundraiser')]
    retained_regos        = len( retained_df )
    retained_ratio        = round( ( retained_regos / total_regos_previous ), 4) if total_regos_previous > 0 else 0.0
    
    retained_active       = retained_df.feat_active.sum()
    retained_active_ratio = round( ( retained_active / retained_regos ), 4) if retained_regos > 0 else 0.0
    retained_funds        = round(retained_df['lcl_fundr_total'].sum(),2)
    retained_apam         = round( ( retained_funds / retained_active ), 2) if retained_active > 0 else 0.0
        
    desc_total_regos_previous = 'RETAINED - No of Fundraisers (previous campaign)'      if params.finance_description else 'RETAINED - No of Fundraisers (' + params.retained_campaign + ')'
    desc_retained_regos       = 'RETAINED - Total Retained from Previous into Current'  if params.finance_description else 'RETAINED - Total Retained from (' + params.retained_campaign + ') into (' + params.previous_campaign + ')'
    desc_retained_funds       = 'RETAINED - Total Funds'                                if params.finance_description else 'RETAINED - Total Funds (' + params.previous_campaign + ')'
    desc_total_regos_current  = 'RETAINED - Total No of Fundraisers (current campaign)' if params.finance_description else 'RETAINED - No of Fundraisers (' + params.previous_campaign + ')'
         
    rates_df = print_measure( rates_df, country, region, 'Retained', 'regos_total_prior', total_regos_previous ,  desc_total_regos_previous)
    rates_df = print_measure( rates_df, country, region, 'Retained', 'regos'            , retained_regos       ,  desc_retained_regos )
    rates_df = print_measure( rates_df, country, region, 'Retained', 'active'           , retained_active      , 'RETAINED - No of Active Fundraisers')
    rates_df = print_measure( rates_df, country, region, 'Retained', 'apam'             , retained_apam        , 'RETAINED - APAM (Active)', str( retained_funds) +  ' / ' + str(retained_active) + ' = ')
    rates_df = print_measure( rates_df, country, region, 'Retained', 'funds'            , retained_funds       ,  desc_retained_funds )   
    rates_df = print_measure( rates_df, country, region, 'Retained', 'ignore'           , retained_ratio       , 'RETAINED - Retained Ratio', str( retained_regos) +  ' / ' + str(total_regos_previous) + ' = ')
    rates_df = print_measure( rates_df, country, region, 'Retained', 'ignore'           , retained_active_ratio, 'RETAINED - Active Ratio', str( retained_active) +  ' / ' + str(retained_regos) + ' = ') 
    rates_df = print_measure( rates_df, country, region, 'Retained', 'comment'          , ''                   , 'RETAINED - Comment' )
    rates_df = print_measure( rates_df, country, region, 'Retained', 'regos_total_curnt', total_regos_current  , desc_total_regos_current )
    
    return rates_df


def returned_fundraisers( params, rates_df, country, region, frs_current):
    
    print_section_title( 'RETURNING Fundraisers (from campaigns before last campaign) - '+country+' - region = '+region )
    
#     returned_df           = frs_current[frs_current['tenure_returning'] == 1]
    returned_df           = frs_current[(frs_current['tenure_returning'] == 1) & (frs_current['customer_type'] == 'fundraiser')]
    returned_regos        = len( returned_df )
    returned_active       = returned_df.feat_active.sum()
    returned_active_ratio = round( ( returned_active / returned_regos ), 4) if returned_regos > 0 else 0.0
    returned_funds        = round(returned_df['lcl_fundr_total'].sum(),2)
    
    returned_apam         = round( ( returned_funds / returned_active ), 2) if returned_active > 0 else 0.0

        
    desc_returned_regos = 'RETURNING - No of Returning Frs before previous campaign' if params.finance_description else 'RETURNING - No of Returning Fundraisers from before (' + params.retained_campaign + ') campaign'
    desc_returned_funds = 'RETURNING - Total Funds'                                  if params.finance_description else 'RETURNING - Total Funds     (' + params.previous_campaign + ')' 
    
    rates_df = print_measure( rates_df, country, region, 'Returned', 'regos'  , returned_regos        , desc_returned_regos)
    rates_df = print_measure( rates_df, country, region, 'Returned', 'active' , returned_active       , 'RETURNING - No of Active Fundraisers' )
    rates_df = print_measure( rates_df, country, region, 'Returned', 'apam'   , returned_apam         , 'RETURNING - APAM (Active)', str( returned_funds) +  ' / ' + str(returned_active) + ' = ')
    rates_df = print_measure( rates_df, country, region, 'Returned', 'funds'  , returned_funds        , desc_returned_funds)
    rates_df = print_measure( rates_df, country, region, 'Returned', 'ignore' , returned_active_ratio , 'RETURNING - Active Ratio', str( returned_active) +  ' / ' + str(returned_regos)  + ' = ')
    rates_df = print_measure( rates_df, country, region, 'Returned', 'comment', ''                    , 'RETURNING - Comment' )
       
    return rates_df


def total_peer_2_peer( params, rates_df, country, region, total_regos_current, total_funds_current):
    
    print_section_title( 'Total PEER 2 PEER Fundraising - '+country+' - region = '+region )
    
    rates_df = print_measure( rates_df, country, region, 'total', 'ignore', total_regos_current   , 'TOTAL PEER 2 PEER - Total Number of Fundraisers' )
    rates_df = print_measure( rates_df, country, region, 'total', 'ignore', total_funds_current   , 'TOTAL PEER 2 PEER - Total Funds Raised' )
    
    return rates_df


def team_direct( params, rates_df, country, region, dnt_current):
    
    print_section_title( 'TEAM DIRECT DONATIONS - '+country+' - region = '+region )
    
    team_direct_df           = frs_current[(frs_current['tenure_retained'] == 1)        & (frs_current['customer_type'] == 'team')]
    
    
    foundation_donation_df  = dnt_current[dnt_current['donation_type'] == 'donate_to_charity']
    foundation_no_donation  = len( foundation_donation_df )
    foundation_funds        = round(foundation_donation_df['lcl_donor_foundation'].sum(),2)
    foundation_ada          = round( ( foundation_funds / foundation_no_donation ), 2) if foundation_no_donation > 0 else 0.0

    
    rates_df = print_measure( rates_df, country, region, 'Foundation', 'donations', foundation_no_donation, 'FOUNDATION - No of Donations' )
    rates_df = print_measure( rates_df, country, region, 'Foundation', 'funds'    , foundation_funds      , 'FOUNDATION - Total Funds' )
    rates_df = print_measure( rates_df, country, region, 'Foundation', 'ada'      , foundation_ada        , 'FOUNDATION - ADA', str( round(foundation_funds,2)) +  ' / ' + str(foundation_no_donation) + ' = ')
    rates_df = print_measure( rates_df, country, region, 'Foundation', 'comment'  , ''                    , 'FOUNDATION - Comment' )
    
    return rates_df


def foundation_donations( params, rates_df, country, region, dnt_current):
    
    print_section_title( 'FOUNDATION DONATIONS - '+country+' - region = '+region )
    
    foundation_donation_df  = dnt_current[dnt_current['donation_type'] == 'donate_to_charity']
    foundation_no_donation  = len( foundation_donation_df )
    foundation_funds        = round(foundation_donation_df['lcl_donor_foundation'].sum(),2)
    foundation_ada          = round( ( foundation_funds / foundation_no_donation ), 2) if foundation_no_donation > 0 else 0.0

    
    rates_df = print_measure( rates_df, country, region, 'Foundation', 'donations', foundation_no_donation, 'FOUNDATION - No of Donations' )
    rates_df = print_measure( rates_df, country, region, 'Foundation', 'funds'    , foundation_funds      , 'FOUNDATION - Total Funds' )
    rates_df = print_measure( rates_df, country, region, 'Foundation', 'ada'      , foundation_ada        , 'FOUNDATION - ADA', str( round(foundation_funds,2)) +  ' / ' + str(foundation_no_donation) + ' = ')
    rates_df = print_measure( rates_df, country, region, 'Foundation', 'comment'  , ''                    , 'FOUNDATION - Comment' )
    
    return rates_df



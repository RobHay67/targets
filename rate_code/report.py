



def print_section_title( description ):
    print ( '-'*130)
    print ( description )
    print ( '-'*130)




def print_measure( rates_df, country, region, tenure, metric, result, measure, formula='' ):
    
    campaign =  2021
    finance_measure = country.upper()+'-'+measure
    tab1 = 55
    tab2 = 40
    
    print ( finance_measure.ljust(tab1), str( formula ).rjust(tab2), str( result ) )
        
    rates_df = rates_df.append( {'campaign':campaign, 'payment_country':country, 'region':region, 'tenure':tenure, 'metric':metric, 'result':result, 'formula':formula, 'finance_measure':finance_measure }, ignore_index=True)  
    
    return rates_df


rates_df_columns = ['campaign', 'payment_country', 'region', 'tenure',  'metric', 'result', 'formula', 'finance_measure']



def print_country(country):
    print ( '='*130)
    print ( country.upper() )
    print ( '='*130)
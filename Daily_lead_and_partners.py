import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    # DF = daily_sales.groupby(['date_id', 'make_name']).agg(
    #   unique_leads=('lead_id', 'nunique'),
    #   unique_partners=  ('partner_id', 'nunique')
    #   ).reset_index()


    # return DF
    dict = {}
    res=[]
    for i in range(len(daily_sales)):
      date_id = daily_sales['date_id'][i]
      make_name = daily_sales['make_name'][i]
      lead_id = daily_sales['lead_id'][i]
      partner_id = daily_sales['partner_id'][i]
      key = (date_id, make_name)

      if key not in dict:
        dict[key] = [set(),set()]
      dict[key][0].add(lead_id)
      dict[key][1].add(partner_id)    
      
      

    for key, values in dict.items():
      res.append([key[0], key[1],len(values[0]), len(values[1])])
    
    DF = pd.DataFrame(res, columns= ('date_id', 'make_name', 'unique_leads', 'unique_partners'))
    
    
    return DF
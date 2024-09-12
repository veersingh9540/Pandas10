import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
  Dict = {}
  res= []
  for i in range(len(activities)):
    product = activities['product'][i]
    date = activities['sell_date'][i]
    if date not in Dict:
      Dict[date] = [] 
    if product not in Dict[date]:
      Dict[date].append(product)

  for key, values in Dict.items():
    res.append([key, len(values), values])

  DF = pd.DataFrame(res, columns=['sell_date', 'num_sold', 'products'])
  DF['products'] = DF['products'].apply(lambda x: ','.join(sorted(x)))

  return DF.sort_values('sell_date')

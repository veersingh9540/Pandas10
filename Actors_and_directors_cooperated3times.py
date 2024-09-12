import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
  # DF = actor_director.groupby(['actor_id', 'director_id']).count().reset_index()

  # return DF[['actor_id', 'director_id']][(DF['timestamp'] >= 3)]
  dict = {}
  res =[]
  for i in range(len(actor_director)):
    actor_id = actor_director['actor_id'][i]
    director_id = actor_director['director_id'][i]

    if (actor_id, director_id) not in dict: 
      dict[(actor_id, director_id)] = 0
    dict[(actor_id, director_id)] = dict[(actor_id, director_id)] + 1

  for key, values in dict.items():
    if values >= 3:
      res.append([key[0], key[1]])


  return pd.DataFrame(res, columns= ['actor_id', 'director_id'])
    
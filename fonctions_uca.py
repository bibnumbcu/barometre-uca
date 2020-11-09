import pandas

##
# fonction pour lire et agréger les données de plusieurs csv (un par année)
# prend en paramètre le préfixe de la source (hal ou wos)
def read_all_csv(file_prefix):
    datas_per_year = []

    for year in range (2016, 2030):
        try:
            datas_df = pandas.read_csv("Data/raw/{}/{}_{}.csv".format(str(year), file_prefix, str(year)), sep=",", encoding='latin-1')
            datas_per_year.append(datas_df)
        except:
            continue
        
    full_datas = pandas.concat(datas_per_year)
    
    return full_datas



## fonction pour filtrer la dataframe de résultats selon un champ
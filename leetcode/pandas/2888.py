import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    # return df1._append(df2) #beats 9run 65mb used 
    # return pd.concat([df1,df2],axis=0) #beats 5run used 64mb
    # return pd.concat([df1,df2]) #beats 13%run
    return pd.merge(df1, df2, how='outer')

    
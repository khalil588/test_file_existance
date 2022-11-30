import glob
import pandas as pd
import os
import time
import xlrd
#creating a list full of the file's names under the directory needed
def ls_file(link):
    y = glob.glob(link)
    return y


#searching for the newest file
def finding_creation_date(x):

    ti_c = os.path.getctime(x)
    c_ti = time.ctime(ti_c)

    # Using the timestamp string to create a
    # time object/structure
    t_obj = time.strptime(c_ti)

    # Transforming the time object to a timestamp
    # of ISO 8601 format
    T_stamp = time.strftime("%Y-%m-%d %H:%M:%S", t_obj)
    return T_stamp
def files_date(link):
    z = {}
    df = pd.DataFrame(ls_file(link), columns=['names'])
    df['creation_time'] = df.apply(lambda df : finding_creation_date(df['names']),axis=1)
    x = df['creation_time'].max()

    y = df.loc[df['creation_time']==x,'names'].values[0]
    z['names'] = y
    z['creation_time'] = df.loc[df['names']==y,'creation_time'].values.item()
    return z

import pandas as pd
from finding_the_newest_file import files_date

def test_existance(db_name,db_link):
    new_file = files_date(db_link)['names']
    df = pd.read_excel(open(db_name,'rb'),sheet_name='sheet1')
    last_old_file = df['names'].tolist()

    if new_file == last_old_file[-1] :
        return False
    else:
        df = df.append(files_date(db_link),ignore_index=True)

        with pd.ExcelWriter(db_name) as writer:
            df.to_excel(writer, sheet_name='sheet1', index=False)
        return True

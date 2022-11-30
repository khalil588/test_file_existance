from testing_file_existance import test_existance
from sending_mail import sendmail
from constant import db_storage,cours_storage,files_bd_name_date,files_cours_name_date,mail_content_bd_src,mail_content_cours_src,mail_content_bd_cours_src
import subprocess

def run_code():
    subprocess.run('python C:/frais/transform_pfe/main.py',shell=True)
    subprocess.call([r'C:/frais/datwarehouse/jobs/dim_BANK_0.1/dim_BANK/dim_BANK_run.bat'])
    subprocess.call([r'C:/frais/datwarehouse/jobs/dim_COUNTRY_0.1/dim_COUNTRY/dim_COUNTRY_run.bat'])
    subprocess.call([r'C:/frais/datwarehouse/jobs/dim_CURRENCY_0.1/dim_CURRENCY/dim_CURRENCY_run.bat'])
    subprocess.call([r'C:/frais/datwarehouse/jobs/dim_DATE_0.1/dim_DATE/dim_DATE_run.bat'])
    subprocess.call([r'C:/frais/datwarehouse/jobs/dim_FOLDER_0.1/dim_FOLDER/dim_FOLDER_run.bat'])
    subprocess.call([r'C:/frais/datwarehouse/jobs/dim_REFERENCE_0.1/dim_REFERENCE/dim_REFERENCE_run.bat'])
    subprocess.call([r'C:/frais/datwarehouse/jobs/dim_STATUS_0.1/dim_STATUS/dim_STATUS_run.bat'])
    subprocess.call([r'C:/frais/datwarehouse/jobs/dim_UNIT_0.1/dim_UNIT/dim_UNIT_run.bat'])
    subprocess.call(r'C:/frais/datwarehouse/jobs/FACT_CHANGE_0.1/FACT_CHANGE/FACT_CHANGE_run.bat')
    subprocess.call([r'C:/frais/datwarehouse/jobs/FACT_BANK_0.1/FACT_BANK/FACT_BANK_run.bat'])






def test_1():
    if (test_existance(files_bd_name_date,db_storage) == False) and (test_existance(files_cours_name_date,cours_storage) == False):
        sendmail(mail_content_bd_cours_src)
        print('mail du cours et bd à été envoyé avec succées!')
        return -1
    elif (test_existance(files_bd_name_date,db_storage) == True) and (test_existance(files_cours_name_date,cours_storage) == False) :
        sendmail(mail_content_cours_src)
        print('mail du cours à été envoyé avec succées!')
        run_code()
        return 1
    elif (test_existance(files_bd_name_date,db_storage) == False) and (test_existance(files_cours_name_date,cours_storage) == True) :
        sendmail(mail_content_bd_src)
        print('mail du frais à été envoyé avec succées!')
        return -1
    else:
        run_code()
        print('jawwek behy')
        return 0
test_1()






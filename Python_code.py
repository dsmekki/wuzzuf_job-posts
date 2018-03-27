""" 
Here we will get exchange rates data for the currencies used by the supply side.
Exchange rates for most used currencies will be extarcted from the Yahoo finance API.
For currencies that used for just one record will be converted manually by using the currency convertor of xe.com
and that also beacuse of the lack of exchange data for these type of currencies in Yahoo finance database.
So the conversion will be done by using a historical exchange rate data based on the value of post_date field.

A list of currencies that will be extracted from the Yahoo API are as follows:
- United States Dollar
- U.A. Emirates Dirham
- Qatari Riyal
- British Pound
- Euro
- Saudi Arabian Riyal
- Jordanian Dinar
- Canadian Dollar
- Indian Rupee

A list of currencies that will be converted manually by using xe.com currency convertor are as follows:
- Kuwaiti Dinar : 25.3996440434 at 2014-06-28
- Ghanaian Cedis : 1.9841621954 at 2015-04-15 
- Dominican Republic Pesos : 0.1711319981 at 2016-02-09
- Ethiopian Birr : 0.3668532577 at 2016-01-20 
- East Caribbean Dollar : 2.8991114884 at 2015-12-15 

Note on Ecuadoran Sucre:
The sucre was the currency of Ecuador between 1884 and 2000.
The currency was replaced by the US dollar as a result of the 1998–99 financial crisis.
So there is no currency named Ecuadoran Sucre those days.
This record will be removed because of its ambiguous nature.

Note on null currency values:
The records that have no currency type data will be removed from the data set.

Note on output csv files:
The output csv files not be merged and converted to a data frame object because of the time interval may be different
for various currency pairs. So to be in a safe side the conversion will be done by filtering on every type of currency
on the Job Posts Excel sheet and making vlookup operation between the job posts file and the exchange rates files.

Note on System Time Sleep and Random Seed Settings:
I used randomly seeded system time sleep to prevent getting bloacked or getting an Error during reading data from
the API. And i also used three tiers loop enclosing try and except statements because the error pattern being
generated during the fetching of data not be accurately recognized.

"""

import pandas_datareader.data as pdr
from datetime import datetime
import time
import random

start = datetime(2014, 1, 1)
end = datetime(2016, 12, 31)

#USD/EGP "United States Dollar" to "Egyptian Pound"
for i in range(3):
    try:
        usd_egp = pdr.DataReader('EGP=X', 'yahoo', start, end)
    except:
        next
usd_egp = usd_egp.Close
usd_egp.to_csv("usd_egp_ex.csv", header=True)
print(len(usd_egp), " Trading Dates for USD/EGP")
random.seed(time.gmtime().tm_sec)
time.sleep(random.randint(20,70))

#AED/EGP "U.A. Emirates Dirham" to "Egyptian Pound"
for i in range(3):
    try:
        egp_aed = pdr.DataReader('EGPAED=X', 'yahoo', start, end)
    except:
        next
egp_aed = egp_aed.Close
aed_egp = egp_aed.apply(lambda x: 1/x)
aed_egp.to_csv("aed_egp_ex.csv", header=True)
print(len(aed_egp), " Trading Dates for AED/EGP")
random.seed(time.gmtime().tm_sec)
time.sleep(random.randint(20,70))

#QAR/EGP "Qatari Riyal" to "Egyptian Pound"
for i in range(3):
    try:
        egp_qar = pdr.DataReader('EGPQAR=X', 'yahoo', start, end)
    except:
        next
egp_qar = egp_qar.Close
qar_egp = egp_qar.apply(lambda x: 1/x)
qar_egp.to_csv("qar_egp_ex.csv", header=True)
print(len(qar_egp), " Trading Dates for QAR/EGP")
random.seed(time.gmtime().tm_sec)
time.sleep(random.randint(20,70))

#GBP/EGP "British Pound" to "Egyptian Pound"
for i in range(3):
    try:
        egp_gbp = pdr.DataReader('EGPGBP=X', 'yahoo', start, end)
    except:
        next
egp_gbp = egp_gbp.Close
gbp_egp = egp_gbp.apply(lambda x: 1/x)
gbp_egp.to_csv("gbp_egp_ex.csv", header=True)
print(len(gbp_egp), " Trading Dates for GBP/EGP")
random.seed(time.gmtime().tm_sec)
time.sleep(random.randint(20,70))

#EUR/EGP "Euro" to "Egyptian Pound"
for i in range(3):
    try:
        egp_eur = pdr.DataReader('EGPEUR=X', 'yahoo', start, end)
    except:
        next
egp_eur = egp_eur.Close
eur_egp = egp_eur.apply(lambda x: 1/x)
eur_egp.to_csv("eur_egp_ex.csv", header=True)
print(len(eur_egp), " Trading Dates for EUR/EGP")
random.seed(time.gmtime().tm_sec)
time.sleep(random.randint(20,70))

#SAR/EGP "Saudi Arabian Riyal" to "Egyptian Pound"
for i in range(3):
    try:
        egp_sar = pdr.DataReader('EGPSAR=X', 'yahoo', start, end)
    except:
        next
egp_sar = egp_sar.Close
sar_egp = egp_sar.apply(lambda x: 1/x)
sar_egp.to_csv("sar_egp_ex.csv", header=True)
print(len(sar_egp), " Trading Dates for SAR/EGP")
random.seed(time.gmtime().tm_sec)
time.sleep(random.randint(20,70))

#JOD/EGP "Jordanian Dinar" to "Egyptian Pound"
for i in range(3):
    try:
        egp_jod = pdr.DataReader('EGPJOD=X', 'yahoo', start, end)
    except:
        next
egp_jod = egp_jod.Close
jod_egp = egp_jod.apply(lambda x: 1/x)
jod_egp.to_csv("jod_egp_ex.csv", header=True)
print(len(jod_egp), " Trading Dates for JOD/EGP")
random.seed(time.gmtime().tm_sec)
time.sleep(random.randint(20,70))

#CAD/EGP "Canadian Dollar" to "Egyptian Pound"
for i in range(3):
    try:
        egp_cad = pdr.DataReader('EGPCAD=X', 'yahoo', start, end)
    except:
        next
egp_cad = egp_cad.Close
cad_egp = egp_cad.apply(lambda x: 1/x)
cad_egp.to_csv("cad_egp_ex.csv", header=True)
print(len(cad_egp), " Trading Dates for CAD/EGP")
random.seed(time.gmtime().tm_sec)
time.sleep(random.randint(20,70))

#INR/EGP "Indian Rupee" to "Egyptian Pound"
for i in range(3):
    try:
        egp_inr = pdr.DataReader('EGPINR=X', 'yahoo', start, end)
    except:
        next
egp_inr = egp_inr.Close
inr_egp = egp_inr.apply(lambda x: 1/x)
inr_egp.to_csv("inr_egp_ex.csv", header=True)
print(len(inr_egp), " Trading Dates for INR/EGP")

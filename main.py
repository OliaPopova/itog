import pandas
import glob

city = pandas.read_csv('city_202206290152.csv')
print(city)


vacation = pandas.read_csv('vacation.csv')
print(vacation['city'])

files=glob.glob('.csv')
print(files)

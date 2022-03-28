# tested by test2.py

# return city, country in formatted string
def city_country(city, country, population=-1):
    if population != -1:
         return (city+", "+country+" - population="+str(population)).title()
    else:
        return (city+", "+country).title
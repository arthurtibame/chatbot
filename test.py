import configparser

config = configparser.ConfigParser()
config.read('urls.ini')
a = config.get('URLS', 'handout_icon1')
b = config.get('URLS', 'kafka_url')  
c = config.get('URLS', 'timetable_url')  

print(a)
print()
print(b)
print()
print(c)
import extract
from database import NEODatabase
from models import NearEarthObject, CloseApproach

neo2 = NearEarthObject(pdes=123, hazardous='Y')
neo1 = NearEarthObject(pdes=433, name='Eros', diameter=16.84, hazardous='N')

cad1 = CloseApproach(des=433, time='1900-Jan-01 00:11',
                     dist='0.0921795123769547',
                     vrel='16.7523040362574')
cad2 = CloseApproach(des=123, time='1900-Jan-02 00:23', dist='0.1234',
                     vrel='12.12345')

print(f"{neo1} \n{neo2}")
print(f'{neo1.fullname}\n{neo2.fullname}')

print(f'{cad1}')
print(f'{cad1.time_str}')

neos = extract.load_neos('data/neos.csv')
cads = extract.load_approaches('data/cad.json')

# neos = {neo1.designation: neo1, neo2.designation: neo2}
# cads = {cad1._designation: cad1, cad2._designation: cad2}

db = NEODatabase(neos, cads)
print(db.get_neo_by_name('SOHO'))
pass

from webexam.database import *
from webexam.models import *
from practice import read_item_bank

# add a admin user
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
first_user = User('xing',role='admin')
first_user.password='1'
db_session.add(first_user)
db_session.commit()
# 
ib = read_item_bank('1.txt')

aircraft_system = Lib('aircraft system')
db_session.add(aircraft_system)
db_session.commit()
ac=Section(aircraft_system.id, 'air conditioning')
fc=Section(aircraft_system.id, 'flight control')
db_session.add_all([ac,fc])
db_session.commit()
for i in range(30):
    s = Subject('SingleSel', ib[i].index, ac.id)
    db_session.add(s)
    db_session.commit()
    a = Answer(s.id, '1')
    db_session.add(a)
    db_session.commit()
    for c in ib[i].choice:
        ch = Option(s.id, c)
        db_session.add(ch)
        db_session.commit()
        
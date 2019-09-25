from pony.orm import Database, PrimaryKey, Required, Set, db_session, Optional
from uuid import uuid4 as gid, UUID
import datetime as dt



db = Database()
print("Radim ")


db.bind(provider='sqlite', filename='Hanuljak-Monika.sqlite', create_db=True)


class Tim(db.Entity):
    id = PrimaryKey(str)
    naziv = Required(str)
    igraci = Set("Igrac")
    rezultati = Set("Rezultati")

class Igrac(db.Entity):
    id = PrimaryKey(str)
    ImeiPrezime = Required(str)
    DatumRodenja= Required(str)
    MjestoRodenja=Required(str)
    Slika=Required(str)
    tim = Set(Tim)
    bodovi_igraca = Set("Bodovi_igraca")




class Bodovi_igraca(db.Entity):
    id = PrimaryKey(str)
    bodovi = Optional(int)
    igraci = Required(Igrac)


class Rezultati(db.Entity):
    id=PrimaryKey(str)
    utakmice=Optional(int)
    ukupno=Optional(int)
    pobjede=Optional(int)
    izgubljene=Optional(int)
    nerjeseno=Optional(int)
    bodovi=Optional(int)
    tim=Required(Tim)



db.generate_mapping(check_tables=True, create_tables=True)

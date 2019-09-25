from model import Tim, Igrac, Bodovi_igraca,Rezultati
from pony.orm import db_session, select
from uuid import uuid4 as gid, UUID


class Timovi:
    @db_session()
    def listaj():

        q = select(s for s in Tim)

        def dohvati_veze(x):
            if "igraci" in x:
                x["igraci"] = [Igrac[y].to_dict() for y in x["igraci"]]
            return x
        timovi = [dohvati_veze(s.to_dict(with_collections=True)) for s in q]
        return timovi

    @db_session
    def dodaj(s):
        try:
            s["id"] = str(gid())
            if "igraci" in s:
                igraci_ukup = s["igraci"]
                svi_igraci = list(Igrac[x] for x in igraci_ukup)
                s["igraci"] = svi_igraci
            kreiran_tim= Tim(**s)
            return True, kreiran_tim.id
        except Exception as e:
            return False, str(e)

    @db_session
    def delete(s):
        try:
            Tim[s].delete()
            return True, None
        except Exception as e:
            return False,str(e)


    @db_session
    def update(s):
        try:

            if "igraci" in s:
                igraci_ukup = s["igraci"]
                svi_igraci = list(Igrac[x] for x in igraci_ukup)
                s["igraci"] = svi_igraci
            Tim[s["id"]].set(**s)

            return True, None

        except Exception as e:
            return False,str(e)


class Igraci:
    @db_session()
    def listaj():
        q = select(s for s in Igrac)
        data = [x.to_dict() for x in q]
        return data,

    @db_session
    def dodaj(s):
        try:
            s["id"] = str(gid())
            s = Igrac(**s)
            return True, None
        except Exception as e:
            return False, str(e)


    @db_session
    def delete(s):
        try:

            Igrac[s].delete()


            return True,None
        except Exception as e:
            return e,print("Igrac je u nekom od timova")


class Bodovi_igraca_:

    @db_session()
    def listaj():
        q = select(i for i in Bodovi_igraca)
        data = [x.to_dict() for x in q]
        return data



    @db_session
    def dodaj(igraci):
        try:
            for s in igraci:
                s["id"] = str(gid())

                s = Bodovi_igraca(**s)
            o = "Uspjesno"
            return True, o

        except Exception as e:
            return False, str(e)

    @db_session
    def update(igraci):
        try:
            for s in igraci:
                Bodovi_igraca[s["id"]].set(**s)

            return True,None

        except Exception as e:
            return False,str(e)


class Rezultati_timova:

    @db_session()
    def listaj():
        q = select(i for i in Rezultati)
        data = [x.to_dict() for x in q]
        return data



    @db_session
    def dodaj(s):
        try:
            s["id"] = str(gid())

            s = Rezultati(**s)

            return True, None

        except Exception as e:
            return False, str(e)

    @db_session
    def update(s):
        try:
            Rezultati[s["id"]].set(**s)
            o = "Uspjesno"
            return True, o

        except Exception as e:
            return False,str(e)

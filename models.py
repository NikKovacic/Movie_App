from google.appengine.ext import ndb


class Sporocilo(ndb.Model):
    naslov = ndb.StringProperty()
    leto = ndb.IntegerProperty()
    ocena = ndb.IntegerProperty()
    imdb = ndb.StringProperty()
    komentar = ndb.StringProperty()
    slika = ndb.StringProperty()
    trailer = ndb.StringProperty()
    #ogled = ndb.BooleanProperty()
    #dat_ogleda = ndb.DateTimeProperty()
    dat_vnosa = ndb.DateTimeProperty(auto_now_add=True)
    izbrisan = ndb.BooleanProperty(default=False)
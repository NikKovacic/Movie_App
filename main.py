#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import os
import jinja2
import webapp2
from google.appengine.api import users
from models import Sporocilo


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if params is None:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            logiran = True
            logout_url = users.create_logout_url('/about')

            params = {"logiran": logiran, "logout_url": logout_url, "user": user}
        else:
            logiran = False
            login_url = users.create_login_url('/about')

            params = {"logiran": logiran, "login_url": login_url, "user": user}

        return self.render_template("about.html", params)

        # def get(self):
        #    return self.render_template("about.html")


class HomeHandler(BaseHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            logiran = True
            logout_url = users.create_logout_url('/')

            params = {"logiran": logiran, "logout_url": logout_url, "user": user}
        else:
            logiran = False
            login_url = users.create_login_url('/')

            params = {"logiran": logiran, "login_url": login_url, "user": user}

        return self.render_template("home.html", params)

        # def get(self):
        #   return self.render_template("home.html")


class VnesiFilmHandler(BaseHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            logiran = True
            logout_url = users.create_logout_url('/vnesi_film')

            params = {"logiran": logiran, "logout_url": logout_url, "user": user}
        else:
            logiran = False
            login_url = users.create_login_url('/vnesi_film')

            params = {"logiran": logiran, "login_url": login_url, "user": user}

        return self.render_template("vnesi_film.html", params)

    def post(self):
        naslov = self.request.get("naslov_filma")
        leto = self.request.get("leto")
        ocena = self.request.get("ocena")
        imdb_link = self.request.get("imdb_link")
        trailer_link = self.request.get("trailer_link")
        komentar = self.request.get("komentar")
        slika = self.request.get("slika_url")
        sporocilo = Sporocilo(naslov=naslov, leto=int(leto), ocena=int(ocena), imdb=imdb_link, trailer=trailer_link,
                              komentar=komentar, slika=slika)
        sporocilo.put()

        self.write(" - ".join([naslov, leto]))

        # def get(self):
        #    return self.render_template("vnesi_film.html")


class SeznamFilmovHandler(BaseHandler):
    def get(self):
        seznam = Sporocilo.query().fetch()
        user = users.get_current_user()

        if user:
            logiran = True
            logout_url = users.create_logout_url('/seznam_filmov')

            params = {"vnosi": seznam, "logiran": logiran, "logout_url": logout_url, "user": user}
        else:
            logiran = False
            login_url = users.create_login_url('/seznam_filmov')

            params = {"logiran": logiran, "login_url": login_url, "user": user}

        return self.render_template("seznam_filmov.html", params=params)

        #  def get(self):
        #      seznam = Sporocilo.query().fetch()
        #      params = {"vnosi": seznam}
        #      return self.render_template("seznam_filmov.html", params=params)


class PodrobnostiHandler(BaseHandler):
    def get(self, sporocilo_id):
        sporocilo = Sporocilo.get_by_id(int(sporocilo_id))
        user = users.get_current_user()

        if user:
            logiran = True
            logout_url = users.create_logout_url('/seznam_filmov')

            params = {"sporocilo": sporocilo, "logiran": logiran, "logout_url": logout_url, "user": user}
        else:
            logiran = False
            login_url = users.create_login_url('/seznam_filmov')

            params = {"sporocilo": sporocilo, "logiran": logiran, "login_url": login_url, "user": user}

        return self.render_template("podrobnosti.html", params=params)


class IzbrisiSporociloHandler(BaseHandler):
    def get(self, sporocilo_id):
        sporocilo = Sporocilo.get_by_id(int(sporocilo_id))
        user = users.get_current_user()

        if user:
            logiran = True
            logout_url = users.create_logout_url('/seznam_filmov')

            params = {"sporocilo": sporocilo, "logiran": logiran, "logout_url": logout_url, "user": user}
        else:
            logiran = False
            login_url = users.create_login_url('/seznam_filmov')

            params = {"sporocilo": sporocilo, "logiran": logiran, "login_url": login_url, "user": user}

        return self.render_template("izbrisi.html", params=params)

    def post(self, sporocilo_id):
        sporocilo = Sporocilo.get_by_id(int(sporocilo_id))
        sporocilo.key.delete()

        return self.redirect_to("seznam_filmov")


class UrediSporociloHandler(BaseHandler):
    def get(self, sporocilo_id):
        sporocilo = Sporocilo.get_by_id(int(sporocilo_id))
        user = users.get_current_user()

        if user:
            logiran = True
            logout_url = users.create_logout_url('/seznam_filmov')

            params = {"sporocilo": sporocilo, "logiran": logiran, "logout_url": logout_url, "user": user}
        else:
            logiran = False
            login_url = users.create_login_url('/seznam_filmov')

            params = {"sporocilo": sporocilo, "logiran": logiran, "login_url": login_url, "user": user}

        return self.render_template("uredi_sporocilo.html", params=params)

    def post(self, sporocilo_id):
        sporocilo = Sporocilo.get_by_id(int(sporocilo_id))
        novi_naslov = self.request.get("naslov")
        novo_leto = self.request.get("leto")
        nova_ocena = self.request.get("ocena")
        novi_imdb = self.request.get("imdb_link")
        novi_komentar = self.request.get("komentar")
        nova_slika = self.request.get("slika_url")
        novi_trailer = self.request.get("trailer_link")

        sporocilo.naslov = novi_naslov
        sporocilo.leto = int(novo_leto)
        sporocilo.ocena = int(nova_ocena)
        sporocilo.imdb = novi_imdb
        sporocilo.komentar = novi_komentar
        sporocilo.slika = nova_slika
        sporocilo.trailer = novi_trailer

        sporocilo.put()

        return self.redirect_to("seznam_filmov")


app = webapp2.WSGIApplication([
    webapp2.Route('/about', MainHandler),
    webapp2.Route('/', HomeHandler),
    webapp2.Route('/vnesi_film', VnesiFilmHandler),
    webapp2.Route('/seznam_filmov', SeznamFilmovHandler, name="seznam_filmov"),
    webapp2.Route('/podrobnosti/<sporocilo_id:\d+>', PodrobnostiHandler),
    webapp2.Route('/podrobnosti/<sporocilo_id:\d+>/izbrisi', IzbrisiSporociloHandler),
    webapp2.Route('/podrobnosti/<sporocilo_id:\d+>/uredi', UrediSporociloHandler),
], debug=True)

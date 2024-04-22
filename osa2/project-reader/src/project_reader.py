from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        
        content = request.urlopen(self._url).read().decode("utf-8")
        #print(content)
        toml_string = content
        parsed = toml.loads(toml_string)
        nimi = parsed['tool']['poetry']['name']
        desci = parsed['tool']['poetry']['description']
        lisenssi = parsed['tool']['poetry']['license']
        riippuvuudet = parsed['tool']['poetry']['dependencies']
        dev_riippuvuudet = parsed['tool']['poetry']['group']['dev']['dependencies']
        #print(dev_riippuvuudet)        
      #  print(f"{nimi} ja desci ois {desci} ja ja lisuri onpi {lisenssi}")
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(nimi, desci, lisenssi, riippuvuudet, dev_riippuvuudet)

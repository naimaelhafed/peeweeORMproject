import datetime

from RelationOnToMany.RelationOneToMany import Module, Etudiant

nouveau_module = Module.create(nom="RO", note=20)
un_Etudiant = Etudiant(module=nouveau_module,
                       nom="mohamed elyaakoubi",
                       date_naissance=datetime.date(1988, 12, 1),
                       cne="1012982900")
un_Etudiant.save()

Etudiants = [{"module": nouveau_module,
              "nom": "Anas BARIK",
              "date_naissance": datetime.date(1990, 7, 31),
              "cne": "1012982901"
              },
             {"module": nouveau_module,
              "nom": "Youssef Mehdi",
              "date_naissance": datetime.date(1990, 7, 31),
              "cne": "1012982902"
              },
             {"module": nouveau_module,
              "nom": "naima elhafed",
              "date_naissance": datetime.date(1990, 7, 31),
              "cne": "1012982903"
              }]

for Etd in Etudiants:
    a = Etudiant(**Etd)
    a.save()

noms = ["Big Data", "Python", "BI"]
for nom in noms:
    module = Module.create(nom=nom)
    module.save()


if __name__ == "__main__":
    etds=Etudiant.select()

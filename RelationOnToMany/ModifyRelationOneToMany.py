from RelationOnToMany.RelationOneToMany import Etudiant, Module

module = Module.select().where(Module.nom == "Big Data").get()
print(module.nom)

# shortcut method
module = Module.get(Module.nom == "Big Data")
print(module.nom)

# change module name
module.nom = "Recherche Operationnelle"
module.save()

module = Module.get(Module.nom == "Recherche Operationnelle")
print(module.nom)
etd = Etudiant.get(Etudiant.nom == "Anas BARIK")
print(etd.nom)

etudiant = Etudiant.select().join(Module).where(
    (Etudiant.nom == "Anas BARIK") &
    (Module.nom == "RO")
).get()
etudiant.nom = "Abderrahim Bouhamidi"
etudiant.save()

etd = Etudiant.get(Etudiant.nom == "Abderrahim Bouhamidi")
print(etd.cne)

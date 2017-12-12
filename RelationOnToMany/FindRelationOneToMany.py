from RelationOnToMany.RelationOneToMany import Etudiant, Module

for etd in Etudiant.select():
    mod = Module.select().join(Etudiant).where(
        (Etudiant.nom == etd.nom)
    ).get()
    print(etd.nom)
    print(etd.cne)
    print(etd.date_naissance)
    print(mod.nom)

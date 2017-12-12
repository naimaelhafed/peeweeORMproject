from RelationOnToMany.RelationOneToMany import Etudiant

etd = Etudiant.get(Etudiant.nom == "Abderrahim Bouhamidi")
etd.delete_instance()




import peewee
import MySQLdb

# database = peewee.MySQLDatabase(MySQLdb.connect("localhost", "root", "", "TESTDB"))


database = peewee.SqliteDatabase("etd.db")


########################################################################
class Module(peewee.Model):
    """
    ORM model de la table Module
    """
    nom = peewee.CharField()
    note = peewee.IntegerField(null=True)

    class Meta:
        database = database


########################################################################
class Etudiant(peewee.Model):
    """
    ORM model de la table Etudiant
    """
    module = peewee.ForeignKeyField(Module)
    nom = peewee.CharField()
    date_naissance = peewee.DateTimeField()
    cne = peewee.CharField()

    class Meta:
        database = database


if __name__ == "__main__":
    try:
        Module.create_table()
    except peewee.OperationalError:
        print("table Module existe deja !")

    try:
        Etudiant.create_table()
    except peewee.OperationalError:
        print("table Etudiant existe deja !")
        #
        # try:
        #     peewee.create_model_tables([Module, Etudiant])
        # except peewee.OperationalError:
        #     print("tables existes deja !")

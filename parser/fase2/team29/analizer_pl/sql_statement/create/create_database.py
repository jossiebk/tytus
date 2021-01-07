from analizer_pl.abstract import instruction
from analizer_pl.statement.expressions import code
from analizer_pl.reports.Nodo import Nodo

class CreateDatabase(instruction.Instruction):
    """
    Clase que representa la instruccion CREATE DATABASE
    Esta instruccion es la encargada de crear una nueva base de datos en el DBMS
    """

    def __init__(self, replace, exists, name, owner, mode, row, column):
        instruction.Instruction.__init__(self, row, column)
        self.exists = exists
        self.name = name
        self.mode = mode
        self.owner = owner
        self.replace = replace

    def execute(self, environment):
        out = "fase1.execution("
        out += '"'
        out += "CREATE "
        out += self.replace
        out += " DATABASE "
        out += self.exists + " "
        out += self.name + " "
        out += self.owner + " "
        out += self.mode + ";"
        out += '")\n'
        return code.C3D(out, "create_db", self.row, self.column)
    def dot(self):
        return Nodo("SQL_INSTRUCTION:_CREATE_DATABASE")

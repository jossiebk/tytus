import re

from models.instructions.shared import Instruction
from models.database import Database
from controllers.type_checker import TypeChecker
from controllers.data_controller import DataController
from controllers.symbol_table import *

class CreateDB(Instruction):

    def __init__(self, properties, replace, noLine, noColumn):
        # if_not_exists:bool, id:str, listpermits: []
        self._properties = properties
        self._replace = replace
        self._noLine = noLine
        self._noColumn = noColumn

    def __repr__(self):
        return str(vars(self))

    def process(self, instrucction):
        typeChecker = TypeChecker()
        database = typeChecker.searchDatabase(self._properties['id'])

        if database:
            if self._properties['if_not_exists']:
                return

            if self._replace:
                typeChecker.deleteDatabase(database.name, self._noLine,
                                           self._noColumn)

        # TODO Verificar permisos y modo
        database = Database(self._properties['id'])
        typeChecker.createDatabase(database, self._noLine,
                                   self._noColumn)


class DropDB(Instruction):

    def __init__(self, if_exists, database_name, noLine, noColumn):
        self._if_exists = if_exists
        self._database_name = database_name
        self._noLine = noLine
        self._noColumn = noColumn

    def __repr__(self):
        return str(vars(self))

    def process(self, instrucction):
        typeChecker = TypeChecker()
        database = typeChecker.searchDatabase(self._database_name)

        if self._if_exists and not database:
            return

        typeChecker.deleteDatabase(self._database_name, self._noLine,
                                   self._noColumn)


class ShowDatabase(Instruction):

    def __init__(self, patherMatch):
        self._patherMatch = patherMatch

    def process(self, instrucction):
        databases = DataController().showDatabases()
        if self._patherMatch != None:
            if self._patherMatch.value[0] == '%' and self._patherMatch.value[-1] == '%':
                # Busca en cualquier parte
                pattern = rf"{self._patherMatch.value[1:-1].lower()}"
                databases = list(filter(lambda x: re.findall(pattern, x.lower()),
                                        databases))

            elif self._patherMatch.value[0] == '%':
                # Busca al final
                pattern = rf".{{0,}}{self._patherMatch.value[1:].lower()}$"
                databases = list(filter(lambda x: re.match(pattern, x.lower()),
                                        databases))

            elif self._patherMatch.value[-1] == '%':
                # Busca al inicio
                pattern = rf"{self._patherMatch.value[:-1].lower()}"
                databases = list(filter(lambda x: re.findall(pattern, x.lower()),
                                        databases))

            else:
                # Busca especificamente
                pattern = rf"{self._patherMatch.value.lower()}$"
                databases = list(filter(lambda x: re.match(pattern, x.lower()),
                                        databases))
        print(databases)  # TODO implementar en la vista a la vista

    def __repr__(self):
        return str(vars(self))


class AlterDatabase(Instruction):
    '''
        ALTER DATABASE recibe ya sea el nombre o el duenio antiguo y lo sustituye por un nuevo nombre o duenio
        si recibe un 1 es porque es la base de datos
        si recibe un 2 es porque es el duenio
    '''

    def __init__(self, alterType, oldValue, newValue):
        self._alterType = alterType
        self._oldValue = oldValue
        self._newValue = newValue

    def process(self, instrucction):
        pass

    def __repr__(self):
        return str(vars(self))


class UseDatabase(Instruction):
    '''
        Use database recibe el nombre de la base de datos que sera utilizada
    '''

    def __init__(self, dbActual):
        self._dbActual = dbActual

    def process(self,instrucction):
        typeChecker = TypeChecker()
        database = typeChecker.searchDatabase(self._dbActual)

        if database:
                SymbolTable()._useDatabase = database
                print(' ')
                print('----------> Base de datos seleccionada correctamente')
                print(' ')
                return

    def __repr__(self):
        return str(vars(self))

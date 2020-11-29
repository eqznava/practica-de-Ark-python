class Bioma:
    def __init__(self):
        self.__NombreBioma = ''
        self.__MantoAcuifero = True
        self.__Cuevas = True
        self.__Recursos = ''
        self.__RelieveDeBioma = ''
    def SetNombreBioma(self, nombrebioma):
        self.__NombreBioma = nombrebioma
    def SiMantoAcuifero(self):
        self.__MantoAcuifero = True
    def NoMantoAcuifero(self):
        self.__MantoAcuifero = False
    def MantoAcuifero(self):
        return self.__MantoAcuifero
    def SiCuevas(self):
        self.__Cuevas = True
    def NoCuevas(self):
        self.__Cuevas = False
    def Cuevas(self):
        return self.__Cuevas
    def SetRecursos(self, recursos):
        self.__Recursos = recursos
    def SetRelieveDeBioma(self, relieve):
        self.__RelieveDeBioma = relieve
    def MostrarBioma(self):
        print('\n--------------------------------------------------------------------------------------------------------\n')
        print('\tNombre de Bioma:',self.__NombreBioma,'\n')
        if self.MantoAcuifero():
            print('\tEncontraras gran cantidad de lagos, lagunas, cascadas, rios subterraneos y mas \(o_o)/ !\n')
        else:
            print('\t\(-.-)/ Lo lamento en este Bioma no encontraras ni gota de agua quizas si hace vas al centro de la tierra ^_^\n')
        if self.Cuevas():
            print('\tEncontraras gran cantidad de cavernas, cuevas, rios subterraneos y mas \(o_o)/ !\n')
        else:
            print('\t\(-.-)/ Lo lamento en este Bioma no encontraras ni un solo lugar para esconderte bajo tierra tendras que hacer tu trinchera ^_^\n')
        print('\tRecursos de este bioma:',self.__Recursos,'\n')
        print('\tRelieves de Bioma:',self.__RelieveDeBioma,'\n')
        print('\n--------------------------------------------------------------------------------------------------------')


class Arka(Bioma):
    def __init__(self):
        self.__Nombre = ''
        self.__Ambientes = ''
        self.__Supervivientes = 0
        self.__Artefactos = True
        self.__CriaturasRaras = ''
    def SetNombre(self, nombre):
        self.__Nombre = nombre
    def SetAmbientes(self, ambientes):
        self.__Ambientes = ambientes
    def SetSupervivientes(self, supervivientes):
        self.__Supervivientes = supervivientes
    def SiArtefactos(self):
        self.__Artefactos = True
    def NoArtefactos(self):
        self.__Artefactos = False
    def Artefactos(self):
        return self.__Artefactos
    def SetCriaturasRaras(self, criaturas):
        self.__CriaturasRaras = criaturas
    def MostrarArka(self):
        print('¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤\n')
        print('\tNombre del Arka:',self.__Nombre,'\n')
        print('\tAmbientes que podras encontrar:\n\n',self.__Ambientes,'\n')
        print('\tNumero de Supervivientes:',self.__Supervivientes,'\n')
        if self.Artefactos():
            print('\tEncontraras una gran cantidad de Artefactos en',self.__Nombre,'\n')
        else:
            print('\tEsta Arka no tiene artefactos \(-.-)/ !!','\n')
        print('\tCriaturas Raras:',self.__CriaturasRaras,'\n')
        self.MostrarBioma()
        print('\n¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤')

arka = Arka()
arka.SetNombre('Valguero')
arka.SetAmbientes('''\tArcoiris en el mapa.
     \tAuroras ocasionales por la noche.
     \tEstrellas fugaces por la noche.
     \tAire helado en el desierto nevado.
     \tUn océano subterráneo llamado The Abyss.
     \tLos cadáveres de Ichthyosaurus y Carbonemys esparcidos a lo largo del lago.
     \tTambién hay un bioma subterráneo llamado trinchera de aberraciones.''')
arka.SetSupervivientes(3)
arka.NoArtefactos()
arka.SetCriaturasRaras('Chalk Golem, Ice Golem y Deinonychus.')
arka.SetNombreBioma('White Cliffs')
arka.SiMantoAcuifero()
arka.NoCuevas()
arka.SetRecursos('Cristal, Obsidiana, Metal, Madera, Fibra, Frutillas, Sal, etc...')
arka.SetRelieveDeBioma('Montañas, LLanuras, Valles.')
arka.MostrarArka()

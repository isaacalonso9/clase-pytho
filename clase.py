class Materia:
    # precondiciones + postcondiciones de los casos de uso 
    # atributos: Encapsulacion
    __calificacion1 = 7.0
    __calificacion2 = 7.0
    __calificacion3 = 7.0
    __notaminima = 4
    __Calificacionfinal = 3.97

    # Metodos : 1 metodo por cada caso de uso 
    # def nombreCasoUso(self, parametros (precondiciones separadas con " ,")):
    def calcularCalificacionfinal(self,calificacion1,calificacion2,calificacion3,notaminima):
        self.__calificacion1 = calificacion1 
        self.__calificacion2 = calificacion2
        self.__calificacion3 = calificacion3
        self.__notaminima = notaminima 
        self.__Calificacionfinal = self.__(calificacion1 + self.calificacion2 + self.calificacion3/ 3)
        return self.__Calificacionfinal
 
 













   








        
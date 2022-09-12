"""calificar - An opinionated, minimal cookiecutter template for Python packages"""

__version__ = '1.0'
__author__ = 'Juan Carlos Lezama <jclezamap@gmail.com>'
__all__ = []


def Calificar( Integrante , Grupo , Respuestas, Taller="", Curso=None):
    import requests
    Respuestas2=""
    if Curso is None:
        Curso='0'
    if type(Respuestas.tolist()) == list:
        Respuestas2=';'.join(map(str, Respuestas))
    datos = {'Integrantes': Integrante, 'Grupo': Grupo,'Curso':Curso,'Respuestas':Respuestas2, 'python':1}
    resp = requests.post('https://economiafinanciera.com.co/?app=excel&modulo=taller&accion=respuestas&Actividad='+Taller, data=datos)
    return "Validación de Puntos:"+resp.text.split("|")[0]+"\r\nNota:"+resp.text.split("|")[1]+"\r\nMensaje:"+resp.text.split("|")[2][1:]    

def ValidacionPuntos( Integrante , Grupo , Respuestas, Taller="", Curso=None):
    import requests
    Respuestas2=""
    if Curso is None:
        Curso='0'
    if type(Respuestas.tolist()) == list:
        Respuestas2=';'.join(map(str, Respuestas))
    datos = {'Integrantes': Integrante, 'Grupo': Grupo,'Curso':Curso,'Respuestas':Respuestas2, 'python':1}
    resp = requests.post('https://economiafinanciera.com.co/?app=excel&modulo=taller&accion=respuestas&Actividad='+Taller, data=datos)
    return resp.text.split("|")[0].split(";")

from django.shortcuts import render

from .models import Alumno,Genero

# Create your views here.
class persona:
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
        super().__init__()

def index(request):
    hijo=persona("juan perez","7")


    lista=["lazaña","charquican","Porotos granados"]

    alumnos= Alumno.objects.all()


    context={"hijo":hijo,"nombre":"claudia andrea","comidas":lista,"alumnos":alumnos}

    return render(request, 'alumnos/index.html', context)          

def crud(request):
    alumnos = Alumno.objects.all()
    context = {"alumnos" :alumnos}
    return render(request, 'alumnos/alumnos_list.html', context)

def alumnosAdd(request):
    if  request.method is not "post":
        
        generos=Genero.objects.all()
        context={'generos':generos}
        return render(request, 'alumnos/alumnos_add.html', context)
    else:



        rut=request.POST["rut"]
        nombre=request.POST["nombre"]
        aPaterno=request.POST["paterno"]
        aMaterno=request.POST["materno"]
        fechaNac=request.POST["fechaNac"]
        genero=request.POST["genero"]
        telefono=request.POST["telefono"]
        email=request.POST["email"]
        direccion=request.POST["direccion"]
        activo="1"

        objGenero=Genero.objects.get(id_genero = genero)
        obj=Alumno.objects.create(  rut=rut,
                                    nombre=nombre,
                                    apellido_paterno=aPaterno,
                                    apellido_materno=aMaterno,
                                    fecha_nacimiento=fechaNac,
                                    id_genero=objGenero,
                                    telefono=telefono,
                                    email=email,
                                    direccion=direccion,
                                    activo=1 )
        obj.save()
        context={'mensaje':"OK, datos grabados..."}
        return render(request, 'alumnos/alumnos_add.html', context)

def alumnos_del(request,pk):
    context={}
    try:
        alumno=Alumno.objects.get(rut=pk)

        alumno.delete()
        mensaje="Bien, datos eliminados..."
        alumnos = Alumno.objects.all()
        context = {'alumnos': alumnos,  'mensaje' : mensaje}
        return render(request, 'alumnos/alumnos_list.html', context)
    except:
        mensaje="Error, rut no existe..."
        alumnos = Alumno.objects.all()
        context = {'alumnos': alumnos,  'mensaje' : mensaje}
        return render(request, 'alumnos/alumnos_list.html', context)

def alumnos_finEdit(request,pk):

    if pk != "":
        alumno=Alumno.objects.get(rut=pk)
        generos=Genero.objects.all()

        print(type(alumno.id_genero.genero))

        context={'alumno':alumno, 'generos':generos}
        if alumno:
            return render(request, 'alumnos/alumnos_edit.html', context)
        else:
            context={'mensaje':"Error, rut no existe..."}
            return render(request, 'alumnos/alumnos_list.html', context)
        

def alumnosUpdate(request):

    if request.method == "POST":


        rut=request.POST["rut"]
        nombre=request.POST["nombre"]
        aPaterno=request.POST["paterno"]
        aMaterno=request.POST["materno"]
        fechaNac=request.POST["fechaNac"]
        genero=request.POST["genero"]
        telefono=request.POST["telefono"]
        email=request.POST["email"]
        direccion=request.POST["direccion"]
        activo="1"

        objGenero=Genero.objects.get(id_genero = genero)

        alumno = Alumno()
        alumno.rut=rut
        alumno.nombre=nombre
        alumno.apellido_paterno=aPaterno
        alumno.apellido_materno=aMaterno
        alumno.fecha_nacimiento=fechaNac
        alumno.id_genero=objGenero
        alumno.telefono=telefono
        alumno.email=email
        alumno.direccion=direccion
        alumno.activo=1
        alumno.save()

        generos=Genero.objects.all()
        context={'mensaje':"Ok, datos actualizados...",'generos':generos,'alumno':alumno }
        return render(request, 'alumnos/alumnos_edit.html', context)
    else:

        alumnos = Alumno.objects.all()
        context={'alumnos':alumnos}
        return render(request, 'alumnos/alumnos_edit.html', context)
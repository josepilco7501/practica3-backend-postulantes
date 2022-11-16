from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Postulante
from .serializers import PostulanteSerializer

class IndexView(APIView):

    def get(self,request):
        context = {'mensaje':'servidor activo'}
        return Response(context)

class PostulantesView(APIView):

    def get(self,request):
        dataPostulantes = Postulante.objects.all()
        serPostulantes = PostulanteSerializer(dataPostulantes, many=True)
        return Response(serPostulantes.data)

    def post(self,request):
        serPostulante = PostulanteSerializer(data=request.data)
        serPostulante.is_valid(raise_exception=True)
        serPostulante.save()

        return Response(serPostulante.data)


class PostulanteDetailView(APIView):

    def get(self,request, postulante_id):
        dataPostulante = Postulante.objects.get(pk=postulante_id)
        serPostulante = PostulanteSerializer(dataPostulante)
        return Response(serPostulante.data)

    def put(self,request,postulante_id):
        dataPostulante = Postulante.objects.get(pk=postulante_id)
        serPostulante = PostulanteSerializer(dataPostulante, data=request.data)
        serPostulante.is_valid(raise_exception=True)
        serPostulante.save()
        return Response(serPostulante.data)

    def delete(self,request,postulante_id):
        dataPostulante = Postulante.objects.get(pk=postulante_id)
        serPostulante = PostulanteSerializer(dataPostulante)
        dataPostulante.delete()
        return Response(serPostulante.data)

    

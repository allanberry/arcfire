from django.http import Http404

from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response

from arcfire.models import Card


class CardSerializer(serializers.ModelSerializer):
    '''
    JSON serializer for Cards.
    '''

    class Meta:
        model = Card
        fields = (
            'pk', 'name', 'text',
            #'relations', 'locations',
            'keywords', 'properties', 'pictures', 'plans',
            'scale', 'text_format', 'sort_order')


class CardViewJson(APIView):
    '''
    Card in JSON format.
    '''
    def get_object(self, pk):
        try:
            return Card.objects.get(pk=pk)
        except Card.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        card = self.get_object(pk)
        serializer = CardSerializer(card)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        card = self.get_object(pk)
        serializer = CardSerializer(card, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        card = self.get_object(pk)
        card.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CardListViewJson(APIView):
    '''
    List of Cards in JSON format.
    '''
    def get(self, request, format=None):
        cards = Card.objects.all()
        serializer = CardSerializer(cards, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
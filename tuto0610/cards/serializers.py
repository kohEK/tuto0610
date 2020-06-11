from django.contrib.auth.models import User
from rest_framework import serializers

from cards.models import Card


class CardSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Card
        fields = ['owner', 'cardname', 'cardlimit']


class UserSerializer(serializers.ModelSerializer):
    cards = CardSerializer(many=True, source='card_set')
    # customer
    # product
    # customer.{product}_set.all()

    class Meta:
        model = User
        fields = ['username', 'cards']

    # u.card_set.all() 유저 인스턴스가 가져오는 카드가나옴]




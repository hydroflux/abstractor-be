from rest_framework import serializers
from .models import User, Document, Abstraction
from django.contrib.auth.hashers import make_password


class UserObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'name'
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'password',
            'email',
            'name'
        )
    
    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            password = make_password(validated_data['password']),
            email = validated_data['email'],
            name = validated_data['name'],
        )

        user.save()

        return user


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = (
            'id',
            'grantor',
            'grantee',
            'book',
            'page',
            'reception_number',
            'document_type',
            'recording_date',
            'legal',
            'related',
            'comment'
        )


class AbstractionSerializer(serializers.ModelSerializer):
    documents = DocumentSerializer(many=True)

    class Meta:
        model = Abstraction
        fields = (
            'id',
            'grantors',
            'grantees',
            'books',
            'pages',
            'reception_numbers',
            'document_types',
            'recording_dates',
            'legals',
            'related_documents',
            'comments'
        )
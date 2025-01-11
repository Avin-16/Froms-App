from rest_framework import serializers
from .models import *

class QuestionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question', 'required', 'question_type', 'choices', 'created_at', 'Updated_at']
        read_only_fields = ['created_at', 'Updated_at']

class ChoicesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Choices
        fields = ["id","choices"]
        read_only_fields = ['created_at', 'Updated_at']

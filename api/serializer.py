from .models import Words
from rest_framework import serializers


class WordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Words
        fields = [
            "id",
            "word_in_japanese",
            "translate_word",
            "sentence_in_japanese",
            "sentence",
            "part_of_speech",
            "last_update",
        ]

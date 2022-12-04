from .models import Words
from rest_framework import serializers


class WordsSerializer(serializers.ModelSerializer):
    part_of_speech = serializers.ChoiceField(
        source='get_part_of_speech_display',
        choices=Words.PARTH_OF_SPEECH_CATEGORIES,
        default=Words.IDK
    )

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

from django.contrib import admin
from .models import Words


# Register your models here.

@admin.register(Words)
class WordsAdmin(admin.ModelAdmin):
    list_display = (
        "word_in_japanese",
        "translate_word",
        "sentence_in_japanese",
        "sentence",
        "part_of_speech",
        "last_update",
    )

    list_filter = (
        "part_of_speech",
    )

    search_fields = [
        "word_in_japanese",
        "part_of_speech",
    ]

from django.db import models


# Create your models here.

class Words(models.Model):
    word_in_japanese = models.CharField(
        max_length=50,
        help_text="Enter a word in japanese",
        verbose_name='Japanese word'
    )

    translate_word = models.CharField(
        max_length=50,
        help_text="Enter the word translation",
        verbose_name="Word translated"
    )

    sentence_in_japanese = models.CharField(
        max_length=150,
        help_text="Enter a sentence in japanese",
        verbose_name="Japanese sentence",
        blank=True
    )

    sentence = models.CharField(
        max_length=250,
        help_text="Enter translation",
        verbose_name="Japanese the sentence translation",
        blank=True
    )

    ADJECTIVE = 'A'
    INTERJECTION = 'I'
    NOUN = 'N'
    PHRASE = 'P'
    QUANTIFIER = 'Q'
    VERB = 'V'
    IDK = 'IDK'
    PARTH_OF_SPEECH_CATEGORIES = [
        (ADJECTIVE, "Adjective"),
        (INTERJECTION, "Interjection"),
        (NOUN, "Noun"),
        (PHRASE, "Phrase"),
        (QUANTIFIER, "Quantifier"),
        (VERB, "Verb"),
        (NOUN, "Noun"),
        (IDK, "IDK"),
    ]
    part_of_speech = models.CharField(
        max_length=3,
        choices=PARTH_OF_SPEECH_CATEGORIES,
        default=IDK
    )

    last_update = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['part_of_speech']

from django.db import models


# Create your models here.

class Words(models.Model):
    word_in_japanese = models.CharField(
        max_length=50,
        help_text="Enter a word in Japanese",
        verbose_name='Japanese word'
    )

    has_kanji = models.BooleanField(
        help_text="Check if there is a kanji character in the word in Japanese",
        verbose_name="Kanji character in the word in Japanese",
        default=False
    )

    translate_word = models.CharField(
        max_length=50,
        help_text="Enter the word translation",
        verbose_name="Word translated"
    )

    sentence_in_japanese = models.CharField(
        max_length=150,
        help_text="Enter a sentence in Japanese with the word in Japanese",
        verbose_name="Japanese sentence",
        blank=True
    )

    sentence = models.CharField(
        max_length=250,
        help_text="Enter the sentence translation",
        verbose_name="Sentence translation",
        blank=True
    )

    ADJECTIVE = 'A'
    INTERJECTION = 'I'
    NOUN = 'N'
    PHRASE = 'P'
    QUANTIFIER = 'Q'
    VERB = 'V'
    OTHER = 'O'
    PARTH_OF_SPEECH_CATEGORIES = [
        (ADJECTIVE, "Adjective"),
        (INTERJECTION, "Interjection"),
        (NOUN, "Noun"),
        (PHRASE, "Phrase"),
        (QUANTIFIER, "Quantifier"),
        (VERB, "Verb"),
        (NOUN, "Noun"),
        (OTHER, "Other"),
    ]
    part_of_speech = models.CharField(
        max_length=3,
        choices=PARTH_OF_SPEECH_CATEGORIES,
        default=OTHER
    )

    last_update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.word_in_japanese}"

    class Meta:
        ordering = ['part_of_speech']
        verbose_name = 'words'
        verbose_name_plural = 'words'

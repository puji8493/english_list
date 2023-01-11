from django.db import models


class WordLists(models.Model):
    category = models.CharField('カテゴリー', max_length=50)
    ja_word = models.CharField('日本語', max_length=300)
    en_word = models.TextField()
    memo = models.TextField()

    def __str__(self):
        return '<WordLists ☆ id=' + str(self.id) + ',' + self.ja_word + ',' + self.en_word + ',' + self.memo + '>'

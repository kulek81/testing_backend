from django.db import models


class Variants(models.Model):
    variant_number = models.IntegerField("variantNumber")

    def __str__(self):
        return str(self.variant_number)


class Topics(models.Model):
    topic = models.CharField("topic", max_length=255)

    def __str__(self):
        return self.topic


class Questions(models.Model):
    variant_number = models.ForeignKey(Variants, on_delete=models.CASCADE, verbose_name="Variant")
    question_text = models.CharField("questionText", max_length=1000)
    topic = models.ForeignKey(Topics, on_delete=models.CASCADE, verbose_name="Topic")

    def __str__(self):
        return self.question_text


class Answers(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    right_answer = models.BooleanField("rightAnswer")
    answer_text = models.CharField("answerText", max_length=1000)

    def __str__(self):
        return self.answer_text

from django.db import models
from django.db.models import Index
from django.utils.translation import gettext_lazy as _


class Post(models.Model):
    title = models.CharField(_('title'), max_length=512, unique=True)
    summary = models.CharField(_('summary'), max_length=2000)
    main_image = models.URLField(_('main image'), max_length=1024, null=True, blank=True)
    date_posted = models.DateTimeField(_('date posted'))
    date_created = models.DateTimeField(_('date created'), auto_now_add=True)
    origin_id = models.PositiveIntegerField(_('origin id'))
    origin_url = models.URLField(_('origin url'), max_length=1024)

    agency = models.ForeignKey(
        'Agency',
        on_delete=models.PROTECT,
        related_name='posts',
        related_query_name='posts',
    )

    tags = models.ManyToManyField(
        to='Tag',
        through='PostTag',
        related_name='posts',
        related_query_name='posts'
    )

    category = models.ForeignKey(
        to='Category',
        on_delete=models.PROTECT,
        related_name='posts',
        related_query_name='posts'
    )


class Tag(models.Model):
    title = models.CharField(_('tag'), max_length=200)

    def __str__(self):
        return self.title


class PostTag(models.Model):
    post = models.ForeignKey(to=Post, on_delete=models.PROTECT)
    tag = models.ForeignKey(to=Tag, on_delete=models.PROTECT)

    class Meta:
        unique_together = ['post', 'tag']


class Category(models.Model):
    title = models.CharField(_('category'), max_length=200, unique=True)
    parent = models.ForeignKey(
        to='self',
        on_delete=models.PROTECT,
        related_name='sub_categories',
        related_query_name='sub_categories',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title


class Paragraph(models.Model):
    class Type(models.TextChoices):
        Text = 'text'
        Image = 'image'

    body = models.CharField(_('body'), max_length=5000)
    type = models.CharField(_('paragraph type'), max_length=10, choices=Type.choices)
    order = models.PositiveSmallIntegerField()

    post = models.ForeignKey(
        to='Post',
        on_delete=models.PROTECT,
        related_name='paragraphs',
        related_query_name='paragraphs'
    )


class Agency(models.Model):
    title = models.CharField(_('agency'), max_length=30)
    code = models.CharField(_('code'), max_length=25)

    class Meta:
        indexes = [Index(fields=['code'])]

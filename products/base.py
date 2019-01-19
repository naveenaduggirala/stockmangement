from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @classmethod
    def has_name(cls):
        return hasattr(cls, 'name')

    class Meta:
        abstract = True

    def __repr__(self):
        if hasattr(self, 'id'):
            return '%s-%s' % (self.__class__.__name__, self.id)
        else:
            return super(BaseModel, self).__repr__()

    @classmethod
    def get(cls, **kwargs):
        if isinstance(cls.objects, InheritanceManager):
            return cls.objects.get_subclass(**kwargs)
        else:
            return cls.objects.get(**kwargs)

    @classmethod
    def verbose_name(cls):
        return string.capwords(cls._meta.verbose_name)

    @classmethod
    def resolve_tag(cls):
        return cls._meta.verbose_name.replace(' ', '_')

    @classmethod
    def field_names(cls):
        return cls._meta.get_all_field_names()
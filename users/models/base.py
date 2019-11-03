from __future__ import unicode_literals

from django.db import models
from django.db.models.manager import EmptyManager
from django.db.models.query import RawQuerySet
from jsonschema import validate

from utils.constants import SerializerVersion


class BaseModelManager(models.Manager):
    ''' Fetch only active rows
    '''

    def get_queryset(self):
        return super(BaseModelManager, self).get_queryset().filter(deleted=False)


class BaseModelAllManager(models.Manager):

    def get_queryset(self):
        return super(BaseModelAllManager, self).get_queryset().all()


class BaseModel(models.Model):
    '''
        extended by all models
    '''
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    deleted_date = models.DateTimeField(null=True, blank=True)
    deleted = models.BooleanField(default=False)

    objects = BaseModelManager()
    all_objects = BaseModelAllManager()

    class Meta:
        abstract = True

    @staticmethod
    def serialize_to_json(data, version=SerializerVersion.V1, exclude=[]):
        if not data or isinstance(data, EmptyManager):
            return []

        if isinstance(data, models.QuerySet) or isinstance(data, RawQuerySet) or isinstance(data, list):
            # if many:
            response_data = []
            for obj in data:
                response_data.append(obj.to_json(version=version, exclude=exclude))
        else:
            response_data = data.to_json(version=version, exclude=exclude)

        return response_data

    @classmethod
    def validate(cls, kwargs, schema):
        """
        :param kwargs: dictionary to be validated
        :return: Boolean

        schema = {
            "type": "object",
            "properties": {
                "client_id": {"type": "number"},
                "sales_user_id": {"type": "number"},
                "phno": {"type": "string"},
                "device_id": {"type": "string"},
                "device_reg_id": {"type": "string"},
            },
            "required": ["client_id", "phno", "sales_user_id"]
        }
        """
        return validate(kwargs, schema)

    def update_obj(self, kwargs):
        """
        :param kwargs: contains all fields to be updated
        ForeignKey's need to be sent as id
        """
        key_list = []
        for key, value in kwargs.items():
            setattr(self, key, value)
            key_list.append(key)
        self.save(update_fields=key_list)
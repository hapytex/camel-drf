import inspect
from camel_drf.text import to_camel_data, to_snake_data

class CamelCaseSerializerMixin:
    def to_representation(self, *args, **kwargs):
        return to_camel_data(super().to_representation(*args, **kwargs))

    def to_internal_value(self, data):
        return super().to_internal_value(to_snake_data(data))


class CamelAPIViewMixin:
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        serializer = getattr(cls, 'serializer_class', None)
        if inspect.isclass(serializer) and not issubclass(serializer, CamelCaseSerializerMixin):
            # patch the serializer_class by making it a member of the CamelCaseSerializer
            cls.serializer_class = type(serializer.__name__, (CamelCaseSerializerMixin, serializer), {})
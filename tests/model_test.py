from polidoro_sqlite_utils import BaseModel
from polidoro_sqlite_utils.types import IntegerField, FloatField, TextField, DatetimeField, TimeField, DateField


class ModelTest(BaseModel):
    integer_field = IntegerField()
    float_field = FloatField()
    text_field = TextField()
    datetime_field = DatetimeField()
    time_field = TimeField()
    date_field = DateField()
    # foreignkey_field = ForeignKey()

    @classmethod
    def get(cls, pk):
        return ModelTest(id=pk)

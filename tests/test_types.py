from datetime import datetime, time, date

from polidoro_sqlite_utils.types import FloatField, TextField, IntegerField, DatetimeField, TimeField, DateField, \
    ForeignKey
from tests.model_test import ModelTest

_now = datetime.now()


def _assert_field_value_and_type(field, field_type, input_value, expected_value):
    value = field.parse(input_value)
    assert isinstance(value, field_type)
    assert expected_value == value


def test_float_field_parse():
    _assert_field_value_and_type(FloatField(), float, '1.006', 1.01)
    _assert_field_value_and_type(FloatField(precision=3), float, '1.006', 1.006)


def test_integer_field_parse():
    _assert_field_value_and_type(IntegerField(), int, '123', 123)


def test_text_field_parse():
    _assert_field_value_and_type(TextField(), str, 1.006, '1.006')


def test_datetime_field_parse():
    _assert_field_value_and_type(DatetimeField(), datetime, _now, _now)
    _assert_field_value_and_type(DatetimeField(), datetime, '2020-02-02 20:02:20', datetime(2020, 2, 2, 20, 2, 20))

    # with data format
    _assert_field_value_and_type(
        DatetimeField(format='%H:%M %d/%m/%y'), datetime, '4:5 1/2/03', datetime(2003, 2, 1, 4, 5)
    )

    # with dateutil parse arguments
    _assert_field_value_and_type(
        DatetimeField(dayfirst=True, null=True), datetime, '4:5 01-02-03', datetime(2003, 2, 1, 4, 5)
    )


def test_time_field_parse():
    _assert_field_value_and_type(TimeField(), time, _now.time(), _now.time())

    # with default format '%H:%M'
    _assert_field_value_and_type(TimeField(), time, '14:20', time(14, 20))

    # with different format
    _assert_field_value_and_type(TimeField(format='%M<>%H'), time, '20<>14', time(14, 20))


def test_date_field_parse():
    _assert_field_value_and_type(DateField(), date, _now.date(), _now.date())
    _assert_field_value_and_type(DateField(), date, '2020-02-02', datetime(2020, 2, 2).date())

    # with data format
    _assert_field_value_and_type(DateField(format='%d/%m/%y'), date, '1/2/03', datetime(2003, 2, 1).date())

    # with dateutil parse arguments
    _assert_field_value_and_type(DateField(dayfirst=True, null=True), date, '01-02-03', datetime(2003, 2, 1).date())


def test_foreignkey_field_parse():
    _assert_field_value_and_type(ForeignKey(ModelTest), ModelTest, ModelTest(id=1), ModelTest(id=1))
    _assert_field_value_and_type(ForeignKey(ModelTest), ModelTest, '1', ModelTest(id=1))

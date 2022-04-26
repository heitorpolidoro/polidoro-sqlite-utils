from datetime import datetime

from tests.model_test import ModelTest

_now = datetime.now()


def test_init_fields():
    test_model = ModelTest()
    for attribute in ['id', 'integer_field', 'float_field', 'text_field', 'datetime_field', 'time_field', 'date_field']:
        assert attribute in test_model.attributes, \
            f'Missing "{attribute}" in model: {list(test_model.attributes.keys())}'


def test_init_with_attributes():
    test_model = ModelTest(float_field=1.0, text_field='text', datetime_field=_now,
                           time_field=_now.time(), date_field=_now.date())

    assert 1.0 == test_model.float_field
    assert 'text' == test_model.text_field
    assert _now == test_model.datetime_field
    assert _now.time() == test_model.time_field
    assert _now.date() == test_model.date_field


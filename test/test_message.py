import datetime
from message import Message


def test_valid_create_message_obj():
    message = create_message_obj()

    assert message is not None
    assert message.user_id == "342342fsd"
    assert isinstance(message.time_to_send, datetime.datetime)
    assert isinstance(message.group_ids, list)


def test_invalid_create_message_obj():
    try:
        user_id_none = {"user_id": ""}
        create_message_obj(**user_id_none)
    except Exception as e:
        assert str(e) == "User Id is required."
    try:
        current_date = datetime.datetime.now().date()
        date_message = {"time_to_send": current_date}
        create_message_obj(**date_message)
    except Exception as e:
        assert str(e) == "Time to send is not in correct datetime format."


def create_message_obj(**kwargs) -> Message:
    date_time_val = create_datetime()
    dummy_data = {
        "user_id": "342342fsd",
        "group_ids": ["sdfds", "2131fsdf"],
        "message_data": "test data",
        "time_to_send": date_time_val,
    }
    dummy_data.update(kwargs)
    message = Message(**dummy_data)
    return message


def create_datetime() -> datetime.datetime:
    current_datetime = datetime.datetime.now()
    time_delta = datetime.timedelta(minutes=5)
    date_time_val = current_datetime + time_delta
    return date_time_val

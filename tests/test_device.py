from daikin_modbus import DaikinAidoo


def test_register_map_and_access() -> None:
    fields = DaikinAidoo.declared_fields
    assert set(fields) == {
        "power", "setpoint", "room_temperature", "hvac_mode", "fan_percentage",
        "louver", "available_modes", "available_speeds", "fan_speed",
        "slave_address", "baud_configuration", "parity_configuration",
    }
    assert fields["power"].writable is True
    assert fields["setpoint"].writable is True
    assert fields["hvac_mode"].writable is True
    assert fields["fan_speed"].writable is True
    for name in ("room_temperature", "fan_percentage", "louver", "available_modes", "available_speeds", "slave_address", "baud_configuration", "parity_configuration"):
        assert fields[name].writable is False


def test_temperature_encoding() -> None:
    field = DaikinAidoo.declared_fields["setpoint"]
    assert field.decode([720]) == 72.0
    assert field.decode([690]) == 69.0
    assert field.encode(74.0) == [740]


def test_numeric_values() -> None:
    assert DaikinAidoo.declared_fields["power"].decode([1]) == 1
    assert DaikinAidoo.declared_fields["fan_speed"].decode([0]) == 0
    assert DaikinAidoo.declared_fields["hvac_mode"].decode([2]) == 2

"""Register-backed Daikin/Airzone component."""

from modbus_connection.model import Component, gauge, integer, raw_register


class DaikinAidoo(Component):
    """Model the Daikin/Airzone Aidoo Modbus register interface.

    Addresses are zero-based Modbus register offsets as used by the existing
    working installation. Temperatures are exposed as Fahrenheit values.
    """

    register_ranges = ((0, 5), (14, 15), (54, 58))

    power = integer(0, signed=False, writable=True)
    """Power state: 0 off, 1 on."""

    setpoint = gauge(1, 0.1, signed=False, writable=True, unit="°F")
    """Temperature setpoint in degrees Fahrenheit."""

    room_temperature = gauge(2, 0.1, signed=False, unit="°F")
    """Measured room temperature in degrees Fahrenheit."""

    hvac_mode = integer(3, signed=False, writable=True)
    """HVAC mode using the device's numeric values."""

    fan_percentage = integer(4, signed=False, unit="%")
    """Reported fan percentage; read-only in this release."""

    louver = integer(5, signed=False)
    """Vertical louver mode; read-only until verified."""

    available_modes = raw_register(14)
    """Bitmask of supported HVAC modes; read-only."""

    available_speeds = raw_register(15)
    """Bitmask of supported fan speeds; read-only."""

    fan_speed = integer(54, signed=False, writable=True)
    """Numeric fan speed; 0 is automatic."""

    slave_address = integer(56, signed=False)
    """Configured Modbus slave address; read-only until verified."""

    baud_configuration = integer(57, signed=False)
    """Configured serial baud-rate code; read-only until verified."""

    parity_configuration = integer(58, signed=False)
    """Configured serial parity code; read-only until verified."""

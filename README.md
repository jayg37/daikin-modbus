# daikin-modbus

Standalone Python device library for the Daikin/Airzone Aidoo Modbus RTU register map.

The library models the device using `modbus-connection` and does not own the Modbus transport. Applications provide a `ModbusUnit`, allowing the same device model to be used with any supported Modbus backend.

## Scope

The initial model covers the complete documented register map used by this project. Registers verified during the original installation remain writable where tested. Registers that have not been tested are deliberately read-only in the library until field validation is completed.

Temperature values are represented in **degrees Fahrenheit** and use the device's x10 register encoding.

## Register map

| Register | Field | Encoding | Access in v0.1 |
|---:|---|---|---|
| 0 | power | 0=off, 1=on | read/write, verified |
| 1 | setpoint | °F × 10 | read/write, verified |
| 2 | room_temperature | °F × 10 | read-only, verified |
| 3 | hvac_mode | 1=auto, 2=cool, 3=heat, 4=fan, 5=dry | read/write, verified |
| 4 | fan_percentage | 0–100, 0=automatic | read-only |
| 5 | louver | 0–7, 8=auto, 9=swing, 10=swirl | read-only |
| 14 | available_modes | bit 0 auto, 1 cool, 2 heat, 3 fan, 4 dry | read-only |
| 15 | available_speeds | documented speed bitmask | read-only |
| 54 | fan_speed | 0=auto, 1,2,3... | read/write, verified |
| 56 | slave_address | Modbus address | read-only |
| 57 | baud_configuration | 8=19200 | read-only |
| 58 | parity_configuration | 2=even | read-only |

## Example

```python
from modbus_connection.model import Component
from daikin_modbus import DaikinAidoo

# `unit` is supplied by the application.
device = DaikinAidoo(unit)
await device.async_update()
print(device.room_temperature)
print(device.setpoint)
await device.write("setpoint", 74.0)
```

The device model contains no Home Assistant code.

## Development

```bash
uv sync
uv run pytest
uv run ruff check .
uv run ruff format --check .
```

See `docs/register-map.md` for implementation notes and verification status.

## License

Apache-2.0

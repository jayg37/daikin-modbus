# Register map and validation status

The model is based on the working Daikin/Airzone Modbus implementation in `Daikin_modbus_communication`.

## Serial protocol

- Modbus RTU
- 19200 baud
- 8 data bits
- Even parity
- 1 stop bit
- Unit/slave ID 1 in the tested installation
- Holding-register reads use function 03
- Writes use holding-register writes

## Validation policy

Registers 0, 1, 2, 3, and 54 were exercised during the original project. Those fields are writable where write behavior was confirmed. Registers 4, 5, 14, 15, 56, 57, and 58 are represented in the model but are read-only in version 0.1.0.

This is intentional: documenting a register does not prove that writing it is safe on every Aidoo firmware version.

## Verified observations

- Register 0 returned `1` when the HVAC was on.
- Register 1 returned `720` for a 72°F target.
- Register 2 returned `690` for a 69°F room temperature.
- Register 3 returned `2` for cooling and `3` for heating.
- Writing register 1 with `740` changed the target to 74°F.
- Register 54 is the numeric fan-speed control and `0` represents automatic speed.

## Unverified fields

Register 4 reports fan percentage, register 5 reports louver state, registers 14 and 15 report capabilities, and registers 56–58 expose serial configuration. These are currently read-only until a live installation confirms both semantics and safe write behavior where applicable.

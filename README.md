# TimeTune

TimeTune is a Python program designed to enhance system clock synchronization features and offer time management tools for Windows devices. It allows users to synchronize their system clocks, manage time zones, and simulate time adjustments by adding time offsets.

## Features

- **System Clock Synchronization:** Synchronize your system clock with internet time servers.
- **Timezone Management:** Set and manage the system timezone.
- **Current Time Display:** Display the current system time.
- **Time Offset Simulation:** Simulate time changes by adding hours and minutes to the current time.
- **Toggle Time Synchronization:** Enable or disable automatic time synchronization.

## Installation

To use TimeTune, ensure you have the following:

- Python 3.x installed on your Windows device.
- Administrator privileges to execute system time-related commands.

## Usage

1. **Synchronize System Clock:**

   ```bash
   python timetune.py
   ```

   This will synchronize your system clock with an internet time server.

2. **Set Timezone:**

   Modify the `set_timezone` method in the code or call it directly with a desired timezone string (e.g., 'UTC', 'Pacific Standard Time').

3. **Add Time Offset:**

   Use the `add_time_offset` method to simulate time changes by adding hours and minutes.

4. **Toggle Time Synchronization:**

   Use the `toggle_time_sync` method to enable or disable time synchronization.

## Note

- TimeTune is specifically designed for Windows devices and uses Windows-specific commands.
- Ensure you run the program with administrative privileges to allow system clock adjustments.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
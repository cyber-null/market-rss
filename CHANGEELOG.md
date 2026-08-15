# Changelog

All notable changes to this project are documented in this file.

## [Unreleased]

### Added

- Added centralized application configuration in `app/config.py`.
- Added environment variable support for:
  - `MARKET_SYMBOLS`
  - `QUOTE_CURRENCY`
  - `UPDATE_INTERVAL`
  - `APP_HOST`
  - `APP_PORT`
  - `LOG_LEVEL`
- Added debug logging messages to the worker.

### Changed

- Updated the worker to use environment-based configuration.
- Added price number formatting for RSS output.
- Updated application and worker logging messages.

### Refactored

- Refactored application configuration to use environment variables.
- Refactored RSS price formatting for improved readability.

### Chore

- Removed temporary `print()` calls from the Flask server.
- Updated logging messages in the application and worker.

---
> writed by AI :)
> because i lazy :)

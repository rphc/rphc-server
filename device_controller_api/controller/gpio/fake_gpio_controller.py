from typing import List, Any, Tuple

from device_controller_api.controller.gpio.gpio_controller import GPIOController, PowerLevel, PinConfig


class FakeGPIOController(GPIOController):

    def configure_pin(self, pin: int, config: PinConfig):
        pass

    def read(self, pin: int):
        pass

    def write(self, pin: int, level: int):
        pass

    def spi_open(self, channel: int, boud: int, flags: int) -> Any:
        pass

    def spi_close(self, handle: Any):
        pass

    def spi_write(self, spi_handle: Any, data: List[int]):
        pass

    def create_wave(self, pin: int, data: List[Tuple[PowerLevel, int]]):
        pass

    def clear_waves(self):
        pass

    def send_wave_chain(self, data):
        pass

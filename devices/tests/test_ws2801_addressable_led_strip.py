from django.test import TestCase

from devices.models import PiGPIO, \
    WS2801AddressableLedStrip


class AddressableLEDStripTestCase(TestCase):

    def setUp(self):
        self.controller = PiGPIO.objects.create(name="controller", hostname="localhost", port=8888)

    def test_create_addressable_led_strip(self):
        try:
            WS2801AddressableLedStrip.objects.create(gpio_controller=self.controller,
                                                     name="Addressable LED Strip",
                                                     spi_channel=0,
                                                     spi_frequency=1000,
                                                     total_led_count=160,
                                                     usable_led_count=89)
        except Exception as e:
            self.fail(e)

    def test_addressable_led_strip_str(self):
        led_strip = WS2801AddressableLedStrip.objects.create(gpio_controller=self.controller,
                                                             name="Addressable LED Strip",
                                                             spi_channel=0,
                                                             spi_frequency=1000,
                                                             total_led_count=160,
                                                             usable_led_count=89)

        self.assertEqual(str(led_strip), "WS2801 Addressable LED Strip (Addressable LED Strip)")

#!/usr/bin/env python

from LedMatrixString import LedMatrixString
from Wheel import Wheel
from bluepy.btle import Scanner, UUID, DefaultDelegate, Peripheral, BTLEException
import itertools
import struct
import sys
import time
import pigpio
if sys.version_info >= (3, 0):
    from functools import reduce


###### CONFIGURE THIS ######

# The Pins. Use Broadcom numbers.
RED_PIN = 17
GREEN_PIN = 22
BLUE_PIN = 27


class Strip():

    def __init__(self, pi):
        self.pi = pi
        self.isEnabled = False
        self.color = 0
        self.r = 0
        self.g = 0
        self.b = 0
        self.a = 255

    def turnOff(self):
        # Turn off all colors
        self.setLights(0, 0, 0, 0)

    def setLights(self, red, green, blue, brightness):
        # Brightness has to be between 0 and 1
        realBrightness = float(brightness) / 255.0

        # Configurate Pi pins
        self.pi.set_PWM_dutycycle(RED_PIN, red * realBrightness)
        self.pi.set_PWM_dutycycle(GREEN_PIN, green * realBrightness)
        self.pi.set_PWM_dutycycle(BLUE_PIN, blue * realBrightness)

    def updateColor(self, currentValue, newValue):
        # Add new value to current value
        currentValue += newValue

        # Shouldn't be higer then 255 or less then 0
        if currentValue > 255:
            return 255
        if currentValue < 0:
            return 0

        return currentValue

    def updateColorValue(self, value):
        retValue = 0

        if value < 0:
            value = -7
        else:
            value = 7

        # Update red color
        if self.color == 0:
            self.r = self.updateColor(self.r, value)
            retValue = self.r

        # Update green color
        if self.color == 1:
            self.g = self.updateColor(self.g, value)
            retValue = self.g

        # Update blue color
        if self.color == 2:
            self.b = self.updateColor(self.b, value)
            retValue = self.b

        # Update alpha / brightness
        if self.color == 3:
            self.a = self.updateColor(self.a, value)
            retValue = self.a

        # Set the new color
        self.setLights(self.r, self.g, self.b, self.a)

        return retValue

    def setColorValues(self, r, g, b):
        # Update red color
        self.r = r

        if self.r > 255:
            self.r = 255
        elif self.r < 0:
            self.r = 0

        # Update green color
        self.g = g

        if self.g > 255:
            self.g = 255
        elif self.g < 0:
            self.g = 0

        # Update blue color
        self.b = b

        if self.b > 255:
            self.b = 255
        elif self.b < 0:
            self.b = 0

        # Set the new color
        self.setLights(self.r, self.g, self.b, self.a)

    def switch(self):
        # Turn off if currently enabled
        if self.isEnabled:
            self.turnOff()
        else:
            # Otherwise turn on
            self.setLights(self.r, self.g, self.b, self.a)

        # Change enabled value
        self.isEnabled = not self.isEnabled

        return self.isEnabled


class NuimoDelegate(DefaultDelegate):

    def __init__(self, nuimo, strip):
        DefaultDelegate.__init__(self)
        self.nuimo = nuimo
        self.strip = strip

    def handleNotification(self, cHandle, data):
        if int(cHandle) == self.nuimo.characteristicValueHandles['BATTERY']:
            self.onBattery(ord(data[0]))
        elif int(cHandle) == self.nuimo.characteristicValueHandles['FLY']:
            self.onFly(ord(data[0]), ord(data[1]))
        elif int(cHandle) == self.nuimo.characteristicValueHandles['SWIPE']:
            self.onSwipe(ord(data[0]))
        elif int(cHandle) == self.nuimo.characteristicValueHandles['ROTATION']:
            value = ord(data[0]) + (ord(data[1]) << 8)
            if value >= 1 << 15:
                value = value - (1 << 16)
            self.onRotate(value)
        elif int(cHandle) == self.nuimo.characteristicValueHandles['BUTTON']:
            self.onButton(ord(data[0]))

    def onBattery(self, batteryState):
        # Nothing to do here
        pass

    def onFly(self, direction, value):
        # Nothing to do here
        pass

    def onSwipe(self, direction):
        # Set color to change
        self.strip.color = direction

        # Swipe to choose for color to change
        if direction == 0:
            self.nuimo.displayLedMatrix(self.nuimo.ledStrings.getR(), 5)
            self.nuimo.displayLedMatrix(
                self.nuimo.ledStrings.getColorBar(self.strip.r), 255)
        if direction == 1:
            self.nuimo.displayLedMatrix(self.nuimo.ledStrings.getG(), 5)
            self.nuimo.displayLedMatrix(
                self.nuimo.ledStrings.getColorBar(self.strip.g), 255)
        if direction == 2:
            self.nuimo.displayLedMatrix(self.nuimo.ledStrings.getB(), 5)
            self.nuimo.displayLedMatrix(
                self.nuimo.ledStrings.getColorBar(self.strip.b), 255)
        if direction == 3:
            self.nuimo.displayLedMatrix(self.nuimo.ledStrings.getA(), 5)
            self.nuimo.displayLedMatrix(
                self.nuimo.ledStrings.getColorBar(self.strip.a), 255)

    """def onRotate(self, value):
        print ('rotate', value)
        # Update value
        newValue = self.strip.setColorValue(value)
        bar = self.ledStrings.getColorBar(newValue)

        if bar != self.nuimo.lastBar:
            # Show on matrix
            self.nuimo.displayLedMatrix(bar, 255)
            self.nuimo.lastBar = bar"""

    def onRotate(self, value):
        if value < 0:
            self.nuimo.rotateAngle -= 7
        else:
            self.nuimo.rotateAngle += 7

        self.nuimo.rotateAngle = self.nuimo.rotateAngle % 360

        colorAtAngle = self.nuimo.wheel.getColorAtAngle(self.nuimo.rotateAngle)
        newValue = self.strip.setColorValues(
            colorAtAngle[0], colorAtAngle[1], colorAtAngle[2])

    def onButton(self, pressState):
        # On press 1 and 0 will be fired on the emulator
        if pressState == 1:
            # Turn on or off
            if self.strip.switch():
                self.nuimo.displayLedMatrix(self.nuimo.ledStrings.getOn(), 2)
            else:
                self.nuimo.displayLedMatrix(self.nuimo.ledStrings.getOff(), 2)


class Nuimo:

    SERVICE_UUIDS = [
        UUID('0000180f-0000-1000-8000-00805f9b34fb'),  # Battery
        UUID('f29b1525-cb19-40f3-be5c-7241ecb82fd2'),  # Sensors
        UUID('f29b1523-cb19-40f3-be5c-7241ecb82fd1')  # LED Matrix
    ]

    CHARACTERISTIC_UUIDS = {
        UUID('00002a19-0000-1000-8000-00805f9b34fb'): 'BATTERY',
        UUID('f29b1529-cb19-40f3-be5c-7241ecb82fd2'): 'BUTTON',
        UUID('f29b1528-cb19-40f3-be5c-7241ecb82fd2'): 'ROTATION',
        UUID('f29b1527-cb19-40f3-be5c-7241ecb82fd2'): 'SWIPE',
        UUID('f29b1526-cb19-40f3-be5c-7241ecb82fd2'): 'FLY',
        UUID('f29b1524-cb19-40f3-be5c-7241ecb82fd1'): 'LED_MATRIX'
    }

    NOTIFICATION_CHARACTERISTIC_UUIDS = [
        #'BATTERY', # Uncomment only if you are not using the iOS emulator (iOS does't support battery updates without authentication)
        'BUTTON',
        'ROTATION',
        'SWIPE',
        'FLY']

    # Notification data
    NOTIFICATION_ON = struct.pack("BB", 0x01, 0x00)
    NOTIFICATION_OFF = struct.pack("BB", 0x00, 0x00)

    def __init__(self, macAddress):
        self.macAddress = macAddress
        self.wheel = Wheel(50)
        self.ledStrings = LedMatrixString()
        self.lastBar = ""
        self.rotateAngle = 0

    def set_delegate(self, delegate):
        self.delegate = delegate

    def connect(self):
        self.peripheral = Peripheral(self.macAddress, addrType='random')
        # Retrieve all characteristics from desires services and map them from
        # their UUID
        characteristics = list(itertools.chain(
            *[self.peripheral.getServiceByUUID(uuid).getCharacteristics() for uuid in Nuimo.SERVICE_UUIDS]))
        characteristics = dict((c.uuid, c) for c in characteristics)
        # Store each characteristic's value handle for each characteristic name
        self.characteristicValueHandles = dict((name, characteristics[uuid].getHandle(
        )) for uuid, name in Nuimo.CHARACTERISTIC_UUIDS.items())
        # Subscribe for notifications
        for name in Nuimo.NOTIFICATION_CHARACTERISTIC_UUIDS:
            self.peripheral.writeCharacteristic(self.characteristicValueHandles[
                                                name] + 1, Nuimo.NOTIFICATION_ON, True)
        self.peripheral.setDelegate(self.delegate)

    def waitForNotifications(self):
        self.peripheral.waitForNotifications(1.0)

    def displayLedMatrix(self, matrix, timeout, brightness=1.0):
        matrix = '{:<81}'.format(matrix[:81])
        bytes = list(map(lambda leds: reduce(lambda acc, led: acc + (1 << led if leds[led] not in [
                     ' ', '0'] else 0), range(0, len(leds)), 0), [matrix[i:i + 8] for i in range(0, len(matrix), 8)]))
        self.peripheral.writeCharacteristic(self.characteristicValueHandles['LED_MATRIX'], struct.pack('BBBBBBBBBBBBB', bytes[0], bytes[1], bytes[2], bytes[3], bytes[
                                            4], bytes[5], bytes[6], bytes[7], bytes[8], bytes[9], bytes[10], max(0, min(255, int(255.0 * brightness))), max(0, min(255, int(timeout * 10.0)))), True)


def connect(strip, scanTimeout=2, reconnectAttempts=1, maxAttempts=10):
    # Max attempts reached
    if reconnectAttempts > maxAttempts:
        print("Failed to connect after %d attempts" % maxAttempts)
        return

    try:
        # Scanning for devices
        print("Scanning for devices (%d / %d)" %
              (reconnectAttempts, maxAttempts))
        scanner = Scanner()
        devices = scanner.scan(scanTimeout)

        for device in devices:
            # Only connect to Nuimos
            if device.connectable and device.getValueText(9) == "Nuimo":
                # Init Nuimo class
                nuimo = Nuimo(device.addr)
                nuimo.set_delegate(NuimoDelegate(nuimo, strip))

                # Connect to Nuimo
                print("Trying to connect to %s." % device.addr)

                nuimo.connect()
                nuimo.displayLedMatrix(LedMatrixString().getRaspberry(), 5)

                print("Connected successfully to %s." % device.addr)
                # Reset reconnect attempts on successfull connect
                reconnectAttempts = 0

                while True:
                    nuimo.waitForNotifications()
                return

        # Found no Nuimo
        print("Couldn't find a Nuimo.")
        connect(strip, scanTimeout + 1, reconnectAttempts + 1)
    except BTLEException:
        print("Failed to connect to %s. Make sure to:\n  1. Run program as root (For Scanning and the Strip)\n  2. Disable the Bluetooth device: hciconfig hci0 down\n  3. Enable the Bluetooth device: hciconfig hci0 up\n  4. Enable BLE: btmgmt le on\n" % nuimo.macAddress)
        connect(strip, scanTimeout + 1, reconnectAttempts + 1)
    except KeyboardInterrupt:
        print("Program aborted.")
        return

if __name__ == "__main__":
    strip = Strip(pigpio.pi())

    print("Press Ctrl+C to cancel.")
    connect(strip)

    strip.turnOff()

# Water Sensor Valve
 This project mimics the operation of a "Water Cop". While commercial use of this device is expensive, a simple cheap clone can be replicated for a mere dollars.
 
## Water Sensor
The water sensor is a simple wheatstone bridge with one leg of the resistor divider being the exposed metal strips in the probe. Due to variation in the installation of the product, the probe's resistivity will change. Using a wide variety of different possible probe gaps, the wheatstone bridge is configurable for up to 15 different resistor combinations. See "total_resistor_combinations.txt" for all possible combinations. The purpose of this configuration is to accomodate for a wide range of possible probe resistivities. 

This device is meant to be used with a probe with a small 2mm gap, which when submerged in conductive water yields a theoretical maximum resistivity of ~360 Ohms. Since this resistance is excluding the resistance of the probe's wire, tolerances must be added. In this scenario, we would recommend using a setting of 562.5 Ohms which corresponds to jumping resistors 3, 4 and 5. At this set point, any measured resistance below the threshold of 562.5 Ohms will trigger the closing of the valve and sounding of the alarm.

Adjustments may be needed for more sensitivity or security. For more sensitivity, refer to the resistor combination file and choose the next highest setting. For more security,  choose the next lowest setting. Continue to do so until the desired operation is achieved. 

## Custom Setting Attachment
This add-on is a customizable attachment that is configurable with either the use the included potentiometer or the solderable resistor footprint. With the included mosfet, an external controller can be attached and control the Water Sensor Valve using the connections with the use of the included external mosfet.

- [ ] Simulate custom setting attachment
- [ ] Control device with custom setting attachment using MCU
- [ ] Setup configurable custom setting attachement using potentiometer

# Water Sensor Valve
 This project mimics the operation of a "Water Cop". While commercial use of this device is expensive, a simple cheap clone can be replicated for a mere dollars.
 
## Water Sensor
The water sensor is a simple wheatstone bridge with one leg of the resistor divider being the exposed metal strips in the probe. Due to variation in the installation of the product, the probe's resistivity will change. Using a wide variety of different possible probe gaps, the wheatstone bridge is configurable for up to 15 different resistor combinations. See [total_resistor_combinations.txt](https://github.com/TannerHollis/Water_Sensor_Valve/blob/main/Water_Valve_Calculations/total_resistor_combinations.txt) for all possible combinations. The purpose of this configuration is to accomodate for a wide range of possible probe resistivities.

A "dirty" or water typically found with contamination in it widely varies in it's resistivity, or it's ability to conduct electricity. Since the resistivity of air is magnitudes larger than the resistivity of water, the effect on the probes open air contacts can be ignored for the theoretical calculations. 

Contaminated water has a resitivity typically between 20 to 2000 Ohms. To calculate the theoretical resistance between two electrical wires submerged in water, one must utilize the resistance formula.

	R = p L / A
 
This device is meant to be used with a probe with a small 2mm gap and approximately 31um^2 of exposed contacts on the probe, which when submerged in conductive water yields a theoretical maximum resistance of ~127 kOhms. Tolerances must be added to assure the proper resistivity is measured. In this scenario, we would recommend using a setting of 84.777 kOhms which corresponds to jumping resistors R3 and R4 corresponding to 127 and 255 kOhm resistors. At this set point, any measured resistance below the threshold of 84.777 kOhms will trigger the closing of the valve and sounding of the alarm.


Adjustments may be needed for more sensitivity or security. For more sensitivity, refer to the resistor combination file and choose the next highest setting. For more security,  choose the next lowest setting. Continue to do so until the desired operation is achieved. 

## Custom Setting Attachment
This add-on is a customizable attachment that is configurable with either the use the included potentiometer or the solderable resistor footprint. With the included mosfet, an external controller can be attached and control the Water Sensor Valve using the connections with the use of the included external mosfet.

- [X] Test and verify first revision
- [X] Verify alarm and valve operation
- [ ] Create custom setting attachment
- [ ] Control device with custom setting attachment using MCU
- [ ] Setup configurable custom setting attachement using potentiometer

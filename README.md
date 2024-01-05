# Getting a PWM fan running on a Ubuntu Raspberry Pi 4
Collection of scripts to control the PWM fan speed on my Ubuntu 22.04 Raspberry Pi 4. Details of the PWM fan case and also sample demo Python scripts I used as a base can we found on the [PI4-FAN-PWM](https://www.waveshare.com/wiki/PI4-FAN-PWM) Wiki page. To create the actual service creation part I drew insparation from a [medium.com article](https://medium.com/codex/setup-a-python-script-as-a-service-through-systemctl-systemd-f0cc55a42267)

Note: I know thsi is not the most efficient code and will optimise it when I have some more time. 


**Creating the relevant Python script on your Raspberry Pi**

1. Create a scripts folder, in my case it is under the `/home/$USER/` folder.
   ```
   mkdir scripts
   ```
2. Change to the scripts folder and then create a fan_service.py file and dump the contents of the fan_service.py file
   ```
   cd scripts
   vi fan_service.py
   ```
3. You will also install the relevant Python Raspberry Pi GPIO dependancies using [pip](https://pypi.org/project/pip/)
   ```
   sudo apt update
   pip install RPi.GPIO
   pip install gpiozero
   ```

4. The you should be ready to test the script. If you want to see the actual temrature and current fan speed make sure to uncomment the each `# print` line in the `fan_service.py` file
   ```
   sudo python fan_service.py
   ```

**Now lets create a service**
1. Now create the service so that the script automaticall starts on reboot and no manual intervention is needed. Make sure you copy over the contents of the `fan.service` file that is part of this repo. Make sure to replace the `$USER` attrivute with your username where the script is stored 
   ```
   sudo nano /etc/systemd/system/fan.service 
   ```
2. Now we need to reload the daemon
   ```
   sudo systemctl daemon-reload
   ```
3. Let’s enable enable the service
   ```
   sudo systemctl enable fan.service
   ```
4. Starting the service.
   ```
   sudo systemctl start fan.service
   ```

**Other userful service commands**
There are several commands you can do to start, stop, restart, and check status.

1. To stop the service.
   ```
   sudo systemctl stop fan.service
   ```
2. To restart.
   ```
   sudo systemctl restart fan.service
   ```
3. To check status.
   ```
   sudo systemctl status fan.service
   ```

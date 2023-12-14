# rPi-fan
Collection of scripts to control fan speed of a Ubuntu Raspberry Pi 4


https://medium.com/codex/setup-a-python-script-as-a-service-through-systemctl-systemd-f0cc55a42267


Cretae a scripts folder
mkdir scripts

Change to the scripts folder and then create a fan_service.py file and dump the contents of the fan_service.py file
cd scripts
vi fan_service.py

Create the service 
sudo nano /etc/systemd/system/fan.service 
and create the contents of the fan.service file

Now we need to reload the daemon.

sudo systemctl daemon-reload
Let’s enable our service so that it doesn’t get disabled if the server restarts.

sudo systemctl enable fan.service
And now let’ start our service.

sudo systemctl start fan.service

There are several commands you can do to start, stop, restart, and check status.

To stop the service.

sudo systemctl stop fan.service
To restart.

sudo systemctl restart fan.service
To check status.

sudo systemctl status fan.service
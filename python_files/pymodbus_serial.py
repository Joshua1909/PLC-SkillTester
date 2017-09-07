#!/usr/bin/env python
#---------------------------------------------------------------------------# 
# Import the various server implementations
#---------------------------------------------------------------------------# 
#from pymodbus.client.sync import ModbusTcpClient as ModbusClient
#from pymodbus.client.sync import ModbusUdpClient as ModbusClient
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
#---------------------------------------------------------------------------# 
# Configure the client logging
#---------------------------------------------------------------------------# 
import logging
logging.basicConfig()
log = logging.getLogger()
#log.setLevel(logging.DEBUG)
#
#---------------------------------------------------------------------------# 
# Choose the client you want
#---------------------------------------------------------------------------# 
# Here is an example of using these options::
#    client = ModbusClient('localhost', retries=3, retry_on_empty=True)
#    client = ModbusClient(method='ascii', port='/dev/pts/2', timeout=1)
#    client = ModbusClient(method='rtu', port='/dev/ttyACM0', timeout=1)
#    client.connect()
#---------------------------------------------------------------------------# 
#
#Read registers on PLC and print register 0
with ModbusClient(method='rtu', port='COM3', timeout=1) as client:
    result = client.read_holding_registers(0, 8, unit=0x01)
    print ("Executing PLC.py)
    print ("Reading Machine State")       
    print ("Machine State =", result.registers[0])
#
#Write state 0 to PLC register 0. Format is "register, state"
with ModbusClient(method='rtu', port='COM3', timeout=1) as client:
    client.write_register(0, 0, unit=0x01)
	print ("Sending Machine to State 0")
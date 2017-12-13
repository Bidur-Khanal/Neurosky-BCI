#!/usr/bin/env python
# encoding: utf-8


# external imports
# threading stuff
from queue import Queue
from threading import Thread, Event
# networking stuff
from socket import *
# misc.
import json
import time

# these are used as default parameters for the classes in this module. They come from the default
# factory settings on the MindWave brand of headsets.
# TODO: move these into a configuration file
HOST = '127.0.0.1'
PORT = 13854
ADDR = (HOST, PORT)
APP_NAME = 'Brain Data'
USER_NAME = 'Bidur'

# this is sent to the ThinkGearConnector to configure it to output json data
headset_conf_dict = {'enableRawOutput': True, 'format': 'Json'}
# this is the character used by ThinkGearConnector to separate JSON objects
HEADSET_JSON_SEPARATOR = '\r'

# this is the data that the ThinkGearConnector sends out
brain_parameters = (lowAlpha, highAlpha, lowBeta, highBeta,
    lowGamma, highGamma, delta, theta,poorSignalLevel,meditation, attention) = ('lowAlpha', 'highAlpha', 'lowBeta', 'highBeta',
    'lowGamma', 'highGamma', 'delta', 'theta','poorSignalLevel','meditation', 'attention')

rawEeg='rawEeg'


#poorSignalLevel='poorSignalLevel'



# these are the two general categories of brainwave data
parameter_categories = (eSense, eegPower) = ('eSense', 'eegPower')
blinkStrength='blinkStrength'

# this is what data gets sent by the ThinkGearConnector before the headset connects
NULL_DATA = {poorSignalLevel: 200}


'''def _extract_rawtuple(data_dict):
    """Returns a tuple of the values extracted from a message dictionary."""
    return (
        data_dict[rawEeg])'''


def _extract_tuple(data_dict):
    """Returns a tuple of the values extracted from a message dictionary."""
    return (
        data_dict[eegPower][lowAlpha],
        data_dict[eegPower][highAlpha],
        data_dict[eegPower][lowBeta],
        data_dict[eegPower][highBeta],
        data_dict[eegPower][lowGamma],
        data_dict[eegPower][highGamma],
        data_dict[eegPower][delta],
        data_dict[eegPower][theta],
        data_dict[poorSignalLevel],
        data_dict[eSense][meditation],
        data_dict[eSense][attention])


def _datastream(check_continue_func, host=HOST, port=PORT):
    """Create a generator that will yield the data messages being sent by the ThinkGearConnector. """
    cs = socket(AF_INET, SOCK_STREAM)
    cs.connect((host, port))
    cs.send(json.dumps(headset_conf_dict, ensure_ascii=False).encode('utf8'))
    data = None
    while check_continue_func():
        temp_json = ''
        cur_char = cs.recv(1)

        while cur_char != b'\r':
            temp_json += cur_char.decode("utf-8")
            cur_char = cs.recv(1)
        data = None
        try:
            data = json.loads(temp_json)
        except ValueError:
            print("ValueError while trying to decode JSON object. discarding JSON that caused the error")
        if data:
            #print(data)
            yield data
        else:
            continue
    cs.close()
    yield data


def _processDataStream(output_queue, shutdown_flag, connected_flag, host, port):
    """Process the data coming in from the headset and load the processed data into a thread
	safe queue until the shutdown_flag is recognized as set."""
    # make the datastream generator
    ds = _datastream(lambda: not shutdown_flag.isSet(), host, port)
    # make a json processor
    json_processor = lambda: ds.__next__()
    # get connected properly and start receiving real data before moving on
    # debug('Attempting to connect to headset...')
    while not connected_flag.isSet():
        raw_data = json_processor()
        if not raw_data == NULL_DATA:
            # getting real data now
            connected_flag.set()
    # should now be getting real data

    for d in ds:
        raw_data = json_processor()
        if blinkStrength in raw_data:
            blinkvalue= raw_data[blinkStrength]
            flat_data['blinkStrength']=blinkvalue
            #print("blink",blinkvalue)
            output_queue.put(flat_data)


        if rawEeg in raw_data:

            flat_data= raw_data
           # print (raw_data[rawEeg])
            output_queue.put(flat_data)
            print(flat_data)



        if eegPower in raw_data and eSense in raw_data:
            # full data set, extract and pump it
            flat_data = dict(zip(brain_parameters, _extract_tuple(raw_data)))
            output_queue.put(flat_data)
            #print(flat_data)


    connected_flag.clear()


class Brain(object):
    """An object that represents the brain of a user in a program. """

    def __init__(self, host=HOST, port=PORT, appName=APP_NAME, userName=USER_NAME):
        """Initialize the brain by storing arguments, and setting up the threading model of the object."""
        self.queue = Queue()
        self.host = host
        self.port = port
        self.app_name = appName
        self.user_name = userName
        self.is_connected_flag = Event()
        self.shutdown_stream = Event()

        self.producer_thread = Thread(target=_processDataStream,
                                      args=(self.queue, self.shutdown_stream, self.is_connected_flag, host, port))
        self.freshest_data = {}
        print(self.freshest_data)
        self.producer_thread.start()

    def isConnected(self):
        """Return True if the headset connection has been made and proper data is being received."""

        return self.is_connected_flag.isSet()

    def getProperty(self, propertyName):
        """Return the most up to date data on the users brain wave activity."""
        if not self.queue.empty():
            self.freshest_data = self.queue.get(False)
        return self.freshest_data[propertyName] if propertyName in self.freshest_data else 0.0

    def __del__(self):
        """Make sure that the producer thread has been shut down and allowed to terminate."""
        self.shutdown_stream.set()
        self.producer_thread.join()

    def __str__(self):
        """Generate a string giving basic info on the brain."""
        template = 'Brain:\n\tis connected: %s\n\thost: %s\tport: %d\n\tappName: %s\tuserName: %s'
        return template % (str(self.isConnected()), str(self.host), self.port, self.app_name, self.user_name)

    def fullstr(self):
        """Generate a string giving the full information regarding the brain."""
        #header = self.__str__() + '\n'

        header=[]
        for p in brain_parameters:
          header.append(self.getProperty(p))
        return header

    def justheaders(self):
        # just for getting the title name : like "lowaplha"
        return brain_parameters



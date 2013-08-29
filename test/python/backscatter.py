from __future__ import print_function
import sys
import serial
import time

RESET_SLEEP_T = 2.0

CMD_GET_FREQ_BACKGROUND = 0
CMD_GET_FREQ_BLUE = 1

RSP_ERROR = 0
RSP_SUCCESS = 1

class Backscatter(serial.Serial):

    def __init__(self, port, timeout=10.0, debug=False):
        params = {'baudrate': 9600, 'timeout': timeout}
        super(Backscatter,self).__init__(port,**params)
        time.sleep(RESET_SLEEP_T)
        self.debug=debug
        self.clearBuffer()

    def clearBuffer(self):
        time.sleep(0.1)
        while self.inWaiting() > 0:
            self.read(self.inWaiting())
            time.sleep(0.1)

    def sendCmd(self,cmd):
        """
        Send command to colorimeter and receiver response.
        """
        self.write('{0}\n'.format(cmd))
        rsp = self.readline()
        self.clearBuffer()
        if self.debug:
            print('cmd: ', cmd)
            print('rsp: ', rsp)

        if len(rsp) < 2:
            raise IOError, 'response from device is too short'

        if rsp[1] == str(RSP_ERROR):
            raise IOError, 'RSP_ERROR: {0}'.format(rsp)

        try:
            rsp = eval(rsp.strip())
        except Exception:
            raise IOError, 'bad response unable to parse result'

        return rsp

    def getFreqBackground(self):
        cmd = '[{0}]'.format(CMD_GET_FREQ_BACKGROUND) 
        rsp = self.sendCmd(cmd)
        return rsp[1]

    def getFreqBlue(self):
        cmd = '[{0}]'.format(CMD_GET_FREQ_BLUE) 
        rsp = self.sendCmd(cmd)
        return rsp[1]
        

# -----------------------------------------------------------------------------
if __name__ == '__main__':

    dev = Backscatter('/dev/ttyACM0')
    freqBack = dev.getFreqBackground()
    freqBlue = dev.getFreqBlue()
    print(freqBack,freqBlue)







    
        

#if defined(ARDUINO) && ARDUINO >= 100
#include "Arduino.h"
#else
#include "WProgram.h"
#endif
#include "SerialHandler.h"
#include "Streaming.h"

const uint8_t DBL_STR_LEN = 30;
const uint8_t DBL_PREC = 12;

void SerialHandler::processInput() { 
    while (Serial.available() > 0) {
        process(Serial.read());
        if (messageReady()) {
            switchYard();
            reset();
        }
    }
}

void SerialHandler::switchYard() { 
    uint8_t cmdId;

    cmdId = readInt(0); 

    switch (cmdId) {

        case CMD_GET_FREQ_BACKGROUND:
            handleGetFreqBackground();
            break;

        case CMD_GET_FREQ_BLUE:
            handleGetFreqBlue();
            break;

        default:
            unknownCmd();
            break;
    }
    colorimeter.led.setOff();
}


void SerialHandler::handleGetFreqBackground() {
    uint32_t freq; 
    //colorimeter.sensor.setChannelBlue();
    colorimeter.sensor.setChannelRed();
    freq = colorimeter.sensor.getFrequency(colorimeter.numSamples);
    Serial << '[' << RSP_SUCCESS;
    Serial << ',' << freq;
    Serial << ']' << endl;

}

void SerialHandler::handleGetFreqBlue() {
    //uint32_t freq = colorimeter.getFrequencyBlue();
    uint32_t freq = colorimeter.getFrequencyRed();
    Serial << '[' << RSP_SUCCESS;
    Serial << ',' << freq;
    Serial << ']' << endl;
}

void SerialHandler::unknownCmd() { 
    // un-recognized command. Send error message.
    Serial << '[' << RSP_ERROR;
    Serial << ',' << "unknown command";
    Serial << "]" << endl;
}

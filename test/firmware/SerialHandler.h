#ifndef _SERIAL_HANDLER_H_
#define _SERIAL_HANDLER_H_
#include "SerialReceiver.h"
#include "Colorimeter.h"

enum {
    CMD_GET_FREQ_BACKGROUND = 0,
    CMD_GET_FREQ_BLUE = 1,
};

const int RSP_ERROR = 0;
const int RSP_SUCCESS = 1;

class SerialHandler: public SerialReceiver {
    public:
        void processInput();
    private:
        void switchYard();
        void handleGetFreqBackground();
        void handleGetFreqBlue();
        void unknownCmd();
};

extern Colorimeter colorimeter;

#endif



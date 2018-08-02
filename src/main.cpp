extern "C"
{
#include <libavformat/avformat.h>
#include <libavcodec/avcodec.h>
#include <libavutil/avutil.h>
#include <libswscale/swscale.h>
}

#include <iostream>

int main(int argc, char** argv){
    std::cout<< "Hello World!\n";

    av_log_set_flags(AV_LOG_SKIP_REPEATED);
}
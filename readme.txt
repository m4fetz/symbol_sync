Modification of the "Symbol Sync" block for GNU Radio

Implementation of an OQPSK Timing error detector, proposed by Jinsuk Seong 
and Hyuckjae Lee.

Source:
"Timing Error Detector for OQPSK Signal",
 IEEE 62nd Vehicular Technology Conference,
 September 2005

Tested and verified under GNURadio 3.7.13.

Modified files:
/lib/timing_error_detector.cc
/lib/timing_error_detector.h
/include/gnuradio/digital/timing_error_detector_type.h
/grc/digital_symbol_sync_xx.xml

The provided install.py script will replace the existing files above with the new ones.
After copying them to the desired destination, they will be installed via "make && make install".

To run the script type:

>>>python install.py [desired directory] 		(home/user/prefix ,if using pybombs)

The provided flowgraph shows the functionality of the block and the recommended parameters.





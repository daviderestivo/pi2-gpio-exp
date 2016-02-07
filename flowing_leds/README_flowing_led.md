# How the SN54HC595 works

**PIN 14 (SER)** is the DATA PIN. The DATA PIN is used to "serially"
input the single bits into the "one bytes" shift register.
When **PIN 11 (SRCLK)**, the SeRial CLocK, goes from LOW to HIGH the value
of SER is stored into  the shift register and the existing values of the
register are shifted to make room for the new bit. After 8 clock cycles
the first bit entered in SER is available in Qh:

SER -> Qa -> Qb -> Qc -> Qd -> Qe -> Qf -> Qg -> Qh -> Qh'

So if for example we enter: 10100011 the output value will be:

   PIN | VALUE
 ------|--------
    Qa | 1
    Qb | 1
    Qc | 0
    Qd | 0
    Qe | 0
    Qf | 1
    Qg | 0
    Qh | 1

So,if you're inputting 8 bits, the first bit ends up in Qh.

**PIN 12 (RCLK)** is maintained LOW while the data is being written to the
shift register. When set to HIGH the values of the shift register are
written to the storage register which are then outputted to pins Qa-Qh.

**PIN 13 (OE)** is the Output Enable. Set to GND (LOW) for normal
operation. If set to HIGH, it will disable the output (Qa-Qh).

**PIN 10 (SRCLR)** is the SeRial CLeaR. When set to LOW clears the shift
register content. Connect to VCC (HIGH) for normal operation.

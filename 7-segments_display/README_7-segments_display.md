# "7 Segments display"'s notes

The 7-segment display is a seven LEDs (hence its name) arranged in a rectangular fashion as shown below. Each of the seven LEDs is called a segment. Both decimal and hex digit can be shown in a 7-segments display. In addition to the 7 segments the DP (dot point) is usually present.

In the below ascii-art the pin layout is shown.

 ```
G  F  CC  A  B
|  |  |   |  |

     __A__
    |     |
    F     B
    |__G__|
    |     |
    E     C
    |     |
     __D__
          .DP

|  |  |   |  |
E  D  CC  C  DP

CC= Common Cathode
 ```

Assuming an SN54HC595 is used to drive the 7-segments display, a possible wiring
layout might be:

  PIN |	VALUE
------|-------
  Qa  | A   
  Qb  | B
  Qc  |	C
  Qd  |	D
  Qe  |	E
  Qf  |	F
  Qg  |	G
  Qh  |	DP (Dot Point)

Below the table used to display the digit from 0-9 (dec) and A-F (hex). Keep in
mind that the first bit on the right represent Qa while the first bit on the
left represent Qh: reverse order when entered in the shift register.

 Digit | BIN | HEX
-------|-----|----
0  |	00111111  |	0x3f
1  |	00000110  |	0x06
2  |	01011011  |	0x5b
3  |	01001111  |	0x4f
4  |	01100110  |	0x66
5  |	01101101  |	0x6d
6  |	01111101  |	0x7d
7  |	00000111  |	0x07
8  |	01111111  |	0x7f
9  |	01101111  |	0x6f
A  |	01110111  |	0x77
B  |	01111100  |	0x7c
C  |	00111001  |	0x39
D  |	01011110  |	0x5e
E  |	01111001  |	0x79
F  |	01110001  |	0x71

A video showing the two 7-Segments displays in action is available here https://www.youtube.com/watch?v=fuL0RQGJ0YI.

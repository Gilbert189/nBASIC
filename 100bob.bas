10 B=99
15 V="s"
20 PRINT B+" bottle"+V+" of beer on the wall,"
30 PRINT B+" bottle"+V+" of beer."
40 PRINT "Take one down, pass it around,"
50 B=B-1
60 IF B<1 THEN 100
61 IF B<2 THEN 80
65 PRINT B+" bottle"+V+" of beer on the wall."
66 PRINT ""
75 GOTO 20
80 V="s"
90 GOTO 65
100 PRINT "No bottles of beer on the wall."
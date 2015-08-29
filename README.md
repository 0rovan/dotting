# dotting

Class Dotter() simply types symbols (dots in default) on screen. This may
be used to make clinets aware that some computing is still happening
in background. Symbol and delay in miliseconds can be defined at class
initalization or set at any time.

##examples:

###1
from dotting import Dotter
from time import sleep
d=Dotter()
d.start()
sleep(3)
d.stop()

###2
from dotting import Dotter
from time import sleep
d=Dotter(200,',')
d.start()
sleep(2)
d.set(symbol='.')
sleep(3)
d.stop()
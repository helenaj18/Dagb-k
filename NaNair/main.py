from UI.airplaneUI import AirplaneUI

from UI.mainmenu import MainMenu

a = AirplaneUI()
a.showAllPlanes()
a.showOnePlane()
a.addAirplane()


MainMenu().start()
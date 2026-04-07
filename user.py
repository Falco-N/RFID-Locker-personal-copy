#Main window modeling.
#Functionality set up
import os # Polkumääritykset
import sys # Käynnistysargumentit
import json # JSON-tiedostojen käsittely

from PySide6 import QtWidgets # Qt-vimpaimet
from PySide6.QtWidgets import QMessageBox, QApplication, QMainWindow # Viestintäikkunat
from PySide6.QtCore import QThreadPool, Slot, Qt, QByteArray # Säikeistys, slot-dekoraattori ja Qt
from PySide6.QtGui import QPixmap, QCursor # Kuvan luku ja kursorin muutokset

from model1 import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow):
    """A class for creating a main window for the application"""

 # Määritellään olionmuodostin ja kutsutaan yliluokkien muodostimia
    def __init__(self):
        super().__init__()

        # Luodaan säikeistystä varten uusi säievaranto
        self.threadPool = QThreadPool.globalInstance()

        # Luodaan käyttöliittymä konvertoidun tiedoston perusteella MainWindow:n ui-ominaisuudeksi. Tämä suojaa lopun MainWindow-olion ylikirjoitukselta, kun ui-tiedostoa päivitetään
        self.ui = Ui_MainWindow()

        # Kutsutaan käyttöliittymän muodostusmetodia setupUi
        self.ui.setupUi(self)
   
        #Need to be modified to RFID identification
        # Rutiini, joka lukee asetukset, jos ne ovat olemassa
        try:
            # Avataam asetustiedosto ja muutetaan se Python sanakirjaksi
            with open('settings.json', 'rt') as settingsFile: # With sulkee tiedoston automaattisesti
                
                jsonData = settingsFile.read()
                self.currentSettings = json.loads(jsonData)
            
            # Puretaan salasana tietokantaoperaatioita varten  switch function to ReadCard.txt
            # self.plainTextPassword = cipher.decryptString(self.currentSettings['password'])
        
        # Jos asetusten luku ei onnistu, näytetään virhedialogi
        except Exception as error:
            title = 'Tietokanta-asetusten luku ei onnistunut'
            text = 'Tietokanta-asetuksien avaaminen ja salasanan purku ei onnistunut'
            detailedText = str(error)
            self.openWarning(title, text, detailedText)      


        

        # Ohjelman käynnistyksessä piilotetaan tarpeettomat elementit
        # self.setInitialElements()


        # OHJELMOIDUT SIGNAALIT
        # ---------------------

        # RFID scan page?
        # self.ui.stackedWidget.setCurrentWidget(self.ui.MainWindow)

        # ToLoan button -> Loan window
        self.ui.ToLoan.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Loan)
        )

        # ToReturn button -> Return Window
        self.ui.ToReturn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Return)
        )

        # ToHistory button -> History window. Add hidden function for all but admin.gs.getUser().hasRole('admin') is to only open for admin variant.
        self.ui.ToHistory.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.History)
        )

        # DoLoan -save data and go back (saveLendingData not yet defined)
        # self.ui.DoLoan.clicked.connect(self.saveLendingData)

        # FromLoan -> UI original page
        self.ui.FromLoan.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.MainPage)
        )

        # DoReturn - save data and go back
        # self.ui.DoReturn.clicked.connect(self.saveLendingData)

        # FromReturn -> UI original page
        self.ui.FromReturn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.MainPage)
        )

        # DoHistory - save data and go back
        # self.ui.DoHistory.clicked.connect(self.saveLendingData)

        # FromHistory -> UI original page
        self.ui.FromHistory.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.MainPage)
        )

# OHJELMOIDUT SLOTIT
# ------------------
    # FUNCTIONS
    # ---------------------

def goBack(self):
    """Return to main page"""
    self.ui.stackedWidget.setCurrentWidget(self.ui.MainWindow)

def saveLendingData(self):
    print("Saving data... (placeholder)")

# Palauta käyttöliittymä alkutilanteeseen
@Slot()
def setInitialElements(self):
    # need to add hide elements such as time/date all

    # Näytetään alkutilanteen elementit
    self.ui.ToLoan.show()


# LUODAAN VARSINAINEN SOVELLUS
# ============================

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    # Asetetaan sovelluksen tyyliksi Fusion, ilman asetusta käyttöjärjestelmän oletustyyli tulee käyttöön
    app.setStyle('fusion')

    # Luodaan objekti pääikkunalle ja tehdään siitä näkyvä
    window = MainWindow() 
    window.show()

    # Käynnistetään sovellus ja tapahtumienkäsittelijä (event loop)
    sys.exit(app.exec())
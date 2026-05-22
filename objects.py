class User:
    def __init__(self):
        self.nickname=""
        self.password="gigathon2026"
        self.auth = False


#Klasa wiązki - głównego obiektu, który będzie sterowany przez użytkownika
class Beam():
    def __init__(self):
        self.position_x = 0.0 #współrzędna określająca położenie wiązki wzdłuż osi akceleratora  
        self.position_y = 0.0 #Współrzędna określająca poprzeczne odchylenie wiązki od idealnego środka rury   
        self.angle = 0.0 #kąt lotu wiązki wyrażony w stopniach, gdzie 0 oznacza lot idealnie na wprost i równolegle do ścian akceleratora  
        
        self.energy = 4.5E-2 #[MeV] #aktualna energia kinetyczna wiązki
        self.current = None #[mA] #prąd wiązki wyliczony na podstawie wydajności cezu i limitu otworu
        self.N_Intensity = None #liczba cząstek w "paczce" wiązki
        self.epsilon = None #emitancja (miara chaosu i rozbieżności wiązki)
        
        self.is_alive = True #flaga logiczna sprawdzająca, czy wiązka nie uległa zniszczeniu 
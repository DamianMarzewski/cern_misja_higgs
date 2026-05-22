"""
+=======================================+
ZAIMPORTOWANIE: 
a) bibliotek:
        os - możliwość używania funkcjonalności systemu operacyjnego komputera
        cmd - pisanie szybciej i wydajniej poleceń dotyczących programu
        time - opóźnianie procesów w terminalu
b) plików/funkcjonalności z innych plików
        utils - łatwe zarządzanie formatowaniem ANSII oraz upiększeniami UI
        object - łatwe zarządzanie obiektami
+=======================================+
"""

import os
import cmd
import time

from utils import Colors, Create_progress_bar 

#Dostęp do formatowania ANSII w bardziej przystepny sposób
colors=Colors()
 
"""
+=======================================+
KONSOLA POLECEŃ SŁUŻĄCA DO STEROWANIA GRĄ
+=======================================+
"""
#KLasa będąca podstawą innych konsoli wykorzystywanych w programie
class FunctionalCommands(cmd.Cmd):
    #Zmienne służące do wyświetlania czytelnego panelu pomocy
    HELP_TITLE = "SYSTEM POMOCY"
    HELP_SUBTITLE = "KOMENDY"
    HELP_COMMANDS = {} 
    
    #Metody biblioteki cmd, które powodują puste miejsca po wykonanej komendzie
    def precmd(self, line):
        """Wywołuje się automatycznie TUŻ PRZED każdą komendą."""
        print()  
        return line 
    
    def postcmd(self, stop, line):
        """Wywołuje się automatycznie PO każdej wykonanej komendzie."""
        print()  
        return stop
    
    #Komendy systemowe tzn. nie wpływające na rozgrywkę
    def do_clear(self, arg):
        """Czyści konsolę."""
        if os.name == 'nt':
            os.system('cls')  
        else:
            os.system('clear')
    
    do_cls = do_clear
    do_wyczysc = do_clear

    def do_exit(self, arg):  
            """Zamyka konsole."""
            
            print("Anulowanie procesu autoryzacji...")
            time.sleep(2)
            print("Wyłączenie systemu...")
            return True  
    
    def default(self, line):
        """Wywołuje się, gdy gracz wpisze nieznaną komendę."""
        
        title="-BŁĄD SYSTEMU CERN-"
        spaces_count = int((80-(len(title)))/2)
        
        print(f"{colors.errors}" + "=" * spaces_count + title + "=" * (spaces_count+1) + "\n")
        print(f"Komenda '{line}' nie została rozpoznana przez system.\n")
        print("="*80 + "\n" + f"{colors.clear}")

    def handling_an_exception(self, text):
        title="-BŁĄD SYSTEMU CERN-"
        spaces_count = int((80-(len(title)))/2)
        
        print(f"{colors.errors}" + "=" * spaces_count + title + "=" * (spaces_count+1) + "\n")
        print(text + "\n")
        print("="*80 + "\n" + f"{colors.clear}")


    def do_help(self, arg):
        """Wyświetla spersonalizowane menu pomocy."""
       
        if arg:
            return super().do_help(arg)
        
        lenght_decoration = 80
        print(f"{colors.bold}{colors.help}" + "\n" + "=" * lenght_decoration)
        print(f"{self.HELP_TITLE:^{lenght_decoration}}")
        print(f"=" * lenght_decoration + f"{colors.clear}")
        
        print(f"{colors.help2}\n[ {self.HELP_SUBTITLE} ]{colors.clear}")
        for cmd_name, cmd_desc in self.HELP_COMMANDS.items():
                print(f"  {cmd_name:<25} - {cmd_desc}")
        
        print(f"{colors.help2}\n[ KOMENDY SYSTEMOWE ]{colors.clear}")
        print(f"  {'clear / cls / wyczysc':<25} - Czyszczenie ekranu konsoli.")
        print(f"  {'help':<25} - Wyświetla menu pomocy.")
        print(f"  {'exit':<25} - Zamknięcie konsoli CERN'U! Nie programu!.")
        
        print(f"{colors.bold}{colors.help}" + "\n" + "-" * lenght_decoration + f"{colors.clear}")
        print(" Wskazówka: Wpisz 'help <nazwa_komendy>', aby uzyskać szczegóły.")
        print(f"{colors.bold}{colors.help}"+"=" * lenght_decoration + "\n" + f"{colors.clear}")

"""
+==============================================+
KONSOLA POLECEŃ SŁUŻĄCA DO AUTORYZACJI PRZED GRĄ
+==============================================+
"""

class AuthorizationPanel(FunctionalCommands):
    #Zdefiniowanie: prefixu wykonywanych komend, krótkiego przywitania użytkownika
    prompt = f"{colors.bold}{colors.prefix_cmd}CERN_AUTORYZACJA>>> {colors.clear}"
    title_intro =f"{'WITAJ W "CERN: MISJA HIGGS" ':^80}"
    intro = f"{colors.bold}{colors.welcome_color_1}" + "=" * 80 + f"{colors.welcome_color_2}\n{title_intro}\n" + f"{colors.welcome_color_1}" + "=" * 80 + "\n\n" + f"{colors.clear}{colors.welcome_color_2}Witaj, Inżynierze! Jesteś jednym krokiem od uruchomienia największego \neksperymentu w historii nauki.  \n\nPrzejdź weryfikację, aby uzyskać dostęp do układu akceleratorów CERN. \n\n" + f"{colors.bold}{colors.welcome_color_1}" + "-" * 80 + "\n" + f"{colors.clear}{colors.welcome_color_2}Wpisz {colors.bold}'help'{colors.bold_off}, aby zobaczyć komendy.\n" + f"{colors.bold}{colors.welcome_color_1}" + "=" * 80 + f"{colors.clear}\n\n"
    
    #Zmienne służące do wyświetlania czytelnego panelu pomocy
    HELP_TITLE = "PANEL AUTORYZACJI CERN - SYSTEM POMOCY"
    HELP_SUBTITLE = "KOMENDY AUTORYZACYJNE"
    HELP_COMMANDS = {
        "login": "Weryfikuje czy użytkownik jest w bazie danych.",
        "password": "Weryfikuje poprawność hasła."
    }

    def __init__(self, uzytkownik):
        super().__init__()
        self.uzytkownik = uzytkownik  
        self.nickname = uzytkownik.nickname 


    #Komendy wpływające na rozgrywkę: pobieranie nazwy od użytkownika, sprawdzenie hasła z dokumentacji
    def do_login(self, arg):
        """Autoryzacja użytkownika. \nUżycie: login <nazwa>"""
        try:
            name = arg.strip()  
        
            if name == "":
                print("Nie podano nazwy użytkownika! Autoryzacja zakończona niepowodzeniem.")
                print("Spróbuj jeszcze raz, wpisując: login <nazwa użytkownika>")
                return 
            
            self.nickname = name
            self.uzytkownik.nickname = name
            print(f"Znaleziono użytkownika w bazie danych! \n\nWitaj {self.nickname}! \n Kontynuuj swoją autoryzacje: password <hasło>")
        
        except Exception as e:
            text = f"Wykonując komendę system napotkał błąd:{type(e).__name__}"
            self.handling_an_exception(text)

    def do_password(self, arg):
        """Weryfikacja hasła. Hasło podane jest w dokumentacji \nUżycie: password <hasło>"""
        try: 
            if self.nickname != "":
                self.password_auth = arg.strip()
                if self.password_auth != self.uzytkownik.password:
                    print("Błędne hasło! Autoryzacja zakończona niepowodzeniem.")
                    print("Spróbuj jeszcze raz wpisać hasło.")
                    return 
                else:
                    print(f"Hasło poprawne! Dostęp do systemów CERN został przyznany.")
                    self.uzytkownik.auth = True
                    return True
            else: 
                print("Nie podano nazwy użytkownika! Autoryzacja zakończona niepowodzeniem.")
                print("Spróbuj jeszcze raz, wpisując: login <nazwa użytkownika>")
                return
            
        except Exception as e:
            text = f"Wykonując komendę system napotkał błąd:{type(e).__name__}"
            self.handling_an_exception(text)

"""
+=======================================+
KONSOLA POLECEŃ SŁUŻĄCA DO STEROWANIA GRĄ
+=======================================+
"""

class ControlPanel(FunctionalCommands):
    #Zdefiniowanie: prefixu wykonywanych komend, krotkiego wytłumaczenia uzżytkonikowi do czego jest dana konsola
    prompt = f"{colors.bold}{colors.prefix_cmd}CERN_CMD>>> {colors.clear}"
    title_intro =f"{'PANEL ZARZĄDZANIA CERN - WITAJ PONOWNIE!':^80}"
    intro = f"{colors.bold}{colors.welcome_color_1}" + "=" * 80 + f"{colors.welcome_color_2}\n{title_intro}\n" + f"{colors.welcome_color_1}" + "=" * 80 + "\n\n" + f"{colors.clear}{colors.welcome_color_2}Etap weryfikacji dla użytkownika zakończony pomyślnie!\n\n" + "System zarządzania akceleratorami zainicjowany pomyślnie! \n\n" + "Użytkownik posiada wszystkie uprawnienia zarządzaniem akceleratorem! \n\n" + f"{colors.bold}{colors.welcome_color_1}" + "-" * 80 + "\n" + f"{colors.clear}{colors.welcome_color_2}Wpisz {colors.bold}'help'{colors.bold_off}, aby zobaczyć komendy.\n" + f"{colors.bold}{colors.welcome_color_1}" + "=" * 80 + f"{colors.clear}\n\n" 
    
    def __init__(self, accelerator, beam):
        super().__init__()
        self.accelerator = accelerator 
        self.beam = beam

        #zdefiniowanie globalnych zmiennych dla tej klasy
        self.n = 0
        self.p = 0
        self.ionization_efficiency = 0
        self.I_S_rf_start_power = 0
        self.I_S_rf_power = 0
        self.rf_work = 0
        self.ne = 0

    #Zmienne służące do wyświetlania czytelnego panelu pomocy
    HELP_TITLE = "PANEL ZARZĄDZANIA CERN - SYSTEM POMOCY"
    HELP_SUBTITLE = "KOMENDY ZARZĄDZANIA"
    HELP_COMMANDS = {
        "otworz_zawor": "Otwiera zawór piezoelektryczny.",
        "moc_startowa_RF": "Ustawia moc startową fal radiowych (RF)",
        "moc_RF": "Ustawia moc roboczą fal radiowych (RF)."
    }
    
    #Komendy wpływające na rozgrywkę
    def do_otworz_zawor(self, arg):
        '''Otwiera zawór piezoelektryczny wtrysku wodoru. \nUżycie: otworz_zawor <czas otwarcia w ms>'''
        try: 
            total_hydrogen_mass = self.accelerator.I_S_calculate_mass_hydrogen(0, int(arg))
            self.n = self.accelerator.I_S_calculate_number_density(total_hydrogen_mass)
            self.p = self.accelerator.I_S_calculate_chamber_pressure(self.n)
            print(f"n wynosi: {self.n}")
            print(f"Ciśnienie w komorze wynosi: {self.p} Pa")
            Create_progress_bar(self.p, 1, 4, 20, 5, "Pa", colors.welcome_color_1, colors.errors, colors.welcome_color_2)
        
        except ValueError:
            text = f"Nie możesz: \n- zostawić pustego pola\n- wpisywać liter \n- podawać wielu argumentów komendzie np. otworz_zawor <argument1> <argument2> \n\nPodaj liczbę całkowitą (czas otwarcia zaworu w ms)!"
            self.handling_an_exception(text)
        
        except Exception as e:
            text = f"Wykonując komendę system napotkał błąd:{type(e).__name__}"
            self.handling_an_exception(text)
        
    def do_moc_startowa_RF(self, arg):
        '''Ustawia moc startową fal radiowych (RF) wymaganą do zapłonu plazmy. \nUżycie: moc_RF <moc w kW>'''
        try: 
            self.ionization_efficiency, self.I_S_rf_start_power = self.accelerator.I_S_calculate_ionization_efficiency(int(arg))
            print(f"Efektywność jonizacji wynosi {self.ionization_efficiency}, moc startowa RF wynosi {self.I_S_rf_start_power}")
        
        except Exception as e:
            text = f"Wykonując komendę system napotkał błąd:{type(e).__name__}"
            self.handling_an_exception(text)

    def do_moc_RF(self, arg):
        '''Ustawia moc roboczą fal radiowych (RF) potrzebną do stabilnego podtrzymania plazmy. \nUżycie: moc_RF <moc w kW>'''
        try:
            self.rf_work, self.I_S_rf_power = self.accelerator.I_S_calculate_RF_field_energy(self.n, int(arg))
            self.ne = self.accelerator.I_S_calculate_electron_density(self.I_S_rf_power, self.ionization_efficiency)
            self.beam.current = self.accelerator.I_S_calculate__beam_current(self.ne)
            self.beam.N_Intensity = self.accelerator.I_S_calculate_beam_intensity(self.beam.I_final)
            self.beam.epsilon = self.accelerator.I_S_calculate_beam_emittance()
        
        except Exception as e:
            text = f"Wykonując komendę system napotkał błąd:{type(e).__name__}"
            self.handling_an_exception(text)

#Rzeczy, które się wykonają kiedy użytkownik odpali ten plik w konsoli
if __name__ == "__main__":
    print("Jesteś w pliku commands!")
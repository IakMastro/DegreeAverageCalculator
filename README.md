# DegreeAverageCalculator
A calculator of the degree average for ICE Uniwa. It is made because in our department there is no indication of what is the current
degree average, and some people would like to know. If you want to use it on your department, then just fork it, change the 
necessary stuff from the code and put your department's classes in the csv files insted. The rest of the README.md will be in
greek.

# ΟΔΗΓΙΕΣ
Ανοίχτε το csv αρχείο και γράψτε σε κάθε μάθημα που έχει περαστεί ο τελικός βαθμός σας στο Services.
Μην ανυσηχείται για μαθημάτα που δεν έχετε περάσει, το έχω φτιάξει έτσι, ώστε να μπορεί να προσπερνάει τα μαθήματα,
που δεν έχουν περαστεί. Μην βάλετε 0 εκεί, θα κάτετε τα πράγματα χειρότερα, και να μην βάλετε επίσης και βαθμούς κάτω του 5.

# ΠΩΣ ΤΟ ΤΡΕΧΩ
Για να τρέξετε το πρόγραμμα, θα πρέπει να έχετε κατεβασμένη την Python 3. Μπορείτε να την βρήτε εδώ: 
https://www.python.org/downloads/release/python-383/, ή εάν χρησιμοποιείται WSL ή Linux μπορείται να το κατεβάσετε από το terminal
με την εξής εντολή:

```bash
sudo apt install python3 # Για Ubuntu/Mint
sudo pacman -S python # Για Arch/Manjaro
```

Επισής θα χρηαστεί να κατεβάσετε και κάτι επιπλεόν, τον Package Manager της Python, το pip. Εάν χρησιμοποιείται Windows είναι ετοίμο,
άλλα σε Linux και WSL πρέπει να ξανά κατέβει.

```bash
sudo apt install pip3 # Για Ubuntu/Mint
sudo pacman -S pip # Για Arch/Manjaro
```

Τέλος, ανοίχτε το CMD ή το Terminal της επιλογής σας και πληκτρολογήστε αυτές τις εντολές:

```bash
pip3 install numpy pandas # Για Ubuntu/Mint
pip install numpy pandas # Για Windows/Arch/Manjaro
```

Τέλος, πάτε στο directory που έχετε κατεβάσει τα αρχεία, ανοίχτε έκει το CMD ή το Terminal και το τρέχετε έτσι:

```bash
python3 DegreeAverageCalculator.py # Για Ubuntu/Mint
python DegreeAverageCalculator.py # Για Windows/Arch/Manjaro
```


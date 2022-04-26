BusinessCards

Plik wyświetla wizytówki, z obiektów uprzednio stworzynych, zwracając okreslone ich atrybuty w tym  długość imienia i nazwiska oddzielonych spacją. 

Następnie zwracany jest string z informacją o wybieranym nr telefonu  oraz imieniu i nazwisku danej osoby.

W dalszej kolejości, wbudowana funkcja generuje automatycznie listę wizytówek, w ilości zdefiniowanej przez użytkownika, zwracająac argumenty dla predefioniowanych parametrów. 

Powyższe mozliwe jest dzięki: 

Zbudowana została  klasa pierwsza (BaseContact) oraz za pomocą dziedziczenia druga klasa (BusinessContact), którą rozszerzono w relacji do  klasy bazowej o przechowywanie informacji związanych z pracą danej osoby czyli stanowisko, nazwa firmy, telefon służbowy. 

Każda z klas zawiera metodę contact(), zwracającą predefiniwany string na każdym z wywoływanych obiektów; Metoda contact() sprecyzowana zostałaa dla każdej klasy osobno.

Każda z klas zawiera __repr__ w celu sformatowania widoku obiektów, tj określenia sposóbu w jaki będą  wyświatlane obiekty danej klasy podczas iteracji  listy obiektów 

Klasy zawierają dekorator, wykorzytywany do zwracania długości imienia i nazwiska, oddzielonych spacją 

W pliku znajduje się funkcja generujaca automatycznie listę wizytówek, w ilości zdefiniowanej przez użytkownika, zwracająac argumenty dla predefioniowanych parametrów. Wprowadzono dwa sposoby: pierwszy polega ne generowaniu instancji klasy, drugi na generowaniu listy obiektów 


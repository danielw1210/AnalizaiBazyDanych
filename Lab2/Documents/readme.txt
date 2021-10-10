Pierwotne dane znajdują się w folderze Original Data w pliku pod nazwą "billboard.csv". Z racji że plik jest w formacie .csv jest on gotowy do zaimportowania 
do programu przetwarzającego dane. Korzystając z pakietu pandas importu danych dokonuje się używając funkcji read_csv().

Przetwarzanie danych polegało na utworzeniu dwóch tabel:
	1. Tabela z danymi piosenek - zawierająca id piosenki, artystę, tytuł piosenki, gatunek muzyczny oraz czas trwania utworu.
	2. Tabela z danymi rankingowymi - zawierająca id piosenki do której odnosi się dana pozycja w rankingu, dokładna data oraz zajmowana w tym dniu pozycja w rankingu

Skrypt realizujący przetwarzanie danych znajduję się w lokalizacji /CommandFiles/DataProcessing.ipynb

Tabela nr. 1 została zapisana w pliku /Analysis Data/SongsData.csv,
Tabela nr. 2 została zapisana w pliku /Analysis Data/RankingData.csv

Ponadto z wykorzystaniem skryptu /CommandFiles/DataAppendix.ipynb opracowany został dodatek do danych znajdujący się w lokalizacji /Documents/DataAppendix.txt
Zebrane dane oraz wykres można znaleźć w yupyter notebook, natomiast podsumowanie w pliku tekstowym.

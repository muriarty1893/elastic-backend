import os
from elastic.indexer import CSVIndexer
from elastic.deleter import IndexDeleter

CSV_FILE_PATH = "data/urunler.csv"

def main():
    indexer = CSVIndexer(indexname="kadir")
    deleter = IndexDeleter(indexname="kadir")

    while True:
        print("\n1) Veriyi Elasticsearch'e Aktar")
        print("2) Elasticsearch Indexindeki Verileri Sil")
        print("3) Cikis")

        choice = input("Secim yap (1/2/3): ")

        if choice == "1":
            if os.path.exists(CSV_FILE_PATH):
                indexer.index_csv(CSV_FILE_PATH)
            else:
                print("HATA: CSV dosyasi bulunamadi!")

        elif choice == "2":
            deleter.delete_all_data()

        elif choice == "3":
            print("Cikis yapildi.")
            break

        else:
            print("Gecersiz giris, tekrar deneyin.")

if __name__ == "__main__":
    main()

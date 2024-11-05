# Class Induk
class Youtuber:
    def __init__(self, name, subscribers):
        self.__name = name  # Encapsulation: menggunakan private variable
        self.__subscribers = subscribers  # Encapsulation: menggunakan private variable

    # Getter untuk nama
    def get_name(self):
        return self.__name

    # Setter untuk nama
    def set_name(self, name):
        self.__name = name

    # Getter untuk jumlah subscribers
    def get_subscribers(self):
        return self.__subscribers

    # Setter untuk jumlah subscribers
    def set_subscribers(self, subscribers):
        if subscribers >= 0:
            self.__subscribers = subscribers
        else:
            print("Jumlah subscribers tidak boleh negatif!")

    # Method untuk memperkenalkan diri
    def introduce(self):
        print(f"Nama Youtuber: {self.__name}, Jumlah Subscribers: {self.__subscribers}")


# Class Turunan
class GamingYoutuber(Youtuber):
    def __init__(self, name, subscribers, favorite_game):
        super().__init__(name, subscribers)  # Memanggil constructor dari class induk
        self.__favorite_game = favorite_game  # Encapsulation: menggunakan private variable

    # Getter untuk favorite_game
    def get_favorite_game(self):
        return self.__favorite_game

    # Setter untuk favorite_game
    def set_favorite_game(self, favorite_game):
        self.__favorite_game = favorite_game

    # Method untuk memperkenalkan diri sebagai Gaming Youtuber
    def introduce(self):
        super().introduce()  # Memanggil method dari class induk
        print(f"Game Favorit: {self.__favorite_game}")


# Membuat objek dari class Youtuber
youtuber1 = Youtuber("MiawAug", 5000000)
youtuber1.introduce()

# Menggunakan setter dan getter
youtuber1.set_subscribers(6000000)
print(f"Jumlah subscribers setelah diupdate: {youtuber1.get_subscribers()}")

# Membuat objek dari class GamingYoutuber
gaming_youtuber1 = GamingYoutuber("MiawAug", 5000000, "Among Us")
gaming_youtuber1.introduce()

# Menggunakan setter dan getter pada objek gaming_youtuber
gaming_youtuber1.set_subscribers(7000000)
gaming_youtuber1.set_favorite_game("Minecraft")
print(f"Jumlah subscribers setelah diupdate: {gaming_youtuber1.get_subscribers()}")
print(f"Game favorit setelah diupdate: {gaming_youtuber1.get_favorite_game()}")
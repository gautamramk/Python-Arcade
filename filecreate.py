# to create the highscore files
import pickle


def main():
    f1 = open("snake.dat", "wb")
    pickle.dump([("---", 0), ("---", 0), ("---", 0),
                 ("---", 0), ("---", 0)], f1)
    f1.close()
    f1 = open("birds.dat", "wb")
    pickle.dump([("---", 0), ("---", 0), ("---", 0),
                 ("---", 0), ("---", 0)], f1)
    f1.close()


main()

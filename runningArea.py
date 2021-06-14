import workingArea as wa
import getMongo as gm


def main():
    while True:
        wrk = wa.App()
        wrk.window_table()
        gvm = gm.GetMongo()
        gvm.get_value_mongo()


if __name__ == '__main__':
    main()

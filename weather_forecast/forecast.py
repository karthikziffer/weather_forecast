import argparse
import __init__ as wf


class Forecast: 
    def __init__(self):

        parser = argparse.ArgumentParser(description = "Forecast Parser")
        parser.add_argument("-p", "--place", help = "Place/Location in string", required = True, default = "")
        parser.add_argument("-t", "--time", help = "Forecast time", required = False, default = None)
        parser.add_argument("-d", "--date", help = "Forecast Date ", required = False, default = None)
        parser.add_argument("-f", "--forecast", help = "Forecast Type ", required = False, default = "daily")

        argument = parser.parse_args()
        status = False


        if argument.place and argument.date:
            wf.forecast(argument.place , argument.time , argument.date)
            status = True
        else:
            wf.forecast(argument.place)
            status = True
        if not status:
            print("Please check the arguments") 


if __name__ == '__main__':
    app = Forecast()
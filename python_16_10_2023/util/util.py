from datetime import datetime, timedelta
import helper.helper as helper
def processLinuxData(up_time):
    time_in_ms=int(up_time.split(":")[1].strip())
    time_in_seconds=time_in_ms/1000
    proccessed_up_time=datetime.fromtimestamp(time_in_seconds)
    current_datetime = datetime.now()
    time_difference=current_datetime - proccessed_up_time
    return proccessed_up_time,time_difference

def processWindowsData(up_time):
    hours_to_subtract,minutes_to_subtract,seconds_to_subtract =helper.getArrayTime(up_time)
    current_datetime = datetime.now()
    time_difference = timedelta(hours=hours_to_subtract, minutes=minutes_to_subtract, seconds=seconds_to_subtract)
    proccessed_up_time = current_datetime - time_difference

    # print("Current Date and Time:", current_datetime)
    # print("Past Date and Time:", proccessed_up_time)
    # print("time_difference:", time_difference)
    return proccessed_up_time,time_difference

def format_time(proccessed_up_time,time_difference):
    format="%a %b %d %H:%M:%S %Y "
    formattedTime="OK - Up since " + datetime.strftime(proccessed_up_time,format) +"("+ str(time_difference).replace(" days,","d").split('.')[0] +")"
    return formattedTime
import util.util as util
def convert(rawData):
    processedData = []
    try:
        for value in rawData:
            if value["os"]=="Windows":
                proccessed_up_time,time_difference=util.processWindowsData(value["up_time"])
                formatted_up_time=util.format_time(proccessed_up_time,time_difference)
                processedData.append({"up_time": formatted_up_time,"os": "Windows"})
            elif value["os"]=="Linux":
                proccessed_up_time,time_difference=util.processLinuxData(value["up_time"])
                formatted_up_time=util.format_time(proccessed_up_time,time_difference)
                processedData.append({"up_time": formatted_up_time,"os": "Linux"})
        return processedData
    except Exception as e:
        print(e)
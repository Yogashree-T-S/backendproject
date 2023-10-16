from flask import jsonify
import model.model as model
def convert(request):
    try:
        DataArr=request.get_json()
        rawData=DataArr.get("data",{})
        if rawData =={}:
            return jsonify({"error":True,"message":"Invalid payload"})
        proccessedData = model.convert(rawData)
        return jsonify({'message': proccessedData})
    except Exception as e:
        print(e)
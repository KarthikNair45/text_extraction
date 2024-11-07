from PIL import Image
from flask_cors import CORS
import os
import json
from flask import Flask,request
import google.generativeai as genai
import typing_extensions as typing
from imagehandle import get_text
app = Flask(__name__)
CORS(app, origins="*")

#api key for gemini
GEMINI_API_KEY=os.environ.get('GEMINI_API_KEY')



#Schema
class License(typing.TypedDict):
    name: str
    license_no: str
    date_of_Exp: str
#Get image from user and return name, license number and date of expiry
@app.route("/upload-image",methods=["POST"])
def uploadImage():
    file = request.files['image']
    img = Image.open(file.stream)
    res=get_text(img)
    #uses gemini api to get name, license no and date of expiry from extracted text
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")
    try:
        response = model.generate_content(f'''{res} from this extract the name, date of expiration and license no. and return it in a json format without any extra spaces.
                                        make sure all the values especially license number is valid. Valid license number would be of this format :- TN9920190000989. This is just an example. DO NOT USE this license number. There might be some errors in the received array as the data is pulled from an image using tesseract ocr so make appropriate changes to make it correct. License number shouldn't have any letters after the first two letters which specifies the state and make sure to put hyphen between the state and the number and remove json markers.''',generation_config=genai.GenerationConfig(
                                        response_mime_type="application/json", response_schema=list[License]
                                        ),)
        print(response.text)
        res=json.loads(response.text)
        print(res[0])
        return json.dumps(res[0])
    except Exception as e:
        print(e)
        return e

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
from flask import *

from haikuGenerator import classifyImage, getConversation, takeSelfie
from textToGcode import *
from printGcode import *

app = Flask(__name__)

updatedFileName="drawing.png"

# def cleanUp():
#     if os.path.isfile(updatedFileName):
#         os.remove(updatedFileName)

def alreadyLoaded():
    if os.path.isfile(updatedFileName):
        return True
    return False

@app.route('/')
def upload():

    return render_template("index.html")


@app.route('/', methods=['GET','POST'])
def success():
    if request.method == 'POST':
        f = request.files['file']
        f.save(updatedFileName)
        # if alreadyLoaded():

            # img processing
        textToSvg(getConversation(classifyImage()))
        svgToGcode()
        writeCode()
            # cleanUp()

        return render_template("index.html")
    return render_template("index.html")

@app.route("/photo", methods=['POST'])
def move_forward():
    #Moving forward code
    # TODO- camera stuff here
    takeSelfie(updatedFileName)
    textToSvg(getConversation(classifyImage()))
    svgToGcode()
    writeCode()
    # cleanUp()
    return render_template('index.html');

if __name__ == "__main__":
    # cleanUp()
    app.run(host='0.0.0.0', port=5000)
from flask import Flask, request, send_file

from PIL import Image, ImageDraw, ImageFont

import requests

from io import BytesIO

app = Flask(__name__)

@app.route('/generate', methods=['GET'])

def generate_image():

    # Get the user avatar URLs from the request parameters

    avatar_url1 = request.args.get('avatar_url1')

    avatar_url2 = request.args.get('avatar_url2')

    # Download the user avatar images

    response1 = requests.get(avatar_url1)

    response2 = requests.get(avatar_url2)

    avatar_image1 = Image.open(BytesIO(response1.content))

    avatar_image2 = Image.open(BytesIO(response2.content))

    # Load the ship template image

    ship_image = Image.open('20230605_012021.png')

    # Resize the user avatar images to fit in the designated area

    avatar_size = (300, 300)

    avatar_image1 = avatar_image1.resize(avatar_size)

    avatar_image2 = avatar_image2.resize(avatar_size)

    # Calculate the positions for placing the user avatars

    x1 = 800

    y1 = 300

    x2 = 100

    y2 = 300

    # Paste the user avatars onto the ship image

    ship_image.paste(avatar_image1, (x1, y1))

    ship_image.paste(avatar_image2, (x2, y2))

    # Save the final image

    ship_image.save('generated_ship.png')

    # Return the generated image as a response

    return send_file('generated_ship.png', mimetype='image/png')

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=8080)


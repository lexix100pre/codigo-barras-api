from flask import Flask, request, send_file
import barcode
from barcode.writer import ImageWriter
import io

app = Flask(__name__)

@app.route("/barcode")
def generar_barcode():
    data = request.args.get("data", "SIN-DATO")
    if not data:
        return "❌ No se proporcionó código", 400

    buffer = io.BytesIO()
    code128 = barcode.get_barcode_class('code128')
    codigo = code128(data, writer=ImageWriter())
    codigo.write(buffer)
    buffer.seek(0)

    return send_file(buffer, mimetype='image/png')

if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
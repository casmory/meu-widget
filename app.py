from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Meu Widget</title>

    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #111827;
            color: white;
            min-height: 100vh;
        }

        .barra {
            height: 70px;
            display: flex;
            align-items: center;
            gap: 10px;
            padding: 12px 15px;
            background: #1f2937;
            box-shadow: 0 2px 10px rgba(0,0,0,.4);
        }

        input {
            flex: 1;
            height: 44px;
            border: none;
            border-radius: 8px;
            padding: 0 14px;
            font-size: 15px;
            outline: none;
        }

        button {
            height: 44px;
            padding: 0 20px;
            border: none;
            border-radius: 8px;
            background: #2563eb;
            color: white;
            font-size: 15px;
            cursor: pointer;
        }

        button:hover {
            background: #1d4ed8;
        }

        .conteudo {
            height: calc(100vh - 70px);
            width: 100%;
        }

        iframe {
            width: 100%;
            height: 100%;
            border: none;
            background: white;
        }

        .aviso {
            padding: 30px;
            text-align: center;
            color: #d1d5db;
        }
    </style>
</head>

<body>

    <div class="barra">
        <input
            id="url"
            type="text"
            placeholder="Cole aqui o link que você quiser..."
            value="https://www.google.com"
        >

        <button onclick="abrirLink()">Abrir</button>
    </div>

    <div class="conteudo">
        <iframe
            id="pagina"
            src="https://www.google.com">
        </iframe>
    </div>

    <script>
        function abrirLink() {
            let url = document.getElementById("url").value.trim();

            if (!url) {
                alert("Cole um link primeiro.");
                return;
            }

            if (!url.startsWith("http://") && !url.startsWith("https://")) {
                url = "https://" + url;
            }

            document.getElementById("pagina").src = url;
        }
    </script>

</body>
</html>
"""

@app.route("/")
def inicio():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)

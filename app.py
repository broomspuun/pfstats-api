from flask import Flask, jsonify


app = Flask(__name__)



@app.route('/first-token', methods=['GET'])
def get_first_token():
    data = {"address":"H9G3pEdKuRdyAg7ytxexJ1o4nTnyem4JkC1w6AsSpump",
            "name":"Pump Fun Puppet",
            "symbol":"PUPPET",
            "icon":"https://ipfs.io/ipfs/QmTbhWFPpLMcyV7HyAmVqjDzsTvouLyHhaEX3zNWEfSuk5",
            "holder":572,
            "creator":"5GDape2FXTo6vbjaNjDo8N2HytjdiBKAvQJEaR3wn281",
            "price":0.00004834,
            "market_cap":48341,}
    return jsonify(data)

@app.route('/top-day', methods=['GET'])
def get_top_day():
    data = {
        "date": "13.06.2024",
        "count": "489167"
    }

    # Возвращаем JSON-ответ
    return jsonify(data)

@app.route('/first-million-account', methods=['GET'])
def get_first_million_account():
    data = {
        "account": "B4RSFCHfHGspoXRu4FnfYXM6s7GEYkQfsJeDm9ABMzjJ",
    }
    # Возвращаем JSON-ответ
    return jsonify(data)

@app.route('/most-buy-less-sales', methods=['GET'])
def get_mb_ls():
    data = {
        "account": "B4RSFCHfHGspoXRu4FnfYXM6s7GEYkQfsJeDm9ABMzjJ",
        "buys": "25039",
        "sales": "180"
    }
    return jsonify(data)

@app.route('/biggest-transaction', methods=['GET'])
def get_biggest_transaction():
    data = {
        "tx": "3bG3WZXLgPmhGxSSXtVDQo6GqtfbWJih86sdjxqRDxH5v1wFuL1VQJU7A98zWSzYVdZSSn9QqSNiuCgGJCuPXgCz",
        "amount": "8543.78"
    }
    return jsonify(data)

@app.route('/most-transactions', methods=['GET'])
def get_mt_account():
    data = {
        "account": "B4RSFCHfHGspoXRu4FnfYXM6s7GEYkQfsJeDm9ABMzjJ",
        "count": "368976"
    }
    return jsonify(data)

@app.route('/most-holders-token', methods=['GET'])
def get_mh_token():
    data = {"address":"AHwhkygt1RUH1zu1U6RWutJNzkMCCKQVrJcGi26Hpump",
            "name":"GEN-Z WORM",
            "symbol":"GENZWORM",
            "icon":"https://ipfs.io/ipfs/QmY9TFx5qo7shcJjZjP14SSktLyo8Zp2m6uA84KhxSBPS2",
            "holder":419,
            "creator":"B4RSFCHfHGspoXRu4FnfYXM6s7GEYkQfsJeDm9ABMzjJ",
            "supply":"998248050489245",
            "price":0.000007990246790448174,
            "market_cap":7976.248281492836}
    return jsonify(data)
@app.route('/first-migrate', methods=['GET'])
def get_first_migrate_token():
    data = {"address":"AHwhkygt1RUH1zu1U6RWutJNzkMCCKQVrJcGi26Hpump",
            "name":"GEN-Z WORM",
            "symbol":"GENZWORM",
            "icon":"https://ipfs.io/ipfs/QmY9TFx5qo7shcJjZjP14SSktLyo8Zp2m6uA84KhxSBPS2",
            "holder":419,
            "creator":"B4RSFCHfHGspoXRu4FnfYXM6s7GEYkQfsJeDm9ABMzjJ",
            "supply":"998248050489245",
            "price":0.000007990246790448174,
            "market_cap":7976.248281492836}
    return jsonify(data)



if __name__ == '__main__':
    app.run(debug=True)

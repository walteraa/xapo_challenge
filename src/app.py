from flask import Flask, request, jsonify
import settings

main_app = Flask(__name__)

main_app.config.update(
    DB_HOST=settings.DB_HOST,
    DB_PASSWD=settings.DB_PASSWD,
    DB_DATABASE=settings.DB_DATABASE,
    DB_USER=settings.DB_USER,
)

@main_app.route("/last")
def get_last():
    from models import PriceRegistry
    query = PriceRegistry.query

    currency = request.args.get('currency', type=str)
    if currency:
        query = query.filter_by(currency = currency)
    size = request.args.get('size', default=1, type=int)
    query = query.order_by(PriceRegistry.created_at.desc()).limit(size)

    return jsonify(json_list = [ pr.serialize() for pr in query.all()]), 200

@main_app.route('/')
def hello_world():
    return 'OK', 200

if __name__ == '__main__':
    main_app.run(host='0.0.0.0', port=9000)

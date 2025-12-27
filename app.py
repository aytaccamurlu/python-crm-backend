
# from flask import Flask, request, jsonify, make_response
# from flask_cors import CORS
# from pymongo import MongoClient
# from bson import ObjectId
# import certifi
# import sys

# app = Flask(__name__)
# # CORS ayarlarını en geniş haliyle, tüm metodlara izin verecek şekilde açıyoruz
# CORS(app, resources={r"/*": {"origins": "*", "methods": ["GET", "POST", "DELETE", "OPTIONS"], "allow_headers": "*"}})

# try:
#     MONGO_URI = "mongodb+srv://aytaccamurlu26_db_user:3HwWLyyOSY1Stvaj@cluster0.vg96nxd.mongodb.net/?appName=Cluster0"
#     ca = certifi.where()
#     client = MongoClient(MONGO_URI, tlsCAFile=ca, tlsAllowInvalidCertificates=True)
#     db = client["crm_sistemi"]
#     customers_col = db["musteriler"]
#     print("✅ MongoDB Bağlantısı Başarılı")
# except Exception as e:
#     print(f"❌ MongoDB Bağlantı Hatası: {e}")

# @app.route('/customers', methods=['GET'])
# def get_customers():
#     try:
#         customers = []
#         for doc in customers_col.find():
#             customers.append({
#                 "id": str(doc["_id"]), # Frontend'e 'id' ismiyle gönderiyoruz
#                 "name": doc.get("name", ""),
#                 "email": doc.get("email", ""),
#                 "phone": doc.get("phone", ""),
#                 "status": doc.get("status", "Potansiyel")
#             })
#         return jsonify(customers)
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# @app.route('/customers', methods=['POST'])
# def add_customer():
#     try:
#         data = request.json
#         result = customers_col.insert_one(data)
#         return jsonify({"message": "Eklendi", "id": str(result.inserted_id)})
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# @app.route('/customers/<id>', methods=['DELETE', 'OPTIONS'])
# def delete_customer(id):
#     if request.method == "OPTIONS":
#         response = make_response()
#         response.headers.add("Access-Control-Allow-Origin", "*")
#         response.headers.add("Access-Control-Allow-Methods", "DELETE, OPTIONS")
#         response.headers.add("Access-Control-Allow-Headers", "*")
#         return response
#     try:
#         customers_col.delete_one({"_id": ObjectId(id)})
#         return jsonify({"message": "Silindi"})
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=5000, debug=True)
#-------------
# from flask import Flask, request, jsonify, make_response
# from flask_cors import CORS
# from pymongo import MongoClient
# from bson import ObjectId
# import certifi
# import csv
# from io import StringIO

# app = Flask(__name__)
# # Tüm metodlara (GET, POST, PUT, DELETE) ve başlıklara izin veriyoruz
# CORS(app, resources={r"/*": {"origins": "*", "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"], "allow_headers": "*"}})

# # MongoDB Bağlantısı
# MONGO_URI = "mongodb+srv://aytaccamurlu26_db_user:3HwWLyyOSY1Stvaj@cluster0.vg96nxd.mongodb.net/?appName=Cluster0"
# client = MongoClient(MONGO_URI, tlsCAFile=certifi.where(), tlsAllowInvalidCertificates=True)
# db = client["crm_sistemi"]
# customers_col = db["musteriler"]

# @app.route('/customers', methods=['GET'])
# def get_customers():
#     customers = []
#     for doc in customers_col.find():
#         customers.append({
#             "id": str(doc["_id"]),
#             "name": doc.get("name", ""),
#             "email": doc.get("email", ""),
#             "phone": doc.get("phone", ""),
#             "status": doc.get("status", "Potansiyel"),
#             "notes": doc.get("notes", "")
#         })
#     return jsonify(customers)

# @app.route('/customers', methods=['POST'])
# def add_customer():
#     data = request.json
#     result = customers_col.insert_one(data)
#     return jsonify({"message": "Eklendi", "id": str(result.inserted_id)})

# @app.route('/customers/<id>', methods=['PUT', 'OPTIONS'])
# def update_customer(id):
#     if request.method == "OPTIONS": return _build_cors_prelight_response()
#     data = request.json
#     customers_col.update_one({"_id": ObjectId(id)}, {"$set": data})
#     return jsonify({"message": "Güncellendi"})

# @app.route('/customers/<id>', methods=['DELETE', 'OPTIONS'])
# def delete_customer(id):
#     if request.method == "OPTIONS": return _build_cors_prelight_response()
#     customers_col.delete_one({"_id": ObjectId(id)})
#     return jsonify({"message": "Silindi"})

# @app.route('/customers/export', methods=['GET'])
# def export_customers():
#     si = StringIO()
#     cw = csv.writer(si)
#     cw.writerow(['Ad Soyad', 'E-posta', 'Telefon', 'Durum', 'Notlar'])
#     for doc in customers_col.find():
#         cw.writerow([doc.get('name',''), doc.get('email',''), doc.get('phone',''), doc.get('status',''), doc.get('notes','')])
#     response = make_response(si.getvalue())
#     response.headers["Content-Disposition"] = "attachment; filename=crm_listesi.csv"
#     response.headers["Content-type"] = "text/csv"
#     return response

# def _build_cors_prelight_response():
#     response = make_response()
#     response.headers.add("Access-Control-Allow-Origin", "*")
#     response.headers.add("Access-Control-Allow-Methods", "PUT, DELETE, OPTIONS")
#     response.headers.add("Access-Control-Allow-Headers", "*")
#     return response

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=5000, debug=True)
#-------------
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from pymongo import MongoClient
from bson import ObjectId
import certifi
from datetime import datetime

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*", "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"], "allow_headers": "*"}})

# MongoDB Bağlantısı
MONGO_URI = "mongodb+srv://aytaccamurlu26_db_user:3HwWLyyOSY1Stvaj@cluster0.vg96nxd.mongodb.net/?appName=Cluster0"
client = MongoClient(MONGO_URI, tlsCAFile=certifi.where(), tlsAllowInvalidCertificates=True)
db = client["crm_sistemi"]
customers_col = db["musteriler"]

@app.route('/customers', methods=['GET'])
def get_customers():
    customers = []
    for doc in customers_col.find():
        customers.append({
            "id": str(doc["_id"]),
            "name": doc.get("name", ""),
            "email": doc.get("email", ""),
            "phone": doc.get("phone", ""),
            "status": doc.get("status", "Potansiyel"),
            "notes": doc.get("notes", ""),
            "reminder_date": doc.get("reminder_date", ""),
            "created_at": doc.get("created_at", "")
        })
    return jsonify(customers)

@app.route('/customers', methods=['POST'])
def add_customer():
    data = request.json
    data['created_at'] = datetime.now().strftime("%d/%m/%Y")
    result = customers_col.insert_one(data)
    return jsonify({"message": "Eklendi", "id": str(result.inserted_id)})

@app.route('/customers/<id>', methods=['PUT', 'OPTIONS'])
def update_customer(id):
    if request.method == "OPTIONS": return _cors_response()
    data = request.json
    customers_col.update_one({"_id": ObjectId(id)}, {"$set": data})
    return jsonify({"message": "Güncellendi"})

@app.route('/customers/<id>', methods=['DELETE', 'OPTIONS'])
def delete_customer(id):
    if request.method == "OPTIONS": return _cors_response()
    customers_col.delete_one({"_id": ObjectId(id)})
    return jsonify({"message": "Silindi"})

def _cors_response():
    res = make_response(); res.headers.add("Access-Control-Allow-Origin", "*");
    res.headers.add("Access-Control-Allow-Methods", "*"); res.headers.add("Access-Control-Allow-Headers", "*");
    return res

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
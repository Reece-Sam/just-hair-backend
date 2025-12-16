 from flask import Blueprint, request, jsonify
from app.models import Service
from app import db,limiter
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity, create_refresh_token
from datetime import timedelta
    

services_bp = Blueprint("services", __name__)




#/ start of endpoint to retrieve or add a new service
@services_bp.route('/api/services', methods=['POST'])
def add_service():
    data = request.get_json()
    new_service = Service(name=data['name'],description=data['description'])

    db.session.add(new_service)
    db.session.commit()
    return jsonify(new_service.to_dict()), 201


#/start of endpoint to get all services
@services_bp.route('/api/services', methods=['GET'])
def fetch_service():
    all_service=Service.query.all()
    return jsonify([services_bp.to_dict() for service in all_service]), 200


#/start of  new endpoint to get service based on id
@services_bp.route('/api/services/<int:id>', methods=['GET'])
def get_service(id):
    service = Service.query.get(id)
    if not service:
        return jsonify({"error": "service not found"}), 404
    return jsonify(service.to_dict()), 200
#/end of endpoint





    
#/start point of delete all services
@services_bp.route('/api/services', methods=['DELETE'])
def delete_service():
    db.session.query(Service).delete()
    db.session.commit()
    return jsonify({"message": "all services deleted successfully"})
#/endpoint of delete all services


#/start point to delete a service

@services_bp.route('/api/services/<int:id>', methods=['DELETE'])
def remove_service(id):
    service = Service.query.get(id)
    if not service:
        return jsonify({"error": "service not found"}), 404
    db.session.delete(service)
    db.session.commit()
    return jsonify({"message": "service deleted successfully"})


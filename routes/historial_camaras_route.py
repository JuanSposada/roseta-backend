from flask import Blueprint, jsonify, request
from models import HistorialCamaras
from schemas import HistorialCamarasSchema
from models import db

# Blueprint historial_camaras
historial_camaras_bp = Blueprint('historial_camaras',__name__)
@historial_camaras_bp.route('/historial-camaras', methods=['GET','POST'])
def historial_camaras():
    if request.method == 'GET':
        historial_camaras_list = HistorialCamaras.query.all()
        historial_camaras_schema = HistorialCamarasSchema(many=True)
        result = historial_camaras_schema.dump(historial_camaras_list)
        return jsonify(result)
    if request.method == 'POST':
        if request.is_json:
            try:
                fecha_hora = request.json['fecha_hora']
                tipo_evento = request.json['tipo_evento']
                url_video = request.json['url_video']
                id_roseta = request.json['id_roseta']
                hist_camara = HistorialCamaras(fecha_hora=fecha_hora,tipo_evento=tipo_evento, url_video=url_video, id_roseta=id_roseta)
                db.session.add(hist_camara)
                db.session.commit()
                hist_camara_schema = HistorialCamarasSchema()
                result = hist_camara_schema.dump(hist_camara)
                return jsonify(result)
            except KeyError:
                return jsonify(message='formato, valores o tipo de dato incorrectos, solo se reciben JSON'),404
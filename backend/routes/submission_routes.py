import json

from flask import request, jsonify, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity

from constants.http_status_codes_constant import HTTP_400_BAD_REQUEST, HTTP_200_OK

from services.class_diagram_class_detection_service import component_separation
from models.actor_and_use_case import ActorANDUseCase
from services.submission_service import save_submission
from services.use_case_model_detection_service import model_object_detection

submission = Blueprint('submissions', __name__, url_prefix='/api/v1/submissions')


@submission.post('/upload')
def upload_submission():
    user_id = 1

    image = request.files['file']
    # json_data = json.loads(request.form['jsondata'])
    # submission_type = json_data['type']
    # assignment_id = json_data['id']
    # comment = json_data['comment']

    if image is None:
        return jsonify({'err': 'invalid request '}), HTTP_400_BAD_REQUEST
    elif image.filename == 'usecase.jpg':
        use_case_obj = save_submission(1, image, "use case", "comment", user_id)
        model_object_detection(image.filename, use_case_obj.id)
        return jsonify({'message': 'upload successful '}), HTTP_200_OK

    elif image.filename == 'class.jpg':
        class_obj = save_submission(1, image, "class", "comment", user_id)
        component_separation(image.filename, class_obj.id)
        return jsonify({'id': str(class_obj.id)}), HTTP_200_OK
    else:
        return jsonify({'err': 'invalid request '}), HTTP_400_BAD_REQUEST

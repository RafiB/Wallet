import json

from flask import (
    Response,
)

from flask.ext.classy import FlaskView, route


class Endpoint(FlaskView):
    route_base = '/rest/api/current/'

    @route('/ping_me', methods=['POST'])
    def ping(self):
        return Response(json.dumps(
            {
                'message': "I don't exist"
            }
        )), 404

from flask_restx import Api
from .subscriber_info import api as subscriber_info_api

api = Api(
    title="Sagewhale API",
    version="0.0.1",
    description="API that ingests JSON or CSV files containing subscriber information",
)

api.add_namespace(subscriber_info_api)

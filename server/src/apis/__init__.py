from flask_restx import Api
from .email_subscriber_info import api as email_subscriber_info_api

api = Api(
    title="Sagewhale API",
    version="0.0.1",
    description="API that ingests JSON or CSV files containing email subscriber performance data",
)

api.add_namespace(email_subscriber_info_api)

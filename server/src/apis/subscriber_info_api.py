import json
from flask_restx import Api, Resource, fields
from werkzeug.datastructures import FileStorage
from controllers.subscriber_info_controller import SubscriberInfoController
from models.responses import SuccessResponse, FailResponse
from http import HTTPStatus
from utils.database import Database


api = Api(
    title="Subscriber Info API",
    version="0.0.1",
    description="API that ingests JSON or CSV files containing subscriber information",
)
namespace = api.namespace(
    "subscriber_info",
    description="Subscriber information related operations",
)

demographics_model = namespace.model(
    "Demographics",
    {
        "id": fields.String(
            required=True,
            description="UUID identifying demographics of subscriber",
        ),
        "gender": fields.String(required=False),
        "age": fields.Integer(required=False),
        "race": fields.String(required=False),
        "marital_status": fields.String(
            required=False, description="Person's relationship with a significant other"
        ),
        "education": fields.String(
            required=False, description="Degree of achieved education"
        ),
        "household_income": fields.String(
            required=False, description="Range of household income"
        ),
    },
)

email_product_model = namespace.model(
    "EmailProduct",
    {
        "product_type": fields.String(
            required=True, description="Type of product email advertised to subscriber"
        ),
        "total_send_rate": fields.Integer(
            required=True, description="Send rate of emails sent to subscriber"
        ),
        "total_open_rate": fields.Integer(
            required=True, description="Open rate of emails sent to subscriber"
        ),
    },
)

email_performance_model = namespace.model(
    "EmailPeformance",
    {
        "id": fields.String(
            required=True,
            description="UUID identifying email performance of subscriber",
        ),
        "products": fields.List(
            fields.Nested(email_product_model),
            required=False,
            description="Product type that was emailed to subscriber",
        ),
        "subscriber_id": fields.Integer(required=True, description="Id of subscriber"),
    },
)

subscriber_model = namespace.model(
    "Subscriber",
    {
        "id": fields.String(required=True, description="UUID identifying subscriber"),
        "first_name": fields.String(
            required=False,
            description="First name of subscriber",
        ),
        "last_name": fields.String(
            required=False,
            description="Last name of subscriber",
        ),
        "full_name": fields.String(
            required=False,
            description="Full name of subscriber",
        ),
    },
)

subscriber_info_model = namespace.model(
    "SubscriberInfo",
    {
        "subscriber": fields.Nested(
            subscriber_model, required=True, description="Subscriber personal data"
        ),
        "demographics": fields.Nested(
            demographics_model,
            required=True,
            description="Statistical characteristics of subscriber",
        ),
        "email_performance": fields.Nested(
            email_performance_model,
            required=True,
            description="Performance of emails sent to subscriber",
        ),
    },
)

upload_parser = namespace.parser()
upload_parser.add_argument("file", location="files", type=FileStorage, required=True)


@namespace.route("/upload/json")
class SubscriberInfoJsonUpload(Resource):
    @namespace.expect(upload_parser)
    def post(self):
        """Store JSON file with content containing subscriber information"""
        args = upload_parser.parse_args()
        uploaded_file = args.get("file")

        if ".json" not in uploaded_file.filename:
            return (
                FailResponse(message="Requires JSON file").as_dict(),
                HTTPStatus.BAD_REQUEST,
            )

        file_content = json.loads(uploaded_file.read())
        SubscriberInfoController(Database()).save_file_content(file_content)

        return SuccessResponse(data=file_content).as_dict(), HTTPStatus.CREATED

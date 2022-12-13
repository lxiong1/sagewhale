from models.subscriber_info_models import Subscriber, Demographics, EmailPerformance


class SubscriberInfoController:
    def __init__(self, database):
        self._database = database

    def save_file_content(self, file_content):
        """Saves subscriber information into database"""
        (
            subscribers_objects,
            demographics_objects,
            email_performances_objects,
        ) = self.__map_to_objects(file_content)

        if subscribers_objects:
            self._database.save_all(subscribers_objects)
        if demographics_objects:
            self._database.save_all(demographics_objects)
        if email_performances_objects:
            self._database.save_all(email_performances_objects)

    def __map_to_objects(self, file_content):
        subscribers_objects = []
        demographics_objects = []
        email_performances_objects = []

        for row in file_content:
            subscriber_id = row.get("id")
            if self._database.session.get(Subscriber, subscriber_id):
                continue

            subscriber = Subscriber(
                **{
                    key: value
                    for key, value in row.items()
                    if key in ["id", "first_name", "last_name", "full_name"]
                }
            )
            subscribers_objects.append(subscriber)

            demographics_data = {"subscriber_id": subscriber_id} | {
                **{
                    key: value
                    for key, value in row.get("demographics").items()
                    if key
                    in [
                        "id",
                        "gender",
                        "age",
                        "race",
                        "marital_status",
                        "education",
                        "household_income",
                    ]
                }
            }
            demographics = Demographics(**demographics_data)
            demographics_objects.append(demographics)

            email_performance_data = {"subscriber_id": subscriber_id} | {
                **{
                    key: value
                    for key, value in row.get("email_performance").items()
                    if key in ["id", "products"]
                }
            }
            email_performance = EmailPerformance(**email_performance_data)
            email_performances_objects.append(email_performance)

        return subscribers_objects, demographics_objects, email_performances_objects

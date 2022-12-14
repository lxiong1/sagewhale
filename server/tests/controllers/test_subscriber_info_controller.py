from controllers.subscriber_info_controller import SubscriberInfoController


def describe_get_all_subscriber_info():
    def test_should_retrieve_all_subscriber_info(mocker, db_mock):
        db_mock.session.execute.return_value = mocker.Mock(name="CursorResult")
        db_mock.session.execute.return_value.mappings.return_value.all.return_value = []
        controller = SubscriberInfoController(db_mock)

        result = controller.get_all_subscriber_info()

        assert result == []


def describe_save_file_content():
    def test_should_save_subscriber_info_to_db(db_mock, file_content):
        db_mock.session.get.return_value = None
        controller = SubscriberInfoController(db_mock)

        controller.save_file_content(file_content)

        assert db_mock.save_all.call_count == 3

    def test_should_not_save_subscriber_info_when_nothing_to_save(
        db_mock, file_content
    ):
        db_mock.session.get.return_value = "anything"
        controller = SubscriberInfoController(db_mock)

        controller.save_file_content(file_content)

        assert db_mock.save_all.call_count == 0

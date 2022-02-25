from app.config import schedule_parser


class TestConfig:
    def test_schedule_parser(self):
        test_data = {
            'args': '0:0; 0; 000:0', 'result': (0, 0, 0,)
        }
        assert schedule_parser(test_data['args']) == test_data['result']

        test_data = {
            'args': '20:02; 999:999', 'result': (72120, 3656340,)
        }
        assert schedule_parser(test_data['args']) == test_data['result']

        test_data = {
            'args': '', 'result': (0,)
        }
        assert schedule_parser(test_data['args']) == test_data['result']

        test_data = {
            'args': '-1:02; 20:02; 4:01; 2+4', 'result': (0, 72120, 14460, 0,)
        }
        assert schedule_parser(test_data['args']) == test_data['result']

        # for test_data in test_data_set:
        #     assert schedule_parser(test_data['args']) == test_data['result'], f'\nError\n{test_data["args"]=}{test_data["result"]=}'

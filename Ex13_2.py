import requests
import pytest

class TestUserAgent:
    user_agents = [
        ("Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30", {'platform': 'Mobile', 'browser': 'No', 'device': 'Android'}),
        ("Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1", {'platform': 'Mobile', 'browser': 'Chrome', 'device': 'iOS'}),
        ("Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)", {'platform': 'Googlebot', 'browser': 'Unknown', 'device': 'Unknown'}),
        ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0", {'platform': 'Web', 'browser': 'Chrome', 'device': 'No'}),
        ("Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1", {'platform': 'Mobile', 'browser': 'No', 'device': 'iPhone'})
    ]

    @pytest.mark.parametrize('user_agent, expected_value', user_agents)
    def test_user_agent(self, user_agent, expected_value):
        url = 'https://playground.learnqa.ru/ajax/api/user_agent_check'
        data = {"User-Agent": user_agent}

        response = requests.get(url, headers=data)

        assert response.status_code == 200, "Wrong status code"

        response_dict = response.json()

        assert "platform" in response_dict, "В ответе нет поля 'platform'"
        assert "browser" in response_dict, "В ответе нет поля 'browser'"
        assert "device" in response_dict, "В ответе нет поля 'device'"

        actual_platform = response_dict['platform']
        actual_browser = response_dict['browser']
        actual_device = response_dict['device']

        expected_platform = expected_value['platform']
        expected_browser = expected_value['browser']
        expected_device = expected_value['device']

        assert actual_platform == expected_platform, f"Actual platform '{actual_platform}' not equal expected platform {expected_platform}"
        assert actual_browser == expected_browser, f"Actual browser '{actual_browser}' not equal expected browser {expected_browser}"
        assert actual_device == expected_device, f"Actual device '{actual_device}' not equal expected device {expected_device}"


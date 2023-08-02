import pytest
import requests

class TestUserAgent:
    user_agent = [
        ("Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"),
        ("Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1"),
        ("Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"),
        ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0"),
        ("Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1")
    ]
    @pytest.mark.parametrize('UserAgent', user_agent)
    def test_user_agent(self, UserAgent):
        url = "https://playground.learnqa.ru/ajax/api/user_agent_check"
        headers = {"User-Agent":UserAgent}


        response = requests.get(url, headers=headers)

        response_dict = response.json()


        assert "platform" in response_dict, "There is no field 'platform' in the header"
        assert "browser" in response_dict, "There is no field 'browser' in the header"
        assert "device" in response_dict, "There is no field 'device' in the header"

        if UserAgent == self.user_agent[0]:
            expected_values = {'platform': 'Mobile', 'browser': 'No', 'device': 'Android'}
        elif UserAgent == self.user_agent[1]:
            expected_values = {'platform': 'Mobile', 'browser': 'Chrome', 'device': 'iOS'}
        elif UserAgent == self.user_agent[2]:
            expected_values = {'platform': 'Googlebot', 'browser': 'Unknown', 'device': 'Unknown'}
        elif UserAgent == self.user_agent[3]:
            expected_values = {'platform': 'Web', 'browser': 'Chrome', 'device': 'No'}
        elif UserAgent == self.user_agent[4]:
            expected_values = {'platform': 'Mobile', 'browser': 'No', 'device': 'iPhone'}
        else:
            expected_values = f"There is no values"

        actual_values = {"platform":response_dict["platform"], "browser":response_dict["browser"], "device":response_dict["device"]}
        assert actual_values == expected_values, "Actual text in the response is not correct"
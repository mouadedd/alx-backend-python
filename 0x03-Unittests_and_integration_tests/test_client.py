#!/usr/bin/env python3
"""test client"""
from io import StringIO
import unittest
from client import GithubOrgClient as git
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, PropertyMock
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """parameterized and patch as decorators"""
    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch("client.get_json")
    def test_org(self, feed, mocked):
        """test the return of link"""
        test = git(feed)
        test.org()
        mocked.called_with_once(test.ORG_URL.format(org=feed))

    def test_public_repos_url(self):
        """ 5-mocking a property """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock:
            payload = {"repos_url": "Hello World"}
            mock.return_value = payload
            test = git('test')
            output = test._public_repos_url
            self.assertEqual(output, payload["repos_url"])

    @patch("client.get_json")
    def test_public_repos(self, mocked):
        """6-more patching"""
        payload = [{"name": "Google"}, {"name": "YouTube"}]
        mocked.return_value = payload

        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock) as mock:
            mock.return_value = "hello world"
            test = git("test")
            output = test.public_repos()

            wanted = [value["name"] for value in payload]
            self.assertEqual(output, wanted)
            mock.assert_called_once()
            mocked.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, state):
        """ 7-parameterized test has_license """
        output = git.has_license(repo, license_key)
        self.assertEqual(output, state)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """8. Integration test: fixtures"""
    @classmethod
    def setUpClass(cls):
        """method called befor test is ran"""
        conf = {'return_value.json.side_effect':
                [
                    cls.org_payload, cls.repos_payload,
                    cls.org_payload, cls.repos_payload
                ]}
        cls.get_patcher = patch('requests.get', **conf)
        cls.mock = cls.get_patcher.start()

    def test_public_repos(self):
        """advanced part 1"""
        self.assertEqual(git("google").public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """advanced part 2"""
        self.assertEqual(git("google").public_repos(license="apache-2.0"),
                         self.apache2_repos)

    @classmethod
    def tearDownClass(cls):
        """method called after running test"""
        cls.get_patcher.stop()


if __name__ == '__main__':
    unittest.main()

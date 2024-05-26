#!/usr/bin/env python3
"""test client"""
import unittest
from client import GithubOrgClient as git
from parameterized import parameterized
from unittest.mock import patch, PropertyMock


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
        def test_has_licence(self, repo, license_key, state):
            """ 7- parameterized """
            output = GithubOrgClient.has_license(repo, license_key)
            self.assertEqual(output, state)

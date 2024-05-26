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

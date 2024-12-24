import sys
import os
import unittest

sys.path.append('C:/Users/DNS/PycharmProjects/search/algorithms-project-69/')

from search_engine.search_engine import search


class TestSearchFunction(unittest.TestCase):

    def test_empty_docs(self):
        """Test for empty docs"""
        result = search([], 'test')
        self.assertEqual(result, [])

    def test_empty_query(self):
        """Test for empty query"""
        result = search([{'id': '1', 'text': 'this is a test'}], '')
        self.assertEqual(result, [])

    def test_no_matching_query(self):
        """Test with not found response"""
        docs = [{'id': '1', 'text': 'this is a test'}, {'id': '2', 'text': 'hello world'}]
        result = search(docs, 'notfound')
        self.assertEqual(result, [])

    def test_single_matching_query(self):
        """Test with one result response"""
        docs = [{'id': '1', 'text': 'this is a test'}, {'id': '2', 'text': 'hello world'}]
        result = search(docs, 'test')
        self.assertEqual(result, ['1'])

    def test_multiple_matching_queries(self):
        """Test with few results response"""
        docs = [
            {'id': '1', 'text': 'this is a test'},
            {'id': '2', 'text': 'no match here'},
            {'id': '3', 'text': 'test is great'},
        ]
        result = search(docs, 'test')
        self.assertEqual(result, ['1', '3'])

    def test_case_sensitivity(self):
        """Test with case-sensitive"""
        docs = [{'id': '1', 'text': 'This is a Test'}]
        result = search(docs, 'test')
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()

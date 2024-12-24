from typing import List, Dict


def search(docs: List[Dict[str, str]], query: str) -> List[str]:
    docs_with_query = []
    if not docs or not query:
        return docs_with_query

    for doc in docs:
        text = doc.get('text')
        if text and query in text.split():
            docs_with_query.append(doc['id'])

    return docs_with_query

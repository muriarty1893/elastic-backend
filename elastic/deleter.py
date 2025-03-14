from .client import create_elastic_client

class IndexDeleter:
    def __init__(self, indexname="kadir"):
        self.indexname = indexname
        self.client = create_elastic_client()

    def delete_all_data(self):
        response = self.client.delete_by_query(
            index=self.indexname,
            body={"query": {"match_all": {}}}
        )
        print(response)


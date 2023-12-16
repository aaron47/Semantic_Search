import config

from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer
import streamlit as st
from translator import TunisianTranslator


class SearchApplication:
    __index_name = "french_products"

    def __init__(self) -> None:
        try:
            self.es: Elasticsearch = Elasticsearch(
                hosts=config.HOSTS,
                basic_auth=config.HTTP_AUTH,
                ca_certs=config.CA_CERTS,
                verify_certs=config.VERIFY_CERTS)
        except ConnectionError as e:
            print(f"Connection Error {e}")

        if self.es.ping():
            print("Successfully connected!")
        else:
            print("Oops!! There was an error")

        self.model: SentenceTransformer = SentenceTransformer("all-mpnet-base-v2")

    def search(self, input_keyword: str):
        tunisian_translator = TunisianTranslator()
        translated_keyword = tunisian_translator.translate(input_keyword)

        vector_of_input_keyword = self.model.encode(translated_keyword)

        query = {
            "field": "DescriptionVector",
            "query_vector": vector_of_input_keyword,
            "k": 10,
            "num_candidates": 500,
        }

        res = self.es.knn_search(index=self.__index_name, knn=query, source=["ProductName", "Description"])

        results = res["hits"]["hits"]

        return results

    def run(self) -> None:
        st.title("Search Myntra Fashion Products")

        search_query = st.text_input("Enter your search query")

        # Input: Users enters search query
        if st.button("Search"):
            if search_query:
                # Perform the search and get resutls
                results = self.search(search_query)

                # Display search results
                st.subheader("Search Results")

                for result in results:
                    with st.container():
                        if "_source" in result:
                            print(result)
                            try:
                                st.header(f"{result['_source']['ProductName']}")
                            except Exception as e:
                                print(e)

                            try:
                                st.write(f"Description: {result['_source']['Description']}")
                            except Exception as e:
                                print(e)
                            st.divider()


if __name__ == "__main__":
    SearchApplication().run()

from http import HTTPStatus 

import pytest
import aiohttp
from sqlalchemy import text

from fastapi.testclient import TestClient

from main import app

class TestApi:
    
    # @pytest.mark.asyncio(loop_scope="session")
    # async def test_add_api(self):

    #     session =aiohttp.ClientSession()


    #     req_url = "http://localhost:8000/api/v1/roles/create_role/"
        
    #     query_data = {"name": "admin", "level": 5}


    #     response = await session.request(
    #         "POST",
    #         req_url,
    #         json=query_data,
    #         params=None

    #     )

    #     assert response.status == HTTPStatus.ACCEPTED


    @pytest.mark.asyncio
    async def test_add_api(self, make_request, test_session):

    
        async with test_session as session:
            req_url = "http://localhost:8000/api/v1/roles/create_role/"  
            query_data = {"name": "user2", "level": 2}


            response = await make_request(
                "POST",
                req_url,
                params=query_data
            )

            dql_query = "SELECT name FROM roles WHERE level = 2"
            query_db = await session.execute(text(dql_query))

            result_db = query_db.scalars().one() 

            assert result_db == "user2"


            assert response.status == HTTPStatus.ACCEPTED



    @pytest.mark.asyncio
    async def test_add_fast_api(self, make_request, test_session):

    
        async with test_session as session:
            client = TestClient(app)
            req_url = "/api/v1/roles/create_role/"   
            query_data = {"name": "user2", "level": 2}


            response = client.post(req_url, json=query_data)

            # response = await make_request(
            #     "POST",
            #     req_url,
            #     params=query_data
            # )

            dql_query = "SELECT name FROM roles WHERE level = 2"
            query_db = await session.execute(text(dql_query))

            result_db = query_db.scalars().one() 

            assert result_db == "user2"


            assert response.status_code == HTTPStatus.ACCEPTED

    



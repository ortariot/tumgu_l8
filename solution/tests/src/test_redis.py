import pytest

from db.cacheservice import cache



class TestRedis:

    def test_eq(self):

        assert 1 == 1


    @pytest.mark.parametrize("a, b", [(1,1), (2, 2), (3, 3)])
    def test_eq_any(self, a, b):

        assert a == b

    
    # @pytest.mark.parametrize("a", [1, 2, 3])
    # @pytest.mark.parametrize("b", [1, 2, 3])
    # def test_eq_any(self, a, b):

    #     assert a == b


    @pytest.mark.parametrize(
            "query_data, answer",
            [
                (
                    {
                        "key": "hello",
                        "value": "world"
                    },
                    {
                        "key": "hello",
                        "value": "world"
                    },                       
                ),
                (
                    {
                        "key": 1,
                        "value": "world"
                    },
                    {
                        "key": 1,
                        "value": "world"
                    },                       
                ),
                   (
                    {
                        "key": "hello",
                        "value": 1
                    },
                    {
                        "key": "hello",
                        "value": 1
                    },                       
                ),
                (
                    {
                        "key": "hello",
                        "value": {"a": 1, "b": 10}
                    },
                    {
                        "key": "hello",
                        "value": {"a": 1, "b": 10}
                    },                       
                ),
            ]

    )
    @pytest.mark.asyncio(loop_scope="session")
    async def test_add(self, query_data, answer):


        await cache.add(key=query_data["key"], value=query_data["value"])
        result = await cache.get(answer["key"])
        assert result == answer["value"]
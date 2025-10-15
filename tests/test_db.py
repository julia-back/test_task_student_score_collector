# import pytest
# from app import User
# from tests.conftest import created_test_db
#
#
# @pytest.mark.asyncio
# async def test(created_test_db):
#     user = User(username="testuser", first_name="Test", last_name="Testy")
#
#     from app.database import db_manager
#     async for session in db_manager.get_session():
#         assert db_manager.db_url == ""
#         session.add(user)
#         await session.commit()
#         user = await session.refresh(user)
#
#         assert user.username == "testuser"
#         assert user.id is not None

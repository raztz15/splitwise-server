import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from controllers.activities import ActivitiesRouter
from controllers.debts import DebtsRouter
from controllers.groups import GroupsRouter
from splitwise_services import UserService, GroupService, DebtsService, ActivitiesService
from controllers import UsersRouter


app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def init_app():
    users_service = UserService()
    users_router = UsersRouter(users_service)
    groups_service = GroupService()
    groups_router = GroupsRouter(groups_service)
    debts_service = DebtsService()
    debts_router = DebtsRouter(debts_service)
    activities_service = ActivitiesService()
    activities_router = ActivitiesRouter(activities_service)
    app.include_router(users_router, prefix="/users")
    app.include_router(groups_router, prefix="/groups")
    app.include_router(debts_router, prefix="/debts")
    app.include_router(activities_router, prefix="/activities")


if __name__ == "__main__":
    init_app()
    uvicorn.run(app)

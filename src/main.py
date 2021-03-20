from api.query import Query
from api.mutation import Mutation
from api.file import file_api
from config import db_url
from model.config import Config

import graphene
import mongoengine
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.graphql import GraphQLApp

mongoengine.connect(host=db_url)
Config.initialize()

import job

app = FastAPI()
app.add_route("/api/graphql", GraphQLApp(schema=graphene.Schema(query=Query, mutation=Mutation)))
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(file_api, prefix="/api/v1")
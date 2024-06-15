# schema.py
import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models import ToDo as ToDoModel, db
from datetime import datetime

class ToDoObject(SQLAlchemyObjectType):
    class Meta:
        model = ToDoModel

class Query(graphene.ObjectType):
    all_todos = graphene.List(ToDoObject, user_id=graphene.String(required=True))

    def resolve_all_todos(self, info, user_id):
        query = ToDoObject.get_query(info)
        return query.filter(ToDoModel.user_id == user_id).all()

class CreateToDo(graphene.Mutation):
    id = graphene.Int()
    title = graphene.String()
    description = graphene.String()
    time = graphene.DateTime()
    user_id = graphene.String()

    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String(required=True)
        time = graphene.DateTime(required=True)
        user_id = graphene.String(required=True)

    def mutate(self, info, title, description, time, user_id):
        todo = ToDoModel(title=title, description=description, time=time, user_id=user_id)
        db.session.add(todo)
        db.session.commit()
        return CreateToDo(id=todo.id, title=todo.title, description=todo.description, time=todo.time, user_id=todo.user_id)

class Mutation(graphene.ObjectType):
    create_todo = CreateToDo.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)

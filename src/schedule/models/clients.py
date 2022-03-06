from pydantic import BaseModel


class ClientBase(BaseModel):
    last_name: str
    first_name: str
    middle_name: str
    email: str
    phone_number: str


class Client(ClientBase):
    id: int

    class Config:
        orm_mode = True

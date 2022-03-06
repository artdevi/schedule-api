from pydantic import BaseModel


class Client:
    id: int
    last_name: str
    first_name: str
    middle_name: str
    email: str
    phone_number: str

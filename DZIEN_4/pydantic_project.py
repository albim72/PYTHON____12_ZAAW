from pydantic import Field
from pydantic.dataclasses import dataclass
import dataclasses
from typing import List,Optional

@dataclass
class User:
    id:int
    name:str="Jan Kowalski"
    friends: List[int] = dataclasses.field(default_factory=lambda : [0])
    age:Optional[int] = dataclasses.field(default=None,metadata=dict(title='Wiek użytkownika',description='nie kłam!'))
    height:Optional[int] = Field(None,title='wzrost w cm',ge=50,le=300)


user= User(id='33')
# print(user.__pydantic_model__.schema())
us1 = User(55,"Olga Kot",[2,],56,177)
print(us1)

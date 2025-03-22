# pydantic

from pydantic import BaseModel, ValidationError, Field, validate_email, validator, root_validator


class City(BaseModel):
    city_id: int
    name: str = Field(alias="cityFullName")

input_json = """
[    
    {
        "city_id": 1,
        "cityFullName": "st.Alamty"
    },
    {
        "city_id": 2,
        "cityFullName": "stAstana"
    }
]

"""

input_json2 = """

    {
        "city_id": 1,
        "cityFullName": "st.Almaty"
    }
"""

try:
    city = City.parse_raw(input_json2)
except ValidationError as e:
    print(e.json())
else:
    print(city.json(by_alias=True))
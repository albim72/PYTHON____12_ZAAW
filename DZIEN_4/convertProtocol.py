from typing import Protocol, Union

#protokól
class Covertible(Protocol):
    def convert(self,data:str)->Union[int,float]:
        pass

#implementacje protokołu
class IntegerConverter:
    def convert(self,data:str)->int:
        return int(data)

class FloatConverter:
    def convert(self,data:str)->float:
        return float(data)

class BoolConverter:
    def convert(self,data:str)->bool:
        return bool(data)

def convert_data(converter:Covertible,data:str)->Union[int,float]:
    return converter.convert(data)


int_converter = IntegerConverter()
float_convereter = FloatConverter()
b_conv = BoolConverter()

result_int = convert_data(int_converter,"55")
result_float = convert_data(float_convereter,"5.77")
r_bool = convert_data(b_conv,"1")

ri = result_int
rf = result_float
rb = r_bool
print(f"Przekonwertowano na int: {ri}")
print(type(ri))
print(f"Przekonwertowano na float: {rf}")
print(type(rf))
print(f"Przekonwertowano na bool: {rb}")
print(type(rb))

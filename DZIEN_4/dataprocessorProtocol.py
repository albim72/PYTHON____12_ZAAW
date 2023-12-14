from typing import Protocol, List, Any

#protokół
class DataProcessor(Protocol):
    def process(self,data:List[Any])->List[Any]:
        pass


#klasa implementująca protokół DataProcessor dla operacji na liczbach
class NumberProcessor:
    def process(self, data: List[Any]) -> List[Any]:
        return [item*2 for item in data if isinstance(item,int) or isinstance(item,float)]


#klasa implementująca protokół DataProcessor dla operacji na ciągach znaków
class StringProcessor:
    def process(self, data: List[Any]) -> List[Any]:
        return [item.upper() for item in data if isinstance(item,str)]


#funkcja przyjmująca obiekt zgodny z protokołem DataProcessor
def process_data(processor:DataProcessor, data:List[Any]) -> List[Any]:
    return processor.process(data)

number_processor = NumberProcessor()
string_processor = StringProcessor()

data_to_process = [1,2,5.5,"hej","czerwony"]

proc_nb = process_data(number_processor,data_to_process)
proc_str = process_data(string_processor,data_to_process)

print(f"Wynik dla liczb:{proc_nb}")
print(f"Wynik dla znaków:{proc_str}")

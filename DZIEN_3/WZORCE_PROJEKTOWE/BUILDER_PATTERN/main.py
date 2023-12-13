from director import Director
from concretebuilder1 import ConcreteBuilder1

director = Director()
builder = ConcreteBuilder1()

director.builder = builder

print('\nProdukt podstawowy:')
director.build_minimal_version()
builder.product.list_parts()


print('\nProdukt pełny:')
director.build_full_version()
builder.product.list_parts()

print('\nProdukt użytkowmnika...:')
builder.produce_part_a()
builder.produce_part_c()
builder.product.list_parts()

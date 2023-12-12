class ContextManager(object):
    def __init__(self):
        print("inicjacja funkcji init()")

    def __enter__(self):
        print("inicjacja funkcji enter()")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("inicjacja funkcji exit()")

with ContextManager() as manager:
    print("działania wewnątrz instrukcji with")

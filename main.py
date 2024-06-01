from packages.Telegram.testRun import run_tests
from packages.Telegram.Client import Client
if __name__ == "__main__":
    # Initialize the client
    client = Client()
    instance = client.create_instance()
    
    # Create instance
    with instance:
        instance.loop.run_until_complete(run_tests(client))

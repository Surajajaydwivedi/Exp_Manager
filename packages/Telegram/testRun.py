# test_runner.py
from ..History.ChatHistory import ChatHistory

history = ChatHistory()

async def run_tests(client):
    
    # Test get_user_details
    # await client.get_user_details()
    
    # Test send_message
    # await client.send_message('Hello, world!')
    
    # Test send_doc
    # Assuming you have a file named 'sample_document.txt' in the same directory
    # with open('sample_document.txt', 'rb') as file:
    #     await client.send_doc(file)
    
    contacts = await client.get_dialogues()
    print(contacts,'sdsdsdsdsdsd')
    history.update_user_list(contacts)
    history.save_to_data()
    # history.print_data()
    
    # Test get_messages
    # for contact in contacts:
    #     await client.get_messages({'id':contact})

# if __name__ == "__main__":
#     # Initialize the client
#     client = Client()
    
#     # Create instance
#     client.create_instance()
#     with client:
#         client.loop.run_until_complete(run_tests(client))

# test_runner.py
from ..History.ChatHistory import ChatHistory
from ..Utils.constants import SUCCESS, FAILED, ME, ID,AUTH_ID,AUTH_HASH

history = ChatHistory()

DEFAULT_CHANNEL_NAME = 'Default Channel Name'
DEFAULT_CHANNEL_ABOUT = 'Default About'

memory={}

async def get_user_details_test(client):
    await client.get_user_details()

async def send_message_test(client):
    await client.send_message('Hello, world!')

async def send_doc_test(client):
    # Assuming you have a file named 'sample_document.txt' in the same directory
    with open('sample_document.txt', 'rb') as file:
        await client.send_doc(file)

async def get_contacts(client):
    if 'contacts' in memory:
        return memory.contacts
    
    contacts =  await client.get_dialogues()
    memory['contacts']=contacts
    return contacts

async def get_contacts_and_update_history(client):
    contacts = await get_contacts(client)
    print(contacts, 'sdsdsdsdsdsd')
    history.update_user_list(contacts)
    history.save_to_data()

async def get_messages_test(client):
    contacts = await get_contacts(client)
    for contact in contacts:
        await client.get_messages(contact)
    
async def channel_exists(contacts, channel_name):
    return any(contact['name'] == channel_name for contact in contacts)

async def create_test_channel(client):
    try:
        contacts = await get_contacts(client)
        print(contacts)
        if await channel_exists(contacts, DEFAULT_CHANNEL_NAME):
            print('Channel Already Exists')
            return FAILED

        request={'title':DEFAULT_CHANNEL_NAME,'about':DEFAULT_CHANNEL_ABOUT}
        await client.create_channel(request)
        print(SUCCESS)
        return SUCCESS
    except Exception as e:
        print(f"Error: {e}")
        return FAILED

async def run_tests(client):
    # await get_user_details_test(client)
    # await send_message_test(client)
    # await send_doc_test(client)
    # await get_contacts_and_update_history(client)
    # await get_messages_test(client)
    await create_test_channel(client)

# if __name__ == "__main__":
#     # Initialize the client
#     client = Client()
    
#     # Create instance
#     client.create_instance()
#     with client:
#         client.loop.run_until_complete(run_tests(client))

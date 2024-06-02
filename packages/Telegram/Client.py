from telethon import TelegramClient
from ..Utils.constants import SUCCESS, FAILED, ME, ID,AUTH_ID,AUTH_HASH
from packages.Utils.utils import convert_date
import os
from dotenv import load_dotenv
from pathlib import Path
from telethon import functions, types



# from ..Utils.constants import SUCCESS, FAILED, ME
# from ..Utils.utils import convert_date
# from dotenv import load_dotenv, dotenv_values 

class Client:
    dotenv_path = Path('.env')
    load_dotenv(dotenv_path)

    def __init__(self):
        self._api_id = os.getenv(AUTH_ID)
        self._api_hash = os.getenv(AUTH_HASH)
        print(self._api_hash,self._api_id)
        self._contacts = {}

    def create_instance(self) -> None:
        """Create a new instance of the Telegram client."""
        self._client = TelegramClient('anon', self._api_id, self._api_hash)
        return self._client

    async def get_user_details(self):
        """Fetch and print details of the currently authenticated user."""
        me = await self._client.get_me()
        print("User Details:")
        print("Username:", me.username)
        print("Phone:", me.phone)
        print("All Data:",me.stringify())
        print()
        return SUCCESS
    
    async def send_message(self, message='Default Message', to=None):
        """
        Send a message to a user or chat.

        Examples:
            # Send a message with markdown and without link preview to 'me'
            message = await client.send_message(
                'me',
                'This message has **bold**, `code`, __italics__ and '
                'a [nice website](https://example.com)!',
                link_preview=False
            )

            # Send a message to a specific chat ID
            await client.send_message(-100123456, 'Hello, group!')

            # Send a message to a contact
            await client.send_message('+34600123123', 'Hello, friend!')

            # Send a message to a username
            await client.send_message('username', 'Testing Telethon!')
        """
        if to is None:
            to = ME
        await self._client.send_message(to, message)
        return SUCCESS
    
    async def send_doc(self, doc, to=None):
        """Send a document to a user or chat."""
        if to is None:
            to = ME
        if not doc:
            return FAILED
        await self._client.send_file(to, doc)
        return SUCCESS

    async def get_messages(self, request=None):
        """
        Fetch and print messages from the 'me' chat.

        Examples:
            # Download media from messages if available
            for message in self._client.iter_messages('me'):
                if message.photo:
                    path = await message.download_media()
                    print('File saved to', path)  # printed after download is done
        """
        if not request:
            return FAILED
        id=request[ID]
        async for message in self._client.iter_messages(id,limit=10):
            date = convert_date(message.date)
            print("Message Details:")
            print("ID:", message.id)
            print("Text:", message.text)
            print("Date:", date, message.date)
            print("From ID:", message.from_id)
            print("Peer ID:", message.peer_id)
            print()
    
    async def get_dialogues(self): 
        dialog_ids=[]
        print('HEY')
        async for dialog in self._client.iter_dialogs():
            print(dialog.name, 'has ID', dialog.id)
            dialog_ids.append({'name':dialog.name,ID:dialog.id})
        return dialog_ids
    
    async def create_channel(self,request) -> str:
        # title=request.title,
        # about=request.about,
        # megagroup=request.megagroup,
        # for_import=request.for_import,
        # forum=request.forum,
        # geo_point=types.InputGeoPoint(
        #     lat=request.lat,
        #     long=request.long,
        #     accuracy_radius=request.accuracy_radius
        # ),
        # address=request.address,
        # ttl_period=request.ttl_period
        if not request or not request['title']:
            return FAILED
        try:
            result = await self._client(functions.channels.CreateChannelRequest(request))
            print(result.stringify())
            return SUCCESS
        except Exception as e:
            print(f"Error: {e}")
            return FAILED

# Example usage:
# client = Client()
# with client:
#     client.loop.run_until_complete(main())
# client.create_instance()
# await client.get_user_details()
# await client.send_message('Hello, world!')
# await client.get_messages()

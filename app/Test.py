import os
from getpass import getpass
import transkribus.pagexml as tk
from transkribus import TranskribusAPI, options_from_env
from transkribus.models import Collection

api = TranskribusAPI(**options_from_env())

collection_name = "Maximo Gomez"
collection = api.list_collections()
collection_id = next((c["colId"] for c in collection if c["colName"] == collection_name), None)

if not collection_id:
    collection = api.create_collection(collection_name)
    collection_id = collection["colId"]
    print(f"✅ Colección creada: {collection_name}")
else:
    print(f"📁 Usando colección existente: {collection_name}")

collection_obj = Collection(collection_id)
folder = os.path.join(os.getcwd(),"Fotos")

for dir in os.listdir(folder):
    new_folder = os.path.join(folder,dir)
    for file in os.listdir(new_folder):
        imagenes = sorted([f for f in os.listdir(new_folder) if f.lower().endswith(".jpg")])
        for imagen in imagenes:
            api.upload_page_image(col_id=collection_id,file=file,title=new_folder)
            print(f"📤 Subida: {file}")


from app import db, session, abort, firestore,os, config, make_response
from app.houses.models.house_model import House


def create_new_house(data):
    try:
        pos = data[u'pos']
        features = data[u'features']
        address = data[u'address']
        contact = data[u'contact']
        services = data[u'services']
        title = data[u'title']
        images = data[u'images']
        public_opinion = data[u'public_opinion']
        meta = data[u'meta']
        description = data[u'description']
        parent_category_id = data[u'parent_category_id']
        sub_category_id = data[u'sub_category_id']
    
        if(pos != None, features != None, address != None, contact != None, title != None, images != None, services != None, public_opinion != None, meta != None, description != None, parent_category_id != None, sub_category_id != None ):
            # try:
            print(data)
            data = House( pos=pos, features=features, address=address, contact=contact, title=title, images=images, services=services, public_opinion=public_opinion, meta=meta, description=description, parent_category_id=parent_category_id, sub_category_id=sub_category_id )
            _data = data.to_dict()
            db.collection(u'Places').add({
                u'pos' : { 
                    u'geohash': _data[u'pos'][u'geohash'],
                    u'geopoint': firestore.GeoPoint(_data[u'pos'][u'geopoint'][u'latitude'], _data[u'pos'][u'geopoint'][u'longitude'])
                    },
                u'features': _data[u'features'],
                u'address': _data[u'address'],
                u'contact': _data[u'contact'],
                u'open_hours': _data[u'open_hours'],
                u'category': _data[u'category'],
                u'title': _data[u'title'],
                u'images': _data[u'images'],
                u'services': _data[u'services'],
                u'public_opinion': _data[u'public_opinion'],
                u'meta': _data[u'meta'],
                u'description': _data[u'description'],
                u'parent_category_id': _data[u'parent_category_id'],
                u'sub_category_id': _data[u'sub_category_id']
            })
            print("=======> added to database")
            return data.to_dict()
    except Exception as e:
        return {
            "error": e,
            "suggest":"make sure the incoming data has the correct expected fields"
        } 
       


def read_house(data, method="all"):
    try:
        if(method == "all"):
            
            house = db.collection(u'Apartments').stream()
            for i in house:
                return(f'{i.id} : {i.to_dict()}')

        elif(method == 1):
            house = db.collection(u'Apartments').document(data["id"]).get()
            print(data)
            return house.to_dict()
    except Exception as e:
        return {
            "error": e,
            "suggest":"make sure the incoming data has the correct expected fields"
        } 


def update_house(data, method="rating"):
    try:
        if(method=="rating"):
            id = data["id"]
            print(id)
            new_update = {"rating":data["rating"]}
            print(new_update)
            rating = db.collection(u'Apartments').document(id).update(new_update)
            print(new_update)
            return "Updated"
    except Exception as e:
        return {
            "error": e,
            "suggest":"make sure the incoming data has the correct expected fields"
        } 

from app import db, session, abort, firestore,os, config, make_response
from app.user.models.user_model import Places


def create_new_place(data):
    title = data[u'title']
    description = data[u'description']
    cordinate = data[u'cordinate']
    image_url = data[u'image_url']
    services = data[u'services']
    contact = data[u'contact']
    meta = data[u'meta']
    rating = data[u'rating']

    # using dummy photourl if none is provided
    if u'image_url' in data:
        image_url = data[u'image_url']
    else:
        image_url = u'https://t3.ftcdn.net/jpg/03/46/83/96/360_F_346839683_6nAPzbhpSkIpb8pmAwufkC7c5eD7wYws.jpg'
    if(title != None and cordinate != None and description != None and rating != None and meta != None and services != None):
        # try:
        print(data)
        data = Places(title=title, description=description, cordinates=cordinate, image_url=image_url, services=services, contact=contact, meta=meta, rating=rating)
        db.collection(u'Places').add(data.to_dict())
        print("=======> added to database")
        return data.to_dict()
        # except Exception as err:
        #     return {
        #         "error": err
        #     }


def read_place(data, method="all"):
    if(method == "all"):
        
        place = db.collection(u'Places').stream()
        for i in place:
            return(f'{i.id} : {i.to_dict()}')

    elif(method == 1):
        place = db.collection(u'Places').document(data["id"]).get()
        print(data)
        return place.to_dict()


def update_place(data, method="rating"):

    if(method=="rating"):
        id = data["id"]
        print(id)
        new_update = {"rating":data["rating"]}
        print(new_update)
        rating = db.collection(u'Places').document(id).update(new_update)
        print(new_update)
        return "Updated"
     
            #  return {
            #      "error": err,
            #      "suggest":"make sure the incoming data has the correct expected fields"
            # } 



    
import models, random
from controller import SessionLocal, engine




def add_DB():

    with SessionLocal.begin() as session:
        numb = str(random.randint(0,500))
        new_item = models.Test1(title=numb, complete=True)
        session.add(new_item)
        session.commit()

def read_DB():
        
    with SessionLocal.begin() as session:

        out = session.query(models.Test1).all()
        
        list(map(lambda x:print(x.id, x.complete),out))
        foo = list(map(lambda x:x.title,out))
        print (foo)

# def drop_DB():
#     with SessionLocal.begin() as session:
#         session.drop(models.Test1)
#         session.commit()

def main():
    models.Base.metadata.create_all(bind=engine)
    add_DB()
    read_DB()
    # drop_DB()

if __name__ == "__main__":
    main()

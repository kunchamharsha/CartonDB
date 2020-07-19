# CartonDB

## Summary

It is a file based Key-Value DB that uses Python's Pickle to serialise data stored.
Why use this ? It is super fast. Can write 3 million small key value pairs in 1 second.

## Use Cases

Ideal for use in cases where you need a quick store before pushing to db, rather than making a network call to the caching server.

## Get Started

> from CartonDb import Carton

> db = Carton(path) //path is where you want the library to save/get your data from 

> db.add(key,value)

> db.get(key)

> db.delete(key)

> db.save() //save is more of a commit feature like in relational databases, that's when the data is flushed to the db store


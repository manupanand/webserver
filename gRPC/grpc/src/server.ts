import path from 'path';
import * as grpc from '@grpc/grpc-js';
import  { GrpcObject, ServiceClientConstructor } from "@grpc/grpc-js"
import * as protoLoader from '@grpc/proto-loader';
import { ProtoGrpcType } from './generated/a';
import { AddressBookServiceHandlers } from './generated/AddressBookService';
import { Status } from '@grpc/grpc-js/build/src/constants';

const packageDefinition=protoLoader.loadSync(path.join(__dirname,'../proto/a.proto'));


const personProto=grpc.loadPackageDefinition(packageDefinition) as unknown as ProtoGrpcType

//ideally it should be databse
const PERSONS=[
    {"name":"manu",
        "age":36
    },
    {
        "name":"niko",
        "age":32
    }
    
]

const handler: AddressBookServiceHandlers =  {
    AddPerson: (call, callback) => {
      let person = {
        name: call.request.name,
        age: call.request.age
      }
      PERSONS.push(person);
      callback(null, person)
    },
    GetPersonByName: (call, callback) => {
      let person = PERSONS.find(x => x.name === call.request.name);
      if (person) {
        callback(null, person)
      } else {
        callback({
          code: Status.NOT_FOUND,
          details: "not found"
        }, null);
      }
    }
  }

const server =new grpc.Server()
server.addService((personProto.AddressBookService ).service,handler)
server.bindAsync('127.0.0.1:50051',grpc.ServerCredentials.createInsecure(),(err, port) => {
    if (err) {
      console.error('Failed to bind server:', err);
      return;
    }
    console.log(`Server running at http://127.0.0.1:${port}`);
    server.start();
  })